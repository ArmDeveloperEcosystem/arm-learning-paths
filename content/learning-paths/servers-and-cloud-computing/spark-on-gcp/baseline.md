---
title: Apache Spark baseline testing on Google Axion C4A Arm VM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Validate Apache Spark installation with a baseline test

With Apache Spark installed successfully on your GCP C4A Arm-based virtual machine, you can now perform simple baseline testing to validate that Spark runs correctly and produces the expected output.

## Run a baseline test for Apache Spark on Arm

Use a text editor of your choice to create a simple Spark job file:

```console
nano ~/spark_baseline_test.scala
```

Add the following code to `spark_baseline_test.scala`:

```scala
val data = Seq(1, 2, 3, 4, 5)
val distData = spark.sparkContext.parallelize(data)

// Basic transformation and action
val squared = distData.map(x => x * x).collect()

println("Squared values: " + squared.mkString(", "))
```

This Scala example shows how to create an RDD (Resilient Distributed Dataset), apply a transformation, and collect results.

Here’s a step-by-step breakdown of the code:

- **`val data = Seq(1, 2, 3, 4, 5)`**: Creates a local Scala sequence of integers  
- **`val distData = spark.sparkContext.parallelize(data)`**: Converts the local sequence into a distributed RDD, so Spark can process it in parallel across CPU cores or cluster nodes  
- **`val squared = distData.map(x => x * x).collect()`**: Squares each element using `map`, then gathers results back to the driver program with `collect`  
- **`println("Squared values: " + squared.mkString(", "))`**: Prints the squared values as a comma-separated list  

## Run the Apache Spark baseline test in Spark shell

Run the test file in the interactive Spark shell:

```console
spark-shell < ~/spark_baseline_test.scala
```

Alternatively, you can start the spark shell and then load the file from inside the shell:

```console
spark-shell
```
```scala
:load spark_baseline_test.scala
```

You should see output similar to:

```output
Squared values: 1, 4, 9, 16, 25
```

This confirms that Spark is running correctly in local mode with its driver, executor, and cluster manager.
