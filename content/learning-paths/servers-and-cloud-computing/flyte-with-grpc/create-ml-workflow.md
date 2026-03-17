---
title: Create ML Training Workflow
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a machine learning workflow using Flyte

In this section, you create a machine learning workflow pipeline using **Flyte**. Flyte workflows allow developers to define machine learning pipelines as Python tasks with explicit dependencies. This enables reproducible and scalable pipeline execution.

The workflow you build will perform the following steps:

- Load a dataset
- Preprocess the data
- Generate features using a gRPC service
- Train a machine learning model
- Evaluate the model performance

This demonstrates how Flyte orchestrates tasks across distributed services within a machine learning pipeline.

## Architecture overview

The Flyte workflow interacts with the gRPC feature engineering service created in the previous section.

```text
Flyte Workflow
        |
        v
Dataset Loader Task
        |
        v
Data Preprocessing Task
        |
        v
Feature Engineering (gRPC Service)
        |
        v
Model Training Task
        |
        v
Model Evaluation Task
        |
        v
Pipeline Result
```

This architecture separates workflow orchestration from feature generation, allowing different components of the pipeline to scale independently.

## Create workflow script

Create the workflow file.

```bash
vi workflow.py
```

Add the following code.

```python
from flytekit import task, workflow
import grpc
import feature_pb2
import feature_pb2_grpc


@task
def load_dataset() -> int:

    print("Loading dataset")

    return 10


@task
def preprocess_data(size: int) -> int:

    print("Preprocessing dataset:", size)

    return size * 2


@task
def generate_features(data: int) -> int:

    channel = grpc.insecure_channel("localhost:50051")

    stub = feature_pb2_grpc.FeatureServiceStub(channel)

    response = stub.GenerateFeatures(
        feature_pb2.FeatureRequest(value=data)
    )

    return response.feature


@task
def train_model(feature: int) -> float:

    print("Training model with feature:", feature)

    accuracy = feature / 20.0

    return accuracy


@task
def evaluate_model(acc: float) -> str:

    print("Model accuracy:", acc)

    if acc > 0.5:
        return "Model performance good"
    else:
        return "Model performance needs improvement"


@workflow
def ml_pipeline() -> str:

    data = load_dataset()

    processed = preprocess_data(size=data)

    feature = generate_features(data=processed)

    accuracy = train_model(feature=feature)

    result = evaluate_model(acc=accuracy)

    return result


if __name__ == "__main__":

    result = ml_pipeline()

    print("Pipeline result:", result)
```

## ML pipeline tasks

The workflow consists of several tasks:

- **Load dataset:** Simulates loading a training dataset.
- **Preprocess data:** Performs preprocessing on the dataset before training.
- **Feature engineering:** Calls the gRPC service to generate features used for model training.
- **Model training:** Simulates training a machine learning model.
- **Model evaluation**: Evaluates the model and determines whether the model performance is acceptable.

## Workflow execution flow

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

## What you've learned and what's next

In this section, you learned how to:

- Create ML workflow tasks using Flyte
- Define dependencies between pipeline steps
- Integrate Flyte tasks with a gRPC microservice
- Orchestrate ML pipeline execution

In the next section, you will run the co**mplete ML training pipeline and observe how Flyte interacts with the feature engineering service during workflow execution**.
