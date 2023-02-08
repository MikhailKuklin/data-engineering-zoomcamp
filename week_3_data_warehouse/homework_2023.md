### Question 1:
What is the count for fhv vehicle records for year 2019?
- 65,623,481
- 43,244,696
- 22,978,333
- 13,942,414

## Solution

*Step 1* Run ETL pipeline to clean and transfer data to GCP
`python etl_web_to_gcs_csv.py`

*Step 2* In GCP, create a table in BigQuery using the data from GCP

```sh
CREATE OR REPLACE EXTERNAL TABLE dezoomcamp_west6.fhv_tripdata2019_csv
OPTIONS (
  format = 'csv',
  uris = ['gs://dtc_data_lake_prime-framing-374716/data/fhv_tripdata_2019-*.csv.gz']
);

SELECT count(*) FROM `dezoomcamp_west6.fhv_tripdata2019_csv`
```

Answer: 43244696

### Question 2:
Write a query to count the distinct number of affiliated_base_number for the entire dataset on both the tables.</br> 
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

- 25.2 MB for the External Table and 100.87MB for the BQ Table
- 225.82 MB for the External Table and 47.60MB for the BQ Table
- 0 MB for the External Table and 0MB for the BQ Table
- 0 MB for the External Table and 317.94MB for the BQ Table 

## Solution

```sh
CREATE OR REPLACE TABLE dezoomcamp_west6.fhv_tripdata2019_mat AS
SELECT *
FROM dezoomcamp_west6.fhv_tripdata2019_csv
```
```sh
SELECT COUNT(DISTINCT affiliated_base_number) FROM `dezoomcamp_west6.fhv_tripdata2019_mat`
```

```sh
SELECT COUNT(DISTINCT affiliated_base_number)
FROM `dezoomcamp_west6.fhv_tripdata2019_csv`
```

Answer: 0 for external and 317.94MB for materialized table

### Question 3:
How many records have both a blank (null) PUlocationID and DOlocationID in the entire dataset?
- 717,748
- 1,215,687
- 5
- 20,332

## Solution

```sh
SELECT COUNT(*)
FROM `dezoomcamp_west6.fhv_tripdata2019_csv`
WHERE PUlocationID IS NULL AND DOlocationID IS NULL;
```

Answer: 717748

### Question 4:
What is the best strategy to optimize the table if query always filter by pickup_datetime and order by affiliated_base_number?
- Cluster on pickup_datetime Cluster on affiliated_base_number
- Partition by pickup_datetime Cluster on affiliated_base_number
- Partition by pickup_datetime Partition by affiliated_base_number
- Partition by affiliated_base_number Cluster on pickup_datetime

## Solution

```sh
CREATE OR REPLACE TABLE `dezoomcamp_west6.fhv_tripdata2019_part_clust`
PARTITION BY DATE(pickup_datetime)
CLUSTER BY affiliated_base_number AS
SELECT * FROM `dezoomcamp_west6.fhv_tripdata2019_mat`
```

Answer: Partition by pickup_datetime Cluster on affiliated_base_number

### Question 5:
Implement the optimized solution you chose for question 4. Write a query to retrieve the distinct affiliated_base_number between pickup_datetime 03/01/2019 and 03/31/2019 (inclusive).</br> 
Use the BQ table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values? Choose the answer which most closely matches.
- 12.82 MB for non-partitioned table and 647.87 MB for the partitioned table
- 647.87 MB for non-partitioned table and 23.06 MB for the partitioned table
- 582.63 MB for non-partitioned table and 0 MB for the partitioned table
- 646.25 MB for non-partitioned table and 646.25 MB for the partitioned table

```sh
SELECT COUNT(DISTINCT affiliated_base_number)
FROM `dezoomcamp_west6.fhv_tripdata2019_part_clust`
WHERE CAST(pickup_datetime as DATE) BETWEEN "2019-01-03" AND "2019-31-03";
```

```sh
SELECT COUNT(DISTINCT affiliated_base_number)
FROM `dezoomcamp_west6.fhv_tripdata2019_mat`
WHERE CAST(pickup_datetime as DATE) BETWEEN "2019-01-03" AND "2019-31-03";
```

Answer:
647.87 MB for non-partitioned table and 23.06 MB for the partitioned table

### Question 6:
Where is the data stored in the External Table you created?

- Big Query
- GCP Bucket
- Container Registry
- Big Table

## Solution

Answer: GCP Bucket

### Question 7:
It is best practice in Big Query to always cluster your data:
- True
- False

## Solution

Answer: False

