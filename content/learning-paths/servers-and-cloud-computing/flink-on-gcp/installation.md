---
title: Install Apache Flink
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Apache Flink on GCP VM
This guide walks you through installing **Apache Flink** and its required dependencies on a **Google Cloud Platform (GCP) SUSE Arm64 Virtual Machine (VM)**. By the end of this section, you will have a fully configured Flink environment ready for job execution and benchmarking.

###  Update the System and Install Java
Before installing Flink, ensure your system packages are up to date and Java is installed.

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y java-17-openjdk java-17-openjdk-devel
```
This step ensures you have the latest system updates and the Java runtime needed to execute Flink applications.

### Download Apache Flink Binary
Next, download the pre-built binary package for **Apache Flink** from the official Apache mirror.

```console
cd /opt
sudo wget https://dlcdn.apache.org/flink/flink-2.1.1/flink-2.1.1-bin-scala_2.12.tgz
```
This command retrieves the official Flink binary distribution for installation on your VM.

{{% notice Note %}}
Flink 2.0.0 introduced Disaggregated State Management architecture, which enables more efficient resource utilization in cloud-native environments, ensuring high-performance real-time processing while minimizing resource overhead.
You can view [this release note](https://flink.apache.org/2025/03/24/apache-flink-2.0.0-a-new-era-of-real-time-data-processing/)

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Flink version 2.0.0, the minimum recommended on the Arm platforms.
{{% /notice %}}

### Extract the Downloaded Archive
Extract the downloaded `.tgz` archive to make the Flink files accessible for configuration.

```console
sudo tar -xvzf flink-2.1.0-bin-scala_2.12.tgz
```
After extraction, you will have a directory named `flink-2.1.0` under `/opt`.

**Rename the extracted directory for convenience:**
For easier access and management, rename the extracted Flink directory to a simple name like `/opt/flink`.

```console
sudo mv flink-2.1.0 /opt/flink
```
This makes future references to your Flink installation path simpler and more consistent.

### Configure Environment Variables
Set the environment variables so the Flink commands are recognized system-wide. This ensures you can run `flink` from any terminal session.

```console
echo "export FLINK_HOME=/opt/flink" >> ~/.bashrc
echo "export PATH=\$FLINK_HOME/bin:\$PATH" >> ~/.bashrc
```

Additionally, create a dedicated log directory for Flink and assign proper permissions:
```console
sudo mkdir -p /opt/flink/log
sudo chown -R $(whoami):$(id -gn) /opt/flink/log
sudo chmod -R 755 /opt/flink/log
```

**Apply the changes:**

```console
source ~/.bashrc
```

### Verify the Installation
To confirm that Flink has been installed correctly, check its version:

```console
flink -v
```

You should see an output similar to:

```output
Version: 2.1.0, Commit ID: 4cb6bd3
```
This confirms that Apache Flink has been installed and is ready for use.
