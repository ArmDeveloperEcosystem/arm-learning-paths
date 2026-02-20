---
title: Real-Time Sensor Data Ingestion on Arm64
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Real-Time Sensor Data Ingestion

In this section, you simulate real-time sensor data using Python and continuously ingest it into TimescaleDB running on an Arm64 VM. This creates a live time-series data stream that can later be visualized using Grafana.

## Architecture Overview

```text
Python Sensor Generator
        |
        v
TimescaleDB Hypertable
```

- A Python script acts as a sensor, generating temperature readings.
- Each reading is written to TimescaleDB.
- TimescaleDB stores the data in a hypertable, optimized for time-series workloads.

This architecture mirrors real-world IoT and telemetry pipelines.

## Install Python Dependencies (SUSE)

```bash
cd $HOME
sudo zypper install -y \
  python3 \
  python3-pip \
  python3-psycopg2
```

**Verify psycopg2:**

```bash
python3 - <<EOF
import psycopg2
print("psycopg2 OK")
EOF
```

The output is similar to:

```output
psycopg2 OK
```

- Confirms that the PostgreSQL driver is correctly installed.
- If the import succeeds, Python can communicate with TimescaleDB.

## Create Sensor Table

```bash
sudo -u postgres psql sensors
```

```psql
CREATE TABLE sensor_data (
  time        TIMESTAMPTZ NOT NULL,
  sensor_id   TEXT NOT NULL,
  temperature DOUBLE PRECISION
);

SELECT create_hypertable('sensor_data', 'time');
```

Created a sensor_data table and converted it into a hypertable for efficient time-series storage.

Press "CTRL-D" to exit back into the SSH shell.

## Create Sensor Ingestion Script

Python script simulates multiple sensors sending readings every 2 seconds and inserts them into TimescaleDB.

Create a new Python file called **sensor_ingest.py** and add the following code to the file:

```python
import time
import random
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="sensors",
    user="postgres",
    host="localhost"
)

cur = conn.cursor()

sensors = ["sensor-1", "sensor-2", "sensor-3"]

while True:
    cur.execute(
        "INSERT INTO sensor_data VALUES (%s, %s, %s)",
        (
            datetime.utcnow(),
            random.choice(sensors),
            round(random.uniform(20, 35), 2)
        )
    )
    conn.commit()
    time.sleep(2)
```

## Run Ingestion in Background

Start the ingestion process as a background job:

```bash
nohup python3 sensor_ingest.py > ingest.log 2>&1 &
```

This ensures the sensor generator continues running even after you close the terminal.

### Verify Data Ingestion

```bash
ps -ef | grep sensor_ingest.py
```

The output is similar to:

```output
gcpuser   5398  2841  0 08:55 pts/0    00:00:00 python3 sensor_ingest.py
gcpuser   5401  2841  0 08:55 pts/0    00:00:00 grep --color=auto sensor_ingest.py
```

```bash
sudo -u postgres psql sensors -c "SELECT COUNT(*) FROM sensor_data;"
```

- Verified sensor ingestion by checking running processes and data count in TimescaleDB.
- The count should increase continuously.

The output is similar to:

```output
gcpuser@tsdb-suse-arm64:~> sudo -u postgres psql sensors -c "SELECT COUNT(*) FROM sensor_data;"
 count
-------
    14
(1 row)

gcpuser@tsdb-suse-arm64:~> sudo -u postgres psql sensors -c "SELECT COUNT(*) FROM sensor_data;"
 count
-------
    15
(1 row)

gcpuser@tsdb-suse-arm64:~> sudo -u postgres psql sensors -c "SELECT COUNT(*) FROM sensor_data;"
 count
-------
    16
(1 row)
```

## Time-Series Optimization

These steps make TimescaleDB production-ready.

### Create Index for Faster Queries

```bash
sudo -u postgres psql sensors
```

Issue the following SQL command:

```psql
CREATE INDEX ON sensor_data (sensor_id, time DESC);
```

This index:

- Improves Grafana query performance
- Optimized for time-range scans

### Enable Data Retention Policy

Automatically remove old data after 7 days:

```sql
SELECT add_retention_policy(
  'sensor_data',
  INTERVAL '7 days'
);
```

- Prevents disk exhaustion
- Runs automatically in the background

### Create Continuous Aggregate (Hourly Averages)

```sql
CREATE MATERIALIZED VIEW sensor_hourly_avg
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', time) AS bucket,
  sensor_id,
  AVG(temperature) AS avg_temp
FROM sensor_data
GROUP BY bucket, sensor_id;
```

Precomputes hourly averages per sensor for faster reporting.

### Add Aggregate Refresh Policy

```sql
SELECT add_continuous_aggregate_policy(
  'sensor_hourly_avg',
  INTERVAL '1 day',
  INTERVAL '1 hour',
  INTERVAL '5 minutes'
);
```

Automates hourly aggregate refresh every 5 minutes for near real-time analytics.

### What this means

| Setting | Meaning            |
| ------- | ------------------ |
| 1 day   | Recompute last day |
| 1 hour  | Skip newest data   |
| 5 min   | Refresh interval   |

### Validate Optimization

```sql
SELECT * FROM sensor_hourly_avg LIMIT 5;
SELECT COUNT(*) FROM sensor_data;
```

Ensures ingestion and aggregation are running correctly and data is available for queries.

The output is similar to:

```output
postgres=# SELECT * FROM sensor_hourly_avg LIMIT 5;
         bucket         | sensor_id |     avg_temp
------------------------+-----------+-------------------
 2026-02-17 08:00:00+00 | sensor-1  |  26.6380487804878
 2026-02-17 08:00:00+00 | sensor-2  |             27.21
 2026-02-17 08:00:00+00 | sensor-3  | 28.13413793103448
(3 rows)

postgres=# SELECT COUNT(*) FROM sensor_data;
 count
-------
  2466
(1 row)


```

Please press "CTRL-D" to exit.

### Set the postgres password

Lets set a password for postgres:

```bash
sudo -u postgres psql
```

Then enter the new password:

```sql
\password postgres
```

Save the password as it will be used in the next section. Please press "CTRL-D" to exit.

## What you've accomplished and what's next

You've successfully:

- Built a fully functioning real-time sensor data ingestion pipeline
- Created TimescaleDB hypertables optimized for time-series storage
- Implemented retention policies to automatically manage data lifecycle
- Created continuous aggregates for faster reporting and analytics
- Set up automated refresh policies for near real-time analytics
- Set the postgres password for use in the Grafana plugin

Next, you'll install Grafana, configure TimescaleDB as a data source, and build a live sensor temperature dashboard to visualize the real-time data you're ingesting.
