---
title: Deploy Apache Spark on Google Axion C4A virtual machine
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Deploy Apache Spark on Google Axion C4A virtual machine

This Learning Path shows how to deploy Apache Spark on a Google Cloud C4A Arm virtual machine running Red Hat Enterprise Linux. It covers installing Java, Scala, Maven, and Spark, followed by functional validation through baseline testing. 
Finally, it includes benchmarking to compare Spark’s performance on Arm64 versus x86 architectures—optimizing data processing workloads on cost-efficient Arm-based infrastructure.

### Install Required Packages 

```console
sudo tdnf update -y
sudo tdnf install -y java-17-openjdk java-17-openjdk-devel git maven wget nano curl unzip tar
```
Verify Java installation: 
```console
java -version
```

### Install Apache Spark on Arm
```console
wget https://downloads.apache.org/spark/spark-3.5.6/spark-3.5.6-bin-hadoop3.tgz
tar -xzf spark-3.5.6-bin-hadoop3.tgz
sudo mv spark-3.5.6-bin-hadoop3 /opt/spark
```
### Set Environment Variables 
Add this line to ~/.bashrc or ~/.zshrc to make the change persistent across terminal sessions.

```cosole
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc

```
Apply changes immediately

```console
source ~/.bashrc 
```

### Verify Spark Installation 

```console
spark-shell --version 
```
You should see an output similar to: 

```output
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.6
      /_/

Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 17.0.15
```
Spark installation is complete. You can now proceed with the baseline testing.
