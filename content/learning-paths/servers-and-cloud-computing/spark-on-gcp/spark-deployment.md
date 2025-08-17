---
title: Deploy Apache Spark on a Google Axion C4A virtual machine
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Deploy Apache Spark on Google Axion C4A virtual machine

In this section you will learn how to deploy Apache Spark on a Google Cloud C4A Arm virtual machine running Red Hat Enterprise Linux. You will install Java, Scala, Maven, and Spark. In the following sections you will run functional tests to validate your installation and benchmarking to compare Spark’s performance on Arm64 versus x86 architectures. 

First, SSH into the Google Cloud C4A VM you created in the previous section. 

On your running VM, install Java, Maven and the other dependencies needed for deploying Spark:


### Install Required Packages 

```console
sudo dnf update -y
sudo dnf install -y java-17-openjdk java-17-openjdk-devel git maven wget nano curl unzip tar
```
Verify Java installation: 
```console
java -version
```
The output will look like:

```output
openjdk 17.0.16 2025-07-15 LTS
OpenJDK Runtime Environment (Red_Hat-17.0.16.0.8-1) (build 17.0.16+8-LTS)
OpenJDK 64-Bit Server VM (Red_Hat-17.0.16.0.8-1) (build 17.0.16+8-LTS, mixed mode, sharing)
```

### Install Apache Spark on Arm

You can now download and install Apache Spark on your running Arm-based virtual machine:

```console
wget https://downloads.apache.org/spark/spark-3.5.6/spark-3.5.6-bin-hadoop3.tgz
tar -xzf spark-3.5.6-bin-hadoop3.tgz
sudo mv spark-3.5.6-bin-hadoop3 /opt/spark
```
### Set Environment Variables
Setup the environment variables to use Spark.
 
Add the lines below to your shell configuration scripts to make the change persistent across terminal sessions:

```console
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc

```
Apply changes immediately by sourcing the script:

```console
source ~/.bashrc 
```

### Verify Spark Installation 

You can now verify your Spark installation:

```console
spark-shell --version 
```
The output should look similar to: 

```output
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.6
      /_/

Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 17.0.15
```
Spark installation is complete. You can now proceed to the next section where you perform baseline testing of Spark.
