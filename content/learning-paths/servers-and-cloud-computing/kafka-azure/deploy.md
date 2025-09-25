---
title: Install Kafka
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Kafka on Azure Cobalt 100

This section walks you through installing latest version of Apache Kafka on an Ubuntu Pro 24.04 Arm virtual machine. You’ll download Kafka, extract it into `/opt`, configure permissions, and verify the installation by checking the installed version.

Follow the below instructions to install Kafka on Ubuntu Pro 24.04 virtual machine.

### Install Java

Kafka requires Java to run. Install it by executing the following commands:
```console
sudo apt update
sudo apt install -y default-jdk
```
### Download and Install Kafka

This sequence of commands downloads Kafka version 4.1.0 to the `/opt` directory, extracts the tarball, renames the folder to kafka for simplicity, and sets ownership so the current user can access and manage the Kafka installation. It prepares the system for running Kafka without permission issues.

```console
cd /opt
sudo curl -O https://archive.apache.org/dist/kafka/4.1.0/kafka_2.13-4.1.0.tgz
sudo tar -xvzf kafka_2.13-4.1.0.tgz
sudo mv kafka_2.13-4.1.0 kafka
sudo chown -R $USER:$USER kafka
```
{{% notice Note %}}
Kafka [3.5.0 release announcement](https://kafka.apache.org/blog#apache_kafka_350_release_announcement) includes a significant number of new features and fixes, including improving Kafka Connect and MirrorMaker 2. They aren't Arm-specific, but can benefit all architectures, including Linux/Arm64.
The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Apache Kafka version 3.5.0 as the minimum recommended on Arm platforms.
{{% /notice %}}

### Check installed Kafka version

These commands navigate to the Kafka installation directory and check the installed Kafka version, confirming that Kafka has been successfully installed and is ready for use.
```console
cd /opt/kafka
bin/kafka-topics.sh --version
```

You should see an output similar to:
```output
4.1.0
```
Kafka installation is complete. You can now proceed with the baseline testing.
