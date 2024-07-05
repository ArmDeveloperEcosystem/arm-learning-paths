---
title: Install the JDK and build an application
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Java

Now that you have an Axion instance running Ubuntu 24.04, you can SSH into it via the Google Cloud console:

![click the console button to SSH to the machine](ssh.png)

This will bring up a separate window with a shell connected to your instance.

Java is not yet installed on this Ubuntu image, so you'll want to install Java. First update `apt`:

```bash
sudo apt update
```

Then install the default Java Runtime Environment:

```bash
sudo apt install default-jre
```

Check to ensure that the JRE is properly installed:


```bash
java -version
```

Once the JRE is installed, you will want to install the default JDK:

```bash
sudo apt install default-jdk
```

After completion of the JDK installation, check the version:

```bash
javac -version
```

{{% notice Note %}}
It's important to ensure that your version of OpenJDK is at least 11.0.9. There is a large performance gap between OpenJDK-11.0.8 and OpenJDK 11.0.9. A patch added in 11.0.9 reduces false-sharing cache contention. For more information you can view [patch JDK-8248214](https://bugs.openjdk.org/browse/JDK-8248214).
{{% /notice %}}

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


## Optional: build Apache Spark

Spark is one of the most popular Java applications in the world. It's a unified analytics engine for large-scale data processing. We will use it as an example of a real-world application that you may want to run on Axion. There are many ways to install Spark, but here you'll build it from source.

{{% notice Note %}}
This build will take around 30 minutes to complete.
{{% /notice %}}


First, clone the Spark repo:

```bash
git clone https://github.com/apache/spark.git
```

Next, cd into the repo directory and run the build script. This will take several minutes:

```bash
cd spark
./build/mvn -DskipTests clean package
```

## Optional: Deploy a Java application on Compute Engine using Google Jump Start

Google provides a Jump Start Solution to quickly deploy a load balanced Java application on Compute Engine along with a high availability database:

[Deploy a Java application using Compute Engine](https://cloud.google.com/architecture/application-development/java-app-gce)

When configuring for Axion, you will just have to change the compute type to C4A.

