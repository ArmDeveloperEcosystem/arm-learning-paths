---
title: Benchmark MySQL with mysqlslap
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The benefits of benchmarking with mysqlslap

Use the  built-in `mysqlslap` tool to understand how MySQL performs on Azure Cobalt 100 (Arm64) VMs.

`mysqlslap` is the official MySQL benchmarking tool used to simulate multiple client connections and measure query performance. It helps evaluate read/write throughput, query response times, and overall MySQL server performance under different workloads, making it ideal for baseline testing and optimization.

## Steps for MySQL benchmarking with mysqlslap

Set up up MySQL benchmarking with these steps.

## Connect to MySQL and create a database

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

## Create a table and populate with data

With a dedicated `benchmark_db` created, the next step is to define a test table and populate it with data. This simulates a realistic workload so that `mysqlslap` can measure query performance against non-trivial datasets.

Create a benchmark table:

```sql
CREATE TABLE benchmark_table (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    score INT
);
```
## Insert sample rows for validation

To quickly verify that inserts work correctly and test small queries, run the following command inside the MySQL shell:

```sql
INSERT INTO benchmark_table (username,score) VALUES 
('John',100),('Jane',200),('Mike',300);
```
This verifies that inserts work correctly and allows you to test small queries.

## Populate table with 1000 rows automatically

For benchmarking, larger datasets give more meaningful results. Use a stored procedure to generate rows programmatically:

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

## Run a simple read/write benchmark

With the `benchmark_table` populated, you can run a synthetic workload using mysqlslap to simulate multiple clients performing inserts or queries at the same time. This tests how well MySQL handles concurrent connections and query execution.

Use the following command:

```console
mysqlslap   --user=admin   --password=`MyStrongPassword!`   --host=127.0.0.1   --concurrency=10   --iterations=5   --query="INSERT INTO benchmark_db.benchmark_table (username,score) VALUES('TestUser',123);"   --create-schema=benchmark_db
```

The table below provides descriptions of the options used:

| Option            | Description                                                      | Example Value                |
|-------------------|------------------------------------------------------------------|------------------------------|
| `--user` / `--password` | MySQL login credentials                                         | `admin` / `MyStrongPassword!`|
| `--host`          | MySQL server address (use `127.0.0.1` for local)                  | `127.0.0.1`                  |
| `--concurrency`   | Number of simultaneous clients                                    | `10`                         |
| `--iterations`    | Number of times to repeat the test                                | `5`                          |
| `--query`         | SQL statement to run repeatedly                                   | `INSERT ...` or `SELECT ...` |
| `--create-schema` | Database in which to run the query                               | `benchmark_db`               |

You should see output similar to:

```output
Benchmark
        Average number of seconds to run all queries: 0.267 seconds
        Minimum number of seconds to run all queries: 0.265 seconds
        Maximum number of seconds to run all queries: 0.271 seconds
        Number of clients running queries: 10
        Average number of queries per client: 1
```

## Run a read benchmark (table scan):

Run the following command to simulate multiple clients querying the table concurrently and record the results:

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

## Understanding the benchmark results 

The following table lists the benchmark metrics with accompanying definitions. 

   | Metric                                   | Description                                                                                                                        |
  |-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
  | **Average number of seconds to run all queries** | The average time it took for all the queries in one iteration to complete across all clients. It gives you a quick sense of overall performance. |
  | **Minimum number of seconds to run all queries** | The fastest time any iteration of queries took.                                                                                     |
  | **Maximum number of seconds to run all queries** | The slowest time any iteration of queries took. The closer this is to the average, the more consistent your performance is.         |
  | **Number of clients running queries**     | Indicates how many simulated users (or connections) ran queries simultaneously during the test.                                     |
  | **Average number of queries per client**  | Shows the average number of queries each client executed in the benchmark iteration                                                | 

## Benchmark summary on Arm64
Here is a summary of benchmark results collected on an Arm64 D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine.

| Query Type | Average Time (s) | Minimum Time (s) | Maximum Time (s) | Clients | Avg Queries per Client |
|------------|-----------------|-----------------|-----------------|--------|----------------------|
| INSERT     | 0.267           | 0.265           | 0.271           | 10     | 1                    |
| SELECT     | 0.263           | 0.261           | 0.264           | 10     | 1                    |


## Insights from the benchmark results

The benchmark results on the Azure Cobalt 100 Arm64 VM show:

- Both `INSERT` and `SELECT` queries performed consistently, with average times of 0.267s and 0.263s respectively.
- The difference between minimum and maximum times was very small for both query types, showing stable and predictable behavior under load.
- With 10 clients and an average of 1 query per client, the system handled concurrent operations efficiently without significant delays.

MySQL on Azure Cobalt 100 Arm64 VMs provides reliable and steady performance for both data insertion and retrieval tasks, making it suitable for applications requiring dependable database operations. 