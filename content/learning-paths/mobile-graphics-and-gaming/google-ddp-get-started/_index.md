---
title: Benchmark TinyStories with Google DDP and an AI agent

description: Use Google Developer Device Platform and an AI agent to compare TinyStories CPU inference with and without KleidiAI optimizations on a remote Pixel phone.

minutes_to_complete: 45

who_is_this_for: Developers who want to use a coding agent to access remote Android hardware and compare machine learning performance on an Arm-based phone.

learning_objectives:
    - Configure a Google Cloud project and local tools for Developer Device Platform (DDP).
    - Verify CLI authentication, enabled DDP services, and device catalog access.
    - Use the Google DDP agent skill with Antigravity to discover, reserve, inspect, and release a remote phone.
    - Use Antigravity to compare TinyStories CPU inference with and without KleidiAI optimizations.

prerequisites:
    - Access to a Google Cloud project with billing enabled and permissions to enable APIs and reserve DDP devices
    - A local macOS or Ubuntu 26.04 computer with a desktop session and permission to install software
    - The [Google Cloud CLI](/install-guides/gcloud/) and permission to install beta commands
    - The [Antigravity CLI](/install-guides/antigravity/) coding agent

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-13T19:27:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0aa08259f8eb66b7c96c727f2a48b338a557ddd908638ea4fe2907dbfe854519
  summary_generated_at: '2026-11-13T19:27:07Z'
  summary_source_hash: 0aa08259f8eb66b7c96c727f2a48b338a557ddd908638ea4fe2907dbfe854519
  faq_generated_at: '2026-11-13T19:27:07Z'
  faq_source_hash: 0aa08259f8eb66b7c96c727f2a48b338a557ddd908638ea4fe2907dbfe854519
  summary: >-
    You'll use Google DDP and Antigravity to compare TinyStories CPU
    inference on a remote Arm-based phone. First, you'll set up a Google Cloud project and local tools,
    then verify credentials, services, and device catalog access. After connecting to a phone,
    you'll ask Antigravity to benchmark llama.cpp with and without KleidiAI. You'll review throughput
    and kernel evidence, check the saved report, and confirm that the billable session has ended.
  faqs:
  - question: What do I need to prepare before requesting a Developer Device Platform phone?
    answer: >-
      Have the Google Cloud CLI, Antigravity CLI, and Python installed. Ensure that Node.js, `curl`, `adb`, and
      `scrcpy` are available on your development computer. Use a Google Cloud project with
      billing enabled and the necessary permissions. Sign in to the CLI, configure
      Application Default Credentials (ADC), and enable the three DDP services.
  - question: What should I verify before reserving a device?
    answer: >-
      Check that `gcloud` shows your intended active account and project, and that ADC
      can obtain a token. Confirm that `devicerun.googleapis.com`,
      `devicestreaming.googleapis.com`, and `testing.googleapis.com` are enabled.
      Inspect the device catalog for a physical configuration with streaming support.
  - question: What does Antigravity handle, and what do I approve?
    answer: >-
      You describe the phone and task in `agy`. Antigravity checks availability,
      prepares the reservation, connects the phone, and opens its screen. Before a
      billable session starts, review the proposed project, device, Android version,
      duration, and estimated cost. After review, approve the reservation in `agy`.
  - question: How do I review the TinyStories comparison?
    answer: >-
      Check that GPU offload was disabled and that both paths used the same model,
      quantization, inputs, thread count, and CPU placement. Check that Antigravity confirmed output agreement before timing and used repeated, warmed-up measurements. Review prompt-processing and token-generation results separately. Review the saved report for throughput, variation, and evidence of which Arm
      kernels ran.
  - question: How do I confirm that the billable device session ended?
    answer: >-
      Check that Antigravity canceled the recorded DDP session and confirmed its cloud
      state is `FINISHED` or `EXPIRED`. Closing the viewer alone doesn't stop billing.
      If the task stops early, ask Antigravity to release the session and verify its state.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: AI/ML
armips:
    - Arm C1
tools_software_languages:
    - Google Cloud
    - Agent Skills
    - Antigravity
    - llama.cpp
    - KleidiAI
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Google Developer Device Platform overview
        link: https://docs.cloud.google.com/developer-device-platform/overview
        type: documentation
    - resource:
        title: Google Developer Device Platform quickstart
        link: https://docs.cloud.google.com/developer-device-platform/quickstart
        type: documentation
    - resource:
        title: Google's Developer Device Platform agent skill
        link: https://docs.cloud.google.com/developer-device-platform/agent-skill
        type: documentation
    - resource:
        title: llama.cpp build instructions and KleidiAI support
        link: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
        type: documentation
    - resource:
        title: Termux installation instructions
        link: https://github.com/termux/termux-app#installation
        type: documentation
### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
