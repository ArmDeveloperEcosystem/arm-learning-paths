---
title: Fine Tuning with PyTorch and Hugging Face
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review fine-tuning scripts

The NVIDIA playbook provides four main fine-tuning scripts, each designed for different scenarios:

**Llama3_3B_full_finetuning.py** - Full supervised fine-tuning for Llama 3.2 3B  
This script trains all model parameters, providing maximum flexibility but requiring more GPU memory. Use this for smaller models when you have sufficient GPU resources and want the best possible fine-tuning results.

**Llama3_8B_LoRA_finetuning.py** - LoRA fine-tuning for Llama 3.1 8B  
This script uses Low-Rank Adaptation (LoRA), which trains only a small number of additional parameters while keeping the base model frozen. This approach dramatically reduces memory requirements and training time while maintaining good performance.

**Llama3_70B_LoRA_finetuning.py** - LoRA fine-tuning for Llama 3.1 70B with FSDP  
For larger 70B models, this script implements LoRA with Fully Sharded Data Parallel (FSDP) support, distributing the model across multiple GPUs to handle the increased memory requirements.

**Llama3_70B_qLoRA_finetuning.py** - QLoRA fine-tuning for Llama 3.1 70B  
This script uses Quantized LoRA (QLoRA), which combines LoRA with 4-bit quantization. This is the most memory-efficient option, allowing you to fine-tune very large models even on systems with limited GPU memory.


The file names only refer to the default model they will use if you don't specify one on the command line, you can use them to train other models of your choosing. This tutorial will use the `Llama3_3B_full_finetuning.py` script. Below are the key sections of that script. 

## Imports and dataset preparation

This section sets up the foundation for finetuning. The imports bring in PyTorch, dataset loading utilities, and Hugging Face libraries for supervised fine-tuning. 

```python

import torch
import argparse
from datasets import load_dataset
from trl import SFTConfig, SFTTrainer
from transformers import AutoModelForCausalLM, AutoTokenizer
```

The `ALPACA_PROMPT_TEMPLATE` defines the instruction-following format for training data with three fields: instruction, input, and response. This is the format that the fine-tuned model will be taught to expect as input and produce as output.

The `get_alpaca_dataset()` function loads the Alpaca dataset and formats each example using the template, appending the EOS (End of String) token. It selects a configurable number of samples (default 500) and shuffles them for training.

```python
# Define prompt templates
ALPACA_PROMPT_TEMPLATE = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.
### Instruction: {}

### Input: {}

### Response: {}"""

def get_alpaca_dataset(eos_token, dataset_size=500):
    # Preprocess the dataset
    def preprocess(x):
        texts = [
            ALPACA_PROMPT_TEMPLATE.format(instruction, input, output) + eos_token
            for instruction, input, output in zip(x["instruction"], x["input"], x["output"])
        ]
        return {"text": texts}

    dataset = load_dataset("tatsu-lab/alpaca", split="train").select(range(dataset_size)).shuffle(seed=42)
    return dataset.map(preprocess, remove_columns=dataset.column_names, batched=True)
```

## Model and tokenizer loading

This section initializes the language model. The `from_pretrained()` method loads a pre-trained language model from Hugging Face. The tokenizer loads the corresponding tokenizer and sets the padding token to match the EOS token, which is necessary for batched training.

```python
    # Load the model and tokenizer
    print(f"Loading model: {args.model_name}")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        dtype=args.dtype,
        device_map="auto",
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
```

## Dataset loading

This section prepares the training data by calling the previously defined `get_alpaca_dataset()` function with the model's tokenizer EOS token and the specified dataset size. The formatted dataset is ready for the trainer to consume.

```python
    # Load and preprocess the dataset
    print(f"Loading dataset with {args.dataset_size} samples...")
    dataset = get_alpaca_dataset(tokenizer.eos_token, args.dataset_size)
```

## Training configuration

This section defines parameters for supervised fine-tuning. Key parameters include `num_train_epochs` (set to 0.01 for a warmup epoch, later changed to full training), `gradient_accumulation_steps` (how many batches to accumulate before updating weights), `learning_rate` (step size for optimizer updates), and `max_length` (maximum sequence length for training samples). The logging parameters control where and how often training metrics are saved.

```python
    # Configure the SFT config
    config = {
        "per_device_train_batch_size": args.batch_size,
        "num_train_epochs": 0.01,  # Warmup epoch
        "gradient_accumulation_steps": args.gradient_accumulation_steps,
        "learning_rate": args.learning_rate,
        "optim": "adamw_torch",
        "save_strategy": 'no',
        "remove_unused_columns": False,
        "seed": 42,
        "dataset_text_field": "text",
        "packing": False,
        "max_length": args.seq_length,
        "torch_compile": False,
        "report_to": "none",
        "logging_dir": args.log_dir,
        "logging_steps": args.logging_steps,
        "gradient_checkpointing": args.gradient_checkpointing,  # Save memory
    }
```

## Model compilation and training

This section handles optional PyTorch compilation and executes the training. If enabled, `torch.compile()` optimizes the model for faster execution on the hardware. A warmup training pass runs a short training session (0.01 epochs) to trigger compilation and avoid compilation overhead during the actual training run. The full training creates an `SFTTrainer` with the full epoch count, then executes the training with `trainer.train()`. The `trainer_stats` variable returns training metrics like loss, throughput, and training time.

```python
    # Compile model if requested
    if args.use_torch_compile:
        print("Compiling model with torch.compile()...")
        model = torch.compile(model)

        # Warmup for torch compile
        print("Running warmup for torch.compile()...")
        SFTTrainer(
            model=model,
            processing_class=tokenizer,
            train_dataset=dataset,
            args=SFTConfig(**config),
        ).train()

    # Train the model
    print(f"\nStarting full fine-tuning for {args.num_epochs} epoch(s)...")
    config["num_train_epochs"] = args.num_epochs
    config["report_to"] = "tensorboard"

    trainer = SFTTrainer(
        model=model,
        processing_class=tokenizer,
        train_dataset=dataset,
        args=SFTConfig(**config),
    )

    trainer_stats = trainer.train()
```

## Model saving

Finally, section saves the fine-tuned model and tokenizer to disk if an output directory is specified. The `trainer.save_model()` method saves the model weights and configuration, while `tokenizer.save_pretrained()` saves the tokenizer configuration and vocabulary. This allows you to load and use the fine-tuned model later for inference or further training.

```python
    # Save model if requested
    if args.output_dir:
        print(f"Saving model to {args.output_dir}...")
        trainer.save_model(args.output_dir)
        tokenizer.save_pretrained(args.output_dir)
        print("Model saved successfully!")
```

## Run the fine-tuning

```bash
python Llama3_3B_full_finetuning.py \
--model_name "meta-llama/Meta-Llama-3-8B" \
--output_dir workspace/Models/Llama-3-8B-FineTuned
```