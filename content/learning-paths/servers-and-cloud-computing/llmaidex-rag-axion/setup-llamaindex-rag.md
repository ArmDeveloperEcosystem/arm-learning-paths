---
title: Install and Configure LlamaIndex on Google Cloud Axion
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install and Configure LlamaIndex on Google Cloud Axion

In this section, you will prepare a Google Cloud Axion Arm64 VM for running a browser-based RAG application using LlamaIndex.

You will:

- Verify the VM architecture
- Install required system packages
- Install Docker
- Install Python 3.11
- Install Ollama
- Pull a lightweight LLM model
- Install LlamaIndex and required Python packages


## Target environment

```text
Cloud: Google Cloud Platform
VM Type: C4A Axion ARM64
OS: SUSE Linux Enterprise Server 15 SP6
Architecture: aarch64
RAM: 16 GB or higher recommended
```

## Terminal usage You'll use

- **Terminal A** → setup, package installation, FastAPI, and testing
- **Terminal B** → Ollama server Open both terminals connected to the VM before starting.

## Verify VM architecture

```bash
uname -m
cat /etc/os-release
```

The output is similar to:

```output
aarch64
NAME="SLES"
VERSION="15-SP5"
VERSION_ID="15.5"
PRETTY_NAME="SUSE Linux Enterprise Server 15 SP5"
ID="sles"
ID_LIKE="suse"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:suse:sles:15:sp5"
DOCUMENTATION_URL="https://documentation.suse.com/"
```

This confirms you are on an Arm-based VM.

## Update the VM
Update all system packages:

```bash
sudo zypper refresh
sudo zypper update -y
```

This ensures your system is up to date before installing anything.

## Install required packages:
Now install Python 3.11 and other tools:

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

**Verify Python:**

```bash
python3.11 --version
```

The output is similar to:

```output
Python 3.11.10
pip 22.3.1 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

## Install Docker and Add current user to Docker group

```bash
sudo zypper install -y docker
sudo systemctl enable docker
sudo systemctl start docker
```

**Check Docker Add current user to Docker group:**

```bash
sudo systemctl status docker
sudo usermod -aG docker $USER
newgrp docker
```

**Test Docker:**

```bash
docker run hello-world
```

The output is similar to:

```output
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

## Create project directory

```bash
mkdir -p ~/llamaindex-rag/data
cd ~/llamaindex-rag
```

**Create and Activate Python virtual environment:**

```bash
python3.11 -m venv rag-env
source rag-env/bin/activate
```

**Upgrade pip:**

```bash
pip install --upgrade pip setuptools wheel
```

## Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Verify:**

```bash
ollama -v
```

The output is similar to:

```output
ollama version is 0.24.0
```

## Start Ollama

```bash
ollama serve
```

Leave Terminal B open and don't run any other commands in it. Ollama must stay running throughout the rest of this Learning Path.

## Open a new terminal

Open a second SSH terminal and run:

```bash
cd ~/llamaindex-rag
source rag-env/bin/activate
```

## Pull an LLM model

```bash
ollama pull llama3.2:1b
```

**Test the model:**

```bash
ollama run llama3.2:1b "Explain RAG in one sentence."
```

The output is similar to:

```output
RAG (Resource Allocation Group) is a method of allocating resources, such as people or equipment, to tasks based on their criticality and urgency,
prioritizing high-priority tasks that have significant consequences if not completed on time.
```

## Install LlamaIndex packages

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

You've successfully installed and configured LlamaIndex on a Google Cloud Axion Arm64 VM running SUSE Linux with Python 3.11. You installed Docker, configured Ollama for local LLM inference, and prepared the environment for building browser-based RAG applications using LlamaIndex and ChromaDB.

Next, you'll build the RAG engine, create the browser UI, and query custom documents using a local large language model.
