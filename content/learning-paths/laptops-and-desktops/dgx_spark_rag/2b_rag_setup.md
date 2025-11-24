---
title: Add documents to the RAG vector database 
weight: 4
layout: "learningpathall"
---

## Prepare a sample document corpus for RAG

You are now ready to add your documents to the RAG database that will be used for retrieval and reasoning. 

This converts your raw knowledge documents into clean, chunked text segments that can later be vectorized and indexed by FAISS.

## Use FAISS for efficient vector search on Arm

FAISS (Facebook AI Similarity Search) is an open-source library developed by Meta AI for efficient similarity search and clustering of dense vectors. It's particularly well-suited for RAG applications because it can quickly find the most relevant document chunks from large collections.

Key advantages of FAISS for this application:

- CPU efficiency: FAISS is highly optimized for Arm CPUs, making it ideal for the Grace CPU in the GB10 platform
- Scalability: Handles millions of vectors with minimal memory overhead
- Speed: Uses advanced indexing algorithms to perform nearest-neighbor searches in milliseconds
- Flexibility: Supports multiple distance metrics (L2, cosine similarity) and index types

## Set up youe RAG workspace and data folder

Create a directory structure for your data:

```bash
mkdir -p ~/rag && cd ~/rag
mkdir pdf text
```

You can add any PDF data sources to your RAG database. 

For illustration, you can add a number of Raspberry Pi documents that you want to use to find out specific information about the Raspberry Pi products. 

Use a text editor to create a file named `datasheet.txt` listing all data source URLs that will be used for the RAG data. Make sure to include one URL per line. 

```console
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

Use `wget` to batch download all the PDFs into `~/rag/pdf`.

```bash
wget -P ~/rag/pdf -i datasheet.txt
```

## Convert PDF documents to text files

Then, create a Python file named `pdf2text.py` with the code below:

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

The resulting text files will form the corpus for semantic retrieval.

Run the Python script to convert all PDFs into text files.

```bash
python pdf2text.py
```

This script converts all PDFs into text files for later embedding.

At the end of the output you see:

```output
Total converted PDFs: 12
```

## Verify your document corpus

You should now see a number of files in your folder. Run the command below to inspect the results: 

```bash
find ~/rag/text/ -type f -name "*.txt" -exec cat {} + | wc -l
```

It will show how many lines are in total. The number is around 100,000.

## Build an embedding and search index with FAISS

Convert your prepared text corpus into vector embeddings and store them in a FAISS index for efficient semantic search.

This stage enables your RAG pipeline to retrieve the most relevant text chunks when you ask questions.

| **Component** | **Role** |
|--------------|------------------------------|
| SentenceTransformer (e5-base-v2) | Generates vector embeddings for each text chunk |
| LangChain and FAISS | Stores and searches embeddings efficiently |
| RecursiveCharacterTextSplitter | Splits long documents into manageable text chunks |

Use e5-base-v2 to encode the documents and create a FAISS vector index.

### Create and run the FAISS builder script


```bash
mkdir -p ~/rag/faiss_index
```

Create a file named `build_index.py` in `~/rag` that will perform the embedding.

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

Run the code to generate the embeddings:

```bash
python build_index.py
```

The script will process the corpus, load approximately 6,000 text chunks, and save the resulting FAISS index to the `~/rag/faiss_index` directory.

You will find two files inside.

- ***index.faiss***
    - A binary file that stores the vector index built using FAISS.
	- It contains the actual embeddings and data structures used for efficient similarity search.
	- This file enables fast retrieval of nearest neighbors for any given query vector.

- ***index.pkl***
    - A pickle file that stores metadata and original document chunks.
	- It maps each vector in `index.faiss` back to its text content and source info, including file name. 
	- Used by LangChain to return human-readable results along with context.

You can verify the FAISS index using the following script.

Save the code below in `check_index.py`.

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

Run the code using:

```bash
python check_index.py
```

The results will look like the following:

```output
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

The execution of `check_index.py` confirms that your local FAISS vector index is functioning correctly for semantic search tasks. 

You performed two distinct queries targeting different product lines within the Raspberry Pi ecosystem: "Raspberry Pi 4 power supply" and "Raspberry Pi Pico SWD debugging".

- For the first query, the system returned three highly relevant results, all sourced from the `cm4io-datasheet.txt` file. These passages provided technical guidance on power requirements, supply voltage ranges, and hardware configurations specific to the Compute Module 4 IO Board. This indicates that the embeddings captured the correct semantic intent and that the FAISS index correctly surfaced content even when specific keywords like "power supply" appeared in varied contexts.

- For the second query, the search retrieved top results from all three relevant datasheets in the Pico family: `pico-datasheet.txt`, `pico-2-datasheet.txt`, and `pico-w-datasheet.txt`. 
The extracted passages consistently explained how the Serial Wire Debug (SWD) port allows developers to reset the system, load and run code without manual input, and perform interactive debugging on the RP2040 or RP2350 microcontrollers. This demonstrates that your chunking and indexing pipeline accurately retained embedded debugging context, and that metadata mapping correctly links each result to its original source document.

This process validates that your system can perform semantic retrieval on technical documents, a core capability of any RAG application.

In summary, both semantic queries were successfully answered using your local vector store, validating that the indexing, embedding, metadata, and retrieval components of your RAG backend are working correctly in a CPU-only configuration.


| **Stage** | **Technology** | **Hardware Execution** | **Function** |
|------------|----------------|------------------------|---------------|
| Document Processing | pypdf, python-docx | Grace CPU | Text extraction |
| Embedding | e5-base-v2 (sentence-transformers) | Grace CPU | Vectorization |
| Retrieval | FAISS + LangChain | Grace CPU | Semantic search |
| Generation | llama.cpp REST Server | Blackwell GPU + Grace CPU | Text generation |
| Orchestration | Python RAG Script | Grace CPU | Pipeline control |
| Unified Memory | NVLink-C2C | Shared | Zero-copy data exchange |

At this point, your environment is fully configured and validated.
You have confirmed that the e5-base-v2 embedding model, FAISS index, and Llama 3.1 8B model are all functioning correctly.

In the next section, you will integrate the validated components into a full Retrieval-Augmented Generation (RAG) pipeline, combining CPU-based retrieval and GPU-accelerated generation.

