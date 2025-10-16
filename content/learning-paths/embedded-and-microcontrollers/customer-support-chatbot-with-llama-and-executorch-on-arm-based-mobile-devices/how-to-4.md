---
title: Building the Chatbot Logic

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Conversation Framework (Python prototype)
```python 
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")

def generate_response(model, query, context):
    prompt = f"### Context:\n{context}\n### User Query:\n{query}\n### Assistant Response:"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
```

###### Context Memory (Simple JSON Store)

```python
import json

def update_memory(user_id, query, response):
    memory = json.load(open("chat_memory.json", "r"))
    memory[user_id].append({"query": query, "response": response})
    json.dump(memory, open("chat_memory.json", "w"))

```

