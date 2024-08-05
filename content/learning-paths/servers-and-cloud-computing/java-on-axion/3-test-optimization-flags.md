---
title: Test performance and optimize
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test Java application performance and optimize

Now that you've built and deployed the Spring Petclinic application, you can use it to test some common JVM performance optimization flags. You can also use it to test the performance difference between Axion instances and previous-generation Google Cloud Arm instances.

## Run performance tests with jmeter

The spring-petclinic repo includes a jmx file that you can use with the jmeter application to test spring-petclinic performance.

To install jmeter, first open a new ssh terminal to your instance (so that you don't interrupt the running spring-petclinic application in your existing terminal window) and run:

```bash
wget https://downloads.apache.org/jmeter/binaries/apache-jmeter-5.6.3.tgz
tar -xzf apache-jmeter-5.6.3.tgz
sudo mv apache-jmeter-5.6.3 /opt/jmeter
sudo ln -s /opt/jmeter/bin/jmeter /usr/local/bin/jmeter
```

To test that jmeter was installed correctly, run

```bash
jmeter --version
```

Once you have verified installation, change directories to the jmeter test file directory (assuming you are already in the spring-petclinic repo base directory):

```bash
cd src/test/jmeter
```

Assuming that the spring-petclinic jar is still running in your other ssh terminal, from your new terminal you can run

```bash
jmeter -n -t petclinic_test_plan.jmx -l results1.jtl
```

In order to test the petclinic application and write results to the `results1.jtl` file.

This file will contain tens of thousands of rows of results, but you can parse it into high level statistics like this:

```bash
jmeter -g results1.jtl -o ./summary_report1
```

This command creates an output directory called `summary_report1`, which contains a file called `statistics.json` with summary statistics.

### Best practices for optimizing your Java application

Many Java flags can alter runtime performance of your applications. Here are some examples:

1. `-XX:-TieredCompilation`: This flag turns off intermediate compilation tiers. This can help if you've got a long-running applications that have predictable workloads, and/or you've observed that the warmup period doesn't significantly impact overall performance.
2. `-XX:ReservedCodeCacheSize` and `-XX:InitialCodeCacheSize`: You can increase these values if you see warnings about code cache overflow in your logs. You can decrease these values if you're in a memory constrained environment, or your application doesn't use much compiled code. The only way to determine optimal values for your application is to test.

Your Petclinic application is a good candidate for the `-XX:-TieredCompilation` flag because it is long-running and has predictable workloads. To test this, stop the Petclinic application and re-run the jar with

```bash
java -XX:-TieredCompilation -jar target/*.jar
```

From a different window, you can run

```bash
jmeter -n -t petclinic_test_plan.jmx -l results2.jtl
```

Which will save test results from your new jar run to the results2.jtl file. You can then create a new summary report:

```bash
jmeter -g results2.jtl -o ./summary_report2
```

And then compare the contents of `summary_report1/statistics.json` to the contents of `summary_report2/statistics.json`. In the `Total` data structure you'll notice that the average response time (`meanResTime`) will be approximately 15% lower for the new run!

Run the following command to list and explore all of the available tuning flags for your JVM:

```bash
java -XX:+PrintFlagsFinal -version
```

You'll notice that this command will show you both the flags and their default settings.

Pay particular attention to the flags labeled `{ARCH product}`, since this denotes an architecture-specific flag.

Some very useful Arm-specific flags are:

* `UseLSE`: Enables the use of Large System Extensions, which are ARM-specific features that can improve performance in multi-core systems.
* `UseNeon`: When true, this enables the use of an advanced single instruction multiple data (SIMD) architecture extension that vastly improves use cases such as multimedia encoding/decoding, user interface, 2D/3D graphics and gaming.
* `UseSVE`: Enables Scalable Vector Extensions, which improves vector operation performance.

The performance tuning parameters are dependent on the application workload and its implementation. Most of the Java based workloads can be migrated to Axion with little to no changes required.
