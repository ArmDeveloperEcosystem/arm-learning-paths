---
title: Fine Tuning Large Language Model - Load Pre-trained Model & Tokenizer
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Fine Tuning Large Language Model - Load Pre-trained Model & Tokenizer

#### Load Pre-trained Model & Tokenizer
The following commands Load the pre-trained model and tokenizer, ensuring compatibility with the fine-tuning task and optimizing memory usage

###### Import Required Modules
- FastLanguageModel: A highly optimized loader for LLaMA models in Unsloth, making it faster and memory-efficient.
- torch: Required for handling tensors and computations.
```python
from unsloth import FastLanguageModel
import torch

```
###### Define Model Configuration
- max_seq_length = 2048 → Defines the maximum number of tokens the model can process at once.
- dtype = None → Auto-selects Float16 for older GPUs (Tesla T4, V100)
- load_in_4bit = True → Enables 4-bit quantization to reduce memory usage
```python
max_seq_length = 2048  
dtype = None          
load_in_4bit = True
```
###### Load the Pre-trained Model
- Loads a 1B parameter fine-tuned LLaMA model
- Loads the optimized LLaMA model with reduced VRAM usage and faster processing
- Loads the corresponding tokenizer for tokenizing inputs properly

```python
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.2-1B-Instruct", 
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
```
###### Parameter-Efficient Fine-Tuning (PEFT) using LoRA (Low-Rank Adaptation) for the pre-trained model
- LoRA Rank (r): Defines the rank of the low-rank matrices used in LoRA
- Target Modules: Specifies which layers should be fine-tuned with LoRA, Includes attention layers (q_proj, k_proj, v_proj, o_proj) and feedforward layers (gate_proj, up_proj, down_proj)
- LoRA Alpha (lora_alpha):Scaling factor for LoRA weights and A higher value makes the LoRA layers contribute more to the model's output
- LoRA Dropout: Dropout randomly disables connections to prevent overfitting
- Bias (bias): No additional bias parameters are trained (optimized for efficiency)
- Gradient Checkpointing: Optimized memory-saving method
- Random Seed: Ensures reproducibility across training runs
- Rank-Stabilized LoRA: Rank stabilization not used
- LoFTQ Quantization: No LoFTQ (Low-bit Quantization) applied
```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, 
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, 
    bias = "none",    
    use_gradient_checkpointing = "unsloth", 
    random_state = 3407,
    use_rslora = False,  
    loftq_config = None, 
)
```