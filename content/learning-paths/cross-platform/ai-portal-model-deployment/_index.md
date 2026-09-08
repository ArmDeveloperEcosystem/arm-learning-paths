---
title: Deploy models with the Arm AI Portal

description: Learn how to find a suitable model in Arm's AI Portal and deploy it on local or remote hardware.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to deploy optimized models from the Arm AI Portal.

learning_objectives: 
    - Discover how AI Portal helps you select a suitable model
    - Deploy a model using instructions on its Hugging Face page
    - Deploy a model using Topo, Arm's deployment tool

prerequisites:
    - An Arm Linux target device to deploy models on, with enough memory and storage for the selected model and application
    - A development host running Windows, macOS, or Linux with internet access and permission to install tools
    - Python 3 with `pip` and virtual environment support
    - Docker and Topo to run containerized code examples from the AI Portal
    - SSH access and permission to provision keys when deploying to a remote target
    - A Hugging Face account for downloading models
    - Basic familiarity with terminal commands and containers

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-04T15:25:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ceb144f04402ee3c107da9dd8c1102d77f1f995601edd2d41dd72594cd8d795d
  summary_generated_at: '2026-09-04T15:25:01Z'
  summary_source_hash: ceb144f04402ee3c107da9dd8c1102d77f1f995601edd2d41dd72594cd8d795d
  faq_generated_at: '2026-09-04T15:25:01Z'
  faq_source_hash: ceb144f04402ee3c107da9dd8c1102d77f1f995601edd2d41dd72594cd8d795d
  summary: >-
    You'll use the Arm AI Portal to compare models with filters and analytics, then follow two
    deployment workflows. First, you'll download the **TinyLlama-1.1B-Chat INT4 — ONNX GenAI (Graviton G4) model**
    from Hugging Face and run it on an Arm Linux target with ONNX Runtime. Then, you'll deploy a
    containerized ExecuTorch image classifier code example with Topo.
  faqs:
  - question: How do I narrow down models on AI Portal?
    answer: >-
      Use the Arm AI Portal's filters and analytics to compare models. Open a model's details page
      to review related content, such as Learning Paths and code examples.
  - question: How do I deploy and test TinyLlama on an Arm Linux target?
    answer: >-
      Install the required Python packages, create a Hugging Face access token, and set it in
      `HF_TOKEN`. Use `snapshot_download` to download the model files, link them from `model_dir`,
      and run the supplied ONNX Runtime test script.
  - question: What do I need on the Arm Linux target to start the TinyLlama deployment?
    answer: >-
      Update the packages and install Python tooling with `sudo apt update` and `sudo apt install
      -y python3-pip python3-venv`. The model is optimized for AWS Graviton 4-based Amazon EC2
      instances, such as M8g.
  - question: What should I check if the deployed image classifier URL is inaccessible?
    answer: >-
      If the deployment succeeded on a cloud instance, make sure that you've enabled access to port
      `7860`. If deployment failed, check the target's available disk space and confirm that the
      Docker container is running with `docker container ls`.
  - question: How do I free port 7860 before deploying another code example?
    answer: >-
      Stop the containers that expose port `7860` with `docker container stop $(docker container ls
      --filter expose=7860 -q)`. You can then deploy another code example that uses the port.
# END generated_summary_faq

author: Andrew Pickard

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - Python
    - Docker
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Discover and deploy AI models with the Arm AI Portal MCP server
        link: /learning-paths/servers-and-cloud-computing/ai-portal-mcp/
        type: website
    - resource:
        title: Deploy containerized workloads to Arm-based Linux targets with Topo
        link: /learning-paths/cross-platform/deploy-containerized-workloads-with-topo/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
