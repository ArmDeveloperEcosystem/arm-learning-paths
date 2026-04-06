---
title: Use MinIO for AI/ML Dataset and Model Storage
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use MinIO for AI/ML Dataset and Model Storage

In this section, you simulate a real-world AI/ML workflow using MinIO.

MinIO serves as an object storage backend for datasets and trained models used in machine learning pipelines.

This demonstrates how MinIO integrates into modern data-driven and AI/ML applications.


## Architecture overview

This architecture represents a simple ML workflow using object storage.

```text
Dataset / Model Files
        │
        ▼
MinIO Object Storage (S3-compatible)
        │
        ▼
Training / Inference Workloads
```

## Scenario

You will simulate a typical ML pipeline:

- Upload a dataset
- Upload a model artifact
- Retrieve data for training or inference

## Create dataset

Create a sample dataset to represent structured training data.

```bash
mkdir ai-dataset
echo "id,name,score" > ai-dataset/data.csv
echo "1,jon,90" >> ai-dataset/data.csv
echo "2,nick,85" >> ai-dataset/data.csv
echo "3,jack,95" >> ai-dataset/data.csv
```

**Why this matters:**

- Represents structured data used in ML training
- Simulates dataset ingestion into object storage
- Mimics real-world data lake inputs

## Upload dataset

Upload the dataset to MinIO.

```bash
mc cp ai-dataset/data.csv local/ml-datasets/
```

## Verify upload

```bash
mc ls local/ml-datasets
```

You should see `data.csv` in the output.

The output is similar to:

```output
[2026-03-24 04:28:25 UTC]    43B STANDARD data.csv
[2026-03-24 04:29:59 UTC]    19B STANDARD model.bin
[2026-03-24 04:16:22 UTC]    13B STANDARD test.txt
[2026-03-24 05:21:04 UTC]     0B dataset/
```

**Why this matters:**

- Confirms successful data ingestion
- Validates object storage functionality

## Create model artifact

Simulate a trained machine learning model.

```bash
mkdir model
echo "fake-model-weights" > model/model.bin
```

**Why this matters:**

- Represents the output of training pipelines
- Mimics model registry storage

## Upload model artifact

```bash
mc cp model/model.bin local/ml-datasets/
```

## Download data for usage

Simulate retrieving data for training or inference.

```bash
mkdir download-test
mc cp --recursive local/ml-datasets download-test/
```

## Verify downloaded data

```bash
ls download-test/ml-datasets
```

You should see:

```bash
data.csv  dataset  model.bin  test.txt
```

Why this matters:

- Confirms data retrieval works correctly
- Simulates how ML jobs access datasets and models

## What this demonstrates

| Real-world concept | Implementation             |
| ------------------ | -------------------------- |
| Data lake          | Dataset stored in MinIO    |
| Model registry     | model.bin stored as object |
| Training input     | Dataset download           |
| Inference          | Model retrieval            |


## Explanation

MinIO provides S3-compatible object storage for AI/ML workflows:

- Datasets are stored as objects in buckets
- Training jobs read datasets from storage
- Models are stored after training
- Inference systems retrieve models when required

This workflow mirrors production-grade ML pipelines used in cloud environments.

## What you've learned 
In this section, you learned how to:

- Use MinIO as object storage for AI/ML datasets
- Store and retrieve model artifacts
- Simulate a real-world ML workflow
- Understand how object storage fits into data pipelines
