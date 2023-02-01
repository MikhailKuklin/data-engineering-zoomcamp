### Question 1:
What is count for fhv vehicles data for year 2019
Can load the data for cloud storage and run a count(*)

## Solution

*Step 1* Run ETL pipeline to clean and transfer data to GCP
`python etl_web_to_gcs.py`

*Step 2* In GCP, create a table in BigQuery using the data from GCP

--- Create external table for 2019 ---
CREATE OR REPLACE EXTERNAL TABLE dezoomcamp_west6.fhv_tripdata2019
OPTIONS (
  format = 'parquet',
  uris = ['gs://dtc_data_lake_prime-framing-374716/data/fhv_tripdata_2019-*.parquet']
);

--- Query to count ---
SELECT count(*) FROM `dezoomcamp_west6.fhv_tripdata2019`

Answer: 43244696

### Question 2:
How many distinct dispatching_base_num we have in fhv for 2019
Can run a distinct query on the table from question 1

## Solution

SELECT COUNT(DISTINCT dispatching_base_num)
FROM `dezoomcamp_west6.fhv_tripdata2019`

Answer: 799

### Question 3:
Best strategy to optimise if query always filter by dropoff_datetime and order by dispatching_base_num
Review partitioning and clustering video.
We need to think what will be the most optimal strategy to improve query performance and reduce cost.

## Solution

Answer: partition for the dates and clustering for dispatching

### Question 4:
What is the count, estimated and actual data processed for query which counts trip between 2019/01/01 and 2019/03/31 for dispatching_base_num B00987, B02060, B02279
Create a table with optimized clustering and partitioning, and run a count(*). Estimated data processed can be found in top right corner and actual data processed can be found after the query is executed.

## Solution

--- Create a table with optimized clustering and partitioning ---
CREATE OR REPLACE TABLE `dezoomcamp_west6.fhv_tripdata2019_part`
PARTITION BY DATE(pickup_datetime)
CLUSTER BY dispatching_base_num AS
SELECT * FROM `dezoomcamp_west6.fhv_tripdata_py`

--- Count ---
SELECT count(*)
FROM `dezoomcamp_west6.fhv_tripdata2019_part`
WHERE CAST(pickup_datetime as DATE) BETWEEN "2019-01-01" AND "2019-03-31"
AND CAST(dropOff_datetime as DATE) BETWEEN "2019-01-01" AND "2019-12-31"
AND dispatching_base_num IN ('B00987','B02060','B02279');

Answer:
*estimated data processed*: This query will process 403.53 (without dropOff) / 604.38 MB when run
*actual data processed*: 143 MB (without dropOff) / 214 MB

### Question 5:
What will be the best partitioning or clustering strategy when filtering on dispatching_base_num and SR_Flag
Review partitioning and clustering video. Partitioning cannot be created on all data types.

## Solution

Clustering for dispatching and partitioning for flat

### Question 6:
What improvements can be seen by partitioning and clustering for data size less than 1 GB
Partitioning and clustering also creates extra metadata.
Before query execution this metadata needs to be processed.

## Solution

No improvements because the size is small e.g. less than 1GB

### Question 7:
In which format does BigQuery save data
Review big query internals video.

## Solution

Columnar

