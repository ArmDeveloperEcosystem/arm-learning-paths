---
title: Install Kafka
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Kafka on Azure Cobalt 100

This section guides you through installing the latest version of Apache Kafka on an Ubuntu Pro 24.04 (Arm64) virtual machine running on Azure Cobalt 100. Kafka is a high-throughput, distributed event streaming platform used for real-time data pipelines and messaging applications. 

## Install Java

Apache Kafka runs on the Java Virtual Machine (JVM), so Java must be installed before setting up Kafka. Use the following commands to update your package index and install the default JDK:
```console
sudo apt update
sudo apt install -y default-jdk
```
This installs the Java Development Kit (JDK), which includes the JVM, compiler, and standard libraries required for running Kafka services.

## Download and install Kafka

Use the following commands to download and install Apache Kafka 4.1.0 in the /opt directory, extract the archive, and set appropriate permissions for your user. This prepares your system to run Kafka without requiring elevated privileges later.

```console
cd /opt
sudo curl -O https://archive.apache.org/dist/kafka/4.1.0/kafka_2.13-4.1.0.tgz
sudo tar -xvzf kafka_2.13-4.1.0.tgz
sudo mv kafka_2.13-4.1.0 kafka
sudo chown -R $USER:$USER kafka
```
{{% notice Note %}}
Kafka [3.5.0 release announcement](https://kafka.apache.org/blog#apache_kafka_350_release_announcement) includes a significant number of new features and fixes, including improving Kafka Connect and MirrorMaker 2, benefiting both x86 and Arm architectures.
The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Apache Kafka version 3.5.0 as the minimum recommended on Arm platforms.
{{% /notice %}}

## Check installed Kafka version

After extraction, verify that Kafka was installed successfully by checking the version:

```console
cd /opt/kafka
bin/kafka-topics.sh --version
```

You should see output similar to:
```output
4.1.0
```
Kafka installation is complete. You can now proceed with the baseline testing.
