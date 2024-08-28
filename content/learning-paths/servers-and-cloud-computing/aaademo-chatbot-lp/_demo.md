---
title: Demo - Run a chatbot on an Arm CPU
overview: Running a chatbot can be expensive at scale, and surprising performance can be achieved with quantized (4 or 8 bit) small LLMs (~7 billion parameters) on Arm CPUs. CPUs are more accessible than GPUs and easier to program for ML for those new to the space. Cost is the largest benefit. Chat with an LLM here to see the price performance for yourself. This demo is running on AWS Graviton 4, on r8g.4xlarge instances via Lambdas.

demo_steps:
  - Set configurable options (or use defaults).
  - Type & send a message to the chatbot.
  - View answer and result metrics to understand its performance.
  - Repeat steps 1-3 as desired. Results will update with each message.

architecture_diagram: diagram.png

configuration_popup_details: Super long list of configuration information to provide to the user. Should be context and all that to be crystal clear what the setup is.

configuration_dropdown_options:
  - parameters:
      param_name: Instance Type
      options:
        - name: C7g.2xlarge
          specs: 
            - 8 CPUs
            - 16 GB RAM
        - name: C7g.4xlarge
          specs: 
            - 16 CPUs
            - 16 GB RAM
        - name: C7g.8xlarge
          specs: 
            - 32 CPUs
            - 32 GB RAM
      selectable: false
      explanation: The specific hardware specs you will be using.

  - parameters:
      param_name: LLM
      options:
        - name: llama-3-8b-instruct
          specs: 
            - Details here as well
        - name: llama-2-7b
          specs: 
            - Details here
      selectable: false
      explanation: The LLM selected affects how performant the model is and such.

  - parameters:
      param_name: Compute Platform
      options:
        - name: AWS Graviton3
          specs: 
            - Details here as well
        - name: AWS Graviton2
          specs: 
            - Details here
      selectable: false
      explanation: The compute hardware series to select between.

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
