---
title: Configure the RAG development environment and models
weight: 3
layout: "learningpathall"
---

## Create the development environment

To get started, you need to set up your development environment and prepare the embedding model and the LLM you will use in the RAG pipeline. 

The embedding model for the solution is e5-base-v2, and the LLM is Llama 3.1 8B Instruct. 

First, create a Python virtual environment to use for the project:

```bash
cd ~
python3 -m venv rag-venv
source rag-venv/bin/activate
```

Next, install the required packages:

```bash
pip install --upgrade pip
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers==4.46.2 sentence-transformers==2.7.0 faiss-cpu langchain==1.0.5 \   
            langchain-community langchain-huggingface huggingface_hub \
            pypdf tqdm numpy
```

These packages provide the essential building blocks of the RAG system:  

- `sentence-transformers` is used for text embedding with the e5-base-v2 model.  
- `faiss-cpu` enables efficient similarity search for document retrieval. 
- `langchain` manages data orchestration between embedding, retrieval, and generation.  
- `huggingface_hub` is used for model download and authentication.  
- `pypdf` extracts and processes text content from documents.  
- `tqdm` provides progress visualization.

Since the pipeline runs on the Grace CPU, the CPU version of FAISS is sufficient and GPU acceleration is not required.

Check the installation by printing the FAISS version:

```bash
python - <<'EOF'
import faiss, transformers
print("FAISS version:", faiss.__version__)
print("FAISS GPU:", faiss.get_num_gpus() > 0)
EOF
```

The output confirms that FAISS is running in CPU mode.

```output
FAISS version: 1.13.0
FAISS GPU: False
```

## Model preparation

Download and organize the models required for the RAG pipeline.

The two models are:

- The Large Language Model (LLM) is Llama 3.1 8B Instruct for text generation.
- The Embedding Model is e5-base-v2 for document vectorization.

Both models will be stored locally under the `~/models` directory for offline operation.

You will need a Hugging Face token to get the embedding model. The instructions will be printed when you run `hf auth login` providing a link to generate a token. 

```bash
mkdir -p ~/models && cd ~/models

# Login to your Hugging Face Token
hf auth login
hf download intfloat/e5-base-v2 --local-dir ~/models/e5-base-v2

# Download GGUF version of Llama 3.1 8B model to save the time for local conversion
wget https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf -P ~/models/Llama-3.1-8B-gguf
```

### Verify the e5-base-v2 model

Run a Python script to verify that the e5-base-v2 model loads correctly and can generate embeddings.

Save the code below in a text file named `vector-test.py`.

```bash
from sentence_transformers import SentenceTransformer
import numpy as np
import os

model_path = os.path.expanduser("~/models/e5-base-v2")
print(f"Loading model from: {model_path}")

try:
    model = SentenceTransformer(model_path)
    sentences = [
        "Arm processors are designed for high efficiency.",
        "The Raspberry Pi uses Arm cores for its SoC."
    ]
    embeddings = model.encode(sentences)

    if isinstance(embeddings, np.ndarray) and embeddings.shape[0] == len(sentences):
        print(" Model loaded and embeddings generated successfully.")
        print("Embedding shape:", embeddings.shape)
        print("First vector snippet:", np.round(embeddings[0][:10], 4))
    else:
        print(" Model loaded, but embedding output seems incorrect.")
except Exception as e:
    print(f" Model failed to load or generate embeddings: {e}")
```


Run the code with:

```bash
python ./vector-test.py
```

The output confirms the e5-base-v2 model can generate embeddings successfully.

```output
 Model loaded and embeddings generated successfully.
Embedding shape: (2, 768)
First vector snippet: [-0.012  -0.0062 -0.0008 -0.0014  0.026  -0.0066 -0.0173  0.026  -0.0238
 -0.0455]
 ```

The e5-base-v2 results show:

- Test sentences: The two example sentences are used to confirm that the model can process text input and generate embeddings correctly. If this step succeeds, the model's tokenizer, encoder, and PyTorch runtime on the Grace CPU are all working together properly.
- Embedding shape (2, 768): The two sentences were converted into two 768-dimensional embedding vectors. 768 is the hidden dimension size of this model.
- First vector snippet: Displays the first 10 values of the first embedding vector. Each number represents a learned feature extracted from the text.

A successful output confirms that the e5-base-v2 embedding model is functional and ready for use.

### Verify the Llama 3.1 model

The llama.cpp runtime will be used for text generation using the Llama 3.1 model. 

Ensure that both the CPU and the GPU builds of llama.cpp have been installed. You can find the instructions in [Unlock quantized LLM performance on Arm-based NVIDIA DGX Spark](/learning-paths/laptops-and-desktops/dgx_spark_llamacpp/).

Verify the `Llama-3.1-8B-Q8_0.gguf` model is working using llama.cpp:

```bash
cd ~/llama.cpp/build-gpu

./bin/llama-cli \
  -m ~/models/Llama-3.1-8B-gguf/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf \
  -p "Hello from RAG user" \
  -ngl 40 --n-predict 64
```

You should see the model load successfully and print a short generated sentence, for example:

```output
Hello from this end! What brings you to this chat? Do you have any questions or topics you'd like to discuss? I'm here to help!
```

Next, check the REST Server, which is needed for the RAG pipeline:

```bash
./bin/llama-server \
  -m ~/models/Llama-3.1-8B-gguf/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf \
  -ngl 40 --ctx-size 8192 \
  --port 8000 \
  --host 0.0.0.0
```

Use another terminal on the same machine to do the health check:

```bash
curl http://127.0.0.1:8000/completion \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain why unified memory improves CPU–GPU collaboration.", "n_predict": 64}'
```

You should see a short JSON payload containing a coherent explanation generated by the model.

Terminate the `llama-server` using Ctrl-C.

{{% notice Note %}}
To test remote access from another machine, replace `127.0.0.1` with the IP address of the machine running `llama-server`.
{{% /notice %}}

With the development setup, tools, and models prepared, you can create the vector database and add your documents.
