---
title: Build Muse Glimmer 30B with Hermes and ExecuTorch on DGX Spark

    
description: Run Hermes on the Arm CPU and Muse Glimmer on the Blackwell GPU of NVIDIA DGX Spark, then use the local agent with text and image capabilities to investigate and repair a broken Python checker.

minutes_to_complete: 90

who_is_this_for: Developers who want to run a local AI agent on NVIDIA DGX Spark using the Hermes Agent framework and the Muse Glimmer 30B parameter model.

learning_objectives:
    - Serve Muse Glimmer 30B with text and image input through a local ExecuTorch CUDA endpoint.
    - Connect Hermes Agent on the Arm-based CPU to the local model server.
    - Restrict agent tools to a dedicated workspace and a network-disabled container.
    - Use image and text inputs to diagnose a release error and verify the agent-generated code repair against acceptance tests.

prerequisites:
    - SSH access to an NVIDIA DGX Spark running Ubuntu 24.04-based DGX OS, NVIDIA driver 580 or later, and the CUDA 13.0 development toolkit
    - Docker Engine installed and permission to run containers
    - Python 3.12 with venv and pip support, curl, Git, as well as C++17 compiler, Make, and CMake 3.26 or later
    - At least 100 GiB of available disk space and 80 GiB of available system memory before the native model export
    - Internet access to download services during setup

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-09T19:30:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 677ba594753b09099a26da604c0a6f4abdc210dcbcade9d00b708d8fb7b01f46
  summary_generated_at: '2026-11-09T19:30:16Z'
  summary_source_hash: 677ba594753b09099a26da604c0a6f4abdc210dcbcade9d00b708d8fb7b01f46
  faq_generated_at: '2026-11-09T19:30:16Z'
  faq_source_hash: 677ba594753b09099a26da604c0a6f4abdc210dcbcade9d00b708d8fb7b01f46
  summary: >-
    You'll serve Muse Glimmer 30B through a local ExecuTorch CUDA endpoint, then connect Hermes on
    the Arm-based CPU. First, you'll verify model access and the restricted Docker sandbox. Then, you'll provide a
    release-summary image so that Hermes can identify the incorrect deployment decision, inspect the
    Python checker, and repair it. You'll run all four acceptance tests and review the code diff.
    Finally, you'll identify ways to extend the agent and add more capabilities.
  # faqs:
  # - question: How do you use the three SSH sessions?
  #   answer: >-
  #     Keep the model server running in the first SSH session. Use the second session to install
  #     and run Hermes after checking the endpoint. Open a third session temporarily to inspect the
  #     Docker container, then use it to run the host-side acceptance tests after the agent repair.
  # - question: What should you check to confirm Hermes is installed before testing the model connection?
  #   answer: >-
  #     Run `~/muse-agent/bin/hermes chat --help`. Expect `Hermes installed` and the CLI help
  #     output; this confirms the CLI launches. Verify the model connection separately using the
  #     checks in this section.
  # - question: Why do external network calls fail from Hermes tools?
  #   answer: >-
  #     Your terminal tool runs inside a Docker container with network access disabled, so external
  #     calls fail. To verify, inspect the container from your third SSH session and confirm its
  #     network mode is `none`.
  # - question: How do you ask Hermes to interpret the image before it repairs the checker?
  #   answer: >-
  #     Start Hermes with `--image "$HOME/muse-agent/release-summary.png"` and ask it to report the
  #     passed, failed, and skipped counts, the displayed decision, and whether deployment should
  #     proceed. Tell it not to run tools or change files yet. Then use the image as context and ask
  #     it to diagnose and repair `/demo/output/release_tool.py`.
  # - question: What should you expect after Hermes repairs the release checker?
  #   answer: >-
  #     Expect all four acceptance tests to pass and print `OK`. Read
  #     `~/muse-agent/demo/output/fix-notes.md` and inspect the diff to confirm that the notes match
  #     the code and test output. Confirm that failed tests block deployment.
# END generated_summary_faq

author: Matt Cossins

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
    - ExecuTorch
    - Hermes Agent
    - Muse Glimmer
    - CUDA

further_reading:
    - resource:
        title: ExecuTorch Muse Glimmer example
        link: https://github.com/pytorch/executorch/blob/main/examples/models/muse-glimmer/README.md
        type: documentation
    - resource:
        title: Muse Glimmer quantized model weights
        link: https://huggingface.co/meta-models/Muse-Glimmer-30B-GGUF
        type: website
    - resource:
        title: Hermes Agent configuration
        link: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
        type: documentation
    - resource:
        title: Running Hermes on a personal or work machine
        link: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine
        type: documentation
    - resource:
        title: Hermes Python CLI
        link: https://hermes-agent.nousresearch.com/docs/user-guide/cli
        type: documentation
    - resource:
        title: Muse Glimmer prompting guide
        link: https://dev.meta.ai/docs/muse-glimmer/prompting
        type: documentation

weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
