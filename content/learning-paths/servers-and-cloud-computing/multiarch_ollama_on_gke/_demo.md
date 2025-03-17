---
title: Run ollama in a multi-architecture nodes and containers environment with on GKE.

overview: | 
  
In this learning path, you will learn how to setup a GKE cluster with both x86 and Arm-based nodes. With nodes running both architectures, you'll next deploy a popular free, open source tool called Ollama which makes it easy to run popular AIML models on any platform (on-prem, locally on your laptop, and on a cloud provider).

Once you are running a multi-architecture cluster, you can take it to the next level to see price performance advantages of running your workloads on Arm vs x86.  Experiment further by researching which existing, and upcoming workloads could benefit most from single, or multi-architectural clusters.


demo_steps:
  - Spin up a GKE cluster with an x86 node.
  - Apply an ollama-x86-based Deployment and Service.
  - Add a new, Arm-based node to the cluster.
  - Apply an ollama-arm-based Deployment to the existing Service.
  - Observe how both nodes on both platforms can be run alongside each other.


diagram: config-diagram-dark.png
diagram_blowup: config-diagram.png

terms_and_conditions: demo-terms-and-conditions.txt


title_chatbot_area: Arm KleidiAI Demo 


prismjs: true  # enable prismjs rendering of code snippets

configuration_popup_details: Super long list of configuration information to provide to the user. Should be context and all that to be crystal clear what the setup is.

configuration_dropdown_options:
  - parameters:
      param_name: LLM
      options:
        - name: llama-3-8b-instruct
          specs: The newest Llama model, with 8 billion parameters.
        - name: llama-2-7b
          specs: Llama2 has 7 billion parameters.
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
    context: This is significantly higher than the average human reading rate of 5 words per second, delivering a stable and usable user chatbot experience from the Llama-3.1-8B LLM.
    color: var(--arm-green)
    min: 5
    max: 1000

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: llm_chatbot_first_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 2                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
