---
title: Model Preparation and Conversion
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To begin working with Llama 3, the pre-trained model parameters can be accessed through Meta’s Llama Downloads page. Users are required to request access by submitting their details and reviewing and accepting the Responsible Use Guide. Upon approval, a license and a download link—valid for 24 hours—are provided. For this exercise, the Llama 3.2 1B Instruct model is utilized; however, the same procedures can be applied to other available variants with only minor modifications.

Convert the model into an ExecuTorch-compatible format optimized for Arm devices
## Script the Model

```python
import torch
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B-Instruct", torch_dtype=torch.float16)
scripted_model = torch.jit.script(model)
scripted_model.save("llama_exec.pt")

```

Install the llama-stack package from pip.
```python 
pip install llama-stack
```

Run the command to download, and paste the download link from the email when prompted.
```python 
llama model download --source meta --model-id Llama3.2-1B-Instruct
```

When the download is finished, the installation path is printed as output.
```python 
Successfully downloaded model to /<path-to-home>/.llama/checkpoints/Llama3.2-1B-Instruct
```
Verify by viewing the downloaded files under this path:
```
ls $HOME/.llama/checkpoints/Llama3.2-1B-Instruct
checklist.chk           consolidated.00.pth     params.json             tokenizer.model

```

Export the model and generate a .pte file by running the appropriate Python command. This command will export the model with KleidiAI optimizations and save the resulting file in your current working directory.

```bash
python3 -m examples.models.llama.export_llama \
--checkpoint $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/consolidated.00.pth \
--params $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/params.json \
-kv --use_sdpa_with_kv_cache \
-X --xnnpack-extended-ops \
--kleidiai \
-qmode 8da4w \
--group_size 64 \
-d fp32 \
--metadata '{"get_bos_id":128000, "get_eos_ids":[128009, 128001, 128006, 128007]}' \
--embedding-quantize 4,32 \
--output_name="llama3_1B_kv_sdpa_xnn_kleidiai_qe_4_64_1024.pte" \
--max_seq_length 1024 \
--max_context_length 1024
```

**Key Export Flags Explained:**
- `-kv --use_sdpa_with_kv_cache`: Enables KV-cache for faster autoregressive generation
- `-X --xnnpack-extended-ops`: Uses XNNPACK backend with extended operations
- `--kleidiai`: **Enables KleidiAI optimized kernels for Arm CPUs** (2-3x speedup)
- `-qmode 8da4w`: 8-bit dynamic activation quantization, 4-bit weight quantization
- `--group_size 64`: Quantization group size (smaller = better quality, larger = smaller model)
- `--embedding-quantize 4,32`: Quantizes embeddings to 4-bit with group size 32


Because Llama 3 has a larger vocabulary size, it is recommended to quantize the embeddings using the parameter --embedding-quantize 4,32. This helps to further optimize memory usage and reduce the overall model size.


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