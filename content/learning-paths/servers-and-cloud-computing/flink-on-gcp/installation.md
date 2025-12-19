---
title: Install Apache Flink
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Apache Flink

This section shows you how to install Apache Flink and its required dependencies on a Google Cloud Platform (GCP) SUSE Arm64 virtual machine.

### Update the system and install Java

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y java-17-openjdk java-17-openjdk-devel
```
This step ensures you have the latest system updates and the Java runtime needed to execute Flink applications.

### Download Apache Flink Binary
Navigate to /opt (a standard location for system-wide tools) and download the official Flink distribution:

```console
cd /opt
sudo wget https://dlcdn.apache.org/flink/flink-2.1.1/flink-2.1.1-bin-scala_2.12.tgz
```
This command retrieves the official Flink binary distribution for installation on your VM.

{{% notice Note %}}
Flink 2.0.0 introduced Disaggregated State Management architecture, which enables more efficient resource utilization in cloud-native environments, ensuring high-performance real-time processing while minimizing resource overhead. See [the Flink 2.0.0 Release Note](https://flink.apache.org/2025/03/24/apache-flink-2.0.0-a-new-era-of-real-time-data-processing/).

For best performance on Arm, the [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends using Flink ≥ 2.0.0.
{{% /notice %}}

### Extract the archive
Untar the archive:

```console
sudo tar -xvzf flink-2.1.1-bin-scala_2.12.tgz
```
After extraction, you will have a directory named `flink-2.1.1` under `/opt`.

Rename it for convenience:
```console
sudo mv flink-2.1.1 /opt/flink
```
This makes configuration, upgrades, and scripting easier for your Flink installation.

### Configure environment variables
Add Flink to your shell environment:

```console
echo "export FLINK_HOME=/opt/flink" >> ~/.bashrc
echo "export PATH=\$FLINK_HOME/bin:\$PATH" >> ~/.bashrc
```

Create a logging directory and assign proper permissions:

```console
sudo mkdir -p /opt/flink/log
sudo chown -R $(whoami):$(id -gn) /opt/flink/log
sudo chmod -R 755 /opt/flink/log
```
Apply the changes:

```console
source ~/.bashrc
```
Adding Flink to the global PATH lets you use commands like `flink`, `start-cluster.sh`, and `taskmanager.sh` from any terminal.

### Verify the installation
To confirm that Flink has been installed correctly, check its version:

```console
flink -v
```

You should see an output similar to:

```output
Version: 2.1.1, Commit ID: 074f8c5
```

Apache Flink is now installed and ready for use.
