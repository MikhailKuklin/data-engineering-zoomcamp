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

`prefect block register -m prefect_gcp`

Step 3. Create Prefect block for enabling GCS bucket

Prefect UI -> Blocks -> GCS bucket -> GCP Credentials

To get credentials, IAM & Admin -> Service Accounts -> Create service account -> Select a role -> BigQuery Admin, Storage Admin -> Keys -> Create a new key -> Download -> Add to Prefect

Step 4. Run the code

`python etl_web_to_gcs.py`

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

*Step 1* Build deployment

`prefect deployment build etl_gcs_to_bq.py:etl_parent_flow -n 'GCS-to-BigQuery'`

*Step 2* Modify parameters in yaml infra file

*Step 3* Apply

`prefect deployment apply etl_parent_flow-deployment.yaml `

*Step 4* Run agent

`prefect agent start --work-queue "default"`

## Question 4. Github Storage Block

Using the `web_to_gcs` script from the videos as a guide, you want to store your flow code in a GitHub repository for collaboration with your team. Prefect can look in the GitHub repo to find your flow code and read it. Create a GitHub storage block from the UI or in Python code and use that in your Deployment instead of storing your flow code locally or baking your flow code into a Docker image. 

Note that you will have to push your code to GitHub, Prefect will not push it for you.

Run your deployment in a local subprocess (the default if you don’t specify an infrastructure). Use the Green taxi data for the month of November 2020.

How many rows were processed by the script?

- 88,019
- 192,297
- 88,605
- 190,225

## Solution

*Step 1* Prefect UI -> Blocks -> GitHub (token should be generated in GitHub in prior)

*Step 2* Build infra file

`prefect deployment build -n etl_github2 -sb github/zoomcamp ./week_2_workflow_orchestration/homework/etl_github_to_gcs.py:etl_web_to_gcs`

*etl_github2*: deployment name
*github/zoomcamp*: name of the block in Prefect
*./week_2_workflow_orchestration/homework/etl_github_to_gcs.py:etl_web_to_gcs`*: path to the flow which should be identical to GitHub from root directory

*Step 3*: Apply

`prefect deployment apply etl_web_to_gcs-deployment.yaml`

*Step 4*: Initiate the run from Prefect UI, start the agent

## Question 6. Secrets

Prefect Secret blocks provide secure, encrypted storage in the database and obfuscation in the UI. Create a secret block in the UI that stores a fake 10-digit password to connect to a third-party service. Once you’ve created your block in the UI, how many characters are shown as asterisks (*) on the next page of the UI?

- 5
- 6
- 8
- 10

## Solution

Go to Prefect UI -> Blocks -> Secret
