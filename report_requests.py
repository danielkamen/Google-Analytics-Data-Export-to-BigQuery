# Define your report requests and table IDs
def get_report_requests(VIEW_ID):
    return [
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