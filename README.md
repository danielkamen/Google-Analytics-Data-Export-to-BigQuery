# Google Analytics Data Export to BigQuery

This Python script extracts data from Google Analytics and loads it into Google BigQuery. Big thanks to gpt4 for helping with the documentation <3

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

### Create VIRTUAL ENV
```shell
python -m venv env
```

### Activate virtual environment
```shell
source env/bin/activate
```


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
3. Replace 'temp.json' with the path to your service account key file.
4. Add VIEW_ID in .env
5. Add start date and end date in .env
5. Replace 'INSERT PROJECT ID' with your Google Cloud project ID.
6. Replace 'INSERT DATASET ID' with your BigQuery dataset ID.
7. Edit the report_requests list to include the Google Analytics reports you want to export, specifying the metrics and dimensions for each report.

## Running the Script

To run the script, navigate to the directory containing the script in your terminal and run the command:

```shell
python your_script_name.py
```

### Formatting
Note that the date output from the Google Analytics API is a YYYYMMDD string. In google sheets / excel use the formula below to format:
`=DATE(LEFT(A2,4),MID(A2,5,2),RIGHT(A2,2))`


Replace 'script.py' with the actual name of the Python script.


SEO so this can find the right people

Moving Google Analytics to BigQuery.
Move GA3 to BigQuery.
Transfer GA3 to BigQuery.
Migrate Google Analytics Data to BigQuery.
Migrate Google Analytics Data into to BigQuery.
