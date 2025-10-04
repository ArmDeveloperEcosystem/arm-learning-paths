---
title: Model Loading & Optimization for ARM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Model Loading & Optimization for ARM

###### Hugging Face Authentication
```bash
Login to Hugging Face (needed for Llama models)
pip install huggingface_hub
huggingface-cli login

Enter your token when prompted
Get token from: https://huggingface.co/settings/tokens

```

###### Load a pre-fine-tuned model (from Hugging Face)
- Example: meta-llama/Llama-3-8B-Instruct or a customer-support fine-tuned variant

###### Model Optimization for ARM (Understanding Quantization)
- Reduces model precision (e.g., 32-bit → 8-bit)
- Decreases memory footprint (~4x reduction)
- Speeds up inference on CPU
- Minimal accuracy loss for most tasks

###### Apply Dynamic Quantization
- Create optimize_model.py

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from torch.quantization import quantize_dynamic
import time
import os

def load_base_model(model_name):
    """Load the base model"""
    print(f"Loading base model: {model_name}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        device_map=None,
        low_cpu_mem_usage=True
    )
    model.eval()
    
    return model, tokenizer

def apply_quantization(model):
    """Apply dynamic quantization"""
    print("Applying dynamic quantization...")
    
    quantized_model = quantize_dynamic(
        model,
        {torch.nn.Linear},  # Quantize linear layers
        dtype=torch.qint8
    )
    
    return quantized_model

def test_model(model, tokenizer, prompt):
    """Test model with a sample prompt"""
    inputs = tokenizer(prompt, return_tensors="pt")
    
    start_time = time.time()
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids,
            max_new_tokens=100,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )
    inference_time = time.time() - start_time
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response, inference_time

def main():
    model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
    
    # Load base model
    base_model, tokenizer = load_base_model(model_name)
    
    # Test base model
    test_prompt = "How do I track my order?"
    print("\nTesting base model...")
    response, base_time = test_model(base_model, tokenizer, test_prompt)
    print(f"Base model inference time: {base_time:.2f}s")
    
    # Apply quantization
    quantized_model = apply_quantization(base_model)
    
    # Test quantized model
    print("\nTesting quantized model...")
    response, quant_time = test_model(quantized_model, tokenizer, test_prompt)
    print(f"Quantized model inference time: {quant_time:.2f}s")
    print(f"Speedup: {base_time / quant_time:.2f}x")
    
    # Save quantized model
    save_dir = "./models/quantized_llama3"
    os.makedirs(save_dir, exist_ok=True)
    
    torch.save(quantized_model.state_dict(), f"{save_dir}/model.pt")
    tokenizer.save_pretrained(save_dir)
    
    print(f"\nQuantized model saved to: {save_dir}")

if __name__ == "__main__":
    main()

```