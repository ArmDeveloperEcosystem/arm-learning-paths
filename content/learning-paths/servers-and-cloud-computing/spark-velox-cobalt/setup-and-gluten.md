---
title: Deploy Spark SQL with Gluten + Velox on Arm64 (Stable Setup)
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy Apache Spark with Gluten + Velox on Arm64

This guide helps you **set up Spark with native acceleration (Gluten + Velox)** on Arm64 (Azure Cobalt 100).

We will build everything step-by-step from scratch.

- Apache Hadoop
- Apache Spark
- Apache Hive Metastore
- Gluten + Velox native engine

## Objective

In this guide, you will:

- Install Hadoop, Spark, and Hive
- Configure a single-node cluster
- Fix Java 17 compatibility issues
- Build Gluten with Velox backend
- Enable native execution (off-JVM)
- Prepare system for benchmarking


## Why Gluten + Velox?

- Spark (default) runs on JVM ❌
- Gluten + Velox runs queries in native C++ engine -

**Benefits:**

- Faster execution  
- Lower CPU usage  
- Better ARM performance  

## Environment

| Component | Value |
|----------|------|
| Architecture | Arm64 |
| OS | Ubuntu 22.04 / 24.04 |
| CPU | 4–8 vCPU |
| RAM | 8–32 GB |
| Disk | ≥ 80 GB |

## System preparation

We install all required tools for:

- Java (Spark/Hadoop)
- Build tools (Gluten)
- Database (Hive metastore)

```console
sudo -i

apt update -y
apt install -y \
openjdk-17-jdk wget tar git curl unzip build-essential \
python3-pip mysql-server maven cmake ninja-build pkg-config libssl-dev
```

These tools are required for:

- Java runtime (Spark/Hadoop)
- Building Gluten (C++ dependencies)
- Hive metastore (MySQL)

## Configure hostname
Hadoop requires proper hostname for internal communication.

```console
hostnamectl set-hostname spark-master
exec console
```

**Why this matters:**

- Required for Hadoop services
- Prevents cluster communication issues

## Configure hosts

Prevents connection errors (very important)

```console
echo "127.0.0.1 spark-master" >> /etc/hosts
```

## Setup passwordless SSH

**Why?**

- Hadoop services use SSH internally.

```console
ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

**Why:**

- Required for Hadoop daemons
- Enables internal communication

## Install Hadoop

**Why?**

Hadoop provides:

- HDFS → Storage
- YARN → Resource manager

```console
cd /opt

wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.1/hadoop-3.3.1-aarch64.tar.gz
tar -xvf hadoop-3.3.1-aarch64.tar.gz
ln -s hadoop-3.3.1 hadoop
```

## Install Spark

Spark is the main engine for SQL and analytics.

```console
wget https://archive.apache.org/dist/spark/spark-3.4.2/spark-3.4.2-bin-hadoop3.tgz
tar -xvf spark-3.4.2-bin-hadoop3.tgz
ln -s spark-3.4.2-bin-hadoop3 spark
```

## Install Hive

Hive provides:

- Metadata (table structure)
- SQL layer for Spark

```cnsole
wget https://archive.apache.org/dist/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz
tar -xvf apache-hive-3.1.3-bin.tar.gz
ln -s apache-hive-3.1.3-bin hive
```

## Environment variables

```console
cat >> ~/.consolerc <<EOF

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-Arm64
export HADOOP_HOME=/opt/hadoop
export SPARK_HOME=/opt/spark
export HIVE_HOME=/opt/hive

export PATH=\$JAVA_HOME/bin:\$HADOOP_HOME/bin:\$SPARK_HOME/bin:\$HIVE_HOME/bin:\$PATH

EOF

source ~/.consolerc
```

**Why?**

- So the system knows where Hadoop/Spark are installed.

## Hadoop directory setup

HDFS needs storage directories.

```console
mkdir -p $HADOOP_HOME/dfs/name
mkdir -p $HADOOP_HOME/dfs/data
mkdir -p /opt/dfs/data
```

## Configure Hadoop

Define cluster behavior (single node setup)

**core-site.xml**

```console
cat > $HADOOP_HOME/etc/hadoop/core-site.xml <<EOF
<configuration>
<property>
<name>fs.defaultFS</name>
<value>hdfs://spark-master:9000</value>
</property>
</configuration>
EOF
```

**hdfs-site.xml**

```console
cat > $HADOOP_HOME/etc/hadoop/core-site.xml <<EOF
<configuration>
<property>
<name>fs.defaultFS</name>
<value>hdfs://spark-master:9000</value>
</property>
</configuration>
EOF
```

**yarn-site.xml (ARM optimized)**

```console
cat > $HADOOP_HOME/etc/hadoop/yarn-site.xml <<EOF
<configuration>
<property><name>yarn.resourcemanager.hostname</name><value>spark-master</value></property>
<property><name>yarn.nodemanager.resource.memory-mb</name><value>8192</value></property>
<property><name>yarn.nodemanager.resource.cpu-vcores</name><value>4</value></property>
</configuration>
EOF
```

## Java 17 compatibility fix

- Without this → Hadoop & Spark crash

```console
cat >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh <<EOF

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-Arm64

export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export YARN_NODEMANAGER_USER=root

export HADOOP_OPTS="--add-opens java.base/java.lang=ALL-UNNAMED"

EOF
```

**Why:**

- Fixes Java 17 reflection issues
- Required for Spark + Gluten stability

## Start Hadoop

```console
hdfs namenode -format

$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh
```

**Verify:**

```console
jps
hdfs dfs -ls /
```

The output is similar to:
```output
159473 DataNode
159876 Jps
159260 NameNode
159725 SecondaryNameNode
108254 RunJar
```

## Setup Hive Metastore

Hive stores table metadata.

```console
mysql -u root <<EOF
CREATE DATABASE hive_metastore;
CREATE USER 'hiveuser'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON hive_metastore.* TO 'hiveuser'@'localhost';
FLUSH PRIVILEGES;
EOF
```

## Initialize Hive

```console
$HIVE_HOME/bin/schematool -dbType mysql -initSchema
nohup hive --service metastore &
```

The output is similar to:

```output
Initialization script completed
schemaTool completed
```

## Build Gluten with Velox

This enables native execution (C++).

```console
cd /opt
git clone https://github.com/apache/incubator-gluten.git
cd incubator-gluten
git checkout v1.3.0
sed -i 's/SPARK_VERSION=ALL/SPARK_VERSION=3.4/' dev/builddeps-veloxbe.sh
sed -i 's/--enable_s3=ON//g' dev/package.sh
mkdir -p /opt/gluten-jars
cp package/target/*.jar /opt/gluten-jars/
```

## Configure Spark (Gluten enabled)

```console
cat > $SPARK_HOME/conf/spark-defaults.conf <<EOF

spark.master yarn

spark.executor.instances 2
spark.executor.cores 2
spark.executor.memory 3g

spark.driver.memory 3g

spark.sql.shuffle.partitions 50

spark.plugins org.apache.gluten.GlutenPlugin
spark.gluten.enabled true

spark.memory.offHeap.enabled true
spark.memory.offHeap.size 2g

spark.gluten.sql.columnar.backend.lib velox

spark.driver.extraClassPath /opt/gluten-jars/*
spark.executor.extraClassPath /opt/gluten-jars/*

EOF
```

## Start Spark Thrift Server

```console
$SPARK_HOME/sbin/start-thriftserver.sh
```

**Validation**

```console
jps
```

The output is similar to:

```output
159473 DataNode
159911 SparkSubmit
160009 Jps
159260 NameNode
159725 SecondaryNameNode
108254 RunJar
```

##  What You Have Accomplished

You have successfully:

- Installed Hadoop, Spark, and Hive  
- Configured a stable Arm64 single-node cluster  
- Fixed Java 17 compatibility issues for Hadoop/Spark  
- Built and integrated Gluten with the Velox backend  
- Enabled native (off-JVM) query execution  
- Optimized Spark configuration for ARM workloads  
- Prepared the environment for large-scale analytics  

## What’s Next

Now that the platform is fully ready, the next step is to **evaluate performance**.

In the next phase, you will:

- Generate TPC-DS dataset (10GB)  
- Load data into HDFS  
- Create Spark SQL tables  
- Run analytical queries  
- Measure execution time  
- Compare performance improvements  

