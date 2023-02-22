## Week 5 Homework

In this homework we'll put what we learned about Spark
in practice.

We'll use high volume for-hire vehicles (HVFHV) dataset for that.

## Question 1. Install Spark and PySpark

* Install Spark
* Run PySpark
* Create a local spark session 
* Execute `spark.version`

What's the output?

What's the output?

3.3.2
2.1.4
1.2.3
5.4

Answer: 3.3.2

## Question 2. HVFHW February 2021

HVFHW June 2021

Read it with Spark using the same schema as we did in the lessons.
We will use this dataset for all the remaining questions.
Repartition it to 12 partitions and save it to parquet.
What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.

- 2MB

- 24MB

- 100MB

- 250MB

## Solution:

Implemented in Databricks:

```sh
df = spark.read.option("header", "true",).option("inferSchema", "true").csv('dbfs:/exploration/fhvhv_tripdata_2021_06_csv.gz')

df_part = df.repartition(12)

df_part.write.mode('overwrite').parquet('exploration/2021/06')

dbutils.fs.ls('exploration/2021/06')
```

Answer: 24MB


## Question 3. Count records 

How many taxi trips were there on February 15?

Consider only trips that started on February 15.


## Question 4. Longest trip for each day

Now calculate the duration for each trip.

Trip starting on which day was the longest? 


## Question 5. Most frequent `dispatching_base_num`

Now find the most frequently occurring `dispatching_base_num` 
in this dataset.

How many stages this spark job has?

> Note: the answer may depend on how you write the query,
> so there are multiple correct answers. 
> Select the one you have.


## Question 6. Most common locations pair

Find the most common pickup-dropoff pair. 

For example:

"Jamaica Bay / Clinton East"

Enter two zone names separated by a slash

If any of the zone names are unknown (missing), use "Unknown". For example, "Unknown / Clinton East". 


## Bonus question. Join type

(not graded) 

For finding the answer to Q6, you'll need to perform a join.

What type of join is it?

And how many stages your spark job has?


## Submitting the solutions

* Form for submitting: https://forms.gle/dBkVK9yT8cSMDwuw7
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 07 March (Monday), 22:00 CET
