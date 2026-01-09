---
title: Dataflow Streaming ETL to ClickHouse
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Dataflow Streaming ETL (Pub/Sub → ClickHouse)
This section implements a real-time streaming ETL pipeline that ingests events from Pub/Sub, processes them using Dataflow (Apache Beam), and writes them into ClickHouse running on a GCP Axion (Arm64) VM.

## Pipeline Overview
Flow

```bash
Pub/Sub → Dataflow (Apache Beam) → ClickHouse (Axion VM)
```

**Key components:**

- Pub/Sub: event ingestion
- Dataflow: streaming ETL and transformation
- ClickHouse: real-time analytical storage on Arm64

### Install Python 3.11 on the Axion VM
Install Python 3.11 and the required system packages

```console
sudo zypper refresh
sudo zypper install -y python311 python311-pip python311-devel gcc gcc-c++
```

Verify installation:

```console
python3.11 --version
pip3.11 --version
```

### Create a Python Virtual Environment (Recommended)
Using a virtual environment avoids dependency conflicts with the system Python.

```console
python3.11 -m venv beam-venv
source beam-venv/bin/activate
```

### Install Apache Beam with GCP Support
Install Apache Beam and the required dependencies for Dataflow:

```console
pip install --upgrade pip
pip install "apache-beam[gcp]"
pip install requests
```

Verify Beam installation:

```console
python -c "import apache_beam; print(apache_beam.__version__)"
```

### Prepare ClickHouse for Streaming Ingestion

Connect to ClickHouse on the Axion VM:

```console
clickhouse client
```

**Creates the target database and table for streaming inserts:**

```sql
CREATE DATABASE IF NOT EXISTS realtime;

CREATE TABLE IF NOT EXISTS realtime.logs
(
    event_time DateTime,
    service String,
    level String,
    message String
)
ENGINE = MergeTree
ORDER BY event_time;
```

Verify the table:

```sql
SHOW TABLES FROM realtime;
```
```output
Query id: aa25de9d-c07f-4538-803f-5473744631bc

   ┌─name─┐
1. │ logs │
   └──────┘
1 row in set. Elapsed: 0.001 sec.
```

**Exit the client:**

```sql
exit;
```

### Validate Pub/Sub (Before Dataflow)
Before running Dataflow, confirm that messages can be published and pulled.

**Publish a test message:**

```console
gcloud pubsub topics publish logs-topic \
  --message '{"event_time":"2025-12-30 12:00:00","service":"api","level":"INFO","message":"PRE-DATAFLOW TEST"}'
```

**Pull the message:**

```console
gcloud pubsub subscriptions pull logs-sub --limit=1 --auto-ack
```

```output
┌───────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────────┬──────────────┬────────────┬──────────────────┬────────────┐
│                                                DATA                                               │     MESSAGE_ID    │ ORDERING_KEY │ ATTRIBUTES │ DELIVERY_ATTEMPT │ ACK_STATUS │
├───────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────┼──────────────┼────────────┼──────────────────┼────────────┤
│ {"event_time":"2025-12-30 12:00:00","service":"api","level":"INFO","message":"PRE-DATAFLOW TEST"} │ 17590032987110080 │              │            │                  │ SUCCESS    │
└───────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────────┴──────────────┴────────────┴──────────────────┴────────────┘
```

Successful output confirms:

- Pub/Sub topic is writable
- Subscription is readable
- IAM is functioning correctly

### Create Dataflow Streaming ETL Script
Create the Dataflow pipeline file:

Purpose
Defines a streaming Beam pipeline that:

- Reads JSON events from Pub/Sub
- Parses messages
- Writes rows to ClickHouse over HTTP

```console
vi dataflow_etl.py
```
Paste the following production-ready streaming pipeline:

