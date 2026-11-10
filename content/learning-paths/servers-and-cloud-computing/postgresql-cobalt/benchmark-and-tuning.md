---
title: Benchmark and optimize PostgreSQL on Cobalt 200
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Measure and improve database performance

In this section, you benchmark PostgreSQL performance and optimize query execution using monitoring and indexing techniques.

At the end of this section, your PostgreSQL deployment is:

* Benchmarked for transactional performance
* Monitored using built-in extensions
* Optimized with indexes
* Tuned for better query execution

## Initialize benchmark dataset

Run the following commands from your VM terminal, after leaving any `psql` session with `\q`. Use `pgbench` to prepare a benchmarking dataset. Initializing this dataset recreates the `pgbench_*` tables in `appdb`; use only the tutorial database.

```console
sudo -u postgres pgbench -i -s 50 appdb
```

At scale factor 50, the command creates standard benchmarking tables, including 5,000,000 account rows, and loads data for testing. The output looks similar to:

```output
dropping old tables...
NOTICE:  table "pgbench_accounts" does not exist, skipping
NOTICE:  table "pgbench_branches" does not exist, skipping
NOTICE:  table "pgbench_history" does not exist, skipping
NOTICE:  table "pgbench_tellers" does not exist, skipping
creating tables...
generating data (client-side)...
5000000 of 5000000 tuples (100%) done (elapsed 64.70 s, remaining 0.00 s)
vacuuming...
creating primary keys...
done in 78.40 s (drop tables 0.00 s, create tables 0.01 s, client-side generate 64.87 s, vacuum 0.11 s, primary keys 13.42 s).
```

## Run benchmark test

Execute the benchmark workload.

```bash
sudo -u postgres pgbench -c 20 -j 4 -T 60 appdb
```

**Parameters used:**

- `-c 20` → number of clients
- `-j 4` → worker threads
- `-T 60` → duration (seconds)

The following result was collected on November 9, 2026, on a **Standard_D4ps_v7** Cobalt 200 VM (4 vCPUs, 16 GiB) in **West US 2**, running **Ubuntu 24.04 LTS** and **PostgreSQL 16.15** with the settings from the installation section:

```output
pgbench (16.15 (Ubuntu 16.15-0ubuntu0.24.04.1))
starting vacuum...end.
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 50
query mode: simple
number of clients: 20
number of threads: 4
maximum number of tries: 1
duration: 60 s
number of transactions actually processed: 86322
number of failed transactions: 0 (0.000%)
latency average = 13.908 ms
initial connection time = 9.057 ms
tps = 1438.044324 (without initial connection time)
```

This is a local synthetic baseline: the client and database share the VM. TPS and latency vary with storage, configuration, client count, and other running services. One run does not establish production capacity or a performance or cost comparison with other VM types.

## Enable query monitoring

Edit the PostgreSQL configuration file.

```bash
sudo nano /etc/postgresql/16/main/postgresql.conf
```

**Set the following parameter** (preserve any other libraries already listed):

```text
shared_preload_libraries = 'pg_stat_statements'
```

**Restart PostgreSQL:**

```bash
sudo systemctl restart postgresql
```

## Enable the extension

Connect as the PostgreSQL superuser:

```bash
sudo -u postgres psql -d appdb
```

Create the extension in `appdb`:

```sql
CREATE EXTENSION pg_stat_statements;
```

## Analyze query performance

The extension collects statistics after it is loaded. Run a workload first so that you have query activity to inspect:

```sql
SELECT SUM(amount) FROM orders WHERE status = 'completed';
```

Retrieve the statements with the highest total execution time:

```sql
SELECT query, total_exec_time, calls
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 5;
```

The output is similar to:

```output
                      query                       | total_exec_time | calls
--------------------------------------------------+-----------------+-------
 SELECT SUM(amount) FROM orders WHERE status = $1 |       20.698387 |     1
 CREATE EXTENSION pg_stat_statements              |        5.146237 |     1
(2 rows)
```

The output shows observed statements and their accumulated execution times in milliseconds. Run representative queries before using these statistics to investigate bottlenecks.

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
 Seq Scan on orders  (cost=0.00..10417.00 rows=252943 width=35) (actual time=0.003..35.424 rows=249671 loops=1)
   Filter: (amount > '500'::numeric)
   Rows Removed by Filter: 250329
 Planning Time: 0.060 ms
 Execution Time: 42.999 ms
(5 rows)
```

A sequential scan is expected here because a large portion of rows match the condition and there is no index on `amount`. Scan choices depend on selectivity, table size, statistics, and planner costs; there is no fixed percentage threshold.

## Add indexes for query performance

PostgreSQL automatically creates indexes on primary key columns, but not on foreign key columns. An index on `orders.customer_id` can help queries that select orders for a specific customer. Queries that aggregate most of the table may still use a sequential scan.

Leave the superuser `psql` session with `\q`, then connect from your VM terminal as the application user.

```bash
psql -h localhost -U appuser -d appdb
```

Create an index on the foreign key column.

```sql
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

Verify the index was created.

```sql
\d orders
```

The output is similar to:

```output
                                     Table "public.orders"
   Column    |            Type             | Collation | Nullable |              Default
-------------+-----------------------------+-----------+----------+------------------------------------
 id          | integer                     |           | not null | nextval('orders_id_seq'::regclass)
 customer_id | integer                     |           |          |
 amount      | numeric                     |           |          |
 status      | text                        |           |          |
 created_at  | timestamp without time zone |           |          | CURRENT_TIMESTAMP
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
    "idx_orders_customer_id" btree (customer_id)
Foreign-key constraints:
    "orders_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(id)
```

The index `idx_orders_customer_id` is now listed alongside the primary key index. Test a selective query:

```sql
EXPLAIN ANALYZE
SELECT * FROM orders WHERE customer_id = 42;
```

The output is similar to:

```output
                                                          QUERY PLAN
-------------------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=4.47..27.86 rows=6 width=35) (actual time=0.019..0.029 rows=8 loops=1)
   Recheck Cond: (customer_id = 42)
   Heap Blocks: exact=8
   ->  Bitmap Index Scan on idx_orders_customer_id  (cost=0.00..4.47 rows=6 width=0) (actual time=0.016..0.016 rows=8 loops=1)
         Index Cond: (customer_id = 42)
 Planning Time: 0.046 ms
 Execution Time: 0.034 ms
(7 rows)
```

Look for an index scan or bitmap index scan using `idx_orders_customer_id`. The plan and timings depend on the generated data and database statistics. Run `\q` to return to your VM terminal.

## Summary

You've successfully benchmarked and optimized PostgreSQL on an Arm64 system. Your setup now includes:

- Transactional benchmarking using pgbench
- Query monitoring with pg_stat_statements
- Indexed tables for improved performance
- Validated execution plans

You now have a validated PostgreSQL baseline on Cobalt 200. Use representative workloads to evaluate further tuning before production deployment.
