---
title: Access the chatbot with rtp-llm using the OpenAI-compatible API
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Setup

You can now move on to using the `rtp-llm` server program and submitting requests using an OpenAI-compatible API.

This enables applications to be created which access the LLM multiple times without starting and stopping it. 

You can also access the server over the network to another machine hosting the LLM.

One additional software package is required for this section. 

Install `jq` on your computer using the following commands:

```bash
sudo apt install jq -y
```

## Running the Server

There are a few different ways you can download the Qwen2 0.5B model. In this Learning Path, you will download the model from Hugging Face.

[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them, and collaborate with others in the community. You can browse through thousands of models that are available for a variety of use cases such as Natural Language Processing (NLP), audio, and computer vision.

The `huggingface_hub` library provides APIs and tools that let you easily download and fine-tune pre-trained models. You will use `huggingface-cli` to download the [Qwen2 0.5B model](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct).

## Install Hugging Face Hub

Install the required Python packages:

```bash
sudo apt install python-is-python3 python3-pip python3-venv -y
```

Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Your terminal prompt now has the `(venv)` prefix indicating the virtual environment is active. Use this virtual environment for the remaining commands.

Install the `huggingface_hub` python library using `pip`:

```bash
pip install huggingface_hub
```

You can now download the model using the huggingface cli:

```bash
huggingface-cli download Qwen/Qwen2-0.5B-Instruct
```

## Start the rtp-llm server

{{% notice Note %}}
The server executable compiled during the previous stage, when you ran `bazelisk build`. {{% /notice %}}

Install the pip wheel in your active virtual environment:

```bash
pip install bazel-bin/maga_transformer/maga_transformer-0.2.0-cp310-cp310-linux_aarch64.whl
pip install grpcio-tools
```
Start the server from the command line. It listens on port 8088:

```bash
export CHECKPOINT_PATH=${HOME}/.cache/huggingface/hub/models--Qwen--Qwen2-0.5B-Instruct/snapshots/c540970f9e29518b1d8f06ab8b24cba66ad77b6d/
export TOKENIZER_PATH=$CHECKPOINT_PATH 
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
MODEL_TYPE=qwen_2 FT_SERVER_TEST=1 python3 -m maga_transformer.start_server
```

## Client

### Using curl

You can access the API using the `curl` command. 

In another terminal, use a text editor to create a file named `curl-test.sh` with the content below: 

```bash
curl http://localhost:8088/v1/chat/completions -H "Content-Type: application/json"   -d '{
    "model": "any-model",
    "messages": [
      {
        "role": "system",
        "content": "You are a coding  assistant, skilled in programming."
      },
      {
        "role": "user",
        "content": "Write a hello world program in C++."
      }
    ]
  }' 2>/dev/null | jq -C
```

The `model` value in the API is not used, and you can enter any value. This is because there is only one model loaded in the server. 

Run the script:

```bash
bash ./curl-test.sh
```

The `curl` command accesses the LLM and you should see the output:

```output
{
  "id": "chat-",
  "object": "chat.completion",
  "created": 1730277073,
  "model": "AsyncModel",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Sure, here's a simple C++ program that prints \"Hello, World!\" to the console:\n\n```cpp\n#include <iostream>\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}\n```\n\nThis program includes the `iostream` library, which is used for input/output operations. The `main` function is the entry point of the program, and it calls the `cout` object to print the message \"Hello, World!\" to the console."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 32,
    "total_tokens": 137,
    "completion_tokens": 105
  }
}
```

In the returned JSON data, you will see the LLM output, including the content created from the prompt. 

### Using Python

You can also use a Python program to access the OpenAI-compatible API.

Create a Python `venv`:

```bash
python -m venv pytest
source pytest/bin/activate
```

Install the OpenAI Python package:
```bash
pip install openai==1.45.0
```

Use a text editor to create a file named `python-test.py` with the content below: 

```python
from openai import OpenAI

client = OpenAI(
        base_url='http://localhost:8088/v1',
        api_key='no-key'
        )

completion = client.chat.completions.create(
  model="not-used",
  messages=[
    {"role": "system", "content": "You are a coding assistant, skilled in programming.."},
    {"role": "user", "content": "Write a hello world program in C++."}
  ],
  stream=True,
)

for chunk in completion:
  print(chunk.choices[0].delta.content or "", end="")
```

Ensure that the server is still running, and then run the Python file:

```bash
python ./python-test.py
```

You should see the output generated by the LLM:

```output
Sure, here's a simple C++ program that prints "Hello, World!" to the console:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}

This program includes the `iostream` library, which is used for input/output operations. The `main` function is the entry point of the program, and it calls the `cout` object to print the message "Hello, World!" to the console.
```

Now you can continue to experiment with different large language models, and have a go at writing scripts to access them.
