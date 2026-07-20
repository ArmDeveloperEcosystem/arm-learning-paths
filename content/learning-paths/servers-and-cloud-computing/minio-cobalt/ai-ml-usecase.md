---
title: Use MinIO for AI/ML Dataset and Model Storage
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you simulate a real-world AI/ML workflow using MinIO. You'll upload a training dataset and a model artifact, then retrieve them to simulate how a training or inference job would access data from object storage.

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

## Simulate an AI/ML storage workflow

### Create a dataset

Create a sample dataset to represent structured training data.

```bash
mkdir ai-dataset
echo "id,name,score" > ai-dataset/data.csv
echo "1,jon,90" >> ai-dataset/data.csv
echo "2,nick,85" >> ai-dataset/data.csv
echo "3,jack,95" >> ai-dataset/data.csv
```

### Upload the dataset

Upload the dataset to MinIO.

```bash
mc cp ai-dataset/data.csv local/ml-datasets/
```

### Verify the upload

Confirm the dataset is stored in the bucket:

```bash
mc ls local/ml-datasets
```

The output is similar to:

```output
[2026-03-24 04:16:22 UTC]    13B STANDARD test.txt
[2026-03-24 04:28:25 UTC]    43B STANDARD data.csv
[2026-03-24 05:21:04 UTC]     0B dataset/
```

### Create a model artifact

Create a file to represent a trained model. In a real pipeline this would be the output of a training job.

```bash
mkdir model
echo "fake-model-weights" > model/model.bin
```

### Upload the model artifact

```bash
mc cp model/model.bin local/ml-datasets/
```

### Download data for training or inference

Simulate a training or inference job retrieving data from storage.

```bash
mkdir download-test
mc cp --recursive local/ml-datasets download-test/
```

### Verify the downloaded data

Confirm the files were retrieved successfully:

```bash
ls download-test/ml-datasets
```

The output is similar to:

```output
data.csv  dataset  model.bin  test.txt
```

This confirms that both the dataset and model artifact are accessible from storage, as a real training or inference job would expect.

## What this demonstrates

| Real-world concept | Implementation             |
| ------------------ | -------------------------- |
| Data lake          | Dataset stored in MinIO    |
| Model registry     | model.bin stored as object |
| Training input     | Dataset download           |
| Inference          | Model retrieval            |


## What you've learned

You've now completed the full Learning Path. You deployed MinIO on an Azure Cobalt 100 virtual machine, benchmarked its storage throughput, validated S3 API compatibility using boto3, and walked through an AI/ML workflow for storing and retrieving datasets and model artifacts.
