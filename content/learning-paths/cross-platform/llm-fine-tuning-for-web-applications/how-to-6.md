---
title: Run LLM inference
weight: 8 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section runs LLM inference using the fine-tuned model. 

1. Import the chat template suitable for Llama 3.1 and ensure the prompts are suitable for inference.

    ```python
    from unsloth.chat_templates import get_chat_template
    ```

2. Apply the chat template to the tokenizer. 

    This code:
    - Updates the tokenizer with the Llama 3.1 chat template.
    - Ensures the input messages are formatted according to Llama 3.1's expected structure.

    ```python
    tokenizer = get_chat_template(
        tokenizer,
        chat_template="llama-3.1",
    )
    ```

3. Enable faster inference.

    Use the command below to:
    - Optimize the model for low-latency inference.
    - Use Unsloth's performance improvements to speed up text generation.checkpoints in "outputs" folder.

    ```python
    FastLanguageModel.for_inference(model)
    ```

4. Define the input conversation in a structured format.

    ```python
    messages = [
        {"i have a question about cancelling order {{Order Number}}"},
    ]
    ```

5. Tokenize the input messages using the parameters.

    The code performs the following tasks:
    - Converts the messages into tokens.
    - The apply_chat_template() function ensures the model receives the correct chat format.
    - tokenize=True: Converts text into numerical token IDs.
    - add_generation_prompt=True: Ensures the assistant's response is expected.
    - return_tensors="pt": Converts input into PyTorch tensors.
    - .to("cuda"): Moves data to GPU for faster processing.

    ```python
    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,  # Must add for generation
        return_tensors="pt",
    ).to("cuda")
    ```

6. Generate the model output based on the input.

    The parameters are:
    - max_new_tokens=64: Limits output length to 64 tokens.
    - use_cache=True: Speeds up generation by caching intermediate results.
    - temperature=1.5: Increases randomness in output (higher value = more diverse text).
    - min_p=0.1: Controls token probability threshold (avoids unlikely tokens).

    ```python
    outputs = model.generate(input_ids=inputs, max_new_tokens=64, use_cache=True, temperature=1.5, min_p=0.1)
    ```

7. Decode the generated output by converting the tokenized output back into human-readable text.

    ```python
    tokenizer.batch_decode(outputs)
    ```

8. Save the LoRA model (including its LoRA weights) to a local directory.

    ```python
    model.save_pretrained("finetune_webbot")
    ```

9. Save the tokenizer configuration into the `finetune_webbot` directory.

    ```python
    tokenizer.save_pretrained("finetune_webbot")
    ```

After saving the fine-tuned model, you can integrate it into your web application for real-time inference. 

Load the model and tokenizer, deploy them using an API such as FastAPI or Flask, and serve responses based on user inputs. This enables seamless AI-powered interactions in your application.