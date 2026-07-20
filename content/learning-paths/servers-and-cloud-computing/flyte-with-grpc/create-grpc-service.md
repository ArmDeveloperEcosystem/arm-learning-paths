---
title: Build a gRPC feature engineering service
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create distributed feature engineering with gRPC

In modern machine learning pipelines, feature engineering is often implemented as a separate service so it can scale independently from the training workflow.

In this section, you create a **gRPC-based feature engineering service** that generates features used by the machine learning pipeline.

The Flyte workflow will call this service during pipeline execution.

## Architecture overview

The feature engineering service acts as an external microservice used by the ML workflow.

```text
Flyte Workflow
        |
        v
Feature Engineering Service (gRPC)
        |
        v
Generated Features for Model Training
```

## Create project directory
Create a directory for the ML workflow project.

```bash
mkdir flyte-ml-pipeline
cd flyte-ml-pipeline
```

## Create protobuf definition
Create the gRPC service definition file.

```bash
vi feature.proto
```

Add the following code.

```protobuf
syntax = "proto3";

service FeatureService {
  rpc GenerateFeatures (FeatureRequest) returns (FeatureResponse);
}

message FeatureRequest {
  int32 value = 1;
}

message FeatureResponse {
  int32 feature = 1;
}
```

This file defines the service interface used by the workflow and the feature service.

## Generate gRPC code

Make sure the `flyte-env` virtual environment is active before running the following commands. If you opened a new terminal, reactivate it:

```bash
source ~/flyte-env/bin/activate
```

Compile the protobuf file to generate Python client and server code.

```bash
python -m grpc_tools.protoc \
-I. \
--python_out=. \
--grpc_python_out=. \
feature.proto
```

The command generates the following files:

```text
feature_pb2.py
feature_pb2_grpc.py
```

These files contain the Python classes used by the gRPC server and client.

Why this matters:

- Protobuf defines a strongly typed service interface
- Generated code simplifies client-server communication
- Enables efficient RPC communication using gRPC

## Create the feature engineering service
Create the server implementation.

```bash
vi feature_server.py
```

Add the following code.

```python
import grpc
from concurrent import futures
import feature_pb2
import feature_pb2_grpc


class FeatureService(feature_pb2_grpc.FeatureServiceServicer):

    def GenerateFeatures(self, request, context):

        value = request.value
        feature = value * 10

        print("Generating feature for:", value)

        return feature_pb2.FeatureResponse(feature=feature)


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    feature_pb2_grpc.add_FeatureServiceServicer_to_server(
        FeatureService(), server
    )

    server.add_insecure_port("[::]:50051")

    server.start()

    print("Feature gRPC service running on port 50051")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
```

The service receives a value from the workflow and generates a derived feature used during model training.

## Run the feature service

Start the gRPC service.

```bash
python feature_server.py
```

The output is similar to:
```output
Feature gRPC service running on port 50051
```

## What you've learned and what's next

- Create a project directory for the ML workflow
- Define a gRPC service using protobuf
- Generate Python client and server code
- Implement a feature engineering microservice
- Start the gRPC feature service

In the next section, you will create a Flyte ML training workflow that calls this feature engineering service during pipeline execution.
