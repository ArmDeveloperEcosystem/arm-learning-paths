---
title: Migrate and optimize a .NET nopCommerce application on Microsoft Azure
description: Migrate, containerize, benchmark, and tune a .NET nopCommerce application on Azure Cobalt so you can validate Arm-based performance before rollout.
    
minutes_to_complete: 75

who_is_this_for: This Learning Path is for .NET and platform engineers migrating a production .NET application to Arm-based infrastructure on Azure.

learning_objectives:
    - Build a pinned nopCommerce release and baseline on Arm with the same .NET toolchain
    - Produce an SBOM and resolve platform-specific dependency cascades
    - Containerize with Dockerfile and .NET SDK multi-arch publish workflows
    - Apply architecture-conditional runtime tuning with measured results
    - Use the Arm MCP Server to automate endpoint selection, test generation, and optimization planning

prerequisites:
    - Azure account with permissions to create virtual machines
    - An Azure Cobalt 100-based virtual machine
    - Azure CLI (`az`) installed locally
    - Docker and .NET 9 SDK familiarity
    - Basic Linux command-line knowledge

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-06T20:45:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: af2852fa1dd4be29fbbc90cffe30efbecf96abad0d960681950ee1b104722e60
  summary_generated_at: '2026-07-06T20:45:31Z'
  summary_source_hash: af2852fa1dd4be29fbbc90cffe30efbecf96abad0d960681950ee1b104722e60
  faq_generated_at: '2026-07-06T20:45:31Z'
  faq_source_hash: af2852fa1dd4be29fbbc90cffe30efbecf96abad0d960681950ee1b104722e60
  summary: >-
    You'll learn how to migrate a .NET nopCommerce application to an
    Arm-based virtual machine powered by Azure Cobalt 100, create a reproducible baseline, and apply
    measured runtime tuning. First, you'll pin a specific nopCommerce release, verify a clean build,
    and capture an endpoint baseline on Arm to control for drift. By running dependency discovery and generating SBOM, you'll surface direct, transitive, and native payloads early to reduce surprises during
    deployment. You'll compare and choose a containerization path between a Dockerfile workflow, and a .NET
    SDK publish with multi-architecture delivery guardrails. Finally, you'll apply
    architecture-conditional runtime settings and validate them against fixed workloads so you
    can keep or discard changes based on repeatable results.
  faqs:
  - question: How should I choose the Azure VM configuration for the baseline?
    answer: >-
      Provision an Azure Cobalt-based environment as described in the [Azure Cobalt Learning Path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/cobalt/) and
      keep the toolchain and runtime configuration stable across runs. The flow was validated
      with Ubuntu 24.04 LTS in `westus2` on an example size of `Standard_D2ps_v6`.
  - question: What should I record when pinning the nopCommerce source?
    answer: >-
      Check out the specified release tag and run `git rev-parse --short=10` to capture the exact
      commit. Record the tag and short commit alongside the baseline results to avoid dependency
      drift.
  - question: How do I map direct and transitive dependencies before migration?
    answer: >-
      From the repository root, use `rg -n "<PackageReference|<ProjectReference" src` to identify
      direct references and the owning projects. Then generate an SBOM and review transitive packages
      to uncover native payloads that could affect Arm deployment.
  - question: Which containerization path should I start with?
    answer: >-
      Use the Dockerfile workflow as the default path for nopCommerce. Switch to .NET SDK publish
      when you want MSBuild-owned image metadata and have a repeatable plan for native packages,
      ensuring the SDK image matches Linux runtime dependencies and smoke-test results.
  - question: How do I know performance tuning changes took effect?
    answer: >-
      Stop the baseline process, set the runtime environment variables, and restart the application
      so the .NET runtime reads the new settings. Measure with fixed workloads and compare against
      the Arm endpoint baseline, keeping settings outside the code to switch profiles without
      rebuilding.
# END generated_summary_faq

author: Joe Stech

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
cloud_service_providers:
  - Microsoft Azure
tools_software_languages:
    - .NET
    - C#
    - Docker
    - Azure CLI
    - PostgreSQL
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: nopCommerce repository
        link: https://github.com/nopSolutions/nopCommerce
        type: documentation
    - resource:
        title: .NET SDK container publish overview
        link: https://learn.microsoft.com/dotnet/core/containers/overview
        type: documentation
    - resource:
        title: GitHub Copilot modernization for .NET
        link: https://learn.microsoft.com/dotnet/core/porting/github-copilot-app-modernization/overview
        type: documentation
    - resource:
        title: .NET on Arm
        link: https://learn.microsoft.com/dotnet/core/install/linux-arm64
        type: documentation
    - resource:
        title: SixLabors ImageSharp
        link: https://docs.sixlabors.com/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
