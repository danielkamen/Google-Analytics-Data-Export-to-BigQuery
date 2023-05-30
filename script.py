import os
from google.cloud import bigquery
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.api_core.exceptions import NotFound

# Set up your service account key file path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'temp.json'

# Set up your GA view ID
VIEW_ID = 'VIEW ID HERE'

# Define your report requests and table IDs
report_requests = [
    {
        'table_id': 'Audience Demographics Gender',
        'report_request': {
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
        },
    },
    {
        'table_id': 'Audience Interests Affinity Categories',
        'report_request': {
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
                {'name': 'ga:interestAffinityCategory'}
            ],
        },
    },
    {
        'table_id': 'Audience Interests In-Market Segments',
        'report_request': {
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
                {'name': 'ga:interestInMarketCategory'}
            ],
        },
    },
    {
        'table_id': 'Audience Interests Other Interests',
        'report_request': {
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
                {'name': 'ga:interestOtherCategory'}
            ],
        },
    },
    {
        'table_id': 'Audience Demographics Age',
        'report_request': {
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
                {'name': 'ga:userAgeBracket'}
            ],
        },
    },
    {
        'table_id': 'Audience Behavior Frequency and Recency',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-09'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:newUsers'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:pageviews'},
                
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:userType'},
                {'name': 'ga:sessionCount'},
                {'name': 'ga:daysSinceLastSession'},
            ],
        },
    },
    {
        'table_id': 'Audience Behavior Engagement',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-09'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:newUsers'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'},
                {'expression': 'ga:goalValueAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:userType'},
                {'name': 'ga:sessionDurationBucket'}
            ],
        },
    },
    {
        'table_id': 'Audience Geo and Device and Network',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:newUsers'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:pageviews'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:percentNewSessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:userType'},
                {'name': 'ga:browser'},
                {'name': 'ga:screenResolution'},
                {'name': 'ga:operatingSystem'},
                {'name': 'ga:mobileDeviceInfo'},
                {'name': 'ga:city'},
                {'name': 'ga:language'},
                {'name': 'ga:hostname'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Google Ads Campaigns And Keyword',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:adClicks'},
                {'expression': 'ga:adCost'},
                {'expression': 'ga:costPerConversion'},
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'},
                {'expression': 'ga:goalValueAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:adwordsCampaignID'},
                {'name': 'ga:campaign'},
                {'name': 'ga:adGroup'},
                {'name': 'ga:sourceMedium'},
                {'name': 'ga:keyword'}
            ],
        },
    },
    {
        'table_id': 'Acquisition All Traffic',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'},
                {'expression': 'ga:goalValueAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:userType'},
                {'name': 'ga:channelGrouping'},
                {'name': 'ga:sourceMedium'},
                {'name': 'ga:fullReferrer'},
                {'name': 'ga:source'},
                {'name': 'ga:medium'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Google Ads Search',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:adClicks'},
                {'expression': 'ga:adCost'},
                {'expression': 'ga:costPerConversion'},
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:adMatchedQuery'},
                {'name': 'ga:adMatchType'},
                {'name': 'ga:adQueryWordCount'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Google Ads Hour of Day',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:hour'},
                {'name': 'ga:dayOfWeekName'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Google Ads Display Targeting Search Keyword',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:adClicks'},
                {'expression': 'ga:adCost'},
                {'expression': 'ga:costPerConversion'},
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:adDisplayUrl'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Google Ads Display Targeting Ad Display Url',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:percentNewSessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:adPlacementUrl'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Google Ads Display Targeting Ad Placement Url',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:percentNewSessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:adPlacementDomain'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Google Ads Video and Shopping Campaigns',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:campaign'},
                {'name': 'ga:adContent'},
                {'name': 'ga:isTrueViewVideoAd'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Social Conversions Source',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:costPerGoalConversion'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:socialNetwork'},
                {'name': 'ga:source'},
                {'name': 'ga:sourceMedium'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Social Conversions Device',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:socialNetwork'},
                {'name': 'ga:deviceCategory'},
                {'name': 'ga:userType'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Social Plugins',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:socialInteractions'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:socialNetwork'},
                {'name': 'ga:source'},
                {'name': 'ga:sourceMedium'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Google Ads Final URLs',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:adClicks'},
                {'expression': 'ga:adCost'},
                {'expression': 'ga:costPerConversion'},
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:adDestinationUrl'},
                {'name': 'ga:adDistributionNetwork'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Social Network Referrals and Landing Pages',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:socialNetwork'},
                {'name': 'ga:hasSocialSourceReferral'},
                {'name': 'ga:landingPagePath'},
                {'name': 'ga:pageTitle'},
                {'name': 'ga:source'},
                {'name': 'ga:sourceMedium'},
                {'name': 'ga:deviceCategory'},
                {'name': 'ga:userType'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Campaigns All Campaigns',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:campaign'},
                {'name': 'ga:campaignCode'},
                {'name': 'ga:source'},
                {'name': 'ga:medium'},
                {'name': 'ga:sourceMedium'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Campaigns Paid Keyword',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:keyword'},
                {'name': 'ga:adMatchedQuery'},
                {'name': 'ga:campaign'},
                {'name': 'ga:campaignCode'},
                {'name': 'ga:source'},
                {'name': 'ga:medium'},
                {'name': 'ga:sourceMedium'}
            ],
        },
    },
    {
        'table_id': 'Behavior Site Content Exits',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:exits'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:users'},
                {'expression': 'ga:exitRate'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:pagePath'}
            ],
        },
    },
    {
        'table_id': 'Behavior Site Search Usage',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:sessions'},
                {'expression': 'ga:percentNewSessions'},
                {'expression': 'ga:newUsers'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:searchUsed'},
                {'name': 'ga:searchCategory'}
            ],
        },
    },
    {
        'table_id': 'Behavior Site Search Search Terms',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:searchUniques'},
                {'expression': 'ga:avgSearchResultViews'},
                {'expression': 'ga:percentSessionsWithSearch'},
                {'expression': 'ga:searchExitRate'},
                {'expression': 'ga:percentSearchRefinements'},
                {'expression': 'ga:searchDuration'},
                {'expression': 'ga:avgSearchDepth'}
            ],
            'dimensions': [
                {'name': 'ga:searchKeyword'},
                {'name': 'ga:searchUsed'},
                {'name': 'ga:searchCategory'}
            ],
        },
    },
    {
        'table_id': 'Behavior Site Search Search Pages',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:searchUniques'},
                {'expression': 'ga:avgSearchResultViews'},
                {'expression': 'ga:percentSessionsWithSearch'},
                {'expression': 'ga:searchExitRate'},
                {'expression': 'ga:percentSearchRefinements'},
                {'expression': 'ga:searchDuration'},
                {'expression': 'ga:avgSearchDepth'}
            ],
            'dimensions': [
                {'name': 'ga:landingPagePath'}
            ],
        },
    },
    {
        'table_id': 'Behavior Events Top Events',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:totalEvents'},
                {'expression': 'ga:uniqueEvents'},
                {'expression': 'ga:eventValue'},
                {'expression': 'ga:avgEventValue'}
            ],
            'dimensions': [
                {'name': 'ga:eventCategory'},
                {'name': 'ga:eventAction'},
                {'name': 'ga:eventLabel'}
            ],
        },
    },
    {
        'table_id': 'Behavior Events Pages',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:totalEvents'},
                {'expression': 'ga:uniqueEvents'},
                {'expression': 'ga:eventValue'},
                {'expression': 'ga:avgEventValue'}
            ],
            'dimensions': [
                {'name': 'ga:pagePath'},
                {'name': 'ga:pageTitle'}
            ],
        },
    },
    {
        'table_id': 'Behavior Site Content Landing Pages',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:landingPagePath'}
            ],
        },
    },
    {
        'table_id': 'Behavior Site Content All Pages Content Drilldown',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:pageviews'},
                {'expression': 'ga:uniquePageviews'},
                {'expression': 'ga:timeOnPage'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:entrances'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:exitRate'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:pagePath'},
                {'name': 'ga:pageDepth'},
                {'name': 'ga:landingPagePath'},
                {'name': 'ga:pageTitle'},
                {'name': 'ga:pagePathLevel1'}
            ],
        },
    },
    {
        'table_id': 'Acquisition Campaigns Organic Keyword',
        'report_request': {
            'viewId': VIEW_ID,
            'dateRanges': [
                {'startDate': '2013-01-01', 'endDate': '2023-05-30'}
            ],
            'metrics': [
                {'expression': 'ga:users'},
                {'expression': 'ga:sessions'},
                {'expression': 'ga:bounceRate'},
                {'expression': 'ga:pageviewsPerSession'},
                {'expression': 'ga:avgSessionDuration'},
                {'expression': 'ga:goalConversionRateAll'},
                {'expression': 'ga:goalCompletionsAll'}
            ],
            'dimensions': [
                {'name': 'ga:date'},
                {'name': 'ga:keyword'},
                {'name': 'ga:source'},
                {'name': 'ga:medium'},
                {'name': 'ga:sourceMedium'},
                {'name': 'ga:landingPagePath'}
            ],
        },
    }
]

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
