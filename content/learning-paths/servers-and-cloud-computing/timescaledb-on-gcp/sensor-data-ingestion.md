---
title: Ingest real-time sensor data on Arm64
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Ingest real-time sensor data

In this section, you simulate real-time sensor data using Python and continuously ingest it into TimescaleDB running on an Arm64 VM. This creates a live time-series data stream that can later be visualized using Grafana.

## Architecture overview

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

## Install Python dependencies

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

## Create a sensor table

Connect to the sensors database and create the `sensor_data` hypertable:

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

Press Ctrl+D to exit back into the SSH shell.

## Create a sensor ingestion script

The following Python script simulates multiple sensors sending readings every two seconds and inserts them into TimescaleDB.

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

## Run ingestion in the background

Start the ingestion process as a background job so it continues running even after you close the terminal:

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

## Optimize time-series performance

These steps make TimescaleDB production-ready.

### Create an index for faster queries

Connect to the sensors database and create an index optimized for time-range scans by sensor:

```bash
sudo -u postgres psql sensors
```

Issue the following SQL command:

```psql
CREATE INDEX ON sensor_data (sensor_id, time DESC);
```

This index improves Grafana query performance for time-range scans.

### Enable a data retention policy

Automatically remove data older than seven days:

```sql
SELECT add_retention_policy(
  'sensor_data',
  INTERVAL '7 days'
);
```

This prevents disk exhaustion and runs automatically in the background.

### Create a continuous aggregate

Precompute hourly averages per sensor for faster reporting:

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

### Add an aggregate refresh policy

Automate hourly aggregate refresh every five minutes for near real-time analytics:

```sql
SELECT add_continuous_aggregate_policy(
  'sensor_hourly_avg',
  INTERVAL '1 day',
  INTERVAL '1 hour',
  INTERVAL '5 minutes'
);
```

The table below explains the three interval parameters:

| Setting | Meaning            |
| ------- | ------------------ |
| 1 day   | Recompute last day |
| 1 hour  | Skip newest data   |
| 5 min   | Refresh interval   |

### Validate the optimization

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

Press Ctrl+D to exit.

### Set the postgres password

Let's set a password for postgres so Grafana can connect in the next section:

```bash
sudo -u postgres psql
```

Then enter the new password:

```sql
\password postgres
```

Save the password — you'll need it when configuring the Grafana data source. Press Ctrl+D to exit.

## What you've accomplished and what's next

You've successfully:

- Built a fully functioning real-time sensor data ingestion pipeline
- Created TimescaleDB hypertables optimized for time-series storage
- Implemented retention policies to automatically manage data lifecycle
- Created continuous aggregates for faster reporting and analytics
- Set up automated refresh policies for near real-time analytics
- Set the postgres password for use in the Grafana plugin

Next, you'll install Grafana, configure TimescaleDB as a data source, and build a live sensor temperature dashboard to visualize the real-time data you're ingesting.
