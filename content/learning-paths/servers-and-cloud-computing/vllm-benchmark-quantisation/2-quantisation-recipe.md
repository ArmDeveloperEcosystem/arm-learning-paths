---
title: Quantisation Recipe
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding quantisation

Quantised models have their weights converted to a lower precision data type, which reduces the memory requirements of the model and can improve performance significantly. In the [Run vLLM inference with INT4 quantization on Arm servers](/learning-paths/servers-and-cloud-computing/vllm-acceleration/) Learning Path we have covered how to quantise a model yourself. There are also many publicly available quantised versions of popular models, such as https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 and https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8, which we will be using in this Learning Path.

The notation w8a8 means that the weights have been quantised to 8-bit integers and the activations (the input data) are dynamically quantised to the same. This allows our kernels to utilise Arm's 8-bit integer matrix multiply feature I8MM. You can learn more about this in the [KleidiAI and matrix multiplication](/learning-paths/cross-platform/kleidiai-explainer/) Learning Path.

The w8a8 models we are using in this Learning Path only apply quantisation to the weights and activations in the linear layers of the transformer blocks. The activation quantisations are applied per-token and the weights are quantised per-channel. That is, each output channel dimension has a scaling factor applied between INT8 and BF16 representations.

## Quantising your own models

If you would prefer to generate your own w8a8 quantised models, the recipe below is provided as an example. This is an optional activity and not a core part of this Learning Path, as it can take several hours to run.

You will need to install the required packages before running the quantisation script.
```bash
pip install compressed-tensors==0.14.0.1
pip install llmcompressor==0.10.0.1
pip install datasets==4.6.0
 
python w8a8_quant.py
```

Where w8a8_quant.py contains:
```python
from transformers import AutoTokenizer
from datasets import Dataset, load_dataset
from transformers import AutoModelForCausalLM
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier
from compressed_tensors.quantization import QuantizationType, QuantizationStrategy
import random
 
model_id = "meta-llama/Meta-Llama-3.1-8B"
 
num_samples = 256
max_seq_len = 4096
 
tokenizer = AutoTokenizer.from_pretrained(model_id)
 
def preprocess_fn(example):
  return {"text": example["text"]}
 
ds = load_dataset("neuralmagic/LLM_compression_calibration", split="train")
ds = ds.shuffle().select(range(num_samples))
ds = ds.map(preprocess_fn)
 
scheme = {
        "targets": ["Linear"],
        "weights": {
            "num_bits": 8,
            "type": QuantizationType.INT,
            "strategy": QuantizationStrategy.CHANNEL,
            "symmetric": True,
            "dynamic": False,
            "group_size": None
        },
        "input_activations":
            {
            "num_bits": 8,
            "type": QuantizationType.INT,
            "strategy": QuantizationStrategy.TOKEN,
            "dynamic": True,
            "symmetric": False,
            "observer": None,
        },
        "output_activations": None,
}
 
recipe = GPTQModifier(
  targets="Linear",
  config_groups={"group_0": scheme},
  ignore=["lm_head"],
  dampening_frac=0.01,
  block_size=512,
)
 
model = AutoModelForCausalLM.from_pretrained(
  model_id,
  device_map="auto",
  trust_remote_code=True,
)
 
oneshot(
  model=model,
  dataset=ds,
  recipe=recipe,
  max_seq_length=max_seq_len,
  num_calibration_samples=num_samples,
)
model.save_pretrained("Meta-Llama-3.1-8B-quantized.w8a8")
```

When this has completed you will need to copy over the tokeniser specific files from the original model before you can run inference on your quantised model.

```bash
cp ~/.cache/huggingface/hub/models--meta-llama--Llama-3.1-8B/snapshots/*/*token*  Meta-Llama-3.1-8B-quantized.w8a8/
```
