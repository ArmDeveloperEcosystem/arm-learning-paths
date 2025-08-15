---
title: Baseline Testing
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Baseline Testing
Since Apache Spark is installed successfully on your Arm virtual machine, let's now perform simple baseline testing to validate that Spark runs correctly and gives expected output.

Run a simple PySpark script, create a file named `test_spark.py`, and add the below content to it:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Test").getOrCreate()
df = spark.createDataFrame([(1, "ARM64"), (2, "Azure")], ["id", "name"])
df.show()
spark.stop()
```
Execute with:
```console
spark-submit test_spark.py
```
You should see an output similar to:

```output
25/07/22 05:16:00 INFO CodeGenerator: Code generated in 10.545923 ms
25/07/22 05:16:00 INFO SparkContext: SparkContext is stopping with exitCode 0.
+---+-----+
| id| name|
+---+-----+
|  1|ARM64|
|  2|Azure|
+---+-----+
```
Output summary:

- The output shows Spark successfully generated code **(10.5ms)** and executed a simple DataFrame operation.
- Displaying the test data **[1, "ARM64"]** and **[2, "Azure"]** before cleanly shutting down **(exitCode 0)**. This confirms a working Spark deployment on Arm64.
