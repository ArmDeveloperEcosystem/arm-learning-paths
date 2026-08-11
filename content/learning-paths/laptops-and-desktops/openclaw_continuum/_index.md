---
title: Extend OpenClaw for a local-first AI assistant across Arm platforms

description: Extend OpenClaw with local memory, document RAG, browser search, deterministic routing, and proactive scheduling, then move the same local-first runtime from NVIDIA DGX Spark with vLLM to a CPU-only Armv9 system with llama.cpp.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for developers who want to extend OpenClaw into a customizable local-first assistant with persistent memory, document RAG, explicit browser search, deterministic routing, and proactive scheduling.

learning_objectives:
    - Explain the local and external data boundaries of an OpenClaw-based runtime.
    - Deploy and validate the reference runtime with local vLLM inference on NVIDIA DGX Spark.
    - Verify persistent memory, document RAG, explicit browser search, deterministic routing, and proactive scheduling with Telegram and Qdrant.
    - Optionally move the same application workflows to a CPU-only Armv9 system through an OpenAI-compatible llama.cpp endpoint.

prerequisites:
    - An NVIDIA DGX Spark system with NVIDIA drivers, Docker and NVIDIA Container Toolkit
    - Administrative access on DGX Spark
    - Access to Telegram through a mobile, desktop, or web client
    - Familiarity with Linux, Docker Compose, and command-line tools
    - (Optional) A Radxa Orion O6 or comparable CPU-only Armv9 system running Debian 12, Docker, and at least 30 GB of memory

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-10T15:59:32Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8160160b7c59c2294a7666d9748b9f1f0115219431558ed7b378d6d3421d86e8
  summary_generated_at: '2026-08-10T15:59:32Z'
  summary_source_hash: 8160160b7c59c2294a7666d9748b9f1f0115219431558ed7b378d6d3421d86e8
  faq_generated_at: '2026-08-10T15:59:32Z'
  faq_source_hash: 8160160b7c59c2294a7666d9748b9f1f0115219431558ed7b378d6d3421d86e8
  summary: >-
    You'll extend OpenClaw into a local-first assistant that runs across Arm platforms with local
    inference and explicit external-data boundaries. First, you'll prepare a DGX Spark with Docker, Ollama, Qdrant, and vLLM. Then, you'll validate memory and
    document RAG, browser search, weather, routing, and scheduled notifications. You can optionally
    move the same workflows to a CPU-only Armv9 system with an OpenAI-compatible llama.cpp endpoint.
  faqs:
  - question: What should I check on the DGX Spark host before starting the containers?
    answer: >-
      Run `uname -m` and confirm the architecture is `aarch64`. Use `nvidia-smi` to verify GPU
      visibility, then run `docker run --rm --gpus all ubuntu nvidia-smi` to confirm GPU access from
      containers.
  - question: How do I get the Telegram bot token and chat ID for the runtime configuration?
    answer: >-
      Start a chat with **BotFather**, send `/newbot`, and copy the HTTP API token it returns. Send a
      test message to your new bot, call `curl "https://api.telegram.org/bot<your-telegram-bot-token>/getUpdates"`,
      and copy `message.chat.id`. Set both values in `.env` before starting the services.
  - question: How do I know that local memory persistence is working?
    answer: >-
      Send `/mem #home The boiler should be inspected every October.` in Telegram, then ask
      `/rag memory: When should the boiler be inspected?`. You should see October in the response. Confirm
      the record directly in the `personal_tracker_memory` Qdrant collection with the documented
      payload query.
  - question: Where do I upload documents for RAG, and how can I confirm ingestion?
    answer: >-
      Create the file on the device running your Telegram client and upload it with the `/knowledge`
      caption. Copy the returned filename, wait for indexing, and ask `/rag <returned-file-name>` a
      question about the file. Check the `personal_knowledge_base` Qdrant payload for that filename
      to confirm ingestion.
  - question: How do I verify that proactive scheduling is active?
    answer: >-
      Create a job with `/cron add`, confirm it's enabled with `/cron list`, and wait for the
      configured time. Check Telegram for the notification and inspect `docker logs --tail 30 openclaw-cron`
      for the `[cron] dynamic job sent` entry. You can use `/cron run <job-id>` to test
      the job without waiting.
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
    - Cortex-X
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - Docker
    - vLLM
    - llama.cpp
    - Ollama

further_reading:
    - resource:
        title: OpenClaw — Personal AI Assistant
        link: https://github.com/openclaw/openclaw
        type: documentation
    - resource:
        title: Build a RAG pipeline on Arm-based NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_rag/
        type: Learning Path
    - resource:
        title: Orchestrate a persistent local AI agent with Hermes on NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_persistent_agent/
        type: Learning Path
    - resource:
        title: Run ERNIE-4.5 Mixture of Experts model on Armv9 with llama.cpp
        link: /learning-paths/cross-platform/ernie_moe_v9/
        type: Learning Path
    - resource:
        title: OpenClaw Arm Continuum repository
        link: https://github.com/odincodeshen/openclaw-arm-continuum
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
