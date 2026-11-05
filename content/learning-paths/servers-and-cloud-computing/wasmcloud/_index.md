---
title: Build and benchmark a WebAssembly app on AWS Graviton with wasmCloud

description: Build a small Rust HTTP application as a WebAssembly component, run it with wasmCloud on AWS Graviton, and measure response time and throughput.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who want to run WebAssembly applications on Arm servers and understand their performance characteristics.

learning_objectives:
  - Identify how a WebAssembly component and its wasmCloud host work together.
  - Build and run a Rust HTTP handler on an AWS Graviton server.
  - Measure warm response time and concurrent request throughput.
  - Interpret the measurements and explain when instance reuse can help.

prerequisites:
  - An AWS account and an [AWS Graviton instance](/learning-paths/servers-and-cloud-computing/csp/) running Ubuntu 24.04 with SSH access and sudo privileges
  - Basic Linux command-line knowledge and familiarity with HTTP requests

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-05T22:51:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 150c6d5fa4400b77d321d754ba5bffefbea725fc85ccea8da33dd0317bdec3ee
  summary_generated_at: '2026-11-05T22:51:49Z'
  summary_source_hash: 150c6d5fa4400b77d321d754ba5bffefbea725fc85ccea8da33dd0317bdec3ee
  faq_generated_at: '2026-11-05T22:51:49Z'
  faq_source_hash: 150c6d5fa4400b77d321d754ba5bffefbea725fc85ccea8da33dd0317bdec3ee
  summary: >-
    You'll build a Rust HTTP handler as a WebAssembly component and run it with wasmCloud on an
    AWS Graviton-based server. You'll prepare the server, inspect and build the handler, then start
    `wash dev` and verify its response. Then, you'll measure warm request time, latency, and throughput
    under one-connection and concurrent load. Finally, you'll interpret the results and consider
    when wasmCloud instance pooling can help your application.
  # faqs:
  # - question: How do I know the wasmCloud development host started correctly?
  #   answer: >-
  #     Wait until `wash dev` prints `INFO listening for HTTP requests address=http://127.0.0.1:8000`.
  #     Keep that terminal running while you send requests from your second SSH terminal.
  # - question: Which endpoint should I send HTTP requests to during testing?
  #   answer: >-
  #     Send requests to `http://127.0.0.1:8000/` from the second SSH terminal on the same server.
  #     The development host listens on the server's loopback interface.
  # - question: Where do I modify the HTTP response, and how do I confirm the change?
  #   answer: >-
  #     Change the greeting in `src/lib.rs`, stop `wash dev` with **Ctrl+C**, and start `wash dev`
  #     again. After the listener message appears, send another request and check that the body
  #     says `hello from Graviton`.
  # - question: What metrics should I record for each test?
  #   answer: >-
  #     For the five timed `curl` requests, record the HTTP status and total time. For the
  #     one-connection and 32-connection `wrk` tests, save latency, requests per second, and any
  #     errors or timeouts.
  # - question: What should I check if my results vary between runs?
  #   answer: >-
  #     Keep `wash dev` running and stop other load tests or builds. Run the client on the same
  #     server, then repeat each test with the same duration, thread count, and connection count.
  #     Compare complete runs before drawing conclusions from small differences.
# END generated_summary_faq

author:
    - Jason Andrews
    - Liam Randall
 
generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: Web
platforms:
  - AWS Graviton
armips:
  - Neoverse
tools_software_languages:
  - wasmCloud
  - Rust
  - WebAssembly
operatingsystems:
  - Linux
further_reading:
  - resource:
      title: wasmCloud application quickstart
      link: https://wasmcloud.com/docs/quickstart/
      type: documentation
  - resource:
      title: wasmCloud runtime
      link: https://wasmcloud.com/docs/runtime/
      type: documentation
  - resource:
      title: wasmCloud benchmark scripts
      link: https://github.com/wasmCloud/wasmCloud/tree/main/scripts/bench
      type: documentation
  - resource:
      title: wasmCloud benchmark results
      link: https://wasmcloud.github.io/arewefastyet/
      type: documentation
  - resource:
      title: wrk HTTP benchmarking tool
      link: https://github.com/wg/wrk
      type: documentation
  - resource:
      title: Install Rust on Arm Linux
      link: /install-guides/rust/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
