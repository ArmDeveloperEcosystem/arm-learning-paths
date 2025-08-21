---
title: Validate Apache Spark on Azure Cobalt 100 Arm64 VMs
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a functional test of Apache Spark on Azure Cobalt 100 

After installing Apache Spark on your Arm64 virtual machine, you can perform simple baseline testing to validate that Spark runs correctly and produces the expected output.

## Create a test Spark application

Use a text editor of your choice to create a file named `test_spark.py` with the following content:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Test").getOrCreate()
df = spark.createDataFrame([(1, "ARM64"), (2, "Azure")], ["id", "name"])
df.show()
spark.stop()
```

## Run the Spark application

Execute the test script with:

```console
spark-submit test_spark.py
```

## Example output

You should see output similar to:

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

## Output summary

- Spark successfully generated code (10.5 ms) and executed a simple DataFrame operation.  
- The test data **[1, "ARM64"]** and **[2, "Azure"]** was displayed before cleanly shutting down (exitCode 0).  
- This confirms a working Spark deployment on Arm64.  
