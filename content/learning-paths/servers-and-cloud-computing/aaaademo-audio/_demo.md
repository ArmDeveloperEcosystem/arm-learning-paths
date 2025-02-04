---
title: Demo - Audio transcription on Arm
overview: | 
  This Arm Kleidi learning path shows how to use a single AWS Graviton instance -- powered by an Arm Neoverse CPU -- to build a simple “Token as a Service” server, used below to provide a chat-bot to serve a small number of concurrent users. 
  
  This architecture would be suitable for businesses looking to deploy the latest Generative AI technologies using their existing CPU compute capacity and deployment pipelines. The demo uses the open source llama.cpp framework, which Arm has enhanced by contributing the latest Arm Kleidi Technologies. Further optimizations are achieved by using the smaller 8 billion parameter Llama 3.1 model, which has been quantized to optimize memory usage. 
  
  Chat with the Llama-3.1-8B LLM below to see the performance for yourself, then follow the learning path to build your own Generative AI service on Arm Neoverse.



demo_steps:
  - Record your voice (giving mic permissions to your browser).
  - Review and send to the LLM.
  - Get transcription and view stats.


title_chatbot_area: Whisper Voice Demo

diagram: audio-pic-clearer.png
diagram_blowup: audio-pic.png

terms_and_conditions: demo-terms-and-conditions.txt


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
demo_template_name: whisper_audio_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 2                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


