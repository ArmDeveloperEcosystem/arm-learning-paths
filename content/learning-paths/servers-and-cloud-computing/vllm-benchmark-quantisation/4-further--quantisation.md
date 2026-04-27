---
title: Quantisation techniques
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Further quantisation

We have used a publicly available w8a8 quantised model to improve performance with a small decrease in accuracy. We have previously covered how to quantise a model to even lower precision (int4) in the [Run vLLM inference with INT4 quantization on Arm servers](/learning-paths/servers-and-cloud-computing/vllm-acceleration/) Learning Path. Further quantisation of the model incurs additional accuracy losses due to the loss in precision. However there are other quantisation techniques that can reduce this accuracy loss. In the [quantisation recipe](/learning-paths/servers-and-cloud-computing/vllm-acceleration/2-quantize-model/) provided in the referenced learning path we use QuantizationModifier to quantise the model weights. The [w8a8 quantised model](https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8#creation) you've been using in this Learning Path was instead quantised with GPTQModifier. GPTQModifier uses a calibration data set to quantise the model weights. We have found GPTQModifier produces smaller degradations in accuracy compared to QuantizationModifier and recommend a recipe like the below for int4 quantisation. 

You will need to install the required packages before running the quantisation script.
```bash
pip install compressed-tensors==0.14.0.1
pip install llmcompressor==0.10.0.1
pip install datasets==4.6.0
 
python w4a8_quant.py
```

Where w4a8_quant.py contains:
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
            "num_bits": 4,
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
model.save_pretrained("Meta-Llama-3.1-8B-quantized.w4a8")
```

## Next steps

Now that you have your environment set up for benchmarking and quantising different models, you can experiment with:
- Longer benchmarking runs
- Benchmarking accuracy with different tasks: hellaswag, winogrande etc.
- Different quantisation techniques
- Different models

Your results will allow you to balance accuracy and performance when making decisions about model deployment.
