---
title: Install dependencies
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path, you will learn how to build a Retrieval-Augmented Generation (RAG) application on Arm-based servers. RAG applications often use vector databases to efficiently store and retrieve high-dimensional vector representations of text data. Vector databases are optimized for similarity search and can handle large volumes of vector data, making them ideal for the retrieval component of RAG systems. In this example, you will utilize [Zilliz Cloud](https://zilliz.com/cloud), the fully-managed Milvus vector database as your vector storage. Zilliz Cloud is available on major cloud such as AWS, GCP and Azure. In this demo you will use Zilliz Cloud deployed on AWS with Arm based servers. For the LLM, you will use the `Llama-3.1-8B` model running on an AWS Arm-based server using `llama.cpp`. 


## Install dependencies
This Learning Path has been tested on an AWS Graviton3 `c7g.2xlarge` instance running Ubuntu 22.04 LTS system.
You need at least four cores and 8GB of RAM to run this example. Configure disk storage up to at least 32 GB.

After you launch the instance, connect to it and run the following commands to prepare the environment.

Install python:

```bash
sudo apt update
sudo apt install python-is-python3 python3-pip python3-venv -y
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install the required python dependencies:

```shell
pip install --upgrade pymilvus openai requests langchain-huggingface huggingface_hub tqdm
```
