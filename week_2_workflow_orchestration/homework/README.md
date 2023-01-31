# Guidelines for the homework week 2

## Question 1

Load January 2020 data

Using the `etl_web_to_gcs.py` flow that loads taxi data into GCS as a guide, create a flow that loads the green taxi CSV dataset for January 2020 into GCS and run it. Look at the logs to find out how many rows the dataset has.

How many rows does that dataset have?

* 447,770
* 766,792
* 299,234
* 822,132

### Solution

Step 1. Create GCS bucket in GCP

Google Storage -> Buckets -> Create a bucket

Step 2. Register Prefect block for enabling GCS bucket

'prefect block register -m prefect_gcp'

Step 3. Create Prefect block for enabling GCS bucket

Prefect UI -> Blocks -> GCS bucket -> GCP Credentials

To get credentials, IAM & Admin -> Service Accounts -> Create service account -> Select a role -> BigQuery Admin, Storage Admin -> Keys -> Create a new key -> Download -> Add to Prefect

Step 4. Run the code

'python etl_web_to_gcs.py'

## Question 2. Scheduling with Cron

Cron is a common scheduling specification for workflows. 

Using the flow in `etl_web_to_gcs.py`, create a deployment to run on the first of every month at 5pm UTC. What’s the cron schedule for that?

- `0 5 1 * *`
- `0 0 5 1 *`
- `5 * 1 0 *`
- `* * 5 1 0`

### Solution

min hours day-of-month week month => 0 5 1 * *

## Question 3. Loading data to BigQuery 

Using `etl_gcs_to_bq.py` as a starting point, modify the script for extracting data from GCS and loading it into BigQuery. This new script should not fill or remove rows with missing values. (The script is really just doing the E and L parts of ETL).

The main flow should print the total number of rows processed by the script. Set the flow decorator to log the print statement.

Parametrize the entrypoint flow to accept a list of months, a year, and a taxi color. 

Make any other necessary changes to the code for it to function as required.

Create a deployment for this flow to run in a local subprocess with local flow code storage (the defaults).

Make sure you have the parquet data files for Yellow taxi data for Feb. 2019 and March 2019 loaded in GCS. Run your deployment to append this data to your BiqQuery table. How many rows did your flow code process?

- 14,851,920
- 12,282,990
- 27,235,753
- 11,338,483

## Solution

etl_gcs_to_bq.py (WIP)
