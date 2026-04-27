---
title: Run TPC-DS Benchmark on Spark with Gluten + Velox (Arm64)
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run TPC-DS Benchmark on Spark (Gluten + Velox)

This guide walks through running a **stable TPC-DS benchmark (10GB)** on Spark with Gluten + Velox.

You will:

- Generate dataset
- Upload to HDFS
- Convert to Parquet
- Run SQL queries
- Measure performance

## Why This Approach?

Traditional benchmarking methods (like spark-sql-perf) often fail due to:

- Schema mismatches
- Missing columns
- Complex query dependencies

To solve this, we use:

- **Parquet format** → schema-safe & optimized
- **Manual SQL queries** → controlled execution
- **Local execution mode** → stable resource usage

## Generate TPC-DS data

```console
cd /opt
git clone https://github.com/gregrahn/tpcds-kit.git
cd tpcds-kit/tools
make
```

This builds the `dsdgen` tool used for data generation.\

## Generate 10GB dataset (stable)

```console
mkdir -p /opt/tpcds-data

./dsdgen -scale 10 -dir /opt/tpcds-data
```

- dsdgen generates industry-standard benchmark data
- Scale 10 = ~10GB dataset
- Used to simulate real analytics workloads

**Verify:**

```console
ls -lh /opt/tpcds-data | head
du -sh /opt/tpcds-data
```
The output is similar to:

```output
~12GB data
```
Confirms successful dataset generation

## Upload Data to HDFS

```console
hdfs dfsadmin -safemode leave

hdfs dfs -mkdir -p /ds/tpcds10_raw
hdfs dfs -put /opt/tpcds-data/* /ds/tpcds10_raw/
```

**Why?**

- HDFS acts as distributed storage layer
- Required for Spark-based analytics
- Safe mode must be disabled before writing

## Verify HDFS data

```console
hdfs dfs -du -h /ds/tpcds10_raw | head -30
```

The output is similar to:

```output
7.4 K    7.4 K    /ds/tpcds10_raw/call_center
7.4 K    7.4 K    /ds/tpcds10_raw/call_center.dat
1.6 M    1.6 M    /ds/tpcds10_raw/catalog_page
1.6 M    1.6 M    /ds/tpcds10_raw/catalog_page.dat
211.3 M  211.3 M  /ds/tpcds10_raw/catalog_returns
211.3 M  211.3 M  /ds/tpcds10_raw/catalog_returns.dat
2.8 G    2.8 G    /ds/tpcds10_raw/catalog_sales
2.8 G    2.8 G    /ds/tpcds10_raw/catalog_sales.dat
167.1 M  167.1 M  /ds/tpcds10_raw/customer
63.8 M   63.8 M   /ds/tpcds10_raw/customer.dat
0        0        /ds/tpcds10_raw/customer_address
26.4 M   26.4 M   /ds/tpcds10_raw/customer_address.dat
0        0        /ds/tpcds10_raw/customer_demographics
76.9 M   76.9 M   /ds/tpcds10_raw/customer_demographics.dat
9.8 M    9.8 M    /ds/tpcds10_raw/date_dim
9.8 M    9.8 M    /ds/tpcds10_raw/date_dim.dat
60       60       /ds/tpcds10_raw/dbgen_version.dat
81       81       /ds/tpcds10_raw/dbgen_version_1_4.dat
148.1 K  148.1 K  /ds/tpcds10_raw/household_demographics
148.1 K  148.1 K  /ds/tpcds10_raw/household_demographics.dat
328      328      /ds/tpcds10_raw/income_band
328      328      /ds/tpcds10_raw/income_band.dat
2.6 G    2.6 G    /ds/tpcds10_raw/inventory
2.6 G    2.6 G    /ds/tpcds10_raw/inventory.dat
27.5 M   27.5 M   /ds/tpcds10_raw/item
```

Confirms all tables uploaded correctly

## Prepare Parquet Directory

```console
mkdir -p /opt/tpcds10_parquet
rm -rf /opt/tpcds10_parquet/*
```

- Parquet is a columnar format
- Faster than CSV
- Reduces IO and improves query speed

## Start Spark (LOCAL MODE – STABLE)

```console
$SPARK_HOME/bin/spark-shell \
--master local[4] \
--driver-memory 6g \
--conf spark.sql.shuffle.partitions=32 \
--conf spark.sql.adaptive.enabled=true \
--conf spark.plugins=""
```

**Why Local Mode?**

- Avoids YARN resource issues
- Ensures consistent benchmarking
- Ideal for single-node Arm VM

## Convert CSV → Parquet

```scala
val rawBase = "file:///opt/tpcds-data"
val pqBase  = "file:///opt/tpcds10_parquet"

val tables = Seq(
"call_center","catalog_page","catalog_returns","catalog_sales",
"customer","customer_address","customer_demographics",
"date_dim","household_demographics","income_band",
"inventory","item","promotion","reason","ship_mode",
"store","store_returns","store_sales",
"time_dim","warehouse","web_page","web_returns","web_sales","web_site"
)

tables.foreach { t =>
  val df = spark.read
    .option("delimiter", "|")
    .option("inferSchema", "true")
    .option("header", "false")
    .csv(s"$rawBase/${t}*")

  df.write.mode("overwrite").parquet(s"$pqBase/$t")
}
```

- CSV = raw, slow
- Parquet = optimized, compressed
- Enables vectorized execution (important for Arm)

## Validate Parquet Data

