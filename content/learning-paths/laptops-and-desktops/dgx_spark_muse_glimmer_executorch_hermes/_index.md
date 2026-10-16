---
title: Build a local Muse Glimmer 30B agent with Hermes and ExecuTorch on NVIDIA DGX Spark

description: Run Hermes on the Arm CPU and Muse Glimmer on the Blackwell GPU of NVIDIA DGX Spark, then use a local agent to diagnose and repair a broken Python release checker.

minutes_to_complete: 90

who_is_this_for: Developers who want to run a local AI agent on NVIDIA DGX Spark using Hermes Agent framework and the Muse Glimmer 30B parameter model.

learning_objectives:
    - Serve Muse Glimmer 30B through a local ExecuTorch CUDA endpoint
    - Connect Hermes Agent on the Arm CPU to the local model server
    - Restrict agent tools to a dedicated workspace and a network-disabled container
    - Verify an agent-generated code repair against acceptance tests

prerequisites:
    - SSH access to an NVIDIA DGX Spark running Ubuntu 24.04-based DGX OS, NVIDIA driver 580 or newer, and the CUDA 13.0 development toolkit
    - Docker Engine installed and permission to run containers
    - Python 3.12 with venv and pip support, curl, Git, a C++17 compiler, Make, and CMake 3.26 or newer
    - At least 100 GiB of available disk space and 80 GiB of available system memory before the native model export
    - Internet access to GitHub, PyPI, the PyTorch and NVIDIA package indexes, Hugging Face, Docker Hub, npm, and the official Hermes installer download services during setup

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
