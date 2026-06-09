---
title: Install and configure LlamaIndex on a Google Cloud C4A virtual machine
description: Learn how to install Python, Ollama, LlamaIndex, ChromaDB, and FastAPI on an Arm-based Google Cloud C4A virtual machine for a browser-based RAG application.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the environment

In this section, you'll prepare a Google Cloud Axion Arm64 VM for running a browser-based RAG application using LlamaIndex.

You'll install required system packages, including Python 3.11, as well as Ollama and LLamaIndex.

### Update the virtual machine

Update all system packages:

```bash
sudo zypper refresh
sudo zypper update -y
```

This ensures your system is up to date before installing anything.

### Install required packages

Install Python 3.11 and the build tools needed to compile Python packages with native extensions:

```bash
sudo zypper install -y \
git \
curl \
wget \
tar \
gzip \
gcc \
gcc-c++ \
make \
cmake \
sqlite3 \
python311 \
python311-pip \
python311-devel \
python311-setuptools \
python311-wheel
```

Verify Python is installed correctly:

```bash
python3.11 --version
```

The output is similar to:

```output
Python 3.11.10
pip 22.3.1 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

<!-- ### (Optional) Install Docker

For this Learning Path, ChromaDB and Ollama run natively. For extended use, you can install Docker so that you can run containerized workloads alongside the RAG pipeline if needed:

```bash
sudo zypper install -y docker
sudo systemctl enable docker
sudo systemctl start docker
```

Verify Docker is running and add your user to the `docker` group so you don't need `sudo` for Docker commands:

```bash
sudo systemctl status docker
sudo usermod -aG docker $USER
newgrp docker
```

Test Docker:

```bash
docker run hello-world
```

The output is similar to:

```output
Hello from Docker!
This message shows that your installation appears to be working correctly.
``` -->

### Create project directory

Create a project directory and a Python virtual environment. The virtual environment isolates the Python packages for this project from your system packages:

```bash
mkdir -p ~/llamaindex-rag/data
cd ~/llamaindex-rag
```

Create and activate the Python virtual environment:

```bash
python3.11 -m venv rag-env
source rag-env/bin/activate
```

Upgrade pip to the latest version:

```bash
pip install --upgrade pip setuptools wheel
```

### Install Ollama

Use the official Linux installer to install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the Ollama version:

```bash
ollama -v
```

The output is similar to:

```output
ollama version is 0.24.0
```

### Check Ollama is running

When installed using the official script, Ollama registers itself as a systemd service and starts automatically. Verify it is running:

```bash
sudo systemctl status ollama
```

If the service is not running, start it:

```bash
sudo systemctl start ollama
```

### Pull an LLM model

With Ollama running, pull the `llama3.2:1b` model. This is a lightweight 1-billion-parameter model suitable for local inference on a 16 GB VM:

```bash
ollama pull llama3.2:1b
```

Test that the model responds correctly:

```bash
ollama run llama3.2:1b "Explain RAG in one sentence."
```

The output is similar to:

```output
Retrieval-Augmented Generation (RAG) is a technique that combines a retrieval step, which fetches relevant documents from a knowledge base, with a generation step, where a large language model uses those documents to produce a grounded, context-aware response.
```

### Install LlamaIndex packages

Install the LlamaIndex core library along with the integrations needed for Ollama, Hugging Face embeddings, and ChromaDB. You'll also install FastAPI and Uvicorn here because the browser-based application you'll build in the next section uses them as the web server:

```bash
pip install llama-index
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
pip install llama-index-vector-stores-chroma
pip install chromadb
pip install sentence-transformers
pip install fastapi
pip install uvicorn
```

## What you've accomplished and what's next

You've now installed and configured LlamaIndex on a Google Cloud C4A Arm64 VM running SUSE Linux with Python 3.11. You configured Ollama for local LLM inference and prepared the environment for building browser-based RAG applications using LlamaIndex and ChromaDB.

Next, you'll build the RAG engine, create the browser UI, and query custom documents using a local large language model.
