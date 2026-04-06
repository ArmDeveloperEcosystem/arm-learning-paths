---
title: Benchmark and Validate MinIO Storage
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark and Validate MinIO Storage

In this section, you evaluate MinIO's performance and validate its compatibility with the Amazon S3 API.

This step demonstrates how MinIO can handle high-throughput workloads and confirms that it can be used as a drop-in replacement for S3 in real-world applications.


## High-throughput benchmark

### Generate test data

Create a dataset to simulate large object storage workloads.

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

**Why this matters:**

- Simulates real-world large file uploads
- Helps evaluate storage throughput
- Mimics AI/ML dataset ingestion


## Upload benchmark

Measure the time required to upload data.

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

**Why this matters:**

- Shows actual upload throughput
- Helps estimate performance for large datasets
- Demonstrates MinIO efficiency on Arm

## Download benchmark

Measure the time required to retrieve data.

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

**Why this matters:**

- Demonstrates high-speed data retrieval
- Validates low-latency access for workloads
- Important for inference and analytics pipelines

## Performance summary on Azure Cobalt ARM (Arm64)

The benchmark results demonstrate strong performance characteristics of MinIO running on Azure Cobalt ARM64 infrastructure.

### Key observations

- **Upload throughput:** ~108 MiB/s  
- **Download throughput:** ~1.50 GiB/s  
- **Upload time (1 GB):** ~9 seconds  
- **Download time (1 GB):** <1 second  

### What this means

- MinIO delivers **high-throughput data ingestion**, suitable for large dataset uploads  
- Extremely fast download speeds enable **low-latency data access** for inference workloads  
- ARM64-based Cobalt processors provide **efficient and consistent performance** for storage-heavy applications  
- The system handles **GB-scale object transfers smoothly**, making it ideal for AI/ML and analytics pipelines  

### Why this is important

- AI/ML workflows require fast access to large datasets and models  
- Data pipelines benefit from high read/write throughput  
- ARM-based infrastructure provides **cost-efficient performance at scale**  

## Validate S3 compatibility (Python)

MinIO provides an S3-compatible API. In this step, you verify compatibility using the Python SDK.

- Ubuntu 24.04 restricts global pip installs, so a virtual environment is required.

## Create a virtual environment

```bash
python3 -m venv minio-env
source minio-env/bin/activate
```

**Why this matters:**

- Isolates Python dependencies
- Avoids system conflicts
- Follows best practices

## Install boto3

```bash
pip install boto3
```

## Create test script

```bash
nano s3_test.py
```

```python
import boto3

s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='admin',
    aws_secret_access_key='StrongPassword123'
)

response = s3.list_buckets()
print(response)
```

## Run the script

```bash
python s3_test.py
```

The output is similar to:

```output
{'ResponseMetadata': {'RequestId': '189FACF71514F6A5', 'HostId': 'dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8', 'HTTPStatusCode': 200, 'HTTPHeaders': {'accept-ranges': 'bytes', 'content-length': '369', 'content-type': 'application/xml', 'server': 'MinIO', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'Origin, Accept-Encoding', 'x-amz-id-2': 'dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8', 'x-amz-request-id': '189FACF71514F6A5', 'x-content-type-options': 'nosniff', 'x-ratelimit-limit': '4562', 'x-ratelimit-remaining': '4562', 'x-xss-protection': '1; mode=block', 'date': 'Tue, 24 Mar 2026 04:35:55 GMT'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'ml-datasets', 'CreationDate': datetime.datetime(2026, 3, 24, 4, 14, 28, 859000, tzinfo=tzlocal())}], 'Owner': {'DisplayName': 'minio', 'ID': '02d6176db174dc93cb1b899f7c6078f08654445fe8cf1b6ce98d8855f66bdbf4'}}
```

**Why this matters:**

- Confirms MinIO behaves like AWS S3
- Validates SDK integration capability
- Ensures compatibility with real applications

**Exit environment**

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


