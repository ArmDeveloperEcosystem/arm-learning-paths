---
title: Vector Database
weight: 30

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a Vector Database?

A vector databases are a specialized database designed to store and query vector representations of data. They are a crucial component of many AI applications. But what exactly are they, and how do they work?

Traditional databases store data in tables or objects with defined attributes. However, they struggle to recognize similarities between data points that aren't explicitly defined.

Vector databases, on the other hand, are designed to store a large numbers of vectors (arrays of numbers), and provide algorithms to be able to search through those stored vectors. That makes it much easier to identify similarities by comparing the vector locations in N dimensional space. This is typically done using distance metrics like cosine similarity or Euclidean distance.

How can we convert complex ideas, like the semantic meaning of a series of words, into a series of of number based vectors? We do so using a process called embedding.

### Embeddings

Embeddings are vectors generated through an AI model. We can convert "tokens" (sections of text) into a point in N dimensional space. 

Then for any given vector, like the embedded token input of a user, we can querying our vector database to find embedded data that is most similar. 

For example, for our use case let's say we want to know which Arm learning path is most relevant to a question a user asks.

First, ahead of time, we have to convert the raw data (Arm learning path content) into more consumable "chunks". In our case, small `yaml` files. Then we run those chunks through our LLM model and embed the content into our FAISS vector database.

### FAISS

FAISS (Facebook AI Similarity Search) is a library developed by Facebook AI Research that is designed to efficiently search for similar vectors in large datasets. FAISS is highly optimized for both memory usage and speed, and best in class nearest neighbor search.

Now in our application, we can take the input from the user and embed it using the same model we used for our database. We then use FAISS nearest neighbor search to compare the user input to the nearest vectors in the database. We then look at the original chunk files for those closest vector. Using the data from those `chunk.yaml` files, we can retrieve the Arm resource(s) most relevant for that user's question.

The retrieved resources are then used to augment the context for the LLM, which generates a final response that is both contextually relevant and contains accurate information.

## Collecting Data into Chunks

We have provided chunk files for you in this example repo.

To access it...

### TODO: Finish this section once we have example data.

### Combine Chunks into FAISS index

Once you have a folder full of yaml files, copy the vector store creation script to that yaml directory.

The file is located in the root of the example repo.

```bash
cp local_vectorstore_creation.py yaml_data
```

### Run the script:

Ensure your local environment has your `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT` set.

Then run the python script to create the FAISS index bin file.

```bash
python local_vectorstore_creation.py
```
