---
title: Install Apache Spark on Azure Cobalt 100 Arm64 processors
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Apache Spark on Azure Cobalt 100 Arm64
Within your running docker container image or your custom Azure Linux VM, follow the instructions to install Spark.

Start by installing Java, Python, and other essential tools: 

## Install Java, Python, and tools for Apache Spark

```console
sudo tdnf update -y
sudo tdnf install -y java-17-openjdk java-17-openjdk-devel git maven wget nano curl unzip awk tar
sudo tdnf install -y python3 python3-pip
```
Verify Java installation:
```console
java -version
```
The output will look like:
```output
openjdk 17.0.16 2025-07-15 LTS
OpenJDK Runtime Environment Microsoft-11926147 (build 17.0.16+8-LTS)
OpenJDK 64-Bit Server VM Microsoft-11926147 (build 17.0.16+8-LTS, mixed mode, sharing)
```

Verify Python installation:
```console
python3 --version
```

The output will look like:
```output
Python 3.12.9
```

## Download and install Apache Spark on Azure Cobalt 100 (Arm64)

You can now download and configure Apache Spark on your Arm-based machine:

```console
wget https://downloads.apache.org/spark/spark-3.5.6/spark-3.5.6-bin-hadoop3.tgz
tar -xzf spark-3.5.6-bin-hadoop3.tgz
sudo mv spark-3.5.6-bin-hadoop3 /opt/spark
```
## Configure environment variables for Apache Spark
Add this line to ~/.bashrc or ~/.zshrc to make the change persistent across terminal sessions.

```cosole
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc
echo 'export JAVA_HOME=/usr/lib/jvm/msopenjdk-17/' >> ~/.bashrc
```
Apply changes immediately in your running shell:

```console
source ~/.bashrc
```

## Verify Apache Spark installation on Azure Cobalt 100

```console
spark-submit --version
```
You should see output like: 

```output
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.6
      /_/

Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 17.0.15
```
Spark installation is complete. You can now proceed with the baseline testing of Spark in the next section.
