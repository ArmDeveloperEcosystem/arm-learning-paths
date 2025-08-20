---
title: How to deploy Apache Spark on Google Axion C4A Arm virtual machines
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## How to deploy Apache Spark on a Google Axion C4A Arm VM in Google Cloud

In this section you deploy Apache Spark on a Google Cloud C4A Arm virtual machine running Red Hat Enterprise Linux. You will install Java, Scala, Maven, and Spark. In the following sections you will run functional tests to validate your installation and benchmarking to compare Spark’s performance on Arm64 versus x86 architectures. 

First, SSH into the Google Cloud C4A VM you created in the previous section. 

## Install Java, Maven, and dependencies for Apache Spark on Arm

On your running VM, install Java, Maven, and the other dependencies needed for deploying Spark:

```console
sudo dnf update -y
sudo dnf install -y java-17-openjdk java-17-openjdk-devel git maven wget nano curl unzip tar
```

Verify the Java installation:

```console
java -version
```

Expected output:

```output
openjdk 17.0.16 2025-07-15 LTS
OpenJDK Runtime Environment (Red_Hat-17.0.16.0.8-1) (build 17.0.16+8-LTS)
OpenJDK 64-Bit Server VM (Red_Hat-17.0.16.0.8-1) (build 17.0.16+8-LTS, mixed mode, sharing)
```

## Install Apache Spark on a Google Axion C4A Arm VM

Download and install Apache Spark on your Arm-based VM:

```console
wget https://downloads.apache.org/spark/spark-3.5.6/spark-3.5.6-bin-hadoop3.tgz
tar -xzf spark-3.5.6-bin-hadoop3.tgz
sudo mv spark-3.5.6-bin-hadoop3 /opt/spark
```

## Configure environment variables for Apache Spark

Set the environment variables to use Spark. Add the following lines to your shell configuration scripts to make the changes persistent across sessions:

```console
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc
```

Apply the changes immediately:

```console
source ~/.bashrc 
```

## Verify Apache Spark installation on Google Axion C4A

Verify your Spark installation:

```console
spark-shell --version 
```

Expected output:

```output
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.6
      /_/

Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 17.0.15
```

Spark installation is complete. Continue to the next section to perform baseline testing of Spark.
