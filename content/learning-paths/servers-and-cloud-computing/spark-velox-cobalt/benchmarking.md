---
title: Run TPC-DS Benchmark on Spark with Gluten + Velox (Arm64)
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run TPC-DS Benchmark on Spark

TPC-DS is an industry-standard benchmark that simulates a decision support workload across a realistic retail data model. In this section you generate a 10 GB TPC-DS dataset, load it into Spark, and run five analytical queries to measure execution time on your Arm64 VM.

You run Spark in local mode using Parquet-formatted data and hand-written SQL queries. This avoids the schema mismatches and resource contention that commonly affect automated benchmarking frameworks such as `spark-sql-perf`, and gives you a reproducible, stable baseline.

## Why Parquet and local mode?

Tools like `spark-sql-perf` often fail against raw TPC-DS data because of schema mismatches between the generated CSV files and the expected column names, missing columns in certain query templates, and YARN resource allocation instability on a single-node VM.

To avoid these issues, you convert the raw data to Parquet before querying. Parquet is a columnar format that Spark reads more efficiently than CSV, and it preserves schema consistently across sessions. Running Spark in local mode eliminates YARN scheduling overhead, which makes query times more reproducible and directly comparable.

## Generate TPC-DS data

Clone the Databricks fork of `tpcds-kit` and build the `dsdgen` data generation tool. The Databricks fork is required here because the original `gregrahn/tpcds-kit` source does not build cleanly on Ubuntu 22.04 or 24.04 with GCC 10+.

```console
cd /opt
git clone https://github.com/databricks/tpcds-kit.git
cd tpcds-kit/tools
make OS=LINUX
```

## Generate 10 GB dataset

Run `dsdgen` to generate the benchmark dataset at scale factor 10, which produces approximately 10 GB of data across 24 TPC-DS tables. This step can take five to ten minutes to complete.

```console
mkdir -p /opt/tpcds-data
./dsdgen -scale 10 -dir /opt/tpcds-data
```

Verify the total size of the generated data:

```console
du -sh /opt/tpcds-data
```

The output is similar to:

```output
12G     /opt/tpcds-data
```

## Upload data to HDFS

Before uploading, take HDFS out of safe mode, which it enters automatically after a restart to protect against data loss. Then create the target directory and upload all generated files.

```console
hdfs dfsadmin -safemode leave
hdfs dfs -mkdir -p /ds/tpcds10_raw
hdfs dfs -put /opt/tpcds-data/* /ds/tpcds10_raw/
```

Verify the upload by checking the sizes of the files in HDFS:

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

## Prepare Parquet output directory

Create a local directory to hold the converted Parquet files. If the directory already exists from a previous run, clear its contents to avoid stale or duplicate data.

```console
mkdir -p /opt/tpcds10_parquet
rm -rf /opt/tpcds10_parquet/*
```

## Configure Spark to use the Hive Metastore

Before starting `spark-shell`, you need to make two configuration changes so that Spark can communicate with the Hive Metastore that was set up in the previous section.

Copy the MySQL JDBC connector into Spark's JAR directory. Spark loads all JARs in this directory at startup, so placing the connector here ensures it is available when Spark connects to the MySQL-backed metastore:

```console
cp /opt/apache-hive-3.1.3-bin/lib/mysql-connector-java-8.0.28.jar /opt/spark/jars/
```

Create a symlink so that Spark picks up the Hive configuration automatically. Spark looks for `hive-site.xml` in its own `conf/` directory at startup:

```console
ln -s /opt/apache-hive-3.1.3-bin/conf/hive-site.xml /opt/spark/conf/hive-site.xml
```

If the symlink already exists from a previous run, remove it first with `rm /opt/spark/conf/hive-site.xml` before re-creating it.

## Start Spark shell

Launch `spark-shell` in local mode with four threads and 6 GB of driver memory. Setting `spark.plugins=""` explicitly disables Gluten for this benchmarking step, establishing a baseline without the Velox native engine. You can compare these results against a Gluten-enabled run later to measure the performance difference provided by native execution.

```console
$SPARK_HOME/bin/spark-shell \
  --master local[4] \
  --driver-memory 6g \
  --conf spark.sql.shuffle.partitions=32 \
  --conf spark.sql.adaptive.enabled=true \
  --conf spark.plugins=""
```

## Convert CSV to Parquet

The raw TPC-DS files are pipe-delimited CSV with no header row. This Scala snippet reads each table into a DataFrame, infers the column schema automatically, and writes the result as Parquet. Run this inside the `spark-shell` session you just started.

```scala
val rawBase = "file:///opt/tpcds-data"
val pqBase  = "file:///opt/tpcds10_parquet"

val tables = Seq(
  "call_center", "catalog_page", "catalog_returns", "catalog_sales",
  "customer", "customer_address", "customer_demographics",
  "date_dim", "household_demographics", "income_band",
  "inventory", "item", "promotion", "reason", "ship_mode",
  "store", "store_returns", "store_sales",
  "time_dim", "warehouse", "web_page", "web_returns", "web_sales", "web_site"
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

Because the CSV files have no header row, Spark assigns generic positional column names (`_c0`, `_c1`, `_c2`, and so on). The benchmark queries in the following steps reference specific columns by these positional names. You can cross-reference column positions against the TPC-DS specification to find the semantic name for each column, for example `ss_item_sk` maps to `_c2` in `store_sales`.

## Validate Parquet data

Count the rows in three of the largest fact tables to confirm the conversion completed without data loss. Run each line individually inside your `spark-shell` session.

```scala
spark.read.parquet("file:///opt/tpcds10_parquet/store_sales").count()
spark.read.parquet("file:///opt/tpcds10_parquet/catalog_sales").count()
spark.read.parquet("file:///opt/tpcds10_parquet/web_sales").count()
```

The output is similar to:

```output
res2: Long = 28800991

res3: Long = 14401261

res4: Long = 7197566
```

The row counts confirm the Parquet conversion completed correctly: `store_sales` contains approximately 28 million rows, `catalog_sales` approximately 14 million, and `web_sales` approximately 7 million. These counts are consistent with a 10 GB TPC-DS scale factor and confirm that no data was lost or corrupted during the CSV-to-Parquet conversion step.

## Register tables

Load each Parquet table as a temporary view so you can query it using Spark SQL. Temporary views exist only for the duration of the current `spark-shell` session.

```scala
tables.foreach { t =>
  val df = spark.read.parquet(s"file:///opt/tpcds10_parquet/$t")
  df.createOrReplaceTempView(t)
}
```

Verify all 24 tables are registered:

```scala
spark.sql("show tables").show(50, false)
```

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

## Define a benchmark timing function

This helper function records wall-clock time before and after query execution, then prints the elapsed time in seconds. Calling `df.count()` forces Spark to fully materialise the query result, which is necessary to get an accurate end-to-end execution time.

```scala
def timedQuery(name: String, sqlText: String): Unit = {
  val t0 = System.nanoTime()
  val df = spark.sql(sqlText)
  df.count()
  val t1 = System.nanoTime()
  println(s"$name took " + (t1 - t0) / 1e9 + " seconds")
}
```

## Run benchmark queries

Each query uses positional column names (`_c2`, `_c22`, and so on) because the TPC-DS CSV files contain no header row. The five queries cover a range of analytical patterns: single-table aggregations across each of the three sales channels, a returns aggregation, and a dimension join.

### 1. Store sales aggregation

Aggregate total sales by item across the `store_sales` table, which at approximately 28 million rows is the largest fact table in the 10 GB dataset.

```scala
timedQuery("q_store_sales_by_item",
  """
  SELECT _c2 AS item_sk, SUM(_c22) AS total_sales
  FROM store_sales
  GROUP BY _c2
  ORDER BY total_sales DESC
  """)
```

The output is similar to:

```output
q_store_sales_by_item took 1.548731698 seconds
```

### 2. Catalog sales aggregation

Aggregate total sales by item across the `catalog_sales` table.

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

### 3. Web sales aggregation

Aggregate total sales by item across the `web_sales` table.

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

### 4. Store returns aggregation

Aggregate total returns by item from the `store_returns` table.

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

### 5. Dimension join

Join `store_sales` with the `item` dimension table to combine transaction totals with item metadata. This query exercises Spark's hash join path and involves a shuffle to co-locate matching rows, which is why it takes noticeably longer than the single-table aggregations. This query type benefits most from Velox's native join execution when Gluten is enabled.

```scala
timedQuery("q_join_store_sales_item",
  """
  SELECT i._c0 AS item_sk, COUNT(*) AS cnt, SUM(s._c22) AS total_sales
  FROM store_sales s
  JOIN item i ON s._c2 = i._c0
  GROUP BY i._c0
  ORDER BY total_sales DESC
  """)
```

The output is similar to:

```output
q_join_store_sales_item took 2.203225285 seconds
```

## Inspect sample results

To verify the query results are meaningful, display the top 10 items by total sales. Items with negative `total_sales` values appear because the TPC-DS schema includes returns and price adjustments that can reduce net sales below zero — this is expected behaviour.

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


## Summary

You've run a complete TPC-DS benchmark baseline on Spark with an Arm64 VM. These results represent execution with Gluten disabled. You can enable Gluten and re-run the same queries to measure the performance improvement provided by the Velox native engine on Arm64.


## Re-run with Gluten + Velox enabled

Now that you have a baseline, re-run the same queries with the Gluten native engine active. Gluten intercepts Spark's physical plan and replaces JVM-based operators with equivalent Velox C++ operators. The Parquet data and SQL queries are unchanged — only the `spark-shell` launch flags differ.

Exit the current `spark-shell` session:

```scala
:quit
```

Restart `spark-shell` with the Gluten plugin and off-heap memory enabled. The `--conf spark.driver.extraClassPath` flag loads the Gluten JAR that was built and copied to `/opt/gluten-jars/` during the setup step.

```console
$SPARK_HOME/bin/spark-shell \
  --master local[4] \
  --driver-memory 6g \
  --conf spark.sql.shuffle.partitions=32 \
  --conf spark.sql.adaptive.enabled=true \
  --conf spark.plugins=org.apache.gluten.GlutenPlugin \
  --conf spark.gluten.enabled=true \
  --conf spark.gluten.sql.columnar.backend.lib=velox \
  --conf spark.memory.offHeap.enabled=true \
  --conf spark.memory.offHeap.size=4g \
  --conf spark.driver.extraClassPath=/opt/gluten-jars/*
```

Once the shell starts, re-register the tables and re-define the timing function. These are identical to the baseline run — no changes are needed to the Scala code:

```scala
val pqBase = "file:///opt/tpcds10_parquet"

val tables = Seq(
  "call_center", "catalog_page", "catalog_returns", "catalog_sales",
  "customer", "customer_address", "customer_demographics",
  "date_dim", "household_demographics", "income_band",
  "inventory", "item", "promotion", "reason", "ship_mode",
  "store", "store_returns", "store_sales",
  "time_dim", "warehouse", "web_page", "web_returns", "web_sales", "web_site"
)

tables.foreach { t =>
  val df = spark.read.parquet(s"$pqBase/$t")
  df.createOrReplaceTempView(t)
}

def timedQuery(name: String, sqlText: String): Unit = {
  val t0 = System.nanoTime()
  val df = spark.sql(sqlText)
  df.count()
  val t1 = System.nanoTime()
  println(s"$name took " + (t1 - t0) / 1e9 + " seconds")
}
```

Run the same five queries:

```scala
timedQuery("q_store_sales_by_item",
  """SELECT _c2 AS item_sk, SUM(_c22) AS total_sales
     FROM store_sales GROUP BY _c2 ORDER BY total_sales DESC""")

timedQuery("q_catalog_sales_by_item",
  """SELECT _c15 AS item_sk, SUM(_c23) AS total_sales
     FROM catalog_sales GROUP BY _c15 ORDER BY total_sales DESC""")

timedQuery("q_web_sales_by_item",
  """SELECT _c3 AS item_sk, SUM(_c21) AS total_sales
     FROM web_sales GROUP BY _c3 ORDER BY total_sales DESC""")

timedQuery("q_store_returns_by_item",
  """SELECT _c2 AS item_sk, SUM(_c16) AS total_returns
     FROM store_returns GROUP BY _c2 ORDER BY total_returns DESC""")

timedQuery("q_join_store_sales_item",
  """SELECT i._c0 AS item_sk, COUNT(*) AS cnt, SUM(s._c22) AS total_sales
     FROM store_sales s JOIN item i ON s._c2 = i._c0
     GROUP BY i._c0 ORDER BY total_sales DESC""")
```

The output is similar to:

```output
q_store_sales_by_item took 2.409203993 seconds
q_catalog_sales_by_item took 0.633359991 seconds
q_web_sales_by_item took 0.552456948 seconds
q_store_returns_by_item took 0.429901026 seconds
q_join_store_sales_item took 1.579735646 seconds
```

The `GlutenFallbackReporter` warning appears for every query and is expected in this configuration. It means that the `Exchange` operator — which handles the shuffle between the partial and final aggregation stages — fell back to JVM execution. The Velox backend does not support the shuffle operator in local mode, so Gluten applies the fallback automatically rather than failing.

The query execution in this configuration follows a split path: Velox handles the Parquet scan and partial aggregation in native C++ columnar format, then converts the intermediate result to JVM row format for the shuffle, and the final aggregation runs on the JVM. This conversion at the `Exchange` boundary adds overhead for smaller queries where shuffle is cheap, but still provides a net benefit for the join query where columnar processing of the large `store_sales` table outweighs the conversion cost.

To confirm whether Gluten is executing the queries natively rather than falling back to JVM operators, inspect the executed query plan after running a query:

```scala
val df = spark.sql("""
  SELECT _c2 AS item_sk, SUM(_c22) AS total_sales
  FROM store_sales GROUP BY _c2
""")
df.count()
println(df.queryExecution.executedPlan)
```

Using `df.queryExecution.executedPlan` after calling `count()` gives you the final physical plan that was actually executed, rather than the pre-execution estimate. This is important because Spark's Adaptive Query Execution (AQE) can change the plan at runtime, and `explain()` alone — without first triggering execution — prints the pre-AQE plan with `isFinalPlan=false`.

For reference, this is what the pre-execution plan looks like when called with `explain()` before `count()`:

```output
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
+- HashAggregate(keys=[_c2#578], functions=[sum(_c22#598)])
   +- Exchange hashpartitioning(_c2#578, 32), ENSURE_REQUIREMENTS, [plan_id=1406]
      +- HashAggregate(keys=[_c2#578], functions=[partial_sum(_c22#598)])
         +- FileScan parquet [_c2#578,_c22#598] Batched: true, DataFilters: [], Format: Parquet,
            Location: InMemoryFileIndex(1 paths)[file:/opt/tpcds10_parquet/store_sales],
            PartitionFilters: [], PushedFilters: [], ReadSchema: struct<_c2:int,_c22:double>
```

The `HashAggregate` and `Exchange` operators are standard Spark JVM operators, which indicates that Gluten is falling back to JVM execution for this aggregation. However, `Batched: true` on the `FileScan` line is significant — this means Spark is reading the Parquet file in columnar batch mode, which Gluten enables for its native Parquet reader. The scan is offloaded to Velox even when the aggregation is not.

When Gluten successfully takes over the full query path, the plan would instead show operators such as `VeloxColumnarToRow`, `GlutenHashAggregateExecTransformer`, and `GlutenColumnarExchange`. If you see only standard Spark operator names, the aggregation and join operators are running on the JVM.

To check whether the Gluten plugin loaded at all, search the driver log for initialisation messages:

```console
grep -i "gluten\|velox" $SPARK_HOME/logs/spark-root-*.out | head -20
```

If Gluten loaded successfully you will see lines similar to `GlutenPlugin: Gluten build info` and `VeloxBackend: Velox backend initialised` near startup.

## Compare baseline vs Gluten + Velox


### Dimension join performance comparison

The most meaningful performance difference between JVM-only and Gluten + Velox is seen in the dimension join query, which joins the large `store_sales` fact table (28 million rows) with the `item` dimension table. This query exercises Spark's hash join and shuffle paths, and benefits most from Velox's native columnar execution before the shuffle boundary.

| Query | Baseline (JVM) | Gluten + Velox | Change |
|-------|---------------|----------------|--------|
| Dimension join (store_sales × item) | 2.203 s | 1.580 s | -28% faster |

In this scenario, Velox offloads the Parquet scan and the hash join to native C++ code, while the shuffle (`Exchange`) and final aggregation still fall back to JVM execution. The result is a significant speedup for this join-heavy query, as the most expensive part—the join itself—is accelerated by Velox. Other queries in the benchmark may not show improvement or can be slower due to the overhead of converting between columnar and row formats at the shuffle boundary, but the dimension join demonstrates the clear benefit of native execution for large, complex operations.

Full offload of the `Exchange` operator to Velox (eliminating JVM fallback) requires enabling the Gluten columnar shuffle, which is configured separately and not covered in this Learning Path.

## What you've accomplished

- Generated an industry-standard TPC-DS benchmark dataset at 10 GB scale
- Converted raw pipe-delimited CSV data to Parquet for efficient Spark querying
- Registered 24 TPC-DS tables as Spark temporary views
- Executed five analytical queries covering aggregation and join patterns on Arm64
- Captured a reproducible JVM baseline and a Gluten + Velox accelerated result for direct comparison

