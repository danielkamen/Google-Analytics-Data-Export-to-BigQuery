# Google Analytics Data Export to BigQuery

This Python script extracts data from Google Analytics and loads it into Google BigQuery.

## Table of Contents
1. [Pre-requisites](#pre-requisites)
2. [Setup Instructions](#setup-instructions)
3. [Running the Script](#running-the-script)

## Pre-requisites

To use this script, you will need:

1. Python 3.7 or higher installed on your machine. You can download Python from the official website [here](https://www.python.org/downloads/)
2. A Google Cloud account with a project where you have permissions to create and manage BigQuery datasets and tables.
3. Access to a Google Analytics account and view, with a service account that has permissions to read data from this view.
4. A service account key file (in JSON format) for authenticating your requests to the Google Analytics API and Google BigQuery.
5. The `google-api-python-client`, `google-auth`, `google-cloud-bigquery`, and `google-auth-httplib2` Python libraries installed in your Python environment.

## Setup Instructions

Follow these steps to set up your environment:

### Install the Required Python Libraries

Run the following command in your terminal to install the necessary Python libraries:

```shell
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib google-auth google-cloud-bigquery
```

### Set Up Your Google Cloud and Google Analytics Access

1. In the Google Cloud Console, create a new project (or select an existing one).
2. Enable the Google Analytics API and BigQuery API for your project.
3. Create a service account for your project in the IAM & Admin section, and generate a JSON key file for this account.
4. In the IAM section, give your service account the roles of "BigQuery Data Editor" and "BigQuery Job User" (for BigQuery access), and "Viewer" role (for Google Analytics access).
5. In your Google Analytics account, add the service account email as a user with Read & Analyze permissions at the view level.

### Set Up Your Python Script

1. Download the Python script.
2. Replace the placeholder values in the script with your actual values:
   - Replace 'path_to_your_service_account_key_file.json' with the path to your service account key file.
   - Replace 'YOUR_GA_VIEW_ID' with your Google Analytics view ID.
   - Replace 'YOUR_DATASET_ID' with your BigQuery dataset ID.
3. Edit the `REPORT_REQUESTS` list to include the Google Analytics reports you want to export, specifying the metrics and dimensions for each report.
4. Edit the `REPORT_TITLES` list to include the titles of the reports, matching the order of the reports in the `REPORT_REQUESTS` list.

## Running the Script

To run the script, navigate to the directory containing the script in your terminal and run the command:

```shell
python your_script_name.py
```


Replace 'your_script_name.py' with the actual name of the Python script.

The script will create a new table in your BigQuery dataset for each report in the `REPORT_TITLES` list, sanitizing the title to create the table ID. It will then fetch each report from Google Analytics and insert the data into the corresponding BigQuery table.

> :warning: Please note that this script does not include error handling for quota limits or retries for transient errors. Depending on the number of reports and frequency of requests, you may need to add these features to the script to adhere to the Google Analytics API and BigQuery usage limits and best practices.
