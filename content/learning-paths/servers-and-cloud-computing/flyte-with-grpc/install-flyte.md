---
title: Install Flyte and Dependencies
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


In this section, you prepare a SUSE Linux Enterprise Server (SLES) arm64 virtual machine and install the core components required to build machine learning workflow pipelines using Flyte.

Flyte provides workflow orchestration for scalable ML pipelines, while gRPC enables efficient communication between distributed services used within those pipelines.

This environment ensures that the workflow orchestration tools and communication libraries run natively on Arm-based Axion processors.

## Architecture overview

This architecture represents a single-node development environment used to build and run distributed machine learning workflows.

```text
SUSE Linux Enterprise Server (arm64)
        │
        ▼
Python 3.11 Environment
        │
        ▼
Flyte SDK
        │
        ▼
gRPC Communication Libraries
```

## Update the system

Update the system packages.

```bash
sudo zypper refresh
sudo zypper update -y
```

## Install system dependencies

Install Python, development tools, and system libraries required to run Flyte workflows.

```bash
sudo zypper install -y \
python311 python311-devel python311-pip \
gcc gcc-c++ make \
git curl
```

**Verify Python installation:**

```bash
python3.11 --version
```

The output is similar to:

```output
Python 3.11.x
```

**Why this matters:**

- Python 3.11 provides improved performance and memory efficiency
- Modern workflow libraries are optimized for Python 3.11
- Ensures compatibility with Flyte and gRPC libraries

## Install Flyte SDK

Install the Flyte Python SDK used to define and execute workflows.

```bash
python3.11 -m pip install --upgrade pip
python3.11 -m pip install flytekit
```

**Verify installation:**

```bash
python3.11 -c "import flytekit; print(flytekit.__version__)"
```

This confirms that Flyte is correctly installed.

## Install gRPC libraries

Install the libraries required for communication between distributed services.

```bash
python3.11 -m pip install grpcio grpcio-tools protobuf
```

These libraries enable remote procedure calls between workflow tasks and microservices.

## Install Flyte CLI

Download and install the Flyte command-line tool.

```bash
curl -L https://github.com/flyteorg/flytectl/releases/latest/download/flytectl_Linux_arm64.tar.gz -o flytectl.tar.gz
tar -xzf flytectl.tar.gz
sudo mv flytectl /usr/local/bin/
```

**Verify Flyte CLI installation**

```bash
flytectl version
```
The output is similar to:

```output
{
  "App": "flytectl",
  "Build": "0a0cbce",
  "Version": "0.8.18",
  "BuildTime": "2026-03-16 11:18:15.958506423 +0000 UTC m=+0.010167662"
}
```
This confirms that the Flyte CLI is correctly installed.

## What you've learned and what's next

In this section, you learned how to:

- Prepared a SUSE arm64 environment for ML workflow development
- Installed Python 3.11 and development dependencies
- Installed Flyte SDK for workflow orchestration
- Installed gRPC libraries for service communication
- Configured Flyte CLI tools

In the next section, you will create a gRPC-based feature engineering service that will be integrated with the Flyte ML workflow pipeline.
