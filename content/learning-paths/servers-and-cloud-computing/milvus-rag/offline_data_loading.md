---
title: Offline Data Loading
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, we will show you how to load private knowledge in our RAG.

### Create the Collection
We use [Zilliz Cloud](https://zilliz.com/cloud) deployed on AWS with Arm-based machines to store and retrieve the vector data. To quick start, simply [register an account](https://docs.zilliz.com/docs/register-with-zilliz-cloud) on Zilliz Cloud for free.

> In addition to Zilliz Cloud, self-hosted Milvus is also a (more complicated to set up) option. We can also deploy [Milvus Standalone](https://milvus.io/docs/install_standalone-docker-compose.md) and [Kubernetes](https://milvus.io/docs/install_cluster-milvusoperator.md) on ARM-based machines. For more information about Milvus installation, please refer to the [installation documentation](https://milvus.io/docs/install-overview.md).

We set the `uri` and `token` as the [Public Endpoint and Api key](https://docs.zilliz.com/docs/on-zilliz-cloud-console#free-cluster-details) in Zilliz Cloud.
```python
from pymilvus import MilvusClient

milvus_client = MilvusClient(
    uri="<your_zilliz_public_endpoint>", token="<your_zilliz_api_key>"
)

collection_name = "my_rag_collection"

```
Check if the collection already exists and drop it if it does.
```python
if milvus_client.has_collection(collection_name):
    milvus_client.drop_collection(collection_name)
```
Create a new collection with specified parameters. 

If we don't specify any field information, Milvus will automatically create a default `id` field for primary key, and a `vector` field to store the vector data. A reserved JSON field is used to store non-schema-defined fields and their values.
```python
milvus_client.create_collection(
    collection_name=collection_name,
    dimension=embedding_dim,
    metric_type="IP",  # Inner product distance
    consistency_level="Strong",  # Strong consistency level
)
```
We use inner product distance as the default metric type. For more information about distance types, you can refer to [Similarity Metrics page](https://milvus.io/docs/metric.md?tab=floating)

### Prepare the data

We use the FAQ pages from the [Milvus Documentation 2.4.x](https://github.com/milvus-io/milvus-docs/releases/download/v2.4.6-preview/milvus_docs_2.4.x_en.zip) as the private knowledge in our RAG, which is a good data source for a simple RAG pipeline.

Download the zip file and extract documents to the folder `milvus_docs`.

```shell
wget https://github.com/milvus-io/milvus-docs/releases/download/v2.4.6-preview/milvus_docs_2.4.x_en.zip
unzip -q milvus_docs_2.4.x_en.zip -d milvus_docs
```

We load all markdown files from the folder `milvus_docs/en/faq`. For each document, we just simply use "# " to separate the content in the file, which can roughly separate the content of each main part of the markdown file.


```python
from glob import glob

text_lines = []

for file_path in glob("milvus_docs/en/faq/*.md", recursive=True):
    with open(file_path, "r") as file:
        file_text = file.read()

    text_lines += file_text.split("# ")
```

### Insert data
We prepare a simple but efficient embedding model [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) that can convert text into embedding vectors.
```python
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
```

Iterate through the text lines, create embeddings, and then insert the data into Milvus.

Here is a new field `text`, which is a non-defined field in the collection schema. It will be automatically added to the reserved JSON dynamic field, which can be treated as a normal field at a high level.
```python
from tqdm import tqdm

data = []

text_embeddings = embedding_model.embed_documents(text_lines)

for i, (line, embedding) in enumerate(
    tqdm(zip(text_lines, text_embeddings), desc="Creating embeddings")
):
    data.append({"id": i, "vector": embedding, "text": line})

milvus_client.insert(collection_name=collection_name, data=data)
```
```text
Creating embeddings: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 72/72 [00:18<00:00,  3.91it/s]
```
