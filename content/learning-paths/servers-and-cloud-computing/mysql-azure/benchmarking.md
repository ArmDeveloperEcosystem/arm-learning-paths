---
title: Benchmark MySQL with mysqlslap
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark MySQL on Azure Cobalt 100 Arm-based instances and x86_64 instances

`mysqlslap` is the official MySQL benchmarking tool used to simulate multiple client connections and measure query performance. It helps evaluate **read/write throughput, query response times**, and overall MySQL server performance under different workloads, making it ideal for baseline testing and optimization.

## Steps for MySQL Benchmarking with mysqlslap

Step 1: Ensure MySQL is Running

```console
sudo /usr/local/mysql/bin/mysqld_safe --datadir=/usr/local/mysql/data &
ps -ef | grep mysqld
```
This command starts the MySQL server in the background using the data in /usr/local/mysql/data. mysqld_safe keeps an eye on MySQL and restarts it automatically if it stops unexpectedly.

2. Connect to MySQL and Create a Database

To access MySQL, use either of these commands depending on whether your root user has a password set:

```console
mysql -u root -p      # Use this if root has a password (you will be prompted to enter it)
mysql -u root         # Use this if root has no password (insecure mode)
```
Once logged in, you can create a benchmark_db using SQL commands like:

```sql
CREATE DATABASE benchmark_db;
USE benchmark_db;
```

3. Create a Table and Populate Data

After logging into MySQL, you can create a table to store benchmark data. Here’s a simple example:

```sql
CREATE TABLE benchmark_table (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    score INT
);
```
Insert some sample rows manually:

```sql
INSERT INTO benchmark_table (username,score) VALUES 
('John',100),('Jane',200),('Mike',300);
```

Or populate automatically with 1000 rows:

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
- The table `benchmark_table` has three columns: `record_id` (primary key), `username`, and `score`.
- You can insert a few rows manually for testing or use a procedure to generate **1000 rows automatically** for more realistic benchmarking

## Run a Simple Read/Write Benchmark

Once your table is ready, you can use `mysqlslap` to simulate multiple clients performing queries. This helps test MySQL’s performance under load.

```console
mysqlslap   --user=root   --password="NewStrongPassword!"   --host=127.0.0.1   --concurrency=10   --iterations=5   --query="INSERT INTO benchmark_db.benchmark_table (username,score) VALUES('TestUser',123);"   --create-schema=benchmark_db
```
- **--user / --password:** MySQL login credentials.
- **--host:** MySQL server address (127.0.0.1 for local).
- **--concurrency:** Number of simultaneous clients (here, 10).
- **--iterations:** How many times to repeat the test (here, 5).
- **--query:** The SQL statement to run repeatedly.
- **--create-schema:** The database in which to run the query.

You should see output similar to the following:

```output
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
Benchmark
        Average number of seconds to run all queries: 0.020 seconds
        Minimum number of seconds to run all queries: 0.020 seconds
        Maximum number of seconds to run all queries: 0.022 seconds
        Number of clients running queries: 10
        Average number of queries per client: 1
```

Below command runs a **read benchmark** on your MySQL database using `mysqlslap`. It simulates multiple clients querying the table at the same time and records the results.

```console
mysqlslap --user=root --password="NewStrongPassword!"  --host=127.0.0.1 --concurrency=10 --iterations=5 --query="SELECT * FROM benchmark_db.benchmark_table WHERE record_id < 500;"  --create-schema=benchmark_db  --verbose | tee -a /tmp/mysqlslap_benchmark.log
```

You should see output similar to the following:

```output
mysqlslap: [Warning] Using a password on the command line interface can be insecure.
Benchmark
        Average number of seconds to run all queries: 0.009 seconds
        Minimum number of seconds to run all queries: 0.009 seconds
        Maximum number of seconds to run all queries: 0.010 seconds
        Number of clients running queries: 10
        Average number of queries per client: 1
```

## Benchmark Results Table Explained:

- **Average number of seconds to run all queries:** This is the average time it took for all the queries in one iteration to complete across all clients. It gives you a quick sense of overall performance.
- **Minimum number of seconds to run all queries:** This is the fastest time any iteration of queries took.
- **Maximum number of seconds to run all queries:** This is the slowest time any iteration of queries took. The closer this is to the average, the more consistent your performance is.
- **Number of clients running queries:** Indicates how many simulated users (or connections) ran queries simultaneously during the test.
- **Average number of queries per client:** Shows the average number of queries each client executed in the benchmark iteration.

## Benchmark summary on Arm64:

For easier comparison, shown here is a summary of benchmark results collected on two different Arm64 environments: a **Docker container running Azure Linux 3.0 hosted on a D4ps_v6 Ubuntu-based Azure virtual machine**, and a **D4ps_v6 Azure virtual machine created from the Azure Linux 3.0 custom image using the AArch64 ISO**.

| Environment              | Benchmark Type | Avg Time (s) | Min Time (s) | Max Time (s) | Clients | Queries per Client |
|--------------------------|----------------|--------------|--------------|--------------|---------|--------------------|
| **Value on Docker**     | Read (SELECT)  | 0.010        | 0.010        | 0.011        | 10      | 1                  |
| **Value on Docker**     | Write (INSERT) | 0.017        | 0.016        | 0.021        | 10      | 1                  |
| **Value on Virtual Machine**   | Read (SELECT)  | 0.009        | 0.009        | 0.010        | 10      | 1                  |
| **Value on Virtual Machine**   | Write (INSERT) | 0.020        | 0.020        | 0.022        | 10      | 1                  |



## Benchmark summary on x86_64:
Shown here is a summary of the benchmark results collected on two different x86_64 environments: a **Docker container running Azure Linux 3.0 hosted on a D4s_v6 Ubuntu-based Azure virtual machine**, and a **D4s_v4 Azure virtual machine created from the Azure Linux 3.0 image published by Ntegral Inc**.           

| Environment        | Benchmark Type | Avg Time (s) | Min Time (s) | Max Time (s) | Clients | Queries per Client |
|--------------------|----------------|--------------|--------------|--------------|---------|--------------------|
| **Value on Docker**          | Read (SELECT)  | 0.010        | 0.009        | 0.011        | 10      | 1                  |
|  **Value on Docker**          | Write (INSERT) | 0.021        | 0.016        | 0.031        | 10      | 1                  |
| **Value on Virtual Machine**             | Read (SELECT)  | 0.017        | 0.016        | 0.018        | 10      | 1                  |
| **Value on Virtual Machine**             | Write (INSERT) | 0.038        | 0.030        | 0.044        | 10      | 1                  |

## Benchmark comparison insights

When comparing the results on Arm64 vs x86_64 virtual machines:

- **Consistent Read Performance:** - On Arm64, both Docker and Virtual Machine environments achieved very similar `SELECT` query times **(~0.009–0.011s)**, showing low latency and high stability for read-heavy workloads.
- **Slight Variation in Write Performance:** - For `INSERT` operations, the Docker setup averaged slightly faster **(0.017s)** than the Virtual Machine **(0.020s)**, although the difference was minimal and both stayed within a narrow range.
- **Low Performance Variability:** - The Arm64 results showed very tight min-to-max ranges, indicating predictable performance across multiple test iterations, which is desirable for production workloads.
- **Key Takeaway:** - Arm64 delivered stable, low-latency MySQL performance in both Docker and VM environments, with negligible differences between the two.

You have now benchmarked MySql on an Azure Cobalt 100 Arm64 virtual machine and compared results with x86_64.
