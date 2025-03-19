---
title: Configure, initialize, and perform fine-tuning 
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section performs fine-tuning using the Supervised Fine-Tuning (SFT) trainer to train the model using the prepared dataset. The trainer manages training configuration, optimization, and logging.

1. Import the necessary libraries. 

    The library summary is:
    - SFTTrainer (from trl) → Handles the fine-tuning process for LLMs using supervised fine-tuning (SFT).
    - TrainingArguments (from transformers) → Defines training hyperparameters like batch size, learning rate, and logging.
    - DataCollatorForSeq2Seq (from transformers) → Prepares batches of text data for training (handles padding, truncation).
    - is_bfloat16_supported() (from unsloth) → Checks if the system supports bfloat16 (a mixed-precision format for optimized training).

    ```python
    from trl import SFTTrainer
    from transformers import TrainingArguments, DataCollatorForSeq2Seq
    from unsloth import is_bfloat16_supported
    ```

2. Initialize the SFT trainer. 

    The parameters are:
    - Loads the Model & Tokenizer → Uses the pre-trained LLM and tokenizer.
    - Specifies the Training Dataset → The dataset (dataset) prepared earlier is used for fine-tuning.
    - Sets Maximum Sequence Length → Defines max_seq_length, ensuring model input size is within the supported limit.
    - Uses Data Collator for Batching → DataCollatorForSeq2Seq dynamically pads and tokenizes text data.
    - Enables Multi-Processing (dataset_num_proc = 2) → Uses two parallel processes for faster data loading.
    - Packing (packing = False) → Disables sequence packing, which can speed up training for shorter sequences.

    ```python
    trainer = SFTTrainer(
        model = model,
        tokenizer = tokenizer,
        train_dataset = dataset,
        dataset_text_field = "instruction",
        max_seq_length = max_seq_length,
        data_collator = DataCollatorForSeq2Seq(tokenizer = tokenizer),
        dataset_num_proc = 2,
        packing = False, 
    ```

3. Define the training hyperparameters. 

    The values are:

    - Batch Size (per_device_train_batch_size = 2) → Uses a small batch size to fit within GPU memory.
    - Gradient Accumulation (gradient_accumulation_steps = 4) → Accumulates gradients over 4 steps before updating model weights.
    - Warmup Steps (warmup_steps = 5) → Gradually increases the learning rate in the initial steps to stabilize training.
    - Training Steps (max_steps = 60) → Runs for 60 optimization steps (adjustable for full training).
    - Learning Rate (learning_rate = 2e-4) → Sets a moderate learning rate for stable fine-tuning.
    - Mixed Precision (fp16 or bf16) → Uses bfloat16 if supported; otherwise, falls back to fp16 for efficient computation.
    - Logging (logging_steps = 1) → Logs training progress every step.
    - Optimizer (optim = "adamw_8bit") → Uses adamw_8bit, which is a memory-efficient optimizer.
    - Weight Decay (weight_decay = 0.01) → Adds regularization to prevent overfitting.
    - Learning Rate Scheduler (lr_scheduler_type = "linear") → Linearly decays the learning rate over time.
    - Random Seed (seed = 3407) → Ensures reproducibility of training results.
    - Output Directory (output_dir = "outputs") → Saves the trained model checkpoints in "outputs" folder.

    ```python
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 60,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
    )
    ```


4. Modify the training approach so that the model learns to focus only on responses rather than both instructions and responses. 

    The code loads the `train_on_responses_only` function from Unsloth’s chat templates.

    ```python
    from unsloth.chat_templates import train_on_responses_only
    ```

    Apply the `train_on_responses_only` to the trainer. This modified the trainer behavior so that instead of training the model on full conversations, it now only learns from the assistant's responses.

    ```python
    trainer = train_on_responses_only(
        trainer,
        instruction_part = "<|start_header_id|>user<|end_header_id|>\n\n",
        response_part = "<|start_header_id|>assistant<|end_header_id|>\n\n",
    )
    ```


5. Inspect how the dataset has been tokenized and prepared for fine-tuning. 

    It checks how input sequences (prompts) and labels (expected model outputs) are formatted.

    Decode a sample training input using the steps:

    - Extracts the tokenized input sequence from the dataset (trainer.train_dataset[5]["input_ids"]).
    - Decodes it back into human-readable text using the tokenizer.
    - This helps verify how instructions and responses were tokenized.

    ```python
    tokenizer.decode(trainer.train_dataset[5]["input_ids"])
    space = tokenizer(" ", add_special_tokens = False).input_ids[0]
    tokenizer.decode([space if x == -100 else x for x in trainer.train_dataset[5]["labels"]])
    ```

6. Train the model by initiating the training process using the trainer object. 

    The trainer has been configured with model, dataset, optimizer, and training parameters:

    - Create an account in [Weights & Biases](https://wandb.ai/)
    -  Logging into [Weights & Biases](https://wandb.ai/) and [W&B server locally](https://wandb.me/wandb-server)
    -  You can locate your [API key](https://wandb.ai/authorize) in your browser at this link
    -  Paste an API key from your profile and press enter

    ```python
    trainer_stats = trainer.train()
    ```