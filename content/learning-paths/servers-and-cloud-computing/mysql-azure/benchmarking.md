---
title: Benchmark MySQL with mysqlslap
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark with mysqlslap

To understand how MySQL performs on Azure Cobalt 100 (Arm64) VMs, you can use the built-in `mysqlslap` tool.

`mysqlslap` is the official MySQL benchmarking tool used to simulate multiple client connections and measure query performance. It helps evaluate read/write throughput, query response times, and overall MySQL server performance under different workloads, making it ideal for baseline testing and optimization.

## Steps for MySQL Benchmarking with mysqlslap

1. Connect to MySQL and Create a Database

Before running `mysqlslap`, you will create a dedicated test database so that benchmarking doesn’t interfere with your application data. This ensures clean test results and avoids accidental modifications to production schemas.
Connect to MySQL using the admin user:

```console
mysql -u admin -p 
```
Once logged in, create a benchmarking database:

```sql
CREATE DATABASE benchmark_db;
USE benchmark_db;
```

2. Create a Table and Populate Data

With a dedicated `benchmark_db` created, the next step is to define a test table and populate it with data. This simulates a realistic workload so that `mysqlslap` can measure query performance against non-trivial datasets.

Create a benchmark table:

```sql
CREATE TABLE benchmark_table (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    score INT
);
```
Insert Sample Rows Manually:

For quick validation:
```sql
INSERT INTO benchmark_table (username,score) VALUES 
('John',100),('Jane',200),('Mike',300);
```
This verifies that inserts work correctly and allows you to test small queries.

Populate Automatically with 1000 Rows

For benchmarking, larger datasets give more meaningful results. You can use a stored procedure to generate rows programmatically:

```sql
DELIMITER //
CREATE PROCEDURE populate_benchmark_data()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 1000 DO
        INSERT INTO benchmark_table (username, score)
        VALUES (CONCAT('Player', i), i*10);
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

CALL populate_benchmark_data();
DROP PROCEDURE populate_benchmark_data;
```
At this stage, you have a populated `benchmark_table` inside `benchmark_db`. This provides a realistic dataset for running `mysqlslap`, enabling you to measure how MySQL performs on Azure Cobalt 100 under read-heavy, write-heavy, or mixed workloads.

## Run a Simple Read/Write Benchmark

With the `benchmark_table` populated, you can run a synthetic workload using mysqlslap to simulate multiple clients performing inserts or queries at the same time. This tests how well MySQL handles concurrent connections and query execution.

```console
mysqlslap   --user=admin   --password=`MyStrongPassword!`   --host=127.0.0.1   --concurrency=10   --iterations=5   --query="INSERT INTO benchmark_db.benchmark_table (username,score) VALUES('TestUser',123);"   --create-schema=benchmark_db
```
- **--user / --password:** MySQL login credentials.
- **--host:** MySQL server address (127.0.0.1 for local).
- **--concurrency:** Number of simultaneous clients (here, 10).
- **--iterations:** How many times to repeat the test (here, 5).
- **--query:** The SQL statement to run repeatedly.
- **--create-schema:** The database in which to run the query.

You should see output similar to:

```output
Benchmark
        Average number of seconds to run all queries: 0.267 seconds
        Minimum number of seconds to run all queries: 0.265 seconds
        Maximum number of seconds to run all queries: 0.271 seconds
        Number of clients running queries: 10
        Average number of queries per client: 1
```

Run a Read Benchmark (table scan):

You can now run a test that simulates multiple clients querying the table at the same time and records the results:

```console
mysqlslap --user=admin --password="MyStrongPassword!"  --host=127.0.0.1 --concurrency=10 --iterations=5 --query="SELECT * FROM benchmark_db.benchmark_table WHERE record_id < 500;"  --create-schema=benchmark_db  --verbose | tee -a /tmp/mysqlslap_benchmark.log
```

You should see output similar to:

```output
Benchmark
        Average number of seconds to run all queries: 0.263 seconds
        Minimum number of seconds to run all queries: 0.261 seconds
        Maximum number of seconds to run all queries: 0.264 seconds
        Number of clients running queries: 10
        Average number of queries per client: 1
```

## Benchmark Results Table Explained:

  Average number of seconds to run all queries: This is the average time it took for all the queries in one iteration to complete across all clients. It gives you a quick sense of overall performance.
  Minimum number of seconds to run all queries: This is the fastest time any iteration of queries took.
  Maximum number of seconds to run all queries: This is the slowest time any iteration of queries took. The closer this is to the average, the more consistent your performance is.
  Number of clients running queries: Indicates how many simulated users (or connections) ran queries simultaneously during the test.
  Average number of queries per client: Shows the average number of queries each client executed in the benchmark iteration.

## Benchmark summary on Arm64:
Here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine**.

| Query Type | Average Time (s) | Minimum Time (s) | Maximum Time (s) | Clients | Avg Queries per Client |
|------------|-----------------|-----------------|-----------------|--------|----------------------|
| INSERT     | 0.267           | 0.265           | 0.271           | 10     | 1                    |
| SELECT     | 0.263           | 0.261           | 0.264           | 10     | 1                    |


## Insights from Benchmark Results

The benchmark results on the Arm64 virtual machine show:

  Balanced Performance for Read and Write Queries: Both `INSERT` and `SELECT` queries performed consistently, with average times of 0.267s and 0.263s, respectively.
  Low Variability Across Iterations: The difference between the minimum and maximum times was very small for both query types, indicating stable and predictable behavior under load.
  Moderate Workload Handling: With 10 clients and an average of 1 query per client, the system handled concurrent operations efficiently without significant delays.
  
This demonstrates that the MySQL setup on Arm64 provides reliable and steady performance for both data insertion and retrieval tasks, making it a solid choice for applications requiring dependable database operations.
