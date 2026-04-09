---
title: Install Flyte and gRPC tools on Axion
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the development environment

In this section, you prepare a SUSE Linux Enterprise Server (SLES) arm64 virtual machine and install the core components required to build machine learning workflow pipelines using Flyte.

Flyte provides workflow orchestration for scalable ML pipelines, while gRPC enables efficient communication between distributed services used within those pipelines.

Running these tools natively on Arm-based Axion processors ensures efficient execution of ML workflows.

## Architecture overview

The development environment consists of a single-node setup used to build and run distributed machine learning workflows.

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
Python 3.11.10
```

**Why this matters:**

- Python 3.11 provides improved performance and memory efficiency
- Modern workflow libraries are optimized for Python 3.11
- Ensures compatibility with Flyte and gRPC libraries

## Create a virtual environment

`flytekit 1.16.15` requires `setuptools<70`, while `grpcio-tools` requires `setuptools>=77`. These constraints are mutually exclusive at the system level. A virtual environment resolves this by isolating the dependency graph from any pre-installed system packages, allowing pip to resolve all constraints together from scratch.

Create and activate a virtual environment:

```bash
python3.11 -m venv flyte-env
source flyte-env/bin/activate
```

Your prompt will change to show `(flyte-env)`, confirming the environment is active. All subsequent `pip install` commands in this Learning Path use this environment.

## Install Flyte SDK and gRPC libraries

With the virtual environment active, upgrade pip and install Flyte together with the gRPC communication libraries in a single step. This lets pip resolve a consistent set of versions, including `setuptools`, across all packages at once.

```bash
pip install --upgrade pip
pip install flytekit grpcio grpcio-tools protobuf
```

**Verify Flyte installation:**

```bash
python -c "import flytekit; print(flytekit.__version__)"
```

The output is similar to:

```output
1.16.15
```

**Verify gRPC installation:**

```bash
python -c "import grpc; import grpc_tools; import google.protobuf; print('gRPC libraries OK')"
```

The output is similar to:

```output
gRPC libraries OK
```

This confirms that Flyte and the gRPC libraries are correctly installed and compatible within the virtual environment.

## Install Flyte CLI

The Flyte CLI is a standalone binary and doesn't use pip, so you install it to the system path independently of the virtual environment.

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

- Prepare a SUSE arm64 environment for ML workflow development
- Install Python 3.11 and development dependencies
- Create a virtual environment to resolve the `setuptools` conflict between `flytekit` and `grpcio-tools`
- Install Flyte SDK and gRPC libraries in a single isolated environment
- Install Flyte CLI tools

In the next section, you will create a gRPC-based feature engineering service that will be integrated with the Flyte ML workflow pipeline.
