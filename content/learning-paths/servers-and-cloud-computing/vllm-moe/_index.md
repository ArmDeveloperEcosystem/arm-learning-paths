---
title: Run and benchmark vLLM mixture of experts models on Arm CPUs

description: Serve BF16 and INT8/W8A8 mixture of experts models with vLLM on Arm CPUs, validate responses, and compare throughput and latency.
    
minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers interested in running and benchmarking mixture of experts (MoE) models with vLLM on Arm CPUs.

learning_objectives:
- Install and verify vLLM for CPU inference on an Arm server.
- Serve BF16 and INT8/W8A8 MoE models and validate a response.
- Benchmark MoE serving performance with vLLM bench serve.
- Compare BF16 and INT8/W8A8 MoE performance using relative speedups.

prerequisites:
- An Arm-based Linux server running Ubuntu 24.04 LTS, with enough CPU cores, memory, and disk space for large MoE models
- CPU support for BF16 and I8MM instructions
- Python 3.12 and basic familiarity with Hugging Face models and vLLM serving

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-26T21:06:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4ed4388a460eb47c480dca2abcccec73e3e493891c2192204ea2dc163165229f
  summary_generated_at: '2026-10-26T21:06:00Z'
  summary_source_hash: 4ed4388a460eb47c480dca2abcccec73e3e493891c2192204ea2dc163165229f
  faq_generated_at: '2026-10-26T21:06:00Z'
  faq_source_hash: 4ed4388a460eb47c480dca2abcccec73e3e493891c2192204ea2dc163165229f
  summary: >-
    You'll set up vLLM on an Arm-based Linux server to serve and benchmark MoE
    models. First, you'll check CPU support and install vLLM. You'll then choose BF16 and INT8/W8A8
    checkpoints, serve each model, and validate a chat response. Next, you'll prepare model-specific
    ShareGPT subsets and benchmark concurrent requests. Finally, you'll compare throughput and latency
    using matching workloads and concurrency values.
#   faqs:
#   - question: How do I know the vLLM server is ready to receive requests?
#     answer: >-
#       Wait for `Application startup complete` in the server terminal to confirm that the server
#       is listening on port `8000`. Then send a test request with `curl` to
#       `/v1/chat/completions`; a response with generated text confirms that inference works.
#   - question: What should I check if the test request fails or I get a port error?
#     answer: >-
#       Check that only one vLLM server is using port `8000`. If another server is running,
#       stop it with **Ctrl+C** and wait for it to exit. Start the desired model server,
#       wait for it to become ready, and retry your request.
#   - question: Which model IDs should I use for the BF16 and INT8/W8A8 runs?
#     answer: >-
#       For BF16, use `google/gemma-4-26B-A4B-it`, `unsloth/gpt-oss-20b-BF16`, or
#       `Qwen/Qwen3-30B-A3B-Thinking-2507`. For INT8/W8A8, use
#       `RedHatAI/Qwen3-30B-A3B-Thinking-2507-quantized.w8a8`. Set the same model ID in
#       your serving and test-request terminals.
#   - question: How do I run the benchmark against the active server?
#     answer: >-
#       Keep the model server running. In another terminal, activate `vllm_env_new` and set
#       `MODEL` to the running model ID. Prepare the ShareGPT subset selected with that model's
#       tokenizer, then run `vllm bench serve` against `/v1/chat/completions` with the matching
#       subset file.
#   - question: How should I interpret and compare the reported metrics?
#     answer: >-
#       Compare request and output-token throughput, time to first token (TTFT), and time per
#       output token (TPOT) at matching concurrency values and workloads. Calculate throughput
#       speedup as optimized throughput divided by baseline throughput: `3.25x` means a 225%
#       increase. Calculate latency reduction as `(baseline - optimized) / baseline × 100%`.
#       You can't recreate the historical pre-optimization baseline with this guide, and you
#       don't evaluate model quality here.
# END generated_summary_faq

author:
- Gauri Sahnan
- Fadi Arafeh

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
- Neoverse
tools_software_languages:
- vLLM
- Python
- PyTorch
- Hugging Face
operatingsystems:
- Linux

further_reading:
- resource:
  title: vLLM Documentation
  link: https://docs.vllm.ai/
  type: documentation
- resource:
  title: vLLM GitHub Repository
  link: https://github.com/vllm-project/vllm
  type: website
- resource:
  title: Hugging Face Model Hub
  link: https://huggingface.co/models
  type: website
- resource:
  title: Build and Run vLLM on Arm Servers
  link: /learning-paths/servers-and-cloud-computing/vllm/
  type: website
- resource:
  title: Run vLLM inference with quantized models and benchmark on Arm servers
  link: /learning-paths/servers-and-cloud-computing/vllm-benchmark-quantisation/
  type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
