---
title: Create and deploy a custom Topo Template

description: Understand how to create and modify Topo Templates, allowing you to deploy your projects as containerized workloads to Arm-based Linux targets over SSH.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded, edge, and cloud software developers who want to create their own Topo Templates projects to be natively deployed with Topo.

learning_objectives:
    - Explain the purpose and structure of a Topo Template
    - Clone and deploy an existing Topo Template and modify it by adding new clone-time arguments
    - Create a new Topo Template from a Docker Compose project
    - Add x-topo metadata for configurable arguments, deployment guidance, and hardware requirements
    - Locate and install Agent Skills to assist with creating and reviewing Topo Templates

prerequisites:
    - Completion of the [Deploy containerized workloads to Arm-based Linux targets with Topo](/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/) Learning Path.
    - A host machine (x86 or Arm) with Linux, macOS, or Windows
    - An Arm-based Linux target accessible over SSH, for example an Arm-based Linux VM, Raspberry Pi, DGX Spark, or NXP i.MX 93
    - Docker installed on the host and target. For installation steps, see [Install Docker](/install-guides/docker/).
    - Basic familiarity with containers and CLI tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T17:18:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 280ddbaed118073072407c7e43c743f4d090e153201401deeec4648f9fb0c4ba
  summary_generated_at: '2026-07-02T17:18:10Z'
  summary_source_hash: 280ddbaed118073072407c7e43c743f4d090e153201401deeec4648f9fb0c4ba
  faq_generated_at: '2026-07-02T17:18:10Z'
  faq_source_hash: 280ddbaed118073072407c7e43c743f4d090e153201401deeec4648f9fb0c4ba
  summary: >-
    This Learning Path guides you through authoring and deploying Topo Templates for Arm-based
    Linux targets over SSH. You start by cloning and running a Hello World template to validate
    your setup, then modify it by adding a new clone-time argument under the x-topo args block
    in compose.yaml. Next, you create a template from an empty directory that serves a simple
    web page with configurable text and color, define standard Compose services, and add x-topo
    metadata for arguments, deployment guidance, and hardware requirements. Optional Agent Skills
    help bootstrap or review your template. By the end, learners have a working template that
    Topo can build on the host and run on an Arm target.
  faqs:
  - question: What result should I expect after running topo clone for the Hello World template?
    answer: >-
      I should see a new directory at ~/topo-welcome with the template files and clone output
      indicating the repository was copied. That confirms Topo can fetch and prepare the template
      locally.
  - question: Where do I add a new clone-time argument like a greeting emoji?
    answer: >-
      I edit compose.yaml and add a new key under the x-topo args section. The template already
      includes GREETING_NAME there, so I add my new argument alongside it.
  - question: How do I document hardware requirements or deployment guidance in a template?
    answer: >-
      I place that information in the x-topo metadata block in compose.yaml. This keeps guidance
      and requirements with the template so users see it during cloning and deployment.
  - question: What components should a new Topo Template include before I test it?
    answer: >-
      It needs a compose.yaml with standard Compose services, an x-topo metadata block, build
      arguments exposed as Topo clone-time parameters, and a container image built for Arm Linux
      targets.
  - question: Which Agent Skill helps convert a Docker Compose project into a Topo Template?
    answer: >-
      I use topo-template-bootstrap to add or improve the template structure in an existing repository.
      The topo-template-context skill provides reference context for x-topo metadata, schema,
      docs, and CLI template behavior.
# END generated_summary_faq

author: Tomas Agustin Gonzalez Orlando

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
    - Cortex-A
    - Cortex-M
tools_software_languages:
    - Topo
    - Docker
    - SSH
operatingsystems:
    - Linux
    - macOS
    - Windows

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Topo Template format
        link: https://github.com/arm/topo-template-format
        type: documentation
    - resource:
        title: Topo repository
        link: https://github.com/arm/topo
        type: documentation
    - resource:
        title: Topo releases
        link: https://github.com/arm/topo/releases/latest
        type: website
    - resource:
        title: remoteproc-runtime
        link: https://github.com/arm/remoteproc-runtime
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