```python
import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

PROJECT_ID = "<GCP_PROJECT_ID>"
SUBSCRIPTION = "projects/<GCP_PROJECT_ID>/subscriptions/<PUBSUB_SUBSCRIPTION_NAME>"
CLICKHOUSE_URL = "projects/<GCP_PROJECT_ID>/subscriptions/<PUBSUB_SUBSCRIPTION_NAME>"

class ParseMessage(beam.DoFn):
    def process(self, element):
        yield json.loads(element.decode("utf-8"))

class WriteToClickHouse(beam.DoFn):
    def process(self, element):
        import requests
        row = (
            f"{element['event_time']}\t"
            f"{element['service']}\t"
            f"{element['level']}\t"
            f"{element['message']}\n"
        )
        requests.post(
            CLICKHOUSE_URL,
            data=row,
            headers={"Content-Type": "text/tab-separated-values"},
            params={"query": "INSERT INTO realtime.logs FORMAT TabSeparated"}
        )

options = PipelineOptions(
    streaming=True,
    save_main_session=True
)

with beam.Pipeline(options=options) as p:
    (
        p
        | "Read from PubSub" >> beam.io.ReadFromPubSub(subscription=SUBSCRIPTION)
        | "Parse JSON" >> beam.ParDo(ParseMessage())
        | "Write to ClickHouse" >> beam.ParDo(WriteToClickHouse())
    )
```

Pipeline logic:

- **ReadFromPubSub** → read streaming messages
- **ParseMessage** → decode JSON
- **WriteToClickHouse** → insert into ClickHouse using TabSeparated format

Replace `<GCP_PROJECT_ID>`, `<PUBSUB_SUBSCRIPTION_NAME>`, and `<CLICKHOUSE_INTERNAL_IP>` with your existing GCP project ID, Pub/Sub subscription name, and the internal IP address of your ClickHouse VM.

Below are the exact commands you can run from your VM to get each required value:

```console
gcloud config get-value project
gcloud pubsub subscriptions list
hostname -I
```

### Run the Dataflow Streaming Job
Launches the pipeline on managed Dataflow workers.

```console
python3.11 dataflow_etl.py \
  --runner=DataflowRunner \
  --project=<GCP_PROJECT_ID> \
  --region=<DATAFLOW_REGION> \
  --temp_location=gs://<GCS_TEMP_BUCKET>/temp \
  --streaming
```

- `<GCP_PROJECT_ID>` – Your Google Cloud project ID (e.g. my-project-123)
- `<DATAFLOW_REGION>` – Region where Dataflow runs (e.g. us-central1)
- `<GCS_TEMP_BUCKET>` – Existing GCS bucket used for Dataflow temp files

```output
Autoscaling is enabled for Dataflow Streaming Engine. Workers will scale between 1 and 100 unless maxNumWorkers is specified.
```

**This indicates:**

- Streaming mode is active
- Workers scale automatically

### End-to-End Validation
Publish live streaming data.

```console
gcloud pubsub topics publish logs-topic \
  --message '{"event_time":"2025-12-30 13:30:00","service":"api","level":"INFO","message":"FRESH DATAFLOW WORKING"}'
```

Verify data in ClickHouse:

```sql
SELECT *
FROM realtime.logs
ORDER BY event_time DESC
LIMIT 5;
```

Output:

```output
SELECT *
FROM realtime.logs
ORDER BY event_time DESC
LIMIT 5

Query id: 74a105d0-2e04-4053-825c-d30e53424d14

   ┌──────────event_time─┬─service───┬─level─┬─message────────────────┐
1. │ 2025-12-30 13:30:00 │ api       │ INFO  │ FRESH DATAFLOW WORKING │
2. │ 2025-12-30 13:00:00 │ api       │ INFO  │ DATAFLOW FINAL SUCCESS │
3. │ 2025-12-30 12:45:00 │ api       │ INFO  │ FINAL DATAFLOW SUCCESS │
4. │ 2025-12-30 08:48:35 │ service-0 │ INFO  │ benchmark message 0    │
5. │ 2025-12-30 08:48:34 │ service-1 │ INFO  │ benchmark message 1    │
   └─────────────────────┴───────────┴───────┴────────────────────────┘
````

This confirms:

- Pub/Sub events are streamed continuously
- Dataflow processes data in real time
- ClickHouse ingests data on Axion (Arm64) via HTTP
- The end-to-end real-time pipeline is operational

This pipeline serves as the foundation for ClickHouse latency benchmarking and real-time analytics on Google Axion.
