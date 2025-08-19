---
title: Install Apache Spark on Microsoft Azure Cobalt 100 processors
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Apache Spark

Install Java, Python, and essential tools on Azure Cobalt 100, then download, configure, and verify Apache Spark for use on the Arm-based platform.
### Install Required Packages 

```console
sudo tdnf update -y
sudo tdnf install -y java-17-openjdk java-17-openjdk-devel git maven wget nano curl unzip tar
sudo dnf install -y python3 python3-pip
```
Verify Java and Python installation:
```console
java -version
python3 --version
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
Spark installation is complete. You can now proceed with the baseline testing.
