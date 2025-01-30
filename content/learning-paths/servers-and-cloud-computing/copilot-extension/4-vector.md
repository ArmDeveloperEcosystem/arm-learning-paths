---
title: Vector Database
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a Vector Database?

A vector database is a specialized database designed to store and query vector representations of data. They are a crucial component of many AI applications. But what exactly are they, and how do they work?

Traditional databases store data in tables or objects with defined attributes. However, they struggle to recognize similarities between data points that aren't explicitly defined. Vector databases, on the other hand, is simply an array of numbers. That makes it much easier to identify similarities by comparing the vector locations in Nth dimensional space. This is typically done using distance metrics like cosine similarity or Euclidean distance.

How can we take complex ideas, like words, and translate them into number based vector? We do so using a process called embedding.

## Embeddings

Embeddings are vectors generated through an AI model. We can convert "tokens" (sections of text) into a point in Nth dimensional space. 

Then for any given vector, like the embedded token input of a user, we can querying our vector database to find embedded data that is most similar. 

For example, for our use case let's say we want to know which Arm learning path is most relavent to a question a user asks.

First, ahead of time, we have to convert the raw data (Arm learning path content) into more comsumable "chunks". In our case, small `yaml` files. Then we run those chunks through our LLM model and embed the content into a vector database.

Now in our application, we can take the input from the user and embed it using the same model. Now we have a database of vectors representing our data, and a new vector based on user input. We find the closest (meaning, most similar) vector in the database, and that connects us to the original chunk file that vector came from. Using the data from that `chunk.yaml`, we can retrive the Arm resource(s) most relavent for that user's question.

The retrieved resources are then used to augment the context for the LLM, which generates a final response that is both contextually relevant and contains accurate information.

## Collecting Data into Chunks

To convert data into `chunk.yaml` files, we used...

### TODO: Write how to generate yaml files? Explanation of how we made example chunks?

To use our example data, you can download our example from S3 using the AWS CLI.

```bash
aws s3 cp s3://arm-github-copilot-extension/yaml_data.zip .
```

Unzip the contents:

```bash
unzip yaml_data.zip
```

## Combine Chunks into FAISS index

Once you have a folder full of yaml files, copy the vectorstore creation script to that yaml directory.

The file is located in the root of the example repo.

```bash
cp local_vectorstore_creation.py yaml_data
```

### Run the script:

Ensure your local environment has your `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT` set.

Then run the python script

```bash
python local_vectorstore_creation.py
```

The FAISS index bin file then be created.