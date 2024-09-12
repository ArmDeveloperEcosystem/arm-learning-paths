---
title: Demo - Run a chatbot on an Arm CPU
overview: Running a chatbot can be expensive at scale, and surprising performance can be achieved with quantized (4 or 8 bit) small LLMs (~7 billion parameters) on Arm CPUs. CPUs are more accessible than GPUs and easier to program for ML for those new to the space. Cost is the largest benefit. Chat with an LLM here to see the price performance for yourself. This demo is running on AWS Graviton 4, on r8g.4xlarge instances via Lambdas.

demo_steps:
  - Type & send a message to the chatbot.
  - Get the chatbot's reply.
  - View stats showing how Graviton runs LLMs. 

diagram: config-diagram.png

configuration_popup_details: Super long list of configuration information to provide to the user. Should be context and all that to be crystal clear what the setup is.

configuration_dropdown_options:
  - parameters:
      param_name: LLM
      options:
        - name: llama-3-8b-instruct
          specs: The newest Llama model, with 8 billion parameters.
        - name: llama-2-7b
          specs: Llama2 has 7 billion paramters.
      selectable: true
      explanation: The LLM selected affects how performant the model is and such.

  - parameters:
      param_name: Instance Type
      options:
        - name: C7g.2xlarge
          specs: This instance has 8 CPUs with 16 GB RAM.
        - name: C7g.4xlarge
          specs: This instance has 16 CPUs with 16 GB RAM.
        - name: C7g.8xlarge
          specs: This instance has 32 CPUs with 32 GB RAM.
      selectable: true
      explanation: The specific hardware specs you will be using.

  - parameters:
      param_name: Compute Platform
      options:
        - name: AWS Graviton3
          specs: Details here as well
        - name: AWS Graviton2
          specs: Details here
      selectable: false
      explanation: The compute hardware series to select between.

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
    context: This is significantly higher than the average human reading rate of 5 words per second, delivering a stable and usable user chatbot experience from the Llama 3.1 LLM.
    color: var(--arm-green)
    min: 5
    max: 1000

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: llm_chatbot_first_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
