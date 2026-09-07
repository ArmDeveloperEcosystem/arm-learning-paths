---
title: Deploy a TinyLlama model from the Arm AI Portal
description: Download TinyLlama from Hugging Face, prepare an Arm Linux target, and test the model with ONNX Runtime GenAI.

weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open the model on Hugging Face

To open the model on Hugging Face, follow these steps:

1. On the [**TinyLlama-1.1B-Chat INT4 — ONNX GenAI (Graviton G4)**](https://developer.arm.com/ai/models/hugging-face/Arm/tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-graviton-g4/tinyllama-1.1b-chat-int4--onnx-genai-graviton-g4-int4-onnx?targetName=AWS+Graviton+G4) model page, scroll to the top and expand **Use this Model**. 
2. Select **Open on Hugging Face**.

You're now ready to deploy the model. Deployment steps are listed for convenience as follows. For detailed instructions, see [How to get started with the model](https://huggingface.co/Arm/tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-graviton-g4#how-to-get-started-with-the-model). 

## Install dependencies

Before you can deploy the TinyLlama model, installing its dependencies. 

The TinyLlama model is optimized for AWS Graviton 4-based Amazon EC2 instances such as M8g. Run the following commands on your Arm Linux target:

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install "onnxruntime>=1.22" "onnxruntime-genai>=0.14" tokenizers jinja2
```

Visit the [Hugging Face access tokens](https://huggingface.co/settings/tokens) page and create an access token of type **Read**. 

{{% notice Note %}}
Copy and save the access token immediately after creating it. The token won't be displayed again after you close the browser or navigate to another window.
{{% /notice %}}

Apply the access token to your environment, replacing `ACCESS_TOKEN` with the token that you generated in Hugging Face:

```bash
export HF_TOKEN=ACCESS_TOKEN
echo 'export HF_TOKEN=ACCESS_TOKEN' >> ~/.bashrc   # Optional - if access is desired in future sessions
```

## Download the model

Run the following Python code to download the model:

```python
from huggingface_hub import snapshot_download

local_dir = snapshot_download(
    repo_id="Arm/tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-graviton-g4",
    allow_patterns=[
        "model.onnx",
        "model.onnx.data",
        "genai_config.json",
        "tokenizer.json",
        "tokenizer_config.json",
        "tokenizer.model",
        "special_tokens_map.json",
        "chat_template.jinja",
    ],
)
```

## Link to the model

In your working directory, create a `model_dir` directory that links to the newly downloaded model:

```bash
ln -s ~/.cache/huggingface/hub/models--Arm--tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-graviton-g4/snapshots/$(ls ~/.cache/huggingface/hub/models--Arm--tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-graviton-g4/snapshots) model_dir
```

If you prefer not to use a link, create a directory named `model_dir` and move or copy the model files into it.

## Test the model with ONNX Runtime

Run the following Python code to load and test the model:

```python
import onnxruntime_genai as og

# Load the model directory (must contain model.onnx + model.onnx.data + genai_config.json + tokenizer)
model = og.Model("./model_dir")
tokenizer = og.Tokenizer(model)

prompt = (
    "<|user|>\nExplain in one paragraph what gravity is and why it matters.</s>\n"
    "<|assistant|>"
)
input_ids = tokenizer.encode(prompt)

params = og.GeneratorParams(model)
params.set_search_options(max_length=256, do_sample=False, temperature=0.0)
generator = og.Generator(model, params)
generator.append_tokens(input_ids)

while not generator.is_done():
    generator.generate_next_token()

print(tokenizer.decode(generator.get_sequence(0)))
```

The output is similar to:

```text
 <|user|>
Explain in one paragraph what gravity is and why it matters.
<|assistant|>
Gravity is the force that holds the Earth, moon, and other celestial bodies in orbit around it. It is a fundamental force of nature that is responsible for the movement of objects in the universe. Gravity is a fundamental force of nature that is responsible for the movement of objects in the universe. It is the force that pulls objects towards the Earth, the moon, and other celestial bodies. Gravity is a force that is present in all objects in the universe, regardless of their size, shape, or composition. It is the force that holds the Earth, moon, and other celestial bodies in orbit around it. Gravity is essential for the functioning of the universe, as it is responsible for the movement of objects in space and the formation of planets, stars, and galaxies. Without gravity, the universe would be a chaotic and unstable place, with no order or structure. Gravity is a fundamental force of nature that is essential for the functioning of the universe.
```

## What you've accomplished and what's next

You've now successfully downloaded a TinyLlama model from the Arm AI Portal, deployed it on an Arm Linux target, and tested it.

Next, you'll deploy an ExecuTorch code example from the AI Portal using Topo.
