---
title: Orchestrate a persistent local AI agent with Hermes on NVIDIA DGX Spark

description: Learn how to build a continuously running local AI agent on NVIDIA DGX Spark by combining Hermes Agent, Ollama, and Qdrant to handle event-driven document ingestion, semantic memory, and contextual retrieval using Arm Grace CPUs.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for developers building persistent local AI agent systems on NVIDIA DGX Spark who want to use Arm Grace CPUs for orchestration and Blackwell GPUs for local LLM inference and embeddings.

learning_objectives:
    - Describe how persistent AI runtimes combine orchestration, semantic memory, and local inference
    - Build a continuously running local AI agent using Hermes Agent, Ollama, and Qdrant
    - Use Arm Grace CPUs to orchestrate event-driven AI workflows on NVIDIA DGX Spark
    - Deploy semantic memory and contextual retrieval pipelines using vector embeddings and Qdrant

prerequisites:
    - An NVIDIA DGX Spark system with at least 15 GB of available disk space
    - Familiarity with running Python scripts and basic Docker container workflows

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:12:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 27302300e57da97c399d266b83f7a4bd4791e528349406e4ab5b2e1323452537
  summary_generated_at: '2026-07-28T16:12:38Z'
  summary_source_hash: 27302300e57da97c399d266b83f7a4bd4791e528349406e4ab5b2e1323452537
  faq_generated_at: '2026-07-28T16:12:38Z'
  faq_source_hash: 27302300e57da97c399d266b83f7a4bd4791e528349406e4ab5b2e1323452537
  summary: >-
    You'll build a continuously running local AI agent on NVIDIA DGX Spark using Arm Grace CPUs for
    orchestration. You'll configure Docker services with a persistent workspace, deploy Ollama,
    Qdrant, Open WebUI, and Hermes Agent, then connect Hermes to Ollama for document summaries and
    Qdrant embeddings. By the end, the services will monitor files, summarize documents, and provide
    contextual retrieval.
  faqs:
  - question: How do I know the base DGX Spark AI runtime is running correctly?
    answer: >-
      You should see containers for Ollama (inference), Qdrant (vector memory), and Open WebUI
      (browser access) running and healthy. Confirm that the persistent workspace exists and is
      mounted as expected.
  - question: Where should I put documents so Hermes picks them up automatically?
    answer: >-
      Place files in `workspace/inbox/`. Hermes watches that path and handles `on_created()` events
      to start the workflow.
  - question: I added Hermes but I don’t see summaries yet — what should I expect at this stage?
    answer: >-
      That is expected. In its initial setup, Hermes acts as an orchestration and event layer,
      printing handling output but not invoking a language model until you connect it to Ollama.
  - question: After I connect Hermes to Ollama, what result should I expect to confirm inference
      is working?
    answer: >-
      When you add a new document to `workspace/inbox/`, Hermes sends the content to the local model
      and you see an AI-generated summary in the runtime output. This indicates the inference
      path is wired correctly.
  - question: How can I confirm persistent semantic memory is active in Qdrant?
    answer: >-
      Qdrant should store an embedding for each processed document. Check that new vector entries
      appear after Hermes handles files and are available for contextual retrieval in the
      workflow.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - Docker 
    - Ollama

further_reading:
    - resource:
        title: NVIDIA DGX Spark
        link: https://www.nvidia.com/en-gb/products/workstations/dgx-spark/
        type: website
    - resource:
        title: Build a RAG pipeline on Arm-based NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_rag/
        type: Learning Path
    - resource:
        title: Build an offline voice chatbot with faster-whisper and vLLM on DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_voicechatbot/
        type: Learning Path
    - resource:
        title: Unlock quantized LLM performance on Arm-based NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_llamacpp/
        type: Learning Path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
