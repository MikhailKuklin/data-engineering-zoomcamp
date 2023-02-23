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

## Question 2. HVFHW June 2021

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

How many taxi trips were there on June 15?

Consider only trips that started on June 15.

- 308,164

- 12,856

- 452,470

- 50,982

## Solution:

`df.filter(f.col("pickup_datetime").cast("date") == "2021-06-15").count()`

```sh
df.createOrReplaceTempView('question5')

spark.sql("""
SELECT COUNT(*) FROM question5 
WHERE (CAST(pickup_datetime as DATE) = '2021-06-15')
""").display()
```

Answer: 452,470

## Question 4. Longest trip for each day

Now calculate the duration for each trip.
How long was the longest trip in Hours?

66.87 Hours
243.44 Hours
7.68 Hours
3.32 Hours

## Solution:

```sh
from pyspark.sql.functions import col, unix_timestamp, max

df = df.withColumn('pickup_timestamp', unix_timestamp(col('pickup_datetime')))
df = df.withColumn('dropoff_timestamp', unix_timestamp(col('dropoff_datetime')))
df = df.withColumn('diff_seconds', col('dropoff_timestamp') - col('pickup_timestamp'))
df = df.withColumn('diff_hours', col('diff_seconds') / 3600)

max_diff_hours = df.agg(max(col('diff_hours')).alias('max_diff_hours')).collect()[0]['max_diff_hours']
print(f"The maximum value in the diff_hours column is {max_diff_hours:.2f} hours.")
```

Answer: 66.87 Hours

## Question 5. User Interface

Spark’s User Interface which shows application's dashboard runs on which local port?

80
443
4040
8080

Answer: 4040

## Question 6. Most frequent pickup location zone

Load the zone lookup data into a temp view in Spark
Zone Data

Using the zone lookup data and the fhvhv June 2021 data, what is the name of the most frequent pickup location zone?

East Chelsea
Astoria
Union Sq
Crown Heights North

## Solution:


```sh
df_join1 = df.join(df_zones, df.PULocationID == df_zones.LocationID)

df_join1.groupby("Zone").count().orderBy(desc("count")).display()
```

Answer: Crown Heights North

## Submitting the solutions

* Form for submitting: https://forms.gle/dBkVK9yT8cSMDwuw7
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 07 March (Monday), 22:00 CET
