---
title: Convert Open Stable Audio model to LiteRT
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Stable Audio Open Model

SAO Model is made of submodules:
* Conditioner
* Diffusion Transformer
* AutoEncoder

We use Google AI Edge Torch tools to convert these models from PyTorch format directly to LiteRT (.tflite) format.

## Setup a python virtual environment

To eliminate dependencies issues, create a virtual environment. In this guide, we will use `virtualenv`

```bash
# Create virtual environment to use Python 3.10
python3.10 -m venv env
 
# Activate virtual environment
source env/bin/activate
```

We will now install the needed python packages for this, including `ai-edge-litert` and `pytorch`

```bash
pip install --no-deps -r requirements.txt
```

We can now use Google AI Edge Torch tools to convert a PyTorch model to TFLite format.

TODO - where are ckpt and json files stored - need to get from hugging face or point to our repo

```console
CUDA_VISIBLE_DEVICES="" python3 ./scripts/export_audiogen.py --model_config "../../sao_small_distilled_model/sao_small_distilled_1_0_config.json" --ckpt_path "../../sao_small_distilled_model/sao_small_distilled_1_0.ckpt"
```
 
 







