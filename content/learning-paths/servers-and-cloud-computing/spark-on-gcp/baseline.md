---
title: Baseline Testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


With Apache Spark installed successfully on your GCP C4A Arm-based virtual machine, you can now perform simple baseline testing to validate that Spark runs correctly and gives expected output. 

## Spark Baseline Test

Using a file editor of your choice, create a simple Spark job file: 
```console
nano ~/spark_baseline_test.scala
```
Copy the content below into `spark_baseline_test.scala`:

```console
val data = Seq(1, 2, 3, 4, 5) 
val distData = spark.sparkContext.parallelize(data) 
 
// Basic transformation and action 
val squared = distData.map(x => x * x).collect() 
 
println("Squared values: " + squared.mkString(", ")) 
```
This is a basic Apache Spark example in Scala, demonstrating how to create an RDD (Resilient Distributed Dataset), perform a transformation, and collect results.

Lets look into the code, step by step:

- **val data = Seq(1, 2, 3, 4, 5)** : Creates a local Scala sequence of integers.
- **val distData = spark.sparkContext.parallelize(data)** : Uses parallelize to convert the local sequence into a distributed RDD (so Spark can operate on it in parallel across cluster nodes or CPU cores).
- **val squared = distData.map(x => x * x).collect()** : `map(x => x * x)` squares each element in the list, `.collect()` brings all the transformed data back to the driver program as a regular Scala collection.
- **println("Squared values: " + squared.mkString(", "))** : Prints the squared values, joined by commas.


### Run the Test in Spark Shell

Run the test you created in the interactive shell: 
```console
spark-shell < ~/spark_baseline_test.scala 
```
The output should look similar to:
```output
Squared values: 1, 4, 9, 16, 25
```
This confirms that Spark is working correctly with its driver, executor, and cluster manager in local mode. 
 
