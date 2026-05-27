---
title: Quantization recipe
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand quantization

Quantized models have their weights converted to a lower precision data type, which reduces the memory requirements of the model and can improve performance significantly. In the [Run vLLM inference with INT4 quantization on Arm servers](/learning-paths/servers-and-cloud-computing/vllm-acceleration/) Learning Path, you can learn how to quantize a model yourself. There are also many publicly available quantized versions of popular models, such as [RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8](https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8) and [RedHatAI/whisper-large-v3-quantized.w8a8](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8), which you'll use in this Learning Path.

The notation `w8a8` means that the weights have been quantized to 8-bit integers and the activations (the input data) are dynamically quantized to the same. This allows Arm's 8-bit integer matrix multiply feature I8MM to be used. For more information, see the [KleidiAI and matrix multiplication](/learning-paths/cross-platform/kleidiai-explainer/) Learning Path.

The w8a8 models used in this Learning Path apply quantization only to the weights and activations in the linear layers of the transformer blocks. The activation quantizations are applied per-token and the weights are quantized per-channel. That is, each output channel dimension has a scaling factor applied between INT8 and BF16 representations.

## (Optional) Quantize your own models 

{{% notice Note %}}
This step is optional. You'll be using pre-quantized models from Hugging Face for the rest of this Learning Path, so you don't need to run this recipe. Quantizing a model yourself can take several hours.
{{% /notice %}}

If you prefer to generate your own w8a8 quantized model rather than using the pre-quantized RedHat models, the following recipe shows how. Install the required packages before running the quantization script.

{{% notice Note %}}
The following commands use specific package versions that were tested with this recipe. To find the latest versions, see [llmcompressor](https://github.com/vllm-project/llm-compressor/releases), [compressed-tensors](https://github.com/neuralmagic/compressed-tensors/releases), and [datasets](https://github.com/huggingface/datasets/releases) on GitHub.
{{% /notice %}}

```bash
pip install compressed-tensors==0.14.0.1
pip install llmcompressor==0.10.0.1
pip install datasets==4.6.0
```

The script uses Generalized Post-Training Quantization (GPTQ) to calibrate the quantization scales. It loads 256 samples from a calibration dataset, runs a forward pass through each linear layer, and computes per-channel weight scales and per-token activation scales. The output is saved as a quantized model in the `Meta-Llama-3.1-8B-quantized.w8a8` directory.

Create a file named `w8a8_quant.py` with the following content:

```python
from transformers import AutoTokenizer
from datasets import Dataset, load_dataset
from transformers import AutoModelForCausalLM
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier
from compressed_tensors.quantization import QuantizationType, QuantizationStrategy
import random
 
model_id = "meta-llama/Meta-Llama-3.1-8B"  # Note: this uses the Meta-prefixed model ID required by llmcompressor
 
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

Run the script. This step can take several hours depending on your hardware:

```bash
python w8a8_quant.py
```

When quantization is completed, copy the tokenizer files from the original model into your quantized model directory before running inference:
```bash
for f in tokenizer.json tokenizer_config.json special_tokens_map.json tokenizer.model; do
  cp ~/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3.1-8B/snapshots/*/"$f" Meta-Llama-3.1-8B-quantized.w8a8/ 2>/dev/null || true
done
```

## What you've accomplished and what's next

You've now learned about quantization of models and the steps to quantize a model if you want to. 

Next, you'll use vLLM to run inference on both quantized and non-quantized models and compare their outputs.


