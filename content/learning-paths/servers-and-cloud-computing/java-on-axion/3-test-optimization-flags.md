---
title: Test performance and optimize
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test Java application performance and optimize

Now that you've built the Renaissance Benchmark jar, you can use it to test some common performance optimization flags on Arm processors. You can also use it to test performance on different Java workloads between Google Cloud x86 instances and Axion instances.

In this Learning Path we are using the Renaissance Benchmarks as examples, but if you have an existing Java application that you'd like to optimize, you can perform these steps on your application instead.

## Build the Renaissance Benchmark Suite

The Renaissance Benchmark Suite is an aggregation of common workloads for the JVM. It's maintained by a collaboration of Oracle Labs and several universities around the world. The benchmarks can be used to optimize the JVM software stack, as well as test JVM performance on specific hardware.

To build the benchmark jar, first clone the repo:

```bash
git clone https://github.com/renaissance-benchmarks/renaissance.git
```

Then switch to the repo directory and run the build:

```bash
cd renaissance
tools/sbt/bin/sbt renaissancePackage
```

The jar will be built in the `target` directory. We will use this jar in the next section.

### Running the kmeans benchmark

*k*-means is a very commonly used clustering algorithm. There's an implementation built in to the Renaissance Benchmarks called scala-kmeans. We'll be using the scala-kmeans benchmark here as an example, but there are many different kinds of big data, machine-learning, and functional programming benchmarks included in the Renaissance suite. A list of them can be found on the (Renaissance docs page)[https://renaissance.dev/docs].

To run the benchmark, first change to the `target` directory that you built in the last section and list the contents of the directory:

```bash
cd target
ls -la
```

The jar that you built should look like `renaissance-gpl-{version string}.jar` where {version string} will be the version that you built. Run the jar like this, replacing the version string with your values: 

```bash
java -jar renaissance-gpl-{version string}.jar scala-kmeans --csv scala-kmeans-default.csv
```

By default the benchmark will run 50 iterations that look like this:

```
====== scala-kmeans (scala) [default], iteration 0 started ======
GC before operation: completed in 29.958 ms, heap usage 41.335 MB -> 26.363 MB.
====== scala-kmeans (scala) [default], iteration 0 completed (214.788 ms) ======
====== scala-kmeans (scala) [default], iteration 1 started ======
GC before operation: completed in 19.807 ms, heap usage 54.160 MB -> 26.348 MB.
====== scala-kmeans (scala) [default], iteration 1 completed (118.817 ms) ======
```

The `--csv scala-kmeans-default.csv` will cause the application to write the benchmark data to a CSV file. You can find the average runtime with an `awk` one-liner like this:

```bash
awk -F',' 'NR>1 {sum+=$2; count++} END {print "Average duration (ns): " (sum/count)/1000000}' scala-kmeans-default.csv
```

On a the `c4a-standard-2` instance running Ubuntu 24.04 with JDK 21, this should yield something like:

```
Average duration (ns): 116.159
```

### Try some optimizations

There are a large number of Java flags that can alter runtime performance of your applications. Here are some examples:

1. `-XX:-TieredCompilation`: This flag turns off intermediate compilation tiers. This can help if you've got a long-running applications that have predictable workloads, and/or you've observed that the warmup period doesn't significantly impact overall performance.
2. `-XX:ReservedCodeCacheSize` and `-XX:InitialCodeCacheSize`: You can increase these values if you see warnings about code cache overflow in your logs. You can decrease these values if you're in a memory constrained environment, or your application doesn't use much compiled code. The only way to determine optimal values for your application is to test.

To list and explore all of the available tuning flags for your JVM, run

```bash
java -XX:+PrintFlagsFinal -version
```

### Applying your knowledge

This Learning Path has only provided a sampling of possible benchmarks, but you can try the same steps with the other benchmarks on the (Renaissance docs page)[https://renaissance.dev/docs]. All workloads will have different performance characteristics, so if you are planning a new application, it may be helpful to find the Renaissance workload that most closely matches your planned workload, and do some tests with various settings to find the optimal JVM environment.

Ultimately, though, just remember that most performance tuning will be unnecessary, and you can just move your Java workloads to Axion with no changes required.