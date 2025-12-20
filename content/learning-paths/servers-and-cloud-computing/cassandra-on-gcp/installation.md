---
title: Install Apache Cassandra
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Apache Cassandra on Ubuntu or SUSE

This guide shows you how to install Apache Cassandra on an Ubuntu or SUSE Linux virtual machine. Cassandra is a highly scalable NoSQL database designed for high availability and fault tolerance.

## Update system packages

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt update
  {{< /tab >}}
  {{< tab header="SUSE Linux" language="bash">}}
sudo zypper refresh
sudo zypper update -y
  {{< /tab >}}
{{< /tabpane >}}

## Install Java

Cassandra requires a Java runtime environment. This example uses Java 17 for optimal performance and compatibility with Cassandra 5.0.5.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt install -y openjdk-17-jdk
  {{< /tab >}}
  {{< tab header="SUSE Linux" language="bash">}}
sudo zypper install -y java-17-openjdk java-17-openjdk-devel
  {{< /tab >}}
{{< /tabpane >}}

## Download Cassandra

```console
wget https://downloads.apache.org/cassandra/5.0.5/apache-cassandra-5.0.5-bin.tar.gz
```

{{% notice Note %}}
Apache Cassandra 5.0 is a major release introducing significant performance, usability, and scalability enhancements. Key features include Storage Attached Indexes (SAI) for flexible querying, Trie-based memtables/SSTables for better efficiency, and the Unified Compaction Strategy (UCS) for automated data management. It also supports JDK 17 for up to 20% performance gains and adds vector search for AI applications. The release marks the end-of-life for the 3.x series, urging users to upgrade for continued support. To learn more, see the [Apache Cassandra 5.0 announcement](https://cassandra.apache.org/_/blog/Apache-Cassandra-5.0-Announcement.html).

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Cassandra version 5.0.0 as the minimum recommended on Arm platforms.
{{% /notice %}}

## Extract and set up Cassandra

```console
tar -xvzf apache-cassandra-5.0.5-bin.tar.gz
mv apache-cassandra-5.0.5 ~/cassandra
```

## Add Cassandra to PATH

To run Cassandra commands from any location, add the `bin` directory to your PATH environment variable:

```console
echo 'export PATH="$HOME/cassandra/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

You can now run `Cassandra` or `cqlsh` from any terminal without specifying the full path.

## Verify installation
Check the installed Cassandra version to confirm the installation:

```console
cassandra -v
```

The output is similar to:

```output
5.0.5
```

Cassandra is now installed and ready for baseline testing.
