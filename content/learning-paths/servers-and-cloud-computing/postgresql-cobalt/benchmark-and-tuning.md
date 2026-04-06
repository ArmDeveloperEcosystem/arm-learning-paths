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
This creates standard benchmarking tables and loads data for testing. The output looks similar to:

```output
dropping old tables...
NOTICE:  table "pgbench_accounts" does not exist, skipping
NOTICE:  table "pgbench_branches" does not exist, skipping
NOTICE:  table "pgbench_history" does not exist, skipping
NOTICE:  table "pgbench_tellers" does not exist, skipping
creating tables...
generating data (client-side)...
5000000 of 5000000 tuples (100%) done (elapsed 6.32 s, remaining 0.00 s)
vacuuming...
creating primary keys...
done in 8.88 s (drop tables 0.00 s, create tables 0.02 s, client-side generate 6.36 s, vacuum 0.14 s, primary keys 2.37 s).
```

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

This result shows the transactional (OLTP) throughput PostgreSQL achieves on this Cobalt 100 Arm64 instance under the configured load. TPS and latency will vary with instance size, client count, and workload shape.

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

A sequential scan is expected because a large portion of rows match the condition. When more than roughly 10–15% of rows qualify, the planner typically prefers a sequential scan over an index scan.

## Add indexes for query performance

PostgreSQL automatically creates indexes on primary key columns, but not on foreign key columns. The `customer_id` column in the `orders` table is a foreign key that join queries filter and group by. Without an index, those joins require a full scan of the orders table.

Connect to the database as the application user if you aren't already.

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

The index `idx_orders_customer_id` is now listed alongside the primary key index. PostgreSQL's query planner will use it for queries that filter or join on `customer_id`, reducing full table scans for those operations.

You've successfully benchmarked and optimized PostgreSQL on an Arm64 system. Your setup now includes:

- Transactional benchmarking using pgbench
- Query monitoring with pg_stat_statements
- Indexed tables for improved performance
- Validated execution plans

Your PostgreSQL deployment is now ready for real-world workloads on Cobalt 100 infrastructure.
