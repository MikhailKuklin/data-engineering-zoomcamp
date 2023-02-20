## Week 4 Homework

All the work has been implemented using dbt Cloud.

### Question 1: 
**What is the count of records in the model fact_trips after running all models with the test run variable disabled and filtering for 2019 and 2020 data only (pickup datetime)**  
You'll need to have completed the "Build the first dbt models" video and have been able to run the models via the CLI. 
You should find the views and models for querying in your DWH.

## Solution:

*Step 1* In dbt, run `dbt run --var 'is_test_run: false'`
*Step 2* In Big Query, run the query:

```sh
SELECT count(*) FROM prime-framing-374716.dbt_mkuklin.fact_trips
WHERE EXTRACT(YEAR FROM pickup_datetime) IN  (2019, 2020) 
```

Answer: 61648442

### Question 2: 
**What is the distribution between service type filtering by years 2019 and 2020 data as done in the videos**

You will need to complete "Visualising the data" videos, either using data studio or metabase. 

Answer: from the [report](fact_trips.pdf), 89.1/10.1

### Question 3: 
**What is the count of records in the model stg_fhv_tripdata after running all models with the test run variable disabled (:false)**  

Create a staging model for the fhv data for 2019 and do not add a deduplication step. Run it via the CLI without limits (is_test_run: false).
Filter records with pickup time in year 2019.

## Solution: 

*Step 1* Create SQL model for fhv_tripdata (models/stg/sts_fhv_tripdata_q2.sql)

```sh
{{ config(materialized='view')}}

select
    dispatching_base_num,

    cast(PULocationID as integer) as pickup_locationid,
    cast(DOLocationID as integer) as dropoff_locationid,

    --timestamps
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,

    --trip info
    sr_flag
from {{ source('staging', 'fhv_tripdata_csv')}}
```

*Step 2* Run query:

```sh
SELECT count(*) FROM `prime-framing-374716.dbt_mkuklin.stg_fhv_tripdata_q2`
where extract(year from pickup_datetime) in (2019)
```

Answer: 43244696

### Question 4: 
**What is the count of records in the model fact_fhv_trips after running all dependencies with the test run variable disabled (:false)**  

Create a core model for the stg_fhv_tripdata joining with dim_zones.
Similar to what we've done in fact_trips, keep only records with known pickup and dropoff locations entries for pickup and dropoff locations. 
Run it via the CLI without limits (is_test_run: false) and filter records with pickup time in year 2019.

## Solution: 

*Step 1* Create SQL model for fhv_tripdata (models/stg/stg_fhv_tripdata_q4.sql)

*Step 2* Modify model/core/schema.yaml by adding:

```sh
models:

    - name: stg_fhv_tripdata_q4
      description: >
```

*Step 3* Create SQL model for joining with taxi zone (models/core/fact_fhv_tripdata_q4) and run:

```sh
dbt build --select stg_fhv_trip_data_mat --var 'is_test_run: false'
```

*Step 4* In BigQuery, run the query:

```sh
SELECT count(*) FROM `prime-framing-374716.dbt_mkuklin.fact_fhv_tripdata_q4`
where extract(year from pickup_datetime) in (2019)
```

Answer: 22998722

### Question 5: 
**What is the month with the biggest amount of rides after building a tile for the fact_fhv_trips table**
Create a dashboard with some tiles that you find interesting to explore the data. One tile should show the amount of trips per month, as done in the videos for fact_trips, based on the fact_fhv_trips table.

## Solution: 

January according to the [report](fact_trips.pdf)

