---
title: ClickHouse Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## ClickHouse Baseline Testing on GCP SUSE VMs
This section validates that ClickHouse is functioning correctly and provides a **basic performance baseline** on a SUSE Linux Arm64 VM.


### Verify ClickHouse is running

```console
sudo systemctl status clickhouse-server
```

This confirms that the ClickHouse server is running correctly under systemd and ready to accept connections.

```output
● clickhouse-server.service - ClickHouse Server
     Loaded: loaded (/etc/systemd/system/clickhouse-server.service; enabled; vendor preset: disabled)
     Active: active (running) since Thu 2025-11-27 05:07:42 UTC; 18s ago
   Main PID: 4229 (ClickHouseWatch)
      Tasks: 814
        CPU: 2.629s
     CGroup: /system.slice/clickhouse-server.service
             ├─ 4229 clickhouse-watchdog server --config=/etc/clickhouse-server/config.xml
             └─ 4237 /usr/bin/clickhouse server --config=/etc/clickhouse-server/config.xml
```

### Connect to ClickHouse
Client connection ensures that the ClickHouse CLI can successfully communicate with the running server.

```console
clickhouse client
```
### Create a test database and table
Database and table creation sets up a dedicated test environment and an analytics-optimized MergeTree table for baseline evaluation.

```sql
CREATE DATABASE baseline_test;
USE baseline_test;
```

You should see an output similar to:
```output
CREATE DATABASE baseline_test
Query id: bc615167-ecd5-4470-adb0-918d8ce07caf
Ok.
0 rows in set. Elapsed: 0.012 sec.


USE baseline_test
Query id: cd49553a-c0ff-4656-a3e5-f0e9fccd9eba
Ok.
0 rows in set. Elapsed: 0.001 sec.
```
Create a simple table optimized for analytics:

```sql
CREATE TABLE events
(
    event_time DateTime,
    user_id UInt64,
    event_type String
)
ENGINE = MergeTree
ORDER BY (event_time, user_id);
```

You should see an output similar to:
```output
Query id: 62ce9b9c-9a7b-45c8-9a58-fa6302b13a88

Ok.

0 rows in set. Elapsed: 0.011 sec.
```

### Insert baseline test data
Data insertion loads a small, controlled dataset to simulate real event data and validate write functionality.
Insert sample data (10,000 rows):

```sql
INSERT INTO events
SELECT
    now() - number,
    number,
    'click'
FROM numbers(10000);
```

You should see an output similar to:
```output
Query id: af860501-d903-4226-9e10-0e34467f7675

Ok.

10000 rows in set. Elapsed: 0.003 sec. Processed 10.00 thousand rows, 80.00 KB (3.36 million rows/s., 26.86 MB/s.)
Peak memory usage: 3.96 MiB.
```

**Verify row count:**

Row count validation verifies that the inserted data is stored correctly and consistently.

```sql
SELECT count(*) FROM events;
```

You should see an output similar to:
```output
Query id: 644f6556-e69b-4f98-98ec-483ee6869d6e

   ┌─count()─┐
1. │   10000 │
   └─────────┘

1 row in set. Elapsed: 0.002 sec.
```

### Baseline read performance test
Baseline read queries measure basic query performance for filtering, aggregation, and grouping, establishing an initial performance reference on the Arm64 VM.

- Run simple analytical queries:

```sql
SELECT count(*) FROM events WHERE event_type = 'click';
```

You should see an output similar to:
```output
Query id: bd609de4-c08e-4f9f-804a-ee0528c94e4d

   ┌─count()─┐
1. │   10000 │
   └─────────┘

1 row in set. Elapsed: 0.003 sec. Processed 10.00 thousand rows, 130.00 KB (2.98 million rows/s., 38.71 MB/s.)
Peak memory usage: 392.54 KiB.
```

- This query groups events by date and counts how many events occurred on each day, returning a daily summary of total events in chronological order.

```sql
SELECT
    toDate(event_time) AS date,
    count(*) AS total_events
FROM events
GROUP BY date
ORDER BY date;
```

You should see an output similar to:
```output
Query id: b3db69f8-c885-419f-9900-53d258f0b996

   ┌───────date─┬─total_events─┐
1. │ 2025-11-27 │        10000 │
   └────────────┴──────────────┘

1 row in set. Elapsed: 0.002 sec. Processed 10.00 thousand rows, 40.00 KB (4.08 million rows/s., 16.33 MB/s.)
Peak memory usage: 785.05 KiB.
```

The baseline tests confirm that ClickHouse is stable, functional, and performing efficiently on the Arm64 VM. With core operations validated, the setup is now ready for detailed performance benchmarking.