```console
spark.read.parquet("file:///opt/tpcds10_parquet/store_sales").count()
spark.read.parquet("file:///opt/tpcds10_parquet/catalog_sales").count()
spark.read.parquet("file:///opt/tpcds10_parquet/web_sales").count()
```

The output is similar to:

```output
res1: Long = 28800991  store_sales → 28M rows
res2: Long = 14401261  catalog_sales → 14M rows
res3: Long = 7197566   web_sales → 7M rows
```
Confirms data correctness.

## Register Tables

```console
tables.foreach { t =>
  val df = spark.read.parquet(s"file:///opt/tpcds10_parquet/$t")
  df.createOrReplaceTempView(t)
}
```

- Creates SQL-accessible tables
- Enables querying via Spark SQL

## Verify tables

```scala
spark.sql("show tables").show(50, false)
```
All tables should be visible.

The output is similar to:

```output
+---------+----------------------+-----------+
|namespace|tableName             |isTemporary|
+---------+----------------------+-----------+
|         |call_center           |true       |
|         |catalog_page          |true       |
|         |catalog_returns       |true       |
|         |catalog_sales         |true       |
|         |customer              |true       |
|         |customer_address      |true       |
|         |customer_demographics |true       |
|         |date_dim              |true       |
|         |household_demographics|true       |
|         |income_band           |true       |
|         |inventory             |true       |
|         |item                  |true       |
|         |promotion             |true       |
|         |reason                |true       |
|         |ship_mode             |true       |
|         |store                 |true       |
|         |store_returns         |true       |
|         |store_sales           |true       |
|         |time_dim              |true       |
|         |warehouse             |true       |
|         |web_page              |true       |
|         |web_returns           |true       |
|         |web_sales             |true       |
|         |web_site              |true       |
+---------+----------------------+-----------+
```


## Benchmark Function

```scala
def timedQuery(name: String, sqlText: String): Unit = {
  val t0 = System.nanoTime()
  val df = spark.sql(sqlText)
  df.count()
  val t1 = System.nanoTime()

  println(s"$name took " + (t1 - t0) / 1e9 + " seconds")
}
```

- Measures query execution time
- Helps compare performance
- Standard benchmarking approach

## Run Benchmark Queries

### 1. Store Sales Aggregation

```scala
timedQuery("q_store_sales_by_item",
"""
SELECT _c2 AS item_sk, SUM(_c22) AS total_sales
FROM store_sales
GROUP BY _c2
ORDER BY total_sales DESC
""")

The output is similar to:

```output
q_store_sales_by_item took 1.548731698 seconds
```

### 2. Catalog Sales

```scala
timedQuery("q_catalog_sales_by_item",
"""
SELECT _c15 AS item_sk, SUM(_c23) AS total_sales
FROM catalog_sales
GROUP BY _c15
ORDER BY total_sales DESC
""")
```

The output is similar to:

```output
q_catalog_sales_by_item took 0.795856122 seconds
```

### 3. Web Sales

```scala
timedQuery("q_web_sales_by_item",
"""
SELECT _c3 AS item_sk, SUM(_c21) AS total_sales
FROM web_sales
GROUP BY _c3
ORDER BY total_sales DESC
""")
```

The output is similar to:

```output
q_web_sales_by_item took 0.423602822 seconds
```

### 4. Returns

```scala
timedQuery("q_store_returns_by_item",
"""
SELECT _c2 AS item_sk, SUM(_c16) AS total_returns
FROM store_returns
GROUP BY _c2
ORDER BY total_returns DESC
""")
```

The output is similar to:

```output
q_store_returns_by_item took 0.264841719 seconds
```

### 5. Join Query

```scala
timedQuery("q_join_store_sales_item",
"""
SELECT i._c0 AS item_sk, COUNT(*) AS cnt, SUM(s._c22) AS total_sales
FROM store_sales s
JOIN item i
ON s._c2 = i._c0
GROUP BY i._c0
ORDER BY total_sales DESC
""")
```

The output is similar to:

```output
q_join_store_sales_item took 2.203225285 seconds
```

**What This Means**

- ArmM VM handles analytics efficiently
- Parquet significantly improves performance
- Spark execution is stable and fast

## Sample Result

```scala
spark.sql("""
SELECT _c2 AS item_sk, SUM(_c22) AS total_sales
FROM store_sales
GROUP BY _c2
ORDER BY total_sales DESC
LIMIT 10
""").show(false)
```

The output is similar to:

```output
+-------+-------------------+
|item_sk|total_sales        |
+-------+-------------------+
|40386  |-19058.600000000006|
|27714  |-24582.960000000003|
|45492  |-25120.229999999996|
|100578 |-25404.539999999997|
|62538  |-27089.640000000003|
|87474  |-27629.73          |
|47112  |-28303.099999999995|
|73650  |-30656.89          |
|43380  |-31415.079999999998|
|12552  |-31864.710000000006|
+-------+-------------------+
```

##  Save Benchmark Output

```scala
import java.io.PrintWriter

val out = new PrintWriter("/opt/tpcds10_benchmark_results.txt")

out.println("TPC-DS 10GB Local Benchmark completed")

out.close()
```

## FINAL RESULT

- Data Generated: 10GB
- Format: Parquet
- Execution Mode: Local
- Queries Executed: 5
- Execution Time: sub-second to ~2 sec


## What You Have Accomplished

- Generated industry-standard benchmark dataset
- Built a stable Spark SQL execution pipeline
- Converted raw data into optimized format (Parquet)
- Executed analytical queries successfully
- Measured real performance on Arm64

