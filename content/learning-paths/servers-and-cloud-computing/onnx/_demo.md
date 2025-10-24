---
title: Run a Phi-4-mini chatbot powered by ONNX Runtime
weight: 2

overview: | 
  This Learning Path shows you how to use a 32-core Azure Dpls_v6 instance powered by an Arm Neoverse N2 CPU to build a simple chatbot that you can use to serve a small number of concurrent users.

  This architecture is suitable for deploying the latest Generative AI technologies with RAG capabilities using their existing CPU compute capacity and deployment pipelines. 
  
  The demo uses the ONNX runtime, which Arm has integrated with KleidiAI. Further optimizations are achieved by using the smaller Phi-4-mini model, which has been optimized at INT4 quantization to minimize memory usage. 

  Chat with the LLM below to see the performance for yourself, and then follow the Learning Path to build your own Generative AI service on Arm Neoverse.


demo_steps:
  - Type and send a message to the chatbot.
  - Receive the chatbot's reply.
  - View performance statistics demonstrating how well Azure Cobalt 100 instances run LLMs. 

diagram: config-diagram-dark.png
diagram_blowup: config-diagram.png

terms_and_conditions: demo-terms-and-conditions.txt

prismjs: true  # enable prismjs rendering of code snippets


rag_data_cutoff_date: 2025/01/17

title_chatbot_area: Phi-4-mini Chatbot Demo



### Specific details to this demo
# ================================================================================
tps_max: 30   # sets stat visuals for tps
tps_ranges:
  - name: Low
    context: Around the average human reading rate of 3-5 words per second.
    color: var(--arm-green)
    min: 0
    max: 5
  - name: High
    context: This is significantly higher than the average human reading rate of 5 words per second, delivering a stable and usable user chatbot experience from the Phi-4-mini LLM using the ONNX runtime.
    color: var(--arm-green)
    min: 5
    max: 1000

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: phi_onnx_chatbot_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
