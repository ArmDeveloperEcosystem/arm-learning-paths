---
title: Install Apache Cassandra
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Apache Cassandra Installation on Ubuntu or SuSE VM
This guide will help you install **Apache Cassandra** on a Ubuntu or SuSE Linux virtual machine. Cassandra is a highly scalable NoSQL database designed for high availability and fault tolerance.

### Update System Packages
Updating system packages ensures that your system has the latest security patches and dependencies required for Cassandra.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt update
  {{< /tab >}}
  {{< tab header="SUSE Linux" language="bash">}}
sudo zypper refresh
sudo zypper update -y
  {{< /tab >}}
{{< /tabpane >}}

### Install Java
Cassandra requires a Java runtime environment. You can use either Java 11 or Java 17. This example uses Java 17 for optimal performance and compatibility with Cassandra 5.0.5.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt install -y openjdk-17-jdk
  {{< /tab >}}
  {{< tab header="SUSE Linux" language="bash">}}
sudo zypper install -y java-17-openjdk java-17-openjdk-devel
  {{< /tab >}}
{{< /tabpane >}}

### Download Cassandra
Download the latest stable release of Apache Cassandra 5.0.5 from the official Apache repository.

```console
wget https://downloads.apache.org/cassandra/5.0.5/apache-cassandra-5.0.5-bin.tar.gz
```
{{% notice Note %}}
Apache Cassandra 5.0 is a major release introducing significant performance, usability, and scalability enhancements. Key features include Storage Attached Indexes (SAI) for flexible querying, Trie-based memtables/SSTables for better efficiency, and the Unified Compaction Strategy (UCS) for automated data management. It also supports JDK 17 for up to 20% performance gains and adds vector search for AI applications. The release marks the end-of-life for the 3.x series, urging users to upgrade for continued support.
You can view [this release note](https://cassandra.apache.org/_/blog/Apache-Cassandra-5.0-Announcement.html)

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends PHP version 5.0.0 as the minimum recommended on the Arm platforms.
{{% /notice %}}

### Extract and Setup Cassandra
Extract the downloaded archive and move it to a dedicated directory for Cassandra.

```console
tar -xvzf apache-cassandra-5.0.5-bin.tar.gz
mv apache-cassandra-5.0.5 ~/cassandra
```

### Enable Running Cassandra from Anywhere
To run Cassandra commands from any location, add the `bin` directory to your PATH environment variable:

```console
echo 'export PATH="$HOME/cassandra/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
Now you can run `Cassandra` or `cqlsh` from any terminal without specifying the full path.

### Verify Installation
Check the installed Cassandra version to confirm the installation:

```console
cassandra -v
```
You should see an output similar to:
```output
5.0.5
```
Cassadra's installation is complete. You can now proceed with the baseline testing.
