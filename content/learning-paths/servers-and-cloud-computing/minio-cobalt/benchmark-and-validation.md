---
title: Benchmark and Validate MinIO Storage
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you evaluate MinIO's performance and validate its compatibility with the Amazon S3 API.

## High-throughput benchmark

### Generate test data

Create a 1 GB dataset using random data to simulate a large object storage workload.

```bash
mkdir dataset
dd if=/dev/urandom of=dataset/file1.bin bs=100M count=10
```

The output is similar to:

```output
10+0 records in
10+0 records out
1048576000 bytes (1.0 GB, 1000 MiB) copied, 2.46018 s, 426 MB/s
```

### Benchmark upload throughput

Measure the time required to upload the dataset.

```bash
time mc cp --recursive dataset local/ml-datasets/
```

The output is similar to:

```output
...r/dataset/file1.bin: 1000.00 MiB / 1000.00 MiB ┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃ 108.90 MiB/s 9s
real    0m9.277s
user    0m0.812s
sys     0m0.353s
```

### Benchmark download throughput

Measure the time required to retrieve the dataset.

```bash
time mc cp --recursive local/ml-datasets dataset-download
```

The output is similar to:

```output
...l-datasets/test.txt: 1000.00 MiB / 1000.00 MiB ┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃ 1.50 GiB/s 0s
real    0m0.739s
user    0m0.058s
sys     0m0.494s
```

## Performance summary on Azure Cobalt 100

Running on a D4ps_v6 Cobalt 100 instance, MinIO achieved ~108 MiB/s upload throughput and ~1.50 GiB/s download throughput for 1 GB transfers. Upload time was approximately 9 seconds and download completed in under one second.

The asymmetry between upload and download speeds is typical for object storage on local disk. The high download throughput is well suited to inference workloads and analytics pipelines that read large datasets repeatedly.

## Validate S3 compatibility using Python

MinIO implements the Amazon S3 API, which means any application or SDK written for S3 can connect to MinIO without modification. You can verify this using the `boto3` Python SDK.


### Create a virtual environment

Ubuntu 24.04 restricts global pip installs, so you need a virtual environment to install `boto3`. Create and activate one with:

```bash
python3 -m venv minio-env
source minio-env/bin/activate
```

### Install boto3

```bash
pip install boto3
```

### Create a test script

Create a Python script that connects to MinIO using the `boto3` S3 client and lists your buckets. The script reads the password from the `MINIO_ROOT_PASSWORD` environment variable. Run the command below to create the file directly without using a text editor:

```bash
cat << 'EOF' > s3_test.py
import boto3
import os

s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='admin',
    aws_secret_access_key=os.environ['MINIO_ROOT_PASSWORD']
)

response = s3.list_buckets()
print("Buckets:")
for bucket in response['Buckets']:
    print(f"  {bucket['Name']} (created {bucket['CreationDate'].strftime('%Y-%m-%d')})")
EOF
```

### Run the script

```bash
python s3_test.py
```

The output is similar to:

```output
Buckets:
  ml-datasets (created 2026-03-24)
```

A successful response confirms MinIO accepts S3 API requests and returns bucket metadata in the same format as AWS S3.

When you're done, deactivate the virtual environment:

```bash
deactivate
```

## What you've learned and what's next

In this section, you learned how to:

- Benchmark MinIO for high-throughput workloads
- Measure upload and download performance
- Interpret performance metrics
- Validate S3 compatibility using Python

In the next section, you will:

- Use MinIO in a real AI/ML workflow
- Store datasets and model artifacts
- Simulate production data pipelines
