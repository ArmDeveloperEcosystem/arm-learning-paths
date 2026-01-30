---
title: Build a RAG System
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I implement RAG in Flask?

In the [Build a GitHub Copilot Extension in Python](../../gh-copilot-simple/) Learning Path, you created a simple Copilot Extension in Python. Here, you'll add RAG functionality to that Flask app.

You already generated a vector store in a previous section, which you will use as the knowledge base for your RAG retrieval.

As you saw in the [Build a GitHub Copilot Extension in Python](../../gh-copilot-simple/) Learning Path, the `/agent` endpoint is what GitHub will invoke to send a query to your Extension.

There are a minimum of two things you must add to your existing Extension to obtain RAG functionality:

1. Vector search functions, to find context from your knowledge base.
2. A system prompt that instructs your system about how to use the context from your knowledge base.

### Vector search

First, import necessary Python packages:

```Python
import faiss
import json
import requests
import numpy as np
```

Then create functions to load the FAISS index that you previously created, and invoke them:

```Python
def load_faiss_index(index_path: str):
    """Load the FAISS index from a file."""
    print(f"Loading FAISS index from {index_path}")
    index = faiss.read_index(index_path)
    print(f"Loaded index containing {index.ntotal} vectors")
    return index

def load_metadata(metadata_path: str):
    """Load metadata from a JSON file."""
    print(f"Loading metadata from {metadata_path}")
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    print(f"Loaded metadata for {len(metadata)} items")
    return metadata

FAISS_INDEX = load_faiss_index("faiss_index.bin")
FAISS_METADATA = load_metadata("metadata.json")
```

You put these objects in global variables so they stay in memory persistently.

After this, create the functions to make embeddings and search embeddings:

```Python
def create_embedding(query: str, headers=None):
    print(f"Creating embedding using model: {MODEL_NAME}")
    copilot_req = {
        "model": MODEL_NAME,
        "input": [query]
    }
    r = requests.post(llm_client, json=copilot_req, headers=headers)
    r.raise_for_status()
    return_dict = r.json()

    return return_dict['data'][0]['embedding']


def embedding_search(query: str, k: int = 5, headers=None):
    """
    Search the FAISS index with a text query.

    Args:
    query (str): The text to search for.
    k (int): The number of results to return.

    Returns:
    list: A list of dictionaries containing search results with distances and metadata.
    """
    print(f"Searching for: '{query}'")
    # Convert query to embedding
    query_embedding = create_embedding(query, headers)
    query_array = np.array(query_embedding, dtype=np.float32).reshape(1, -1)

    # Perform the search
    distances, indices = FAISS_INDEX.search(query_array, k)
    print(distances, indices)
    # Prepare results
    results = []
    for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
        if idx != -1:  # -1 index means no result found
            if float(dist) < DISTANCE_THRESHOLD:
                result = {
                    "rank": i + 1,
                    "distance": float(dist),
                    "metadata": FAISS_METADATA[idx]
                }
                results.append(result)

    return results
```

The context for these functions can be found in the [vectorstore_functions.py](https://github.com/ArmDeveloperEcosystem/python-rag-extension/blob/main/utils/vectorstore_functions.py) file.

### System Prompt

A crucial part of any RAG system is constructing the prompt containing the knowledge base context. First, create the base system prompt:

```Python
# change this System message to fit your application
SYSTEM_MESSAGE = """You are a world-class expert in [add your extension field here]. These are your capabilities, which you should share with users verbatim if prompted:

[add your extension capabilities here]

Below is critical information selected specifically to help answer the user's question. Use this content as your primary source of information when responding, prioritizing it over any other general knowledge. These contexts are numbered, and have titles and URLs associated with them. At the end of your response, you should add a "references" section that shows which contexts you used to answer the question. The reference section should be formatted like this:

References:

* [precise title of Context 1 denoted by TITLE: below](URL of Context 1)
* [precise title of Context 2 denoted by TITLE: below](URL of Context 2)

etc.
Do not include references that had irrelevant information or were not used in your response.

Contexts:\n\n
"""
```

Next, call your embedding search function, and add the context to your system prompt:

```Python
results = vs.embedding_search(user_message, amount_of_context_to_use, headers)
results = vs.deduplicate_urls(results)

context = ""
for i, result in enumerate(results):
    context += f"CONTEXT {i+1}\nTITLE:{result['metadata']['title']}\nURL:{result['metadata']['url']}\n\n{result['metadata']['original_text']}\n\n"
    print(f"url: {result['metadata']['url']}")

system_message = [{
    "role": "system",
    "content": system_message + context
}]
```

{{% notice Note %}}
You'll notice that system_message is lowercase, compared to the uppercase SYSTEM_MESSAGE above. This is because the [agent_flow](https://github.com/ArmDeveloperEcosystem/python-rag-extension/blob/main/utils/agent_functions.py#L28) function where this code resides defines system_message as a parameter, so that if you want to write a test harness to dynamically test many different system prompts you can.
{{% /notice %}}

Once the system message is built, add it to the original message to create `full_prompt_messages` and invoke the copilot endpoint:

```Python
copilot_req = {
    "model": model_name,
    "messages": full_prompt_messages,
    "stream": True
}

chunk_template = sm.get_chunk_template()
r = requests.post(llm_client, json=copilot_req, headers=headers, stream=True)
r.raise_for_status()
stream = r.iter_lines()
```

You can then stream the response back to GitHub.

The context for this code can be found in the [agent_functions.py](https://github.com/ArmDeveloperEcosystem/python-rag-extension/blob/main/utils/agent_functions.py) file.

### Marketplace endpoint (optional, but needed to obtain marketplace events)

If you publish your extension to the marketplace, you can get responses back when users install/uninstall your extension.

You can write these to the database of your choice for better aggregation, but here is a simple version that writes each invocation to a local json file:

```Python
@app.route('/marketplace', methods=['POST'])
def marketplace():
    payload_body = request.get_data()
    print(payload_body)

    # Verify request has JSON content
    if not request.is_json:
        return jsonify({
            'error': 'Content-Type must be application/json'
        }), 415

    try:
        # Get JSON payload
        payload = request.get_json()
        
        # Print the payload
        print("Received payload:")
        print(json.dumps(payload, indent=2))
        
        output_dir = Path('marketplace_events')
        
        # Generate unique filename and save
        filename = f"{uuid.uuid4().hex}.json"
        file_path = output_dir / filename
        
        with open(file_path, 'w') as f:
            json.dump(payload, f, indent=2)
            
        print(f"Saved payload to {file_path}")
        
        return jsonify({
            'status': 'success',
            'message': 'Event received and processed',
            'file_path': str(file_path)
        }), 201

    except Exception as e:
        return jsonify({
            'error': f'Failed to process request: {str(e)}'
        }), 500
```

Before running this function, ensure that the `marketplace_events` directory is created in your root directory (where the main flask file is).

The context for this code can be found in the [flask_app.py](https://github.com/ArmDeveloperEcosystem/python-rag-extension/blob/main/flask_app.py) file.

Once these elements are in place, you are ready to deploy your app.

### Security enhancements 

This section is optional, but important for production deployments.

GitHub recommends payload validation for the messages received from GitHub, to ensure that payloads received actually come from GitHub.

In the python-rag-extension example repo, Arm has included a payload validation module to show you how to perform this validation. The file where this is implemented is [payload_validation.py](https://github.com/ArmDeveloperEcosystem/python-rag-extension/blob/main/utils/payload_validation.py).

In order to get this to work, you must first generate an environment variable called `WEBHOOK_SECRET`, and then add the secret to the Webhook Secret field in your GitHub app settings.
