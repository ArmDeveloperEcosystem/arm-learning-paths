---
title: Adding Agentic AI Capabilities
weight: 6 

### FIXED, DO NOT MODIFY
layout: learningpathall
---
Enable the chatbot to perform reasoning, make decisions, and execute actions autonomously

##  Define Agentic Loop
```python 
class AgenticChatbot:
    def __init__(self, model):
        self.model = model

    def observe(self, input):
        return f"User said: {input}"

    def think(self, observation):
        return f"Decide best next step based on intent."

    def act(self, decision):
        if "refund" in decision:
            return "Processing refund..."
        elif "troubleshoot" in decision:
            return "Let's check your device settings."
        else:
            return "Connecting you with an agent."

    def respond(self, query):
        obs = self.observe(query)
        thought = self.think(obs)
        action = self.act(thought)
        return f"Reasoning: {thought}\nAction: {action}"
```
## Integrate Llama with Reasoning Loop
```python 
def generate_agentic_response(query, context):
    reasoning = agent.respond(query)
    model_response = generate_response(model, query, context)
    return reasoning + "\n\n" + model_response
```