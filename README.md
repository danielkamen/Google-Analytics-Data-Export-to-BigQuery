# Google-Analytics-Data-Export-to-BigQuery
This Python script extracts data from Google Analytics and loads it into Google BigQuery.


Table of Contents
Pre-requisites
Setup Instructions
Running the Script
Pre-requisites
To use this script, you will need:

Python 3.7 or higher installed on your machine. You can download Python from the official website here: https://www.python.org/downloads/

A Google Cloud account with a project where you have permissions to create and manage BigQuery datasets and tables.

Access to a Google Analytics account and view, with a service account that has permissions to read data from this view.

A service account key file (in JSON format) for authenticating your requests to the Google Analytics API and Google BigQuery.

The google-api-python-client, google-auth, google-cloud-bigquery, and google-auth-httplib2 Python libraries installed in your Python environment.

Setup Instructions
Follow these steps to set up your environment:

Install the Required Python Libraries: Run the following command in your terminal to install the necessary Python libraries:

css
Copy code
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib google-auth google-cloud-bigquery
If you are using a virtual environment (which is good practice), make sure you've activated the environment before running this command.

Set Up Your Google Cloud and Google Analytics Access:

In the Google Cloud Console, create a new project (or select an existing one).

Enable the Google Analytics API and BigQuery API for your project.

Create a service account for your project in the IAM & Admin section, and generate a JSON key file for this account.

In the IAM section, give your service account the roles of "BigQuery Data Editor" and "BigQuery Job User" (for BigQuery access), and "Viewer" role (for Google Analytics access).

In your Google Analytics account, add the service account email as a user with Read & Analyze permissions at the view level.

Set Up Your Python Script:

Download the Python script.

Replace the placeholder values in the script with your actual values:

Replace 'path_to_your_service_account_key_file.json' with the path to your service account key file.

Replace 'YOUR_GA_VIEW_ID' with your Google Analytics view ID.

Replace 'YOUR_DATASET_ID' with your BigQuery dataset ID.

Edit the REPORT_REQUESTS list to include the Google Analytics reports you want to export, specifying the metrics and dimensions for each report.

Edit the REPORT_TITLES list to include the titles of the reports, matching the order of the reports in the REPORT_REQUESTS list.
