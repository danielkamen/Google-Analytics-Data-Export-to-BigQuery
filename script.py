import os
from google.cloud import bigquery
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.api_core.exceptions import NotFound
from report_requests import get_report_requests

# Set up your service account key file path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'temp.json'

# Set up your GA view ID
VIEW_ID = 'VIEW ID HERE'

def initialize_analyticsreporting():
    credentials = service_account.Credentials.from_service_account_file(
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
        scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    return build('analyticsreporting', 'v4', credentials=credentials)

def create_table(project_id, dataset_id, table_id, schema):
    client = bigquery.Client(project=project_id)
    
    table_ref = client.dataset(dataset_id).table(table_id)
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)
    print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")

def insert_rows(project_id, dataset_id, table_id, rows_to_insert):
    client = bigquery.Client(project=project_id)

    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    errors = []
    for i in range(0, len(rows_to_insert), 1000):
        batch_rows = rows_to_insert[i:i+1000]
        errors.extend(client.insert_rows_json(table, batch_rows))

    if errors:
        print("Encountered errors while inserting rows: {}".format(errors))

def get_report(analytics, report_request):
    report_responses = []
    page_token = None

    while True:
        # Add the page token to the report request
        report_request['pageToken'] = page_token

        # Execute the report request
        response = analytics.reports().batchGet(
            body={'reportRequests': [report_request]}
        ).execute()

        # Append the report response to the list
        report_responses.append(response)

        # Check if there are more pages available
        next_page_token = response['reports'][0].get('nextPageToken')
        if next_page_token:
            page_token = next_page_token
        else:
            break

    return report_responses

def main():
    analytics = initialize_analyticsreporting()
    report_requests = get_report_requests(VIEW_ID)

    for request in report_requests:
        table_id = request['table_id']
        report_request = request['report_request']

        report = get_report(analytics, report_request)

        # Extract schema from report
        dimensions = report_request['dimensions']
        metrics = report_request['metrics']
        schema = [bigquery.SchemaField(dim['name'].replace('ga:', ''), 'STRING') for dim in dimensions]
        schema += [bigquery.SchemaField(metric['expression'].replace('ga:', ''), 'STRING') for metric in metrics]

        project_id = 'INSERT PROJECT ID'
        dataset_id = 'INSERT DATASET ID'
        
        # Create a new table with a counter if the row limit exceeds 1000
        table_counter = 1
        while True:
            new_table_id = f"{table_id}_{table_counter}"
            try:
                bigquery.Client(project=project_id).get_table(f"{project_id}.{dataset_id}.{new_table_id}")
            except NotFound:
                create_table(project_id, dataset_id, new_table_id, schema)
                break
            table_counter += 1
        
        # Extract data from report
        rows = []
        for response in report:
            if 'rows' in response['reports'][0]['data']:
                rows += response['reports'][0]['data']['rows']
        rows_to_insert = []
        for row in rows:
            record = {}
            for i, dim in enumerate(dimensions):
                record[dim['name'].replace('ga:', '')] = row['dimensions'][i]
            for i, metric in enumerate(metrics):
                record[metric['expression'].replace('ga:', '')] = row['metrics'][0]['values'][i]
            rows_to_insert.append(record)

        # Insert rows into the corresponding table
        insert_rows(project_id, dataset_id, new_table_id, rows_to_insert)

if __name__ == '__main__':
    main()
