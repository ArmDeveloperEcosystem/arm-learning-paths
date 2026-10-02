---
title: Deploy Phi-4-mini model with ONNX Runtime on Azure Cobalt 100

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers, ML engineers, and cloud practitioners looking to deploy Microsoft's Phi Models on Arm-based servers using ONNX Runtime.

learning_objectives:
    - Quantize and run the Phi-4-mini model with ONNX Runtime on Azure.
    - Analyze performance on Arm Neoverse N2-based Azure VMs powered by Cobalt 100.

prerequisites:
    - A Microsoft Azure [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/)
    - Basic understanding of Python and machine learning concepts
    - Familiarity with ONNX Runtime and Azure cloud services
    - Knowledge of large language model (LLM) fundamentals

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:42:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8c80b9778bfd1b0393e43e5eff673f0f83ec1e49c221ad33fe378fa6e5eba082
  summary_generated_at: '2026-10-01T19:42:07Z'
  summary_source_hash: 8c80b9778bfd1b0393e43e5eff673f0f83ec1e49c221ad33fe378fa6e5eba082
  faq_generated_at: '2026-10-01T19:42:07Z'
  faq_source_hash: 8c80b9778bfd1b0393e43e5eff673f0f83ec1e49c221ad33fe378fa6e5eba082
  summary: >-
    You'll build ONNX Runtime on an Arm-based Azure server powered by Cobalt 100 and use it to run a Phi-4-mini
    chatbot. First, you'll prepare Ubuntu 24.04 LTS, quantize and convert the model, and start the Python
    chatbot with `onnxruntime_genai`. You'll then send text prompts and inspect the terminal metrics,
    including tokens per second and time to first token, to validate inference and assess basic
    performance on the Arm CPU.
  faqs:
  - question: What do I pass to the `--model_path` argument in the chatbot script?
    answer: >-
      Use the path to the quantized and converted Phi-4-mini model assets that onnxruntime_genai
      expects. Make sure the quantization and conversion step completed successfully before starting
      the server.
  - question: Which execution provider should I choose when running the chatbot?
    answer: >-
      If you're unsure, keep the default execution provider, `follow_config`,
      so that the script uses providers defined in the model config. Override only if you need to explicitly
      set a different provider, as the script clears providers when you do.
  - question: How do I know that the chatbot server started correctly?
    answer: >-
      You should see the model load without errors and a prompt to enter text. After you send a
      prompt, the terminal prints generation metrics such as tokens per second and time to first
      token.
  - question: Do I need to use the exact Azure VM size used in the example?
    answer: >-
      No. The instructions were tested on a 32-core Azure `Dpls_v6` Cobalt 100 VM, but you can
      use another Arm-based Cobalt 100 instance. Use a comparable instance if you want results
      similar to the example output.
  - question: How can I limit the number of tokens in a chatbot response?
    answer: >-
      Set `--max_length` (or `-l`) when you run `phi4.py`. This limit includes both the prompt
      and generated tokens, so it isn't a limit on the response alone. If you omit the option,
      the script uses a maximum length of 2048 tokens.
# END generated_summary_faq

author: Nobel Chowdary Mandepudi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
armips:
    - Neoverse
subjects: ML
platforms:
  - Microsoft Azure Cobalt
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - ONNX Runtime

further_reading:
    - resource:
        title: ONNX Runtime Docs
        link: https://onnxruntime.ai/docs/
        type: documentation
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: Democratizing Generative AI with CPU-Based Inference
        link: https://blogs.oracle.com/ai-and-datascience/post/democratizing-generative-ai-with-cpu-based-inference
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has a weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths use this wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
