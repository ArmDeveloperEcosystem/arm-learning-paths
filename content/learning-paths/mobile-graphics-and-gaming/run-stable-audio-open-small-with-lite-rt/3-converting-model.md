---
title: Convert Open Stable Audio Small model to LiteRT
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Stable Audio Open Small

|Submodule|Description|
|------|------|
|Conditioners| Includes a T5-based text encoder for the input prompt and a numerical duration encoder. These components convert the inputs into embeddings passed to the DiT model. |
|Diffusion Transformer (DiT)| Denoises random noise over multiple steps to produce structured latent audio, guided by conditioner embeddings. |
|AutoEncoder| Compresses audio waveforms into a latent representation for processing by the DiT model, and decompresses the output back into audio. |

The submodules work together to provide the pipeline as shown below:
![Model structure#center](./model.png)

As part of this section, we will explore two different conversion routes, to convert the submodules to [LiteRT](https://ai.google.dev/edge/litert) format.

1. ONNX --> LiteRT using the onnx2tf tool. This is the traditional two-step approach (PyTorch --> ONNX--> LiteRT). We will use it to convert the Conditioners submodule.

2. PyTorch --> LiteRT using the Google AI Edge Torch tool. We will use this tool to convert the DiT and AutoEncoder submodules.

### Create virtual environment and install dependencies

The Conditioners submodule is made of the T5Encoder model. You will use the ONNX to TFLite conversion for this submodule.

To avoid dependency issues, create a virtual environment. In this guide, we will use `virtualenv`:

```bash
cd $WORKSPACE
python3.10 -m venv env
source env/bin/activate
```

Clone the examples repository:

```bash
cd $WORKSPACE
git clone https://github.com/ARM-software/ML-examples.git
cd ML-examples/kleidiai-examples/audiogen/
```

We now install the needed python packages for this, including *onnx2tf* and *ai_edge_litert*

```bash
bash install_requirements.sh
```

{{% notice %}}

If you are using GPU on your machine, you may notice the following error:
```text
Traceback (most recent call last):
  File "$WORKSPACE/env/lib/python3.10/site-packages/torch/_inductor/runtime/hints.py",
  line 46, in <module> from triton.backends.compiler import AttrsDescriptor
ImportError: cannot import name 'AttrsDescriptor' from 'triton.backends.compiler'
($WORKSPACE/env/lib/python3.10/site-packages/triton/backends/compiler.py)
.
ImportError: cannot import name 'AttrsDescriptor' from 'triton.compiler.compiler'
($WORKSPACE/env/lib/python3.10/site-packages/triton/compiler/compiler.py)
```

Install the following dependency and rerun the script:
```bash
pip install triton==3.2.0
bash install_requirements.sh
```

{{% /notice %}}

### Convert Conditioners Submodule

The Conditioners submodule is based on the T5Encoder model. We convert it first to ONNX, then to LiteRT.

For this conversion we include the following steps:
1. Load the Conditioners submodule from the Stable Audio Open Small model configuration and checkpoint.
2. Export the Conditioners submodule to ONNX via *torch.onnx.export()*.
3. Convert the resulting ONNX file to LiteRT using *onnx2tf*.

You can use the provided script to convert the Conditioners submodule:

```bash
python3 ./scripts/export_conditioners.py --model_config "$WORKSPACE/model_config.json" --ckpt_path "$WORKSPACE/model.ckpt"
```

After successful conversion, you now have a `tflite_conditioners` directory containing models with different precisions (e.g., float16, float32).

We will be using the float32.tflite model for on-device inference.

### Convert DiT and AutoEncoder

To convert the DiT and AutoEncoder submodules, use the [Generative API](https://github.com/google-ai-edge/ai-edge-torch/tree/main/ai_edge_torch/generative/) provided by the ai-edge-torch tools. This enables you to export a generative PyTorch model directly to tflite using three main steps:

1. Model re-authoring.
2. Quantization.
3. Conversion.

Convert the DiT and AutoEncoder submodules using the provided python script:
```bash
python3 ./scripts/export_dit_autoencoder.py --model_config "$WORKSPACE/model_config.json" --ckpt_path "$WORKSPACE/model.ckpt"
```

After successful conversion, you now have `dit_model.tflite` and `autoencoder_model.tflite` models in your current directory.

More detailed explanation of the above scripts is available [here](https://github.com/ARM-software/ML-examples/blob/main/kleidiai-examples/audiogen/scripts/README.md)

For easier access, we add all needed models to one directory:

```bash
export LITERT_MODELS_PATH=$WORKSPACE/litert-models
mkdir $LITERT_MODELS_PATH
cp conditioners_tflite/conditioners_float32.tflite $LITERT_MODELS_PATH
cp dit_model.tflite $LITERT_MODELS_PATH
cp autoencoder_model.tflite $LITERT_MODELS_PATH
```

With all three submodules converted to LiteRT format, you're ready to build LiteRT and run the model on a mobile device in the next step.









