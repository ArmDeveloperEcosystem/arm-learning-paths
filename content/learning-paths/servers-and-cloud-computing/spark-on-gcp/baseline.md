---
title: Baseline Testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


Since Apache Spark is installed successfully on your GCP C4A Arm virtual machine, let's now perform simple baseline testing to validate that Spark runs correctly and gives expected output. 

## Spark Baseline Test

Create a simple Spark job file: 
```console
nano ~/spark_baseline_test.scala
```
Below is this content of **spark_baseline_test.scala** file:

```scala
val data = Seq(1, 2, 3, 4, 5) 
val distData = spark.sparkContext.parallelize(data) 
 
// Basic transformation and action 
val squared = distData.map(x => x * x).collect() 
 
println("Squared values: " + squared.mkString(", ")) 
```
Code Explanation:
This code is a basic Apache Spark example in Scala, demonstrating how to create an RDD (Resilient Distributed Dataset), perform a transformation, and collect results.

What it does, step by step:

- **val data = Seq(1, 2, 3, 4, 5)** : Creates a local Scala sequence of integers.
- **val distData = spark.sparkContext.parallelize(data)** : Uses parallelize to convert the local sequence into a distributed RDD (so Spark can operate on it in parallel across cluster nodes or CPU cores).
- **val squared = distData.map(x => x * x).collect()** : `map(x => x * x)` squares each element in the list, `.collect()` brings all the transformed data back to the driver program as a regular Scala collection.
- **println("Squared values: " + squared.mkString(", "))** : Prints the squared values, joined by commas.


### Run the Test in Spark Shell

Run the test in the interactive shell: 
```console
spark-shell < ~/spark_baseline_test.scala 
```
You should see an output similar to:
```output
Squared values: 1, 4, 9, 16, 25
```
This confirms that Spark is working correctly with its driver, executor, and cluster manager in local mode. 
 
