## Week 6 Homework 

In this homework, there will be two sections, the first session focus on theoretical questions related to Kafka 
and streaming concepts and the second session asks to create a small streaming application using preferred 
programming language (Python or Java).

### Question 1: 

**Please select the statements that are correct**

- Kafka Node is responsible to store topics
- Zookeeper is removed from Kafka cluster starting from version 4.0
- Retention configuration ensures the messages not get lost over specific period of time.
- Group-Id ensures the messages are distributed to associated consumers

#### Answer: all

### Question 2: 

**Please select the Kafka concepts that support reliability and availability**

- Topic Replication
- Topic Paritioning
- Consumer Group Id
- Ack All

#### Answer: Topic Replication and Ack All

### Question 3: 

**Please select the Kafka concepts that support scaling**  

- Topic Replication
- Topic Paritioning
- Consumer Group Id
- Ack All

#### Answer: Topic Partitioning and Consumer Group Id

### Question 4: 

**Please select the attributes that are good candidates for partitioning key. 
Consider cardinality of the field you have selected and scaling aspects of your application**  

- payment_type
- vendor_id
- passenger_count
- total_amount
- tpep_pickup_datetime
- tpep_dropoff_datetime

#### Answer: vendor_id, tpep_pickup_datetime, tpep_dropoff_datetime

### Question 5: 

**Which configurations below should be provided for Kafka Consumer but not needed for Kafka Producer**

- Deserializer Configuration
- Topics Subscription
- Bootstrap Server
- Group-Id
- Offset
- Cluster Key and Cluster-Secret

#### Answer: Deserializer Configuration, Topics Subscription, Group-Id, Offset
