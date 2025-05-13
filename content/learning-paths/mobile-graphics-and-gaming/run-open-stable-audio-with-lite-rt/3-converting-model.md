---
title: Convert Open Stable Audio model to LiteRT
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Stable Audio Open Model

SAO Model is made of three submodules:
* Conditioners
  * Consist of T5-based text encoder for the input prompt and a number conditioner for total seconds input. The conditioners encode the inputs into numerical values to be passed to DiT model.
* Diffusion Transformer (DiT)
  * It takes a random noise, and denoises it through a defined number of steps, to resemble what the conditioners intent.
* AutoEncoder
  * It compresses the input waveforms into amanageable sequence length to be processed by the DiT model. At the end of de-noising step, it decompreses the result into a waveform.

As part of this step, we will covert each of the three submodules into [LiteRT](https://ai.google.dev/edge/litert) format, we will use two separate conversion routes:
1. Conditioners submodule - ONNX to TFLite using [onnx2tf](https://github.com/PINTO0309/onnx2tf) tool.
2. DiT and AutoEncoder submodules - PyTorch to TFLite using Google AI Edge Torch tool. 

### Convert Conditioners

The Conditioners submodule is made of the T5Encoder model. We will use the ONNX to TFLite conversion for this submodule.

Clone the examples repository:
```bash
cd $WORKSPACE
git clone https://git.research.arm.com/gen-ai/sai/audio-stale-open-litert/-/tree/main/
cd audio-stale-open-litert
```

To eliminate dependencies issues, create a virtual environment. In this guide, we will use `virtualenv`

```bash
# Create virtual environment to use Python 3.10
python3.10 -m venv onnxvenv
 
# Activate virtual environment
source onnxvenv/bin/activate
```

We will now install the needed python packages for this

```bash
bash install_requirements_conditioners.sh
```

Convert the Conditioners submodule first to onnx and then to tflite.

```python
# Conversion to ONNX
torch.onnx.export(
        model,
        example_inputs,
        output_path,
        input_names=[], #Model inputs, a list of input tensors
        output_names=[], #Model outputs, a list of output tensors
        opset_version=15,
    )
```

```text
onnx2tf -i "input_onnx_model_path" -o "tflite_folder_path"
```

The above commands will create one .onnx model and a tflite_folder_path with a fp16.tflite and a fp32.tflite model. We will be using only one of these models to run the AudioGen inference pipeline on the mobile phone.

Converting the conditioners submodule using the provided python script
```bash
python3 ./scripts/export_conditioners.py --model_config "../sao_small_distilled/sao_small_distilled_1_0_config.json" --ckpt_path "../sao_small_distilled/sao_small_distilled_1_0.ckpt"
```

Once the Conditioners submodule has been converted successfully, deactive the virtual enviroment

```bash
deactivate
```


### Convert DiT and AutoEncoder


To convert the DiT and AutoEncoder submodules, we use the [Generative API](https://github.com/google-ai-edge/ai-edge-torch/tree/main/ai_edge_torch/generative/) provided in by the ai-edge-torch tools. This will help us export a generative pytorch model directly to tflite using three main steps: 

1. model re-authoring
2. quantization
3. conversion

Create a new virtual environment and install the requirements:
```bash
python3.10 -m venv venv
source venv/bin/activate
bash install_requirements_dit_autoencoder.sh
```

Converting the DiT and AutoEncoder submodules using the provided python script
```bash
CUDA_VISIBLE_DEVICES="" python3 ./scripts/export_audiogen.py --model_config "../sao_small_distilled/sao_small_distilled_1_0_config.json" --ckpt_path "../sao_small_distilled/sao_small_distilled_1_0.ckpt" 
```

Once the DiT and AutoEncoder submodules have been converted successfully, deactive the virtual enviroment

```bash
deactivate
```









