---
title: Prepare the dataset
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Prepare the dataset for fine-tuning by formatting it to match the LLaMA-3.1 chat template.

1. Import the chat template functionality from Unsloth and structure the dataset in a format that LLaMA-3.1 expects.

    ```python
    from unsloth.chat_templates import get_chat_template
    ```

2. Apply the chat template to tokenizer and ensure the prompt formatting is consistent when training the model.

    ```python
    tokenizer = get_chat_template(
        tokenizer,
        chat_template = "llama-3.1",
    )
    ```

3. Format the dataset prompts using the steps below:
    - Extract the instruction column from the dataset.
    - Apply the chat template formatting to each instruction.
    - Return a new dictionary with the formatted text.

    ```python
    def formatting_prompts_func(examples):
        convos = examples["instruction"]
        texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
        return { "text" : texts, }
    pass
    ```

4. Load the [customer support chatbot training dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset) from Hugging Face.

    The dataset contains example conversations with instructions for fine-tuning.

    ```python
    from datasets import load_dataset
    dataset = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset", split = "train")
    ```

    The image below shows the dataset loading:

![example image alt-text#center](2.png )

5. Import the standardization function.

    The function `standardize_sharegpt` helps in structuring dataset inputs in a ShareGPT-like format (a commonly used format for LLM fine-tuning). This ensures that the data follows a standardized format required for effective instruction tuning.

    ```python
    from unsloth.chat_templates import standardize_sharegpt
    ```

6. Define a function to format the dataset and extract the instruction (input text) and response (output text) from the dataset.

    This stores the data as `instruction_text` and `response_text`.

    ```python
    def formatting_prompts_func(examples):
        return { "instruction_text": examples["instruction"], "response_text": examples["response"] }
    ```

7. Format the dataset by applying `formatting_prompts_func` to every record in the dataset. 

    Use batch processing (batched=True) for efficiency.

    ```python
    def formatting_prompts_func(examples):
        return { "instruction_text": examples["instruction"], "response_text": examples["response"] }
    ```

    The image below shows batch processing progress:

![example image alt-text#center](3.png )