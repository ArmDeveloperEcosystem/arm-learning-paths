---
title: Set up your testing environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.11 or later
- Docker Engine or Docker Desktop
- Git

You can verify Docker is running by executing:

```bash
docker info
```

The output shows your Docker configuration. If Docker isn't running, start the Docker daemon before proceeding.

## Clone the Arm MCP repository

First, clone the Arm MCP server repository which contains the test framework:

```bash
git clone https://github.com/arm/mcp.git
cd mcp
```

## Build the MCP server Docker image

The integration tests require a locally built Docker image of the MCP server. Build it from the repository root:

```bash
docker buildx build -f mcp-local/Dockerfile -t arm-mcp .
```

This command creates a Docker image tagged as `arm-mcp:latest`. The build process takes several minutes as it generates the vector database for the knowledge base.

To verify the image was created successfully:

```bash
docker images arm-mcp
```

The output is similar to:

```output
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
arm-mcp      latest    a1b2c3d4e5f6   2 minutes ago   1.2GB
```

## Create a Python virtual environment

Create an isolated Python environment for your test dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows, activate the environment using:

```bash
venv\Scripts\activate
```

## Install test dependencies

The test framework requires Pytest and Testcontainers. Install them using the provided requirements file:

```bash
pip install -r mcp-local/tests/requirements.txt
```

The requirements file contains:

```text
testcontainers
pytest
```

You can also install these packages directly:

```bash
pip install testcontainers pytest
```

## Verify your setup

Run a quick verification to ensure everything is configured correctly:

```bash
python -c "from testcontainers.core.container import DockerContainer; print('Testcontainers ready')"
```

The output confirms Testcontainers can interact with Docker:

```output
Testcontainers ready
```

## Understanding the test directory structure

The test files are located in `mcp-local/tests/`:

```text
mcp-local/tests/
├── constants.py      # Test data and expected responses
├── requirements.txt  # Python dependencies
├── sum_test.s        # Sample Arm assembly file for MCA tests
└── test_mcp.py       # Main test file
```

- **constants.py**: Contains MCP request payloads and expected responses for each tool being tested.
- **test_mcp.py**: The main test file that uses Testcontainers to spin up the MCP server and run assertions.
- **sum_test.s**: A sample Arm assembly file used to test the LLVM-MCA analysis tool.

## What you've accomplished and what's next

In this section:
- You cloned the Arm MCP repository and built the server Docker image.
- You set up a Python virtual environment with Pytest and Testcontainers.
- You explored the test directory structure.

In the next section, you will examine the test code and understand how to write integration tests for MCP servers.
