---
# User change
title: "Background"

weight: 2

layout: "learningpathall"
---

## Background


##### Advantages of using Amazon DynamoDB 

Amazon Web Services (AWS) provides a fully-managed NoSQL database service called Amazon DynamoDB, which is designed to deliver fast and predictable performance with seamless scalability. DynamoDB allows users to offload the administrative burdens of operating and scaling a distributed database, so they don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. It offers built-in security, backup and restore, and in-memory caching for internet-scale applications. DynamoDB supports key-value and document data structures, making it an ideal choice for IoT, and many other applications that require low-latency data access at any scale.

##### Partitioning

Amazon DynamoDB uses partitioning, which is a mechanism that allows the database to scale horizontally, and distribute large amounts of data across multiple servers while ensuring quick data access and high availability. The system automatically manages the partitioning of data based on the table's primary key. DynamoDB tables use a primary key that can either be single-attribute (a partition key) or composite (a partition key and a sort key). The partition key's value is used by DynamoDB as input to an internal hash function, which outputs the partition in which the data will be stored. Each item's partition key value is hashed, and the resulting hash value determines the physical partition where the item and its associated values are stored. This approach helps in evenly distributing data across partitions, maximizing scalability and performance. 

As the amount of data in DynamoDB grows, or the throughput requirements change, DynamoDB can increase the number of partitions to distribute data across additional nodes. This enables the database to maintain consistent performance, despite an increase in workload. Users do not need to manually manage partitions, DynamoDB automatically partitions the data in the background, adjusting its placement to optimize performance and storage efficiency. This feature is particularly useful in handling uneven data access patterns, or what is often referred to as "hot keys." When you provision read and write throughput capacity on your DynamoDB table, the service ensures that this capacity is evenly distributed across all partitions. This feature helps to avoid performance bottlenecks and ensures that the database can handle large volumes of concurrent read and write operations.

##### Rules Engine

The Rules Engine in AWS IoT Core is a powerful feature designed to process and route data between IoT devices and other AWS services or external endpoints. It provides the necessary tools to create scalable and efficient IoT applications by enabling real-time data processing and decision-making based on the messages published to AWS IoT Core. 

The Rules Engine evaluates incoming MQTT messages published to AWS IoT Core based on the rules you define. Each rule is essentially an SQL-like query that selects data from specific MQTT topics as messages arrive. Users define rules using an SQL-like syntax that allows selecting and processing data from the MQTT messages. For instance, you can specify conditions to filter and extract data from the message payload. After processing the messages, the Rules Engine can perform various actions based on the data and conditions specified in the rule. Actions include sending data to other AWS services such as Lambda, DynamoDB, S3, or external HTTP endpoints, making it highly versatile in integrating with broader AWS capabilities. The Rules Engine can transform or enrich the incoming data before sending it to another service. This includes operations like concatenating strings, calculating new values, or even using functions to modify the data format.

The AWS IoT Core Rules Engine dramatically simplifies the development of IoT solutions by efficiently managing data flow and enabling complex, condition-based actions directly within the IoT infrastructure. This leads to more responsive, dynamic, and efficient IoT systems.

In this Learning Path, you learn how to use the Rules Engine from AWS IoT Core to capture data sent from the IoT emulator running on an Arm64-powered device. The data is automatically written to the DynamoDB database.
