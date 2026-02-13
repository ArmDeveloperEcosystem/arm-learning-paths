---
title: Fine-tune a model with PyTorch and Hugging Face
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you understand how fine-tuning works, it's time to look at the actual code. In this section, you'll walk through the key parts of the NVIDIA playbook's fine-tuning script, patch it to load the Raspberry Pi dataset, and run it to produce your own fine-tuned Llama model.

## Review the fine-tuning scripts

The NVIDIA playbook provides four main fine-tuning scripts, each designed for different scenarios:

| Script | Approach | Best for |
|--------|----------|----------|
| `Llama3_3B_full_finetuning.py` | Full fine-tuning (all parameters) | Smaller models where GPU memory isn't a constraint |
| `Llama3_8B_LoRA_finetuning.py` | LoRA (frozen base + small trainable adapters) | Mid-size models with reduced memory needs |
| `Llama3_70B_LoRA_finetuning.py` | LoRA + FSDP (distributed across GPUs) | Large models that need multi-GPU sharding |
| `Llama3_70B_qLoRA_finetuning.py` | QLoRA (LoRA + 4-bit quantization) | Very large models on memory-limited systems |

The file names refer to the default model each script uses, but you can pass a different model on the command line. This Learning Path uses `Llama3_3B_full_finetuning.py`. The key sections of that script are explained below. 

## Imports and dataset preparation

The script starts by importing PyTorch, dataset loading utilities, and the Hugging Face libraries used for supervised fine-tuning.

```python
import torch
import argparse
from datasets import load_dataset
from trl import SFTConfig, SFTTrainer
from transformers import AutoModelForCausalLM, AutoTokenizer
```

The `ALPACA_PROMPT_TEMPLATE` defines the instruction-following format for training data with three fields: instruction, input, and response. Each training example is formatted using this template so the model learns to recognize the pattern and produce structured answers.

The `get_alpaca_dataset()` function loads the Alpaca dataset from Hugging Face by default and formats each example using the template, appending the EOS (End of String) token. You'll patch this function later to load the Raspberry Pi dataset from a local JSONL file instead.

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

The `from_pretrained()` method downloads and initializes a pre-trained language model from Hugging Face. The tokenizer is loaded alongside it, with the padding token set to match the EOS token (required for batched training).

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

With the model and tokenizer loaded, the script prepares the training data by calling `get_alpaca_dataset()` with the tokenizer's EOS token and the specified dataset size. By default the script downloads the Alpaca dataset from Hugging Face, but you'll patch this function to load the Raspberry Pi JSONL file instead.

```python
    # Load and preprocess the dataset
    print(f"Loading dataset with {args.dataset_size} samples...")
    dataset = get_alpaca_dataset(tokenizer.eos_token, args.dataset_size)
```

## Training configuration

The training configuration controls how the SFT process runs. Notable parameters include `num_train_epochs` (initially set to 0.01 for a warmup pass, then updated for full training), `gradient_accumulation_steps` (batches to accumulate before each weight update), `learning_rate` (optimizer step size), and `max_length` (maximum sequence length). The logging parameters determine where and how often training metrics are recorded.

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

If `torch.compile()` is enabled, the script first optimizes the model graph for faster execution on the hardware. A short warmup pass (0.01 epochs) triggers compilation so the overhead doesn't affect the actual training run. After warmup, the script creates an `SFTTrainer` with the full epoch count and calls `trainer.train()`. The returned `trainer_stats` object contains metrics like loss, throughput, and training time.

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

## Patch the script for the Raspberry Pi dataset

The script loads the Alpaca dataset from Hugging Face by default. You need to patch the dataset loading function to use the local Raspberry Pi JSONL file instead.

First, open a new terminal on the DGX Spark (not inside the container) and navigate to the directory where you launched the Docker container. This is the directory that gets mounted as `/workspace` inside the container. Download the dataset file:

```bash
wget https://learn.arm.com/learning-paths/laptops-and-desktops/pytorch-finetuning-on-spark/raspberry_pi_qa.jsonl
```

Because this directory is mounted into the container with `-v ${PWD}:/workspace`, the file is immediately available inside the container at `/workspace/raspberry_pi_qa.jsonl`.

Back inside the container, copy the dataset into the script's working directory:

```bash
cp /workspace/raspberry_pi_qa.jsonl .
```

The following `sed` command replaces the `get_alpaca_dataset()` function to load from a local JSONL file instead of Hugging Face. The replacement function reads the Raspberry Pi Q&A pairs and formats them using the same Alpaca prompt template:

```bash
sed -i '/^def get_alpaca_dataset/,/^    return dataset\.map/c\
def get_alpaca_dataset(eos_token, dataset_size=500):\
    def preprocess(x):\
        texts = [\
            ALPACA_PROMPT_TEMPLATE.format(instruction, inp, output) + eos_token\
            for instruction, inp, output in zip(x["instruction"], x["input"], x["output"])\
        ]\
        return {"text": texts}\
    dataset = load_dataset("json", data_files="raspberry_pi_qa.jsonl", split="train")\
    if len(dataset) > dataset_size:\
        dataset = dataset.select(range(dataset_size))\
    return dataset.map(preprocess, remove_columns=dataset.column_names, batched=True)' Llama3_3B_full_finetuning.py
```

The key difference is `load_dataset("json", data_files="raspberry_pi_qa.jsonl", split="train")`, which reads the local file instead of downloading from Hugging Face. The function still applies the same Alpaca prompt template and EOS token.

## Run the fine-tuning

With the dataset patch applied, you're ready to run the fine-tuning. The command below trains the Llama 3.1 8B model using full fine-tuning on the Raspberry Pi dataset:

```bash
python Llama3_3B_full_finetuning.py \
--model_name "meta-llama/Llama-3.1-8B" \
--dataset_size 300 \
--output_dir "/workspace/models/Llama-3.1-8B-FineTuned"
```

The `--dataset_size 300` flag tells the script to use all entries in the Raspberry Pi dataset (the default is 500, but a smaller, focused dataset can be more effective than a larger generic one). The `--output_dir` flag saves the fine-tuned model and tokenizer to the specified directory. Because you mounted your current directory into the container with `-v ${PWD}:/workspace`, the saved model is also accessible from the host system.

Training takes a few minutes on DGX Spark. When it completes, you'll see a summary with metrics like runtime, samples per second, and loss, followed by a confirmation that the model was saved.

## What you've accomplished and what's next

In this section you:

- Reviewed the available fine-tuning scripts and their approaches
- Walked through each stage of the full fine-tuning script
- Patched the dataset loading function to use Raspberry Pi datasheet Q&A pairs
- Ran full fine-tuning and saved the resulting model with `--output_dir`

In the next section, you'll serve both the original and fine-tuned models and compare their responses to Raspberry Pi hardware questions.