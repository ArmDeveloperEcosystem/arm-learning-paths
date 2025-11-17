---
title: Setting Up and Validating the RAG Foundation
weight: 3
layout: "learningpathall"
---

## Setting Up and Validating the RAG Foundation

In the previous session, you verified that your **DGX Spark (GB10)** system is correctly configured with the Grace CPU, Blackwell GPU, and CUDA 13 environment.

This module prepares the software and data foundation that enables the RAG workflow in later stages.

In this module, you will:
- Set up and validate the core environment for the RAG pipeline.
- Load and test the **E5-base-v2** embedding model.
- Build a local **FAISS** index for document retrieval.
- Prepare and verify the **Llama 3.1 8B Instruct** model for text generation.
- Confirm GPU acceleration and overall system readiness.

## Step 1 - Create The Development Environment

```bash
# Create and activate a virtual environment
cd ~
python3 -m venv rag-venv
source rag-venv/bin/activate

# Upgrade pip and install base dependencies
pip install --upgrade pip
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers==4.46.2 sentence-transformers==2.7.0 faiss-cpu langchain==1.0.5 \   
            langchain-community langchain-huggingface huggingface_hub \
            pypdf tqdm numpy
```

**Why these packages?**  
These libraries provide the essential building blocks of the RAG system:  
- **sentence-transformers** — used for text embedding with the E5-base-v2 model.  
- **faiss-cpu** — enables efficient similarity search for document retrieval. Since this pipeline runs on the Grace CPU, the CPU version of FAISS is sufficient — GPU acceleration is not required for this stage. 
- **LangChain** — manages data orchestration between embedding, retrieval, and generation.  
- **huggingface_hub** — handles model download and authentication.  
- **pypdf** — extracts and processes text content from documents.  
- **tqdm** — provide progress visualization.


Check installation:
```bash
python - <<'EOF'
import faiss, transformers
print("FAISS version:", faiss.__version__)
print("FAISS GPU:", faiss.get_num_gpus() > 0)
EOF
```

The output confirms that FAISS is running in CPU mode (FAISS GPU: False), which is expected for this setup.
```
FAISS version: 1.12.0
FAISS GPU: False
```

## Step 2 – Model Preparation

Download and organize the models required for the **GB10 Local RAG Pipeline**:

- **LLM (Large Language Model)** — llama-3-8b-instruct for text generation.
- **Embedding Model** — E5-base-v2 for document vectorization.

Both models will be stored locally under the `~/models` directory for offline operation.

```bash
mkdir -p ~/models && cd ~/models

# Login to your Hugging Face Token
hf auth login
hf download intfloat/e5-base-v2 --local-dir ~/models/e5-base-v2

# Download GGUF version of llama-3.1 8B model to save the time for local conversion
wget https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf -P ~/models/Llama-3.1-8B-gguf
```

### Verify the **E5-base-v2** model

Run a Python script to verify that the **E5-base-v2** model loads correctly and can generate embeddings.

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

Expected output should confirm the E5-base-v2 model can generate embeddings successfully.”
```
 Model loaded and embeddings generated successfully.
Embedding shape: (2, 768)
First vector snippet: [-0.012  -0.0062 -0.0008 -0.0014  0.026  -0.0066 -0.0173  0.026  -0.0238
 -0.0455]
 ```

Interpret the E5-base-v2 Result:

- ***Test sentences***: The two example sentences are used to confirm that the model can process text input and generate embeddings correctly. If this step succeeds, it means the model’s tokenizer, encoder, and PyTorch runtime on the Grace CPU are all working together properly.
- ***Embedding shape (2, 768)***: The two sentences were converted into two 768-dimensional embedding vectors — 768 is the hidden dimension size of this model.
- ***First vector snippet***: Displays the first 10 values of the first embedding vector. Each number represents a learned feature extracted from the text.

A successful output confirms that the ***E5-base-v2 embedding model*** is functional and ready for use on the Grace CPU.


### Verify the **llama-3.1-8B** model

Then, you are going to verify the gguf model.

The **llama.cpp** runtime will be used for text generation.  
Please ensure that both the **CPU** and **GPU** builds have been installed following the previous [learning path](https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_llamacpp/2_gb10_llamacpp_gpu/).

Perform a quick verification test on `llama-3.1-8B-Q8_0.gguf`

```bash
cd ~/llama.cpp/build-gpu

./bin/llama-cli \
  -m ~/models/Llama-3.1-8B-gguf/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf \
  -p "Hello from RAG user" \
  -ngl 40 --n-predict 64
```

You should see the model load successfully and print a short generated sentence, for example:

```
Hello from this end! What brings you to this chat? Do you have any questions or topics you'd like to discuss? I'm here to help!
```

Then, you need to check ***REST Server*** which you will need to use in RAG pipeline in next session.

```bash
./bin/llama-server \
  -m ~/models/Llama-3.1-8B-gguf/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf \
  -ngl 40 --ctx-size 8192 \
  --port 8000 \
  --host 0.0.0.0
```

Use another terminal in the same machine to do the health checking:

```bash
curl http://127.0.0.1:8000/completion \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain why unified memory improves CPU–GPU collaboration.", "n_predict": 64}'
```

A short JSON payload containing a coherent explanation generated by the model.

{{% notice Note %}}
To test remote access from another machine, replace `127.0.0.1` with the GB10 IP address.
{{% /notice %}}


## Step 3 – Prepare a Sample Document Corpus

Prepare the text corpus that your **RAG system** will use for retrieval and reasoning.
This stage converts your raw knowledge documents into clean, chunked text segments that can later be **vectorized and indexed** by FAISS.

### Create a workspace and data folder
We’ll use a consistent directory layout so later scripts can find your data easily.

```bash
mkdir -p ~/rag && cd ~/rag
mkdir pdf text
```

List all the source PDF URLs into a file, one per line.
In this learning path, we collect all of Raspberry Pi datasheet links into file called `datasheet.txt`

```
https://datasheets.raspberrypi.com/cm/cm1-and-cm3-datasheet.pdf
https://datasheets.raspberrypi.com/cm/cm3-plus-datasheet.pdf
https://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf
https://datasheets.raspberrypi.com/cm4io/cm4io-datasheet.pdf
https://datasheets.raspberrypi.com/cm4s/cm4s-datasheet.pdf
https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf
https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf
https://datasheets.raspberrypi.com/picow/pico-2-w-datasheet.pdf
https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf
https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf
https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf
https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf
```

Use `wget` to batch download all of pdf into `~/rag/pdf`
```bash
wget -P ~/rag/pdf -i datasheet.txt
```

### Convert PDF into txt file

Then, create a python file `pdf2text.py`

```python
from pypdf import PdfReader
import glob, os

pdf_root = os.path.expanduser("~/rag/pdf")
txt_root = os.path.expanduser("~/rag/text")
os.makedirs(txt_root, exist_ok=True)

count = 0
for file in glob.glob(os.path.join(pdf_root, "**/*.pdf"), recursive=True):
    print(f"File processing {file}")
    try:
        reader = PdfReader(file)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)

        rel_path = os.path.relpath(file, pdf_root)
        txt_path = os.path.join(txt_root, os.path.splitext(rel_path)[0] + ".txt")
        os.makedirs(os.path.dirname(txt_path), exist_ok=True)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        count += 1
        print(f"Converted: {file} -> {txt_path}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"\nTotal converted PDFs: {count}")
print(f"Output directory: {txt_root}")
```

The resulting text files will form the base corpus for semantic retrieval in later steps.

Run the Python script to convert all PDFs into text files.

```bash
python pdf2text.py
```

This script converts all PDFs into text files for later embedding.

### Verify your corpus
You should now see something like this in your folder:
```bash
find ~/rag/text/ -type f -name "*.txt" -exec cat {} + | wc -l
```

It will show how many line in total.


## Step 4 – Build an Embedding and Search Index

Convert your prepared text corpus into **vector embeddings** and store them in a **FAISS index** for efficient semantic search.

This stage enables your RAG pipeline to retrieve the most relevant text chunks when users ask questions.

| **Component** | **Role** |
|--------------|------------------------------|
| **SentenceTransformer (E5-base-v2)** | Generates vector embeddings for each text chunk |
| **LangChain + FAISS** | Stores and searches embeddings efficiently |
| **RecursiveCharacterTextSplitter** | Splits long documents into manageable text chunks |

Use **E5-base-v2** to encode the documents and create a FAISS vector index.

### Create the FAISS builder script

Save the following as `build_index.py` in `~/rag`

```bash
mkdir -p ~/rag/faiss_index
```

The embedding process (about 10 minutes on CPU) will batch every 100 text chunks for progress logging.

```python
import os, glob
from tqdm import tqdm

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Paths
data_dir = os.path.expanduser("~/rag/text")
model_dir = os.path.expanduser("~/models/e5-base-v2")
index_dir = os.path.expanduser("~/rag/faiss_index")

os.makedirs(index_dir, exist_ok=True)

# Load embedding model (CPU only)
embedder = HuggingFaceEmbeddings(
    model_name=model_dir,
    model_kwargs={"device": "cpu"}
)

print(f" Embedder loaded on: {embedder._client.device}")
print(f" Model path: {model_dir}")

# Collect and split all text files (recursive)
docs = []
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)

print("\n Scanning and splitting text files...")
for path in glob.glob(os.path.join(data_dir, "**/*.txt"), recursive=True):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
        if not text.strip():
            continue
        rel_path = os.path.relpath(path, data_dir)
        for chunk in splitter.split_text(text):
            docs.append(Document(page_content=chunk, metadata={"source": rel_path}))

print(f" Total chunks loaded: {len(docs)}")

# Prepare inputs for embedding
texts = [d.page_content for d in docs]
metadatas = [d.metadata for d in docs]

"""
# Full embedding with progress logging every 100 chunks
print("\n Embedding text chunks (batch log every 100)...")
embeddings = []
for i, chunk in enumerate(texts):
    embedding = embedder.embed_documents([chunk])[0]
    embeddings.append(embedding)
    if (i + 1) % 100 == 0 or (i + 1) == len(texts):
        print(f" Embedded {i + 1} / {len(texts)} chunks")
"""
# Batch embedding
embeddings = []
batch_size = 16
for i in range(0, len(texts), batch_size):
    batch_texts = texts[i:i+batch_size]
    batch_embeddings = embedder.embed_documents(batch_texts)
    embeddings.extend(batch_embeddings)
    print(f" Embedded {i + len(batch_texts)} / {len(texts)}")

# Pair (text, embedding) for FAISS
text_embeddings = list(zip(texts, embeddings))

print("\n Saving FAISS index...")
db = FAISS.from_embeddings(
    text_embeddings,
    embedder,
    metadatas=metadatas
)
db.save_local(index_dir)
print(f"\n FAISS index saved to: {index_dir}")
```


**Run it:**
```bash
python build_index.py
```

The script will process the corpus, load approximately 6,000 text chunks, and save the resulting FAISS index to: `~/rag/faiss_index`

You will find two of files inside.
- ***index.faiss***
    - A binary file that stores the vector index built using ***FAISS***.
	- It contains the actual embeddings and data structures used for ***efficient similarity search*** (e.g., L2 distance, cosine).
	- This file enables fast retrieval of nearest neighbors for any given query vector.
- ***index.pkl***
    - A ***Pickle*** file that stores metadata and original document chunks.
	- It maps each vector in index.faiss back to its ***text content and source info*** (e.g., file name).
	- Used by LangChain to return human-readable results along with context.

You can verify the FAISS index using the following script.

```python
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

model_path = os.path.expanduser("~/models/e5-base-v2")
index_path = os.path.expanduser("~/rag/faiss_index")

embedder = HuggingFaceEmbeddings(model_name=model_path)
db = FAISS.load_local(index_path, embedder, allow_dangerous_deserialization=True)

query = "raspberry pi 4 power supply"
results = db.similarity_search(query, k=3)

for i, r in enumerate(results, 1):
    print(f"\nResult {i}")
    print(f"Source: {r.metadata.get('source')}")
    print(r.page_content[:300], "...")

query = "Use SWD debug Raspberry Pi Pico"    
results = db.similarity_search(query, k=3)

for i, r in enumerate(results, 4):
    print(f"\nResult {i}")
    print(f"Source: {r.metadata.get('source')}")
    print(r.page_content[:300], "...")
```

The results will look like the following:

```
Result 1
Source: cm4io-datasheet.txt
Raspberry Pi Compute Module 4 IO Board. We recommend budgeting 9W for CM4.
If you want to supply an external +5V supply to the board, e.g. via J20 or via PoE J9, then we recommend that L5 be
removed. Removing L5 will prevent the on-board +5V and +3.3V supplies from starting up and +5V coming out of  ...

Result 2
Source: cm4io-datasheet.txt
power the CM4. There is also an on-board +12V to +3.3V DC-DC converter PSU which is only used for the PCIe slot. The
+12V input feeds the +12V PCIe slot, the external PSU connector and the fan connector directly. If these aren’t being
used then a wider input supply is possible (+7.5V to +28V).
With  ...

Result 3
Source: cm4io-datasheet.txt
that Raspberry Pi 4 Model B has, and for general usage you should refer to the Raspberry Pi 4 Model B documentation .
The significant difference between CM4IO and Raspberry Pi 4 Model B is the addition of a single PCIe socket. The
CM4IO has been designed as both a reference design for CM4 or to be u ...

Result 4
Source: pico-datasheet.txt
mass storage device), or the standard Serial Wire Debug (SWD) port can reset the system and load and run code
without any button presses. The SWD port can also be used to interactively debug code running on the RP2040.
Raspberry Pi Pico Datasheet
Chapter 1. About Raspberry Pi Pico 4
Getting started  ...

Result 5
Source: pico-2-datasheet.txt
mass storage device), or the standard Serial Wire Debug (SWD) port can reset the system and load and run code
without any button presses. The SWD port can also be used to interactively debug code running on the RP2350.
 TIP
Getting started with Raspberry Pi Pico-series  walks through loading progra ...

Result 6
Source: pico-w-datasheet.txt
without any button presses. The SWD port can also be used to interactively debug code running on the RP2040.
Getting started with Pico W
The Getting started with Raspberry Pi Pico-series book walks through loading programs onto the
board, and shows how to install the C/C++ SDK and build the example  ...
```

The execution of `check_index.py` confirmed that your local ***FAISS vector index*** is functioning correctly for semantic search tasks. 

You performed two distinct queries targeting different product lines within the Raspberry Pi ecosystem: ***Raspberry Pi 4 power supply*** and ***Raspberry Pi Pico SWD debugging***.

- For the first query, ***raspberry pi 4 power supply***, the system returned three highly relevant results, all sourced from the `cm4io-datasheet.txt` file. These passages provided technical guidance on power requirements, supply voltage ranges, and hardware configurations specific to the Compute Module 4 IO Board. This indicates that the embeddings captured the correct semantic intent, and that the FAISS index correctly surfaced content even when specific keywords like ***power supply*** appeared in varied contexts.

- For the second query, ***Use SWD debug Raspberry Pi Pico***, the search retrieved top results from all three relevant datasheets in the Pico family: `pico-datasheet.txt`, `pico-2-datasheet.txt`, and `pico-w-datasheet.txt`. 
The extracted passages consistently explained how the ***Serial Wire Debug (SWD)*** port allows developers to reset the system, load and run code without manual input, and perform interactive debugging on the RP2040 or RP2350 microcontrollers. This demonstrates that your chunking and indexing pipeline accurately retained embedded debugging context, and that metadata mapping correctly links each result to its original source document.

This process validates that your system can perform semantic retrieval on technical documents — a core capability of any RAG application.

In summary, both semantic queries were successfully answered using your local vector store, validating that the indexing, embedding, metadata, and retrieval components of your RAG backend are working correctly in a CPU-only configuration.


| **Stage** | **Technology** | **Hardware Execution** | **Function** |
|------------|----------------|------------------------|---------------|
| Document Processing | pypdf, python-docx | Grace CPU | Text extraction |
| Embedding | E5-base-v2 (sentence-transformers) | Grace CPU | Vectorization |
| Retrieval | FAISS + LangChain | Grace CPU | Semantic search |
| Generation | llama.cpp REST Server | Blackwell GPU + Grace CPU | Text generation |
| Orchestration | Python RAG Script | Grace CPU | Pipeline control |
| Unified Memory | NVLink-C2C | Shared | Zero-copy data exchange |

At this point, your environment is fully configured and validated.
You have confirmed that the E5-base-v2 embedding model, FAISS index, and Llama 3.1 8B model are all functioning correctly.

In the next module, you will integrate all these validated components into a full **Retrieval-Augmented Generation (RAG)** pipeline, combining CPU-based retrieval and GPU-accelerated generation on the ***Grace–Blackwell (GB10)*** platform.