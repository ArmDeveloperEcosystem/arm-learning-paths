---
title: Vector Database
weight: 10

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

FAISS (Facebook AI Similarity Search) is a library developed by Facebook AI Research that is designed to efficiently search for similar vectors in large datasets. FAISS is highly optimized for both memory usage and speed, making it the fastest similarity search algorithm available.

One of the key reasons FAISS is so fast is its implementation of efficient Approximate Nearest Neighbor (ANN) search algorithms. ANN algorithms allow FAISS to quickly find vectors that are close to a given query vector without having to compare it to every single vector in the database. This significantly reduces the search time, especially in large datasets.

Additionally, FAISS performs all searches in-memory, which means that it can leverage the full speed of the system's RAM. This in-memory search capability ensures that the search operations are extremely fast, as they avoid the latency associated with disk I/O operations.

In our application, we can take the input from the user and embed it using the same model we used for our database. We then use FAISS nearest neighbor search to compare the user input to the nearest vectors in the database. We then look at the original chunk files for those closest vectors. Using the data from those `chunk.yaml` files, we can retrieve the Arm resource(s) most relevant for that user's question.

The retrieved resources are then used to augment the context for the LLM, which generates a final response that is both contextually relevant and contains accurate information.

### In Memory Deployment

To ensure that our application scales efficiently, we will copy the FAISS database into every deployment instance. By deploying a static in-memory vector store in each instance, we eliminate the need for a centralized database, which can become a bottleneck as the number of requests increases.

When each instance has its own copy of the FAISS database, it can perform vector searches locally, leveraging the full speed of the system's RAM. This approach ensures that the search operations are extremely fast and reduces the latency associated with network calls to a centralized database.

Moreover, this method enhances the reliability and fault tolerance of our application. If one instance fails, others can continue to operate independently without being affected by the failure. This decentralized approach also simplifies the deployment process, as each instance is self-contained and does not rely on external resources for vector searches.

By copying the FAISS database into every deployment, we achieve a scalable, high-performance solution that can handle a large number of requests efficiently.

## Collecting Data into Chunks

We have provided scripts in the [python-rag-extension github repo](https://github.com/ArmDeveloperEcosystem/python-rag-extension/) to convert an Arm learning path into a series of `chunk.yaml` files for use in our RAG application.

### Chunk Creation Script Set up

Navigate to the `vectorstore` folder in the [python-rag-extension github repo](https://github.com/ArmDeveloperEcosystem/python-rag-extension/).

```bash
cd vectorstore
```

It is recommended to use a virtual environment to manage dependencies.

Ensure you have `conda` set up in your development environment. If you aren't sure how, you can follow this [Installation Guide](https://learn.arm.com/install-guides/anaconda/).

To create a new conda environment, use the following command:

```sh
conda create --name vectorstore python=3.11
```

Once set up is complete, activate the new environment:

```sh
conda activate vectorstore
```

Install the required packages:

```sh
conda install --file vectorstore-requirements.txt
```

### Generate Chunk Files

To generate chunks, use the following command:

```sh
python chunk_a_learning_path.py --url <LEARNING_PATH_URL>
```

Replace `<LEARNING_PATH_URL>` with the URL of the learning path you want to process. If no URL is provided, the script will default to a [known learning path URL](https://learn.arm.com/learning-paths/cross-platform/kleidiai-explainer).

The script will process the specified learning path and save the chunks as YAML files in a `./chunks/` directory.

## Combine Chunks into FAISS index

Once you have a `./chunks/` directory full of yaml files, we now need to use FAISS to create our vector database.

### OpenAI Key and Endpoint

Ensure your local environment has your `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT` set.

#### If needed, generate Azure OpenAI keys and deployment 

1. **Create an OpenAI Resource**:
    - Go to the [Azure Portal](https://portal.azure.com/).
    - Click on "Create a resource".
    - Search for "OpenAI" and select "Azure OpenAI Service".
    - Click "Create".

1. **Configure the OpenAI Resource**:
    - Fill in the required details such as Subscription, Resource Group, Region, and Name.
    - Click "Review + create" and then "Create" to deploy the resource.

1. **Generate API Key and Endpoint**:
    - Once the resource is created, navigate to the resource page.
    - Under the "Resource Management->Keys and Endpoint" section, you will find the key and endpoint values.
    - Copy these values and set them in your local environment.

    ```sh
    export AZURE_OPENAI_KEY="<your_openai_key>"
    export AZURE_OPENAI_ENDPOINT="https://<your_openai_endpoint>.openai.azure.com/"
    ```

    You now have the necessary keys to use Azure OpenAI in your application.

1. **Deploy text-embedding-ada-002 model**
    - Go inside Azure AI Foundry for your new deployment
    - Under "Deployments", ensure you have a deployment for "text-embedding-ada-002"

### Generate Vector Database Files

Run the python script to create the FAISS index `.bin` and `.json` files.

**NOTE:** This assumes the chunk files are located in a `chunks` subfolder, as they should automatically be.

```bash
python local_vectorstore_creation.py
```

Copy the generated `bin` and `json` files to the root directory of your Flask application.

THey should be in the `vectorstore/chunks` folder. Since you are likely still in the `vectorstore` folder, run this command to copy:

```bash
cp chunks/faiss_index.bin ../
cp chunks/metadata.json ../
```

Your vector database is now ready for your flask application.