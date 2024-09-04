---
title: Demo - Run a chatbot on an Arm CPU
overview: Running a chatbot can be expensive at scale, and surprising performance can be achieved with quantized (4 or 8 bit) small LLMs (~7 billion parameters) on Arm CPUs. CPUs are more accessible than GPUs and easier to program for ML for those new to the space. Cost is the largest benefit. Chat with an LLM here to see the price performance for yourself. This demo is running on AWS Graviton 4, on r8g.4xlarge instances via Lambdas.

demo_steps:
  - Set configurable options (or use defaults).
  - Type & send a message to the chatbot.
  - View answer and result metrics to understand its performance.
  - Repeat steps 1-3 as desired. Results will update with each message.

diagram: arch_diagram.png

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
tps_max: 50   # sets stat visuals for tps
tps_ranges:
  - name: Low
    context: TPS is low right now. The reasons why are x, y, and z.
    color: red
    min: 0
    max: 10
  - name: Mid
    context: Average TPS throughput. This is considered good enough for human readability.
    color: yellow
    min: 10
    max: 25
  - name: High
    context: Excellent TPS - a high quality UX is being delivered. Due to x, y, and z reasons.
    color: green
    min: 25
    max: 1000

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: llm_chatbot_first_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
