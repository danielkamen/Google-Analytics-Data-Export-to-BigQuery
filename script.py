import os
from google.cloud import bigquery
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up your service account key file path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path_to_your_service_account_key_json_file'

# Set up your GA view ID
VIEW_ID = 'your_GA_view_ID'

# Define your report request
report_request = {
    'viewId': VIEW_ID,
    'dateRanges': [
            {'startDate': '2013-01-01', 'endDate': '2023-05-09'}
        ],
    'metrics': [
            {'expression': 'ga:users'},
            {'expression': 'ga:newUsers'},
            {'expression': 'ga:sessions'},
            {'expression': 'ga:bounceRate'},
            {'expression': 'ga:pageviewsPerSession'},
            {'expression': 'ga:avgSessionDuration'}
        ],
    'dimensions': [
            {'name': 'ga:date'},
            {'name': 'ga:userType'},
            {'name': 'ga:userGender'}
        ],
}

def initialize_analyticsreporting():
    # Initialize the Analytics Reporting service with credentials
    credentials = service_account.Credentials.from_service_account_file(
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
        scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    return build('analyticsreporting', 'v4', credentials=credentials)

def get_report(analytics, report_request):
    # Retrieve the report using the Analytics Reporting service
    return analytics.reports().batchGet(
        body={
            'reportRequests': [report_request]
        }
    ).execute()

def create_table(project_id, dataset_id, table_id, schema):
    # Create a BigQuery table
    client = bigquery.Client(project=project_id)
    
    table_ref = client.dataset(dataset_id).table(table_id)
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)
    print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")

def insert_rows(project_id, dataset_id, table_id, rows_to_insert):
    # Insert rows into a BigQuery table
    client = bigquery.Client(project=project_id)

    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    errors = client.insert_rows_json(table, rows_to_insert)
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

def main():
    # Initialize the Analytics Reporting service
    analytics = initialize_analyticsreporting()
    
    # Get the report from Google Analytics
    report = get_report(analytics, report_request)

    # Extract schema from report
    dimensions = report_request['dimensions']
    metrics = report_request['metrics']
    schema = [bigquery.SchemaField(dim['name'].replace('ga:', ''), 'STRING') for dim in dimensions]
    schema += [bigquery.SchemaField(metric['expression'].replace('ga:', ''), 'STRING') for metric in metrics]

    project_id = 'your_project_id'
    dataset_id = 'your_dataset_id'
    table_id = 'your_new_table_id'
    
    # Create the BigQuery table
    create_table(project_id, dataset_id, table_id, schema)

    # Extract data from report and prepare rows for insertion
    rows = report['reports'][0]['data']['rows']
    rows_to_insert = []
    for row in rows:
        record = {}
        for i, dim in enumerate(dimensions):
            record[dim['name'].replace('ga:', '')] = row['dimensions'][i]
        for i, metric in enumerate(metrics):
            record[metric['expression'].replace('ga:', '')] = row['metrics'][0]['values'][i]
        rows_to_insert.append(record)
    
    # Insert rows into the BigQuery table
    insert_rows(project_id, dataset_id, table_id, rows_to_insert)

if __name__ == '__main__':
    main()
