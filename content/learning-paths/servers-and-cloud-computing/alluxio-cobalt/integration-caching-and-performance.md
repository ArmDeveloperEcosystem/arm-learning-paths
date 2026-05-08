---
title: Integrate Alluxio with Apache Spark and optimize performance
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Integrate Alluxio with Apache Spark

In this section, you'll integrate Alluxio with Apache Spark, enable caching, and optimize data access performance.

You'll learn how to connect Spark with Alluxio, enable in-memory caching, and measure performance improvements as a result of reduced repeated disk reads.

<!-- ## Why integrate Alluxio with Spark?

**Without Alluxio:**

```text
Spark → Disk → Slow (every time)
```

**With Alluxio:**

```text
Spark → Alluxio → Memory → Fast
```

Alluxio caches frequently accessed data in memory, reducing repeated disk reads. -->

## Install Apache Spark

```bash
cd ~
wget https://archive.apache.org/dist/spark/spark-3.4.2/spark-3.4.2-bin-hadoop3.tgz
tar -xvzf spark-3.4.2-bin-hadoop3.tgz

sudo mv spark-3.4.2-bin-hadoop3 /opt/spark
sudo chown -R $USER:$USER /opt/spark
```

## Configure Spark environment

```bash
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin' >> ~/.bashrc
source ~/.bashrc
```

## Connect Spark with Alluxio

Open the Spark configuration file and add the Alluxio filesystem implementation and client JAR paths:

```bash
nano $SPARK_HOME/conf/spark-defaults.conf
```

```bash
spark.hadoop.fs.alluxio.impl=alluxio.hadoop.FileSystem
spark.driver.extraClassPath=/opt/alluxio/client/alluxio-2.9.4-client.jar
spark.executor.extraClassPath=/opt/alluxio/client/alluxio-2.9.4-client.jar
```

These properties register Alluxio's Hadoop-compatible filesystem implementation so Spark can resolve `alluxio://` URIs, and add the Alluxio client JAR to both the driver and executor classpaths.

## Create a dataset

Create a sample dataset in `/mnt/data/demo`. Files placed in `/mnt/data` are accessible to Spark through the `alluxio:///` URI prefix because `/mnt/data` is configured as Alluxio's root underlying file system:

```bash
rm -rf /mnt/data/demo
mkdir -p /mnt/data/demo
```

The following loop generates 100,000 records, creating a small but representative dataset for the caching benchmark:

```bash
for i in {1..100000}; do
  echo "record $i - alluxio spark learning" >> /mnt/data/demo/data.txt
done
```

Verify the file was created successfully:

```bash
wc -l /mnt/data/demo/data.txt
```

The output is similar to:

```output
100000 /mnt/data/demo/data.txt
```

## Start the Spark shell

Start the interactive Spark shell. This opens a Scala REPL with a pre-configured `SparkSession` available as `spark`. All commands in the following sections run inside this shell:

```bash
spark-shell
```

The output is similar to:

```output
Welcome to
 ____ __
 / __/__ ___ _____/ /__
 _\ \/ _ \/ _ `/ __/ '_/
 /___/ .__/\_,_/_/ /_/\_\ version 3.4.2
 /_/

Using Scala version 2.12.17 (OpenJDK 64-Bit Server VM, Java 11.0.30)
 Type in expressions to have them evaluated.
 Type :help for more information.

scala>
```

## Load data via Alluxio

```scala
val df = spark.read.text("alluxio:///demo/data.txt")
df.count()
```

The expected output is:

```output
100000
```

## Enable caching

`df.cache()` marks the DataFrame for Spark's in-memory caching. The subsequent `df.count()` triggers a full read, loading the data from Alluxio into Spark's cache. After this step, repeat reads on `df` are served from Spark's in-memory cache rather than going back through Alluxio:

```scala
df.cache()
df.count()
```

## Measure performance

First run:

```scala
val t1 = System.nanoTime()
df.count()
val t2 = System.nanoTime()
println((t2 - t1)/1e9 + " seconds")
```

Second run after caching:

```scala
val t3 = System.nanoTime()
df.count()
val t4 = System.nanoTime()
println((t4 - t3)/1e9 + " seconds")
```

Run both timing blocks and compare the printed values. The output is similar to:

```output
0.44 seconds
0.39 seconds
```

The second run is faster because Spark serves the result directly from its in-memory cache, bypassing Alluxio and the underlying storage entirely.


## Verify in Alluxio UI

Open the Alluxio UI. Replace `<VM-IP>` with the public IP of your VM:

```text
http://<VM-IP>:19999
```

![Alluxio cluster load and worker resource usage during Spark job execution on Azure Cobalt 100 VM#center](images/alluxio-load.png "Alluxio cluster load and worker utilization during processing")

![Alluxio data browser showing cached files and directories on Azure Cobalt 100 VM#center](images/alluxio-data.png "Alluxio data view displaying cached datasets")

The UI shows files stored in Alluxio namespace. You can see cached files and directories available for fast access. 

### Alluxio caching activity

After running `df.cache()` and `df.count()`, return to the Alluxio Web UI and look for:

- Increased worker memory usage in the worker summary
- Cached file blocks listed in the data browser
- Active data access reflected in the cluster metrics

{{% notice Note %}}This Learning Path uses local disk as the underlying storage to keep the setup self-contained. The performance advantage of Alluxio is most significant when the underlying storage is remote — for example, Azure Blob Storage, Amazon S3, or HDFS. In those configurations, Alluxio caches data in local worker memory after the first read, so subsequent Spark jobs access cached data at memory speed instead of making repeated remote storage round-trips.{{% /notice %}}

<!-- ## Key concepts

- Alluxio sits between compute and storage
- Frequently used data is cached in memory
- Spark reads cached data instead of disk
- This improves analytics performance significantly -->

## What you've accomplished 

You've now connected Apache Spark to Alluxio on an Azure Cobalt 100 Arm64 VM, loaded data through the Alluxio namespace, and measured the difference between an uncached and a cached read. You can verify the caching activity in the Alluxio Web UI, where worker memory usage increases and cached file blocks become visible after the first read.

To see the full performance benefit of Alluxio, you can replace the local disk UFS with a remote storage backend such as Azure Blob Storage. In that configuration, Alluxio caches data in local worker memory after the first read, eliminating repeated remote storage round-trips for subsequent Spark jobs.
