import os
import re
from google.cloud import bigquery
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up your service account key file path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path_to_your_service_account_key_file.json'

# Set up your GA view ID
VIEW_ID = 'YOUR_GA_VIEW_ID'

# Define your reports
# You can add more reports to this list
REPORT_REQUESTS = [
    # Your actual report requests go here...
]

# Define your report titles
REPORT_TITLES = [
    "Audience Interests Affinity Categories",
    "Audience Interests In-Market Segments",
    "Audience Interests Other Interests",
    # ...add more report titles here
]

def initialize_analyticsreporting():
    credentials = service_account.Credentials.from_service_account_file(
        'path_to_your_service_account_key_file.json', scopes=['https://www.googleapis.com/auth/analytics.readonly'])
    
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics

def get_report(analytics, report_request):
    return analytics.reports().batchGet(
        body={
            'reportRequests': report_request
        }
    ).execute()

def sanitize_title(title):
    # Remove any non-word character (anything other than letter, number or underscore)
    sanitized = re.sub(r'\W+', '', title)
    # Replace spaces with underscores
    sanitized = sanitized.replace(' ', '_')
    return sanitized

def create_table(dataset_id, table_id):
    bq_client = bigquery.Client()

    # Define the full table ID
    full_table_id = f"{bq_client.project}.{dataset_id}.{table_id}"

    table = bigquery.Table(full_table_id)
    bq_client.create_table(table)

def main():
    analytics = initialize_analyticsreporting()

    dataset_id = 'YOUR_DATASET_ID'

    # Create tables for each report
    for title in REPORT_TITLES:
        sanitized_title = sanitize_title(title)
        create_table(dataset_id, sanitized_title)

    for report_request in REPORT_REQUESTS:
        try:
            report = get_report(analytics, report_request)
            to_bigquery(report)
        except HttpError as error:
            print(f"An error occurred: {error}")

if __name__ == '__main__':
    main()
