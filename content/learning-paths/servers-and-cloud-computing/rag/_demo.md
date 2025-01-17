---
title: Run a llama.cpp chatbot powered by Arm Kleidi technology

overview: | 
  Some description of this sucker.


demo_steps:
  - Type & send a message to the chatbot.
  - Receive the chatbot's reply.
  - View stats showing how well AWS Graviton runs LLMs. 

diagram: config-diagram-dark.png
diagram_blowup: config-diagram.png

terms_and_conditions: demo-terms-and-conditions.txt

prismjs: true  # enable prismjs rendering of code snippets

example_user_prompts:
  - Do Hyperscan and Snort3 work on Graviton4?
  - How can I easily build multi-architecture Docker images?
      
rag_data_cutoff_date: 2025/01/17

title_chatbot_area: Arm RAG Demo

prismjs: true



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
    context: This is significantly higher than the average human reading rate of 5 words per second, delivering a stable and usable user chatbot experience from the Llama-3.1-8B LLM.
    color: var(--arm-green)
    min: 5
    max: 1000

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: llm_chatbot_rag_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 2                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
