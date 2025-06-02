---
title: Online RAG
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Prepare the Embedding Model

In your Python script, generate a test embedding and print its dimension and the first few elements.

For the LLM, you will use the OpenAI SDK to request the Llama service that you launched previously. You do not need to use an API key because it is running locally on your machine.

Append the code below to `zilliz-llm-rag.py`:

```python
test_embedding = embedding_model.embed_query("This is a test")
embedding_dim = len(test_embedding)
print(embedding_dim)
print(test_embedding[:10])
```
Run the script. The output should look like:

```output
384
[0.03061249852180481, 0.013831384479999542, -0.02084377221763134, 0.016327863559126854, -0.010231520049273968, -0.0479842908680439, -0.017313342541456223, 0.03728749603033066, 0.04588735103607178, 0.034405000507831573]
```

### Retrieve data for a query

Now specify a common question about Milvus, and search for the question in the collection, in order to retrieve the top 3 semantic matches.

Append the code shown below to `zilliz-llm-rag.py`:

```python
question = "How is data stored in milvus?"

search_res = milvus_client.search(
    collection_name=collection_name,
    data=[
        embedding_model.embed_query(question)
    ],  # Use the `emb_text` function to convert the question to an embedding vector
    limit=3,  # Return top 3 results
    search_params={"metric_type": "IP", "params": {}},  # Inner product distance
    output_fields=["text"],  # Return the text field
)

import json

retrieved_lines_with_distances = [
    (res["entity"]["text"], res["distance"]) for res in search_res[0]
]
print(json.dumps(retrieved_lines_with_distances, indent=4))
```
Run the script again, and the output with the top 3 matches should look like:

```output
[
    [
        " Where does Milvus store data?\n\nMilvus deals with two types of data, inserted data and metadata. \n\nInserted data, including vector data, scalar data, and collection-specific schema, are stored in persistent storage as incremental log. Milvus supports multiple object storage backends, including [MinIO](https://min.io/), [AWS S3](https://aws.amazon.com/s3/?nc1=h_ls), [Google Cloud Storage](https://cloud.google.com/storage?hl=en#object-storage-for-companies-of-all-sizes) (GCS), [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs), [Alibaba Cloud OSS](https://www.alibabacloud.com/product/object-storage-service), and [Tencent Cloud Object Storage](https://www.tencentcloud.com/products/cos) (COS).\n\nMetadata are generated within Milvus. Each Milvus module has its own metadata that are stored in etcd.\n\n###",
        0.6488019824028015
    ],
    [
        "How does Milvus flush data?\n\nMilvus returns success when inserted data are loaded to the message queue. However, the data are not yet flushed to the disk. Then Milvus' data node writes the data in the message queue to persistent storage as incremental logs. If `flush()` is called, the data node is forced to write all data in the message queue to persistent storage immediately.\n\n###",
        0.5974207520484924
    ],
    [
        "What is the maximum dataset size Milvus can handle?\n\n  \nTheoretically, the maximum dataset size Milvus can handle is determined by the hardware it is run on, specifically system memory and storage:\n\n- Milvus loads all specified collections and partitions into memory before running queries. Therefore, memory size determines the maximum amount of data Milvus can query.\n- When new entities and collection-related schema (currently only MinIO is supported for data persistence) are added to Milvus, system storage determines the maximum allowable size of inserted data.\n\n###",
        0.5833579301834106
    ]
]
```
### Use the LLM to obtain a RAG response

You are now ready to use the LLM and obtain a RAG response. 

For the LLM, you will use the OpenAI SDK to request the Llama service you launched in the previous section. You do not need to use an API key because it is running locally on your machine. 

You will then convert the retrieved documents into a string format. Define system and user prompts for the Language Model. This prompt is assembled with the retrieved documents from Milvus. Finally, use the LLM to generate a response based on the prompts.

Append the code below into `zilliz-llm-rag.py`:

```python
from openai import OpenAI

llm_client = OpenAI(base_url="http://localhost:8080/v1", api_key="no-key")

context = "\n".join(
    [line_with_distance[0] for line_with_distance in retrieved_lines_with_distances]
)

SYSTEM_PROMPT = """
Human: You are an AI assistant. You are able to find answers to the questions from the contextual passage snippets provided.
"""
USER_PROMPT = f"""
Use the following pieces of information enclosed in <context> tags to provide an answer to the question enclosed in <question> tags.
<context>
{context}
</context>
<question>
{question}
</question>
"""

response = llm_client.chat.completions.create(
    model="not-used",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ],
)
print(response.choices[0].message.content)

```

{{% notice Note %}}
Make sure your llama.cpp server from the previous section is running before you proceed.
{{% /notice  %}}

Run the script one final time with these changes using `python3 zilliz-llm-rag.py`. The output should look like:

```output
Milvus stores data in two types: inserted data and metadata. Inserted data, including vector data, scalar data, and collection-specific schema, are stored in persistent storage as incremental log. Milvus supports multiple object storage backends such as MinIO, AWS S3, Google Cloud Storage (GCS), Azure Blob Storage, Alibaba Cloud OSS, and Tencent Cloud Object Storage (COS). Metadata are generated within Milvus and each Milvus module has its own metadata that are stored in etcd.
```
Congratulations! You have successfully built a RAG application using a LLM and Zilliz Cloud all on your Arm-based infrastructure.


