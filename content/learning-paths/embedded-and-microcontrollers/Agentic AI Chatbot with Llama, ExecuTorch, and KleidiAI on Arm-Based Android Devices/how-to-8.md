---
title: Designing the Agentic Brain
weight: 8 
layout: learningpathall
---

## From Chatbot to Agent
A standard chatbot answers questions based on its training data. An **Agent** can *do* things. It perceives the user's intent, decides which tool to use, and executes an action.

On mobile devices, resources are limited. We cannot run massive "Agent Frameworks" like LangChain easily. Instead, we rely on **Prompt Engineering** and **Structured Outputs** to build a lightweight Agentic Loop.

## The Agentic Loop
1.  **Observe**: Receive user input.
2.  **Think**: The LLM analyzes the input and decides if it needs a tool.
3.  **Act**: If a tool is needed, the LLM outputs a specific command.
4.  **Result**: The Android App executes the command and feeds the result back to the LLM.
5.  **Response**: The LLM generates the final answer.

## Prompt Engineering for Tools
To make Llama 3.2 "Agentic", we must give it a **System Prompt** that defines its persona and the available tools.

### The System Prompt
This prompt tells the model *how* to behave. We instruct it to output JSON or a specific tag when it wants to use a tool.

```text
<|start_header_id|>system<|end_header_id|>
You are a helpful Android Customer Support Agent.
You have access to the following tools:

1.  **check_battery_status**: Returns the current battery level and health. Use this when users ask about battery life or heating.
2.  **check_order_status(order_id)**: Returns the status of an order. Use this when users ask "Where is my order?".

If you need to use a tool, output ONLY the tool call in this format:
ACTION: tool_name(arguments)

Example:
User: "My phone is hot."
Assistant: ACTION: check_battery_status()

User: "Where is order #12345?"
Assistant: ACTION: check_order_status("12345")

If no tool is needed, just answer the user.
<|eot_id|>
```

## Simulating the Agent (Python)
Before moving to Android, verify your prompt works using Python.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "meta-llama/Llama-3.2-1B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)

system_prompt = """You are a helpful Android Customer Support Agent.
You have access to the following tools:
1. check_battery_status: Returns battery level.
If you need to use a tool, output ONLY: ACTION: tool_name()
"""

def query_model(user_input):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
    
    outputs = model.generate(input_ids, max_new_tokens=128)
    response = tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)
    return response

# Test 1: Normal Chat
print(f"User: Hi")
print(f"Agent: {query_model('Hi')}")

# Test 2: Tool Call
print(f"User: My battery is draining fast.")
print(f"Agent: {query_model('My battery is draining fast.')}")
```

### Expected Output
For the second test, the model should output something like:
`ACTION: check_battery_status()`

If it outputs conversational filler ("I can help with that. ACTION: ..."), you need to refine the prompt to be stricter ("output ONLY...").

## Next Steps
Now that we have a prompt that reliably triggers "Actions", we will implement the **Android Runtime** to catch these actions and execute real Kotlin code.