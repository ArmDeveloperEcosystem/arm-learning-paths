---
title: Establish a ClickHouse baseline on Arm
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Establish a ClickHouse baseline

This section shows you how to validate that ClickHouse is functioning correctly and establish a basic performance baseline on your SUSE Linux Arm64 virtual machine.

### Verify ClickHouse is running

Verify that the ClickHouse server is running:

```console
sudo systemctl status clickhouse-server
```

The output is similar to:

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

Connect to the ClickHouse server using the client:

```console
clickhouse client
```

### Create a test database and table

Create a test database and table to establish a controlled environment for baseline evaluation:

```sql
CREATE DATABASE baseline_test;
USE baseline_test;
```

The output is similar to:

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

Create a table optimized for analytics:

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

The output is similar to:

```output
Query id: 62ce9b9c-9a7b-45c8-9a58-fa6302b13a88

Ok.

0 rows in set. Elapsed: 0.011 sec.
```

### Insert baseline test data

Data insertion loads a small, controlled dataset to simulate real event data and validate write functionality. Insert sample data (10,000 rows):

```sql
INSERT INTO events
SELECT
    now() - number,
    number,
    'click'
FROM numbers(10000);
```

The output is similar to:

```output
Query id: af860501-d903-4226-9e10-0e34467f7675

Ok.

10000 rows in set. Elapsed: 0.003 sec. Processed 10.00 thousand rows, 80.00 KB (3.36 million rows/s., 26.86 MB/s.)
Peak memory usage: 3.96 MiB.
```

Verify the row count:

```sql
SELECT count(*) FROM events;
```

The output is similar to:

```output
Query id: 644f6556-e69b-4f98-98ec-483ee6869d6e

   ┌─count()─┐
1. │   10000 │
   └─────────┘

1 row in set. Elapsed: 0.002 sec.
```

### Baseline read performance test

{{% notice Note %}}
The results below are intended to establish a baseline for this environment and configuration, not to serve as a comprehensive benchmark or comparison.
{{% /notice %}}

Run a simple filtered count query:

```sql
SELECT count(*) FROM events WHERE event_type = 'click';
```

The output is similar to:

```output
Query id: bd609de4-c08e-4f9f-804a-ee0528c94e4d

   ┌─count()─┐
1. │   10000 │
   └─────────┘

1 row in set. Elapsed: 0.003 sec. Processed 10.00 thousand rows, 130.00 KB (2.98 million rows/s., 38.71 MB/s.)
Peak memory usage: 392.54 KiB.
```

Run a query that groups events by date and counts occurrences:

```sql
SELECT
    toDate(event_time) AS date,
    count(*) AS total_events
FROM events
GROUP BY date
ORDER BY date;
```

The output is similar to:

```output
Query id: b3db69f8-c885-419f-9900-53d258f0b996

   ┌───────date─┬─total_events─┐
1. │ 2025-11-27 │        10000 │
   └────────────┴──────────────┘

1 row in set. Elapsed: 0.002 sec. Processed 10.00 thousand rows, 40.00 KB (4.08 million rows/s., 16.33 MB/s.)
Peak memory usage: 785.05 KiB.
```

Exit the client:

```console
exit
```

## What you've accomplished and what's next

You’ve validated that ClickHouse is stable and functional on the Arm64 virtual machine and established a basic performance baseline you can build on.
