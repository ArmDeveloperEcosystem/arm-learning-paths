---
title: Run ML Training Pipeline
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Run ML Training Pipeline

In this section, you execute the distributed machine learning pipeline built using **Flyte and gRPC**.

The ML workflow will:

- load a dataset
- Preprocess the data
- generate features using a gRPC microservice
- train a model
- evaluate model performance

The feature engineering service runs independently and communicates with the workflow using **gRPC remote procedure calls**.

## Start the feature engineering service

First, start the feature engineering service that was created in the previous section.

```bash
python3.11 feature_server.py
```

The output is similar to:
```output
Feature gRPC service running on port 50051
```

Leave this terminal running because the ML pipeline will send requests to this service.

## Run the ML workflow pipeline

Open a new terminal session. Navigate to the project directory.

```bash
cd ~/flyte-ml-pipeline
```

**Run the workflow:**

```bash
python3.11 workflow.py
```

## Example pipeline execution output

The output is similar to:

```output
Loading dataset
Preprocessing dataset: 10
Training model with feature: 200
Model accuracy: 10.0
Pipeline result: Model performance good
```

## What happens during execution

During pipeline execution the following steps occur:

1. The dataset is loaded by the Flyte task.
2. The dataset is preprocessed.
3. The workflow sends a request to the gRPC feature engineering service.
4. The gRPC service generates features.
5. The workflow uses the generated features to simulate model training.
6. The model performance is evaluated.
7. The pipeline returns the final result.

## Pipeline execution flow

```text
Load Dataset
      │
      ▼
Preprocess Data
      │
      ▼
Feature Engineering (gRPC Service)
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Pipeline Result
```

## Verify the gRPC service interaction

You can observe activity in the terminal running the feature service. When the workflow sends a request, the service prints a message similar to:

```output
Feature gRPC service running on port 50051
Generating feature for: 20
```

This confirms that the Flyte workflow successfully communicated with the gRPC service.

## What you've learned and what's next

In this section, you learned how to:

- Start the gRPC feature engineering service
- Execute the Flyte ML workflow pipeline
- Observe task execution across distributed services
- Verify communication between the workflow and the microservice

In the next section, you will explore the architecture of a distributed ML training pipeline implemented with Flyte and gRPC on Axion infrastructure.
