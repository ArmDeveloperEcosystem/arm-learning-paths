---
title: Benchmark and Tune PostgreSQL
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Benchmark and Tune PostgreSQL

In this section, you benchmark PostgreSQL performance and optimize query execution using monitoring and indexing techniques.

At the end of this section, your PostgreSQL deployment is:

* Benchmarked for transactional performance  
* Monitored using built-in extensions  
* Optimized with indexes  
* Tuned for better query execution  

## Initialize benchmark dataset

Use `pgbench` to prepare a benchmarking dataset.

```console
sudo -u postgres pgbench -i -s 50 appdb
```
This creates standard benchmarking tables and loads data for testing.

## Run benchmark test

Execute the benchmark workload.

```bash
sudo -u postgres pgbench -c 20 -j 4 -T 60 appdb
```

**Parameters used:**

- `c 20` → number of clients
- `j 4` → worker threads
- `T 60` → duration (seconds)

The output is similar to:

```output
pgbench (16.13 (Ubuntu 16.13-0ubuntu0.24.04.1))
starting vacuum...end.
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 50
query mode: simple
number of clients: 20
number of threads: 4
maximum number of tries: 1
duration: 60 s
number of transactions actually processed: 144162
number of failed transactions: 0 (0.000%)
latency average = 8.327 ms
initial connection time = 10.771 ms
tps = 2401.873115 (without initial connection time)
```

This demonstrates strong transactional (OLTP) performance on Cobalt 100 ARM64 infrastructure.

## Enable query monitoring

Edit the PostgreSQL configuration file.

```bash
sudo nano /etc/postgresql/16/main/postgresql.conf
```

**Add the following parameter:**

```bash
shared_preload_libraries = 'pg_stat_statements'
```

**Restart PostgreSQL:**

```bash
sudo systemctl restart postgresql
```

## Enable the extension

```bash
sudo -u postgres psql -d appdb
```

```sql
CREATE EXTENSION pg_stat_statements;
```

## Analyze query performance

Retrieve the most expensive queries:

```sql
SELECT query, total_exec_time, calls
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 5;
```

The output is similar to:

```output
                query                | total_exec_time | calls
-------------------------------------+-----------------+-------
 CREATE EXTENSION pg_stat_statements |        6.995225 |     1
(1 row)
```

This helps identify performance bottlenecks.

## Analyze query execution

Run an execution plan for a sample query.

```sql
EXPLAIN ANALYZE
SELECT * FROM orders WHERE amount > 500;
```

The output is similar to:

```output
                                                   QUERY PLAN
----------------------------------------------------------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..10417.00 rows=248493 width=35) (actual time=0.015..60.679 rows=250660 loops=1)
   Filter: (amount > '500'::numeric)
   Rows Removed by Filter: 249340
 Planning Time: 0.248 ms
 Execution Time: 69.429 ms
(5 rows)
```

A sequential scan is expected because a large portion of rows match the condition.

## What you've accomplished

You've successfully benchmarked and optimized PostgreSQL on an Arm64 system. Your setup now includes:

- Transactional benchmarking using pgbench
- Query monitoring with pg_stat_statements
- Indexed tables for improved performance
- Validated execution plans

Your PostgreSQL deployment is now ready for real-world workloads on Cobalt 100 infrastructure.
