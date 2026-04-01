---
title: Install and Run Qdrant
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you prepare a SUSE Linux Enterprise Server (SLES) arm64 virtual machine and deploy **Qdrant**, an open-source vector database designed for efficient similarity search and vector indexing.

Qdrant enables applications to store and retrieve embeddings — numerical vector representations of data such as text, images, and audio. These embeddings allow applications to perform **semantic search and AI-powered retrieval**.

Running Qdrant on **Google Axion Arm-based infrastructure** enables efficient execution of modern AI workloads including semantic search, recommendation systems, and chatbot retrieval pipelines.

## Architecture overview

This architecture represents a simple vector search system where embeddings are generated and stored in Qdrant, enabling fast semantic similarity queries.

```text
SUSE Linux Enterprise Server (arm64)
        |
        v
Docker Container Runtime
        |
        v
Qdrant Vector Database
        |
        v
Vector Embeddings Storage
        |
        v
Semantic Similarity Search
```

## Update the system

Update package repositories and installed packages.

```bash
sudo zypper refresh
sudo zypper update -y
```

## Install required packages

Install Docker and Python dependencies.

```bash
sudo zypper install -y docker python3 python3-pip git
sudo zypper install -y python311 python311-pip
```

## Create a virtual environment

Create and activate a virtual environment to isolate Python dependencies and avoid system-level package conflicts.

```bash
python3.11 -m venv qdrant-env
source qdrant-env/bin/activate
pip install --upgrade pip
```

Your prompt changes to show `(qdrant-env)` when the environment is active. Use this environment for all subsequent Python commands in this Learning Path.

**Verify Python installation:**

```bash
python3.11 --version
```

The output is similar to:
```output
Python 3.11.10
```

**Why this matters:**

- Python 3.11 provides improved performance and memory efficiency.
- It ensures compatibility with modern AI libraries used in vector search pipelines.

## Enable Docker

Start and enable the Docker service.

```bash
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER ; newgrp docker
```
The newgrp command avoids the need to logout and back in for the docker group permissions to take effect.

## Verify Docker installation

```bash
docker --version
```

The output is similar to:
```output
Docker version 28.5.1-ce, build f8215cc26
```

Docker runs Qdrant in an isolated container environment.

## Run the Qdrant vector database

Start the Qdrant container.

```bash
docker run -d \
-p 6333:6333 \
-p 6334:6334 \
-v $(pwd)/qdrant_storage:/qdrant/storage \
qdrant/qdrant
```

**This command:**

- Runs Qdrant in detached mode
- Exposes ports 6333 and 6334
- Creates persistent storage for vector data

The output is similar to:
```output
latest: Pulling from qdrant/qdrant
3ea009573b47: Pull complete
4f4fb700ef54: Pull complete
ea8055cf6833: Pull complete
9d7bb093ff98: Pull complete
13053c6d0c21: Pull complete
c017fa517b2b: Pull complete
3e2c95baf78f: Pull complete
b940a5cd37f5: Pull complete
Digest: sha256:f1c7272cdac52b38c1a0e89313922d940ba50afd90d593a1605dbbc214e66ffb
Status: Downloaded newer image for qdrant/qdrant:latest
1af9f6ac9cef017016837667f68aeed22a74f0f6352effd568dfa188337820c0
```

## Verify Qdrant

Check running containers.

```bash
docker ps
```

The output is similar to:
```output
1af9f6ac9cef   qdrant/qdrant   "./entrypoint.sh"   13 seconds ago   Up 11 seconds   0.0.0.0:6333-6334->6333-6334/tcp, [::]:6333-6334>6333-6334/tcp   inspiring_dijkstra
```

This confirms the Qdrant container is running successfully.

## Test the Qdrant API

Verify the Qdrant service by calling the REST API.

```bash
curl http://localhost:6333
```

You should see an output similar to:
```output
{"title":"qdrant - vector search engine","version":"1.17.0","commit":"4ab6d2ee0f6c718667e553b1055f3e944fef025f"}gcpuser@qdrant-arm64~>
```

This confirms the vector database service is reachable and ready for use.

## What you've learned and what's next

In this section, you learned how to:

- Prepare a SUSE Linux arm64 environment on Axion
- Install Docker and Python dependencies
- Deploy the Qdrant vector database container
- Verify that the vector database is running correctly
- Access the Qdrant API endpoint

In the next section, you will generate vector embeddings using a transformer model and store them in Qdrant, enabling semantic search and AI-powered retrieval.
