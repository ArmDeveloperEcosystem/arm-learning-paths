---
title: Fine Tuning Large Language Model - Running Inference
weight: 7 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Fine Tuning Large Language Model - Running Inference


###### Import Chat Template
- This function provides a predefined chat format suitable for Llama 3.1.
- Ensures that prompts are structured correctly for inference.


```python
from unsloth.chat_templates import get_chat_template
```

######  Apply Chat Template to the Tokenizer
- Updates the tokenizer with the Llama 3.1 chat template.
- Ensures the input messages are formatted according to Llama 3.1's expected structure.

```python
tokenizer = get_chat_template(
    tokenizer,
    chat_template="llama-3.1",
)


```
###### Enable Faster Inference
- Optimizes the model for low-latency inference.
- Uses Unsloth’s performance improvements to speed up text generation.checkpoints in "outputs" folder.

```python
FastLanguageModel.for_inference(model)

```


###### Define Input Messages
- Defines a conversation in a structured format
```python
messages = [
    {"i have a question about cancelling oorder {{Order Number}}"},
]
```
######  Tokenize Input Messages
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
###### Generate Model Output
- Generates text based on the input.
- max_new_tokens=64: Limits output length to 64 tokens.
- use_cache=True: Speeds up generation by caching intermediate results.
- temperature=1.5: Increases randomness in output (higher value = more diverse text).
- min_p=0.1: Controls token probability threshold (avoids unlikely tokens).
```python
outputs = model.generate(input_ids=inputs, max_new_tokens=64, use_cache=True, temperature=1.5, min_p=0.1)
```
###### Decode the Generated Output
- Converts tokenized output back into human-readable text

```python
tokenizer.batch_decode(outputs)
```

###### Save the LoRA Model Locally
- Saves the model (including its LoRA weights) to a local directory 

```python
model.save_pretrained("finetune_webbot")
```
###### Save the Tokenizer Locally
- Saves the tokenizer configuration into the "finetune_webbot" directory

```python
tokenizer.save_pretrained("finetune_webbot")
```
After saving the fine-tuned model, you can integrate it into your web application for real-time inference. Load the model and tokenizer, deploy them using an API (e.g., FastAPI, Flask), and serve responses based on user inputs. This enables seamless AI-powered interactions in your application.