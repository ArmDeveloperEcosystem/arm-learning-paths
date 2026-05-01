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

Before you begin, switch to the root user and install all required system packages. This ensures you have the correct Java version, build tools, and database dependencies for Spark, Hadoop, Hive, and Gluten on Arm64.

```console
sudo -i
apt update
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

Set the hostname to `spark-master` so Hadoop and Spark can communicate reliably on a single-node cluster. This prevents common networking issues during service startup.

```console
hostnamectl set-hostname spark-master
exec bash
```

## Configure hosts

Prevents connection errors (very important)

Append the hostname to `/etc/hosts` to ensure all Hadoop and Spark services resolve the local node correctly.

```console
echo "127.0.0.1 spark-master" >> /etc/hosts
```

## Setup passwordless SSH

**Why?**

- Hadoop services use SSH internally.

Generate an SSH key pair for passwordless authentication. Hadoop daemons use SSH to manage services internally, so this step is required for smooth operation.

```console
ssh-keygen -t rsa -P ""
```

When prompted to enter the file location, press Enter to accept the default:

```output
Enter file in which to save the key (/root/.ssh/id_rsa):
Your identification has been saved in /root/.ssh/id_rsa
Your public key has been saved in /root/.ssh/id_rsa.pub
```

Append the public key to `authorized_keys` to enable passwordless SSH for the root user:

```console
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

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

Download and extract Apache Spark 3.4.2 built for Hadoop 3. This is the main analytics engine for running SQL and DataFrame workloads.

```console
wget https://archive.apache.org/dist/spark/spark-3.4.2/spark-3.4.2-bin-hadoop3.tgz
tar -xvf spark-3.4.2-bin-hadoop3.tgz
ln -s spark-3.4.2-bin-hadoop3 spark
```

## Install Hive

Hive provides:

- Metadata (table structure)
- SQL layer for Spark

Download and extract Apache Hive 3.1.3. Hive provides the SQL metadata layer and metastore for Spark SQL.
```console
wget https://archive.apache.org/dist/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz
tar -xvf apache-hive-3.1.3-bin.tar.gz
ln -s apache-hive-3.1.3-bin hive
```

## Environment variables

Set up environment variables for Java, Hadoop, Spark, and Hive. This ensures all commands and scripts can find the correct binaries and configuration files.

```console
cat >> ~/.consolerc <<EOF

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
export HADOOP_HOME=/opt/hadoop
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
export YARN_CONF_DIR=${HADOOP_HOME}/etc/hadoop
export SPARK_HOME=/opt/spark
export HIVE_HOME=/opt/hive

export PATH=\$JAVA_HOME/bin:\$HADOOP_HOME/bin:\$SPARK_HOME/bin:\$HIVE_HOME/bin:\$PATH

EOF
```

Apply the environment changes to your current shell:

```console
source ~/.consolerc
```

## Hadoop directory setup

HDFS needs storage directories.

Create the required HDFS storage directories for the NameNode and DataNode. This is necessary for Hadoop to manage its file system state.

```console
mkdir -p $HADOOP_HOME/dfs/name
mkdir -p $HADOOP_HOME/dfs/data
mkdir -p /opt/dfs/data
```

## Configure Hadoop

Define cluster behavior (single node setup)

**core-site.xml**

Create a minimal `core-site.xml` to define the default HDFS URI for your single-node cluster.

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

Create a minimal `hdfs-site.xml` to configure HDFS for single-node operation.

```console
cat > $HADOOP_HOME/etc/hadoop/hdfs-site.xml <<EOF
<configuration>
<property>
    <name>dfs.replication</name>
    <value>1</value>
</property>
<property>
    <name>dfs.hosts</name>
    <value>/opt/hadoop/etc/hadoop/workers</value>
</property>
<property>
    <name>dfs.namenode.name.dir</name>
    <value>file:/opt/hadoop/dfs/name</value>
</property>
<property>
    <name>dfs.namenode.data.dir</name>
    <value>file:/opt/hadoop/dfs/data</value>
</property>
<property>
    <name>dfs.datanode.data.dir</name>
    <value>/opt/dfs/data</value>
</property>
</configuration>
EOF
```

**yarn-site.xml (ARM optimized)**

Create a minimal `yarn-site.xml` optimized for Arm64, specifying the resource manager hostname and available resources.

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

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64

export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
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

export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh
```

The output from `start-dfs.sh` is similar to:

```output
Starting namenodes on [spark-master]
Starting datanodes
Starting secondary namenodes [spark-master]
```

The output from `start-yarn.sh` is similar to:

```output
Starting resourcemanager
Starting nodemanagers
```

**Verify:**

```console
jps
```

The output is similar to:
```output
53856 ResourceManager
54469 Jps
54245 NodeManager
53526 SecondaryNameNode
53036 NameNode
53276 DataNode
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

## Configure Hive to use MySQL

By default, Hive uses the embedded Derby database for its metastore. Derby does not support MySQL SQL syntax, which causes the schema initialization to fail. You need to download the MySQL JDBC connector and configure Hive to connect to the MySQL metastore you created in the previous step.

Download the MySQL JDBC connector:

```console
wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.28/mysql-connector-java-8.0.28.jar -P $HIVE_HOME/lib/
```

Create `hive-site.xml` with the MySQL connection details:

```console
cat > $HIVE_HOME/conf/hive-site.xml <<EOF
<configuration>
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://localhost/hive_metastore?createDatabaseIfNotExist=true</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.cj.jdbc.Driver</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>hiveuser</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>123456</value>
  </property>
  <property>
    <name>hive.metastore.schema.verification</name>
    <value>false</value>
  </property>
</configuration>
EOF
```

## Initialize Hive

Initialize the Hive metastore schema in MySQL and start the Hive metastore service in the background. This step is required before Spark can use Hive tables for SQL analytics.

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

Build the Gluten project with the Velox backend to enable native C++ query execution in Spark. This process downloads all dependencies, compiles the engine, and prepares the JARs needed for Spark integration. The `sed` commands ensure the build targets Spark 3.4 and disables S3 support for simplicity.

```console
cd /opt
git clone https://github.com/apache/incubator-gluten.git
cd incubator-gluten
git checkout v1.3.0
sed -i 's/SPARK_VERSION=ALL/SPARK_VERSION=3.4/' dev/builddeps-veloxbe.sh
sed -i 's/--enable_s3=ON//g' dev/package.sh
./dev/package.sh
mkdir -p /opt/gluten-jars
cp package/target/*.jar /opt/gluten-jars/
```

## Configure Spark (Gluten enabled)

Configure Spark to use the Gluten plugin and Velox backend by creating a `spark-defaults.conf` file. This enables native execution, sets resource limits, and ensures the correct JARs are loaded for both the driver and executors.

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

Start the Spark Thrift Server, which allows you to connect to Spark SQL using JDBC/ODBC clients. This is the main entry point for running SQL queries and benchmarks.

```console
$SPARK_HOME/sbin/start-thriftserver.sh
```

**Validation**

```console
jps
```

The output is similar to:

```output
53856 ResourceManager
229942 Jps
54245 NodeManager
229910 ExecutorLauncher
53526 SecondaryNameNode
229637 SparkSubmit
55622 RunJar
53036 NameNode
53276 DataNode
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

