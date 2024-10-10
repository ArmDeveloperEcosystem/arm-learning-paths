---
title: Prerequisite
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

In this tutorial, you learn how to build a Retrieval-Augmented Generation (RAG) application on Arm-based infrastructures. For vector storage, we utilize [Zilliz Cloud](https://zilliz.com/cloud), the fully-managed Milvus vector database. Zilliz Cloud is available on major cloud such as AWS, GCP and Azure. In this demo we use Zilliz Cloud deployed on AWS with Arm machines. For LLM, we use the `Llama-3.1-8B` model on the AWS Arm-based server CPU using `llama.cpp`. 


## Prerequisite
To run this example, we recommend you to use [AWS Graviton](https://aws.amazon.com/ec2/graviton/), which provides a cost-effective way to run ML workloads on Arm-based servers. This notebook has been tested on an AWS Graviton3 `c7g.2xlarge` instance with Ubuntu 22.04 LTS system.

You need at least four cores and 8GB of RAM to run this example. Configure disk storage up to at least 32 GB. We recommend that you use an instance of the same or better specification.

After you launch the instance, connect to it and run the following commands to prepare the environment.

Install python on the server:

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
