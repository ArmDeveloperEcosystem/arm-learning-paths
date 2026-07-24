---
title: Create and deploy a custom Topo Project

aliases:
    - /learning-paths/cross-platform/create-your-own-topo-templates/

description: Understand how to create and modify Topo Projects, allowing you to deploy your projects as containerized workloads to Arm-based Linux targets over SSH.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded, edge, and cloud software developers who want to create their own Topo Projects to be natively deployed with Topo.

learning_objectives:
    - Explain the purpose and structure of a Topo Project
    - Clone and deploy an existing Topo Project and modify it by adding new clone-time parameters
    - Create a new Topo Project from a Docker Compose project
    - Add x-topo metadata for configurable parameters, deployment guidance, and hardware requirements
    - Locate and install Agent Skills to assist with creating and reviewing Topo Projects

prerequisites:
    - Completion of the [Deploy containerized workloads to Arm-based Linux targets with Topo](/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/) Learning Path.
    - A host machine (x86 or Arm) with Linux, macOS, or Windows
    - An Arm-based Linux target accessible over SSH, for example an Arm-based Linux VM, Raspberry Pi, DGX Spark, or NXP i.MX 93
    - Docker installed on the host and target. For installation steps, see [Install Docker](/install-guides/docker/).
    - Basic familiarity with containers and CLI tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:10:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 280ddbaed118073072407c7e43c743f4d090e153201401deeec4648f9fb0c4ba
  summary_generated_at: '2026-07-02T19:10:34Z'
  summary_source_hash: 280ddbaed118073072407c7e43c743f4d090e153201401deeec4648f9fb0c4ba
  faq_generated_at: '2026-07-02T19:10:34Z'
  faq_source_hash: 280ddbaed118073072407c7e43c743f4d090e153201401deeec4648f9fb0c4ba
  summary: >-
    You'll author and deploy Topo Projects to Arm-based
    Linux targets over SSH. First, you'll clone and run a starter project to confirm your setup, then edit
    its `compose.yaml` to add `x-topo.parameters` entries that make the greeting emoji configurable at clone
    time. Next, you'll create a new project from an empty directory that serves a simple web page
    with configurable text and color while learning the core pieces of a project: standard Compose
    services, `x-topo` metadata, and build arguments for Arm Linux targets. You'll also see
    where to find optional Agent Skills to assist with creating or converting projects, and how
    to recognize a successful deployment by observing the configured behavior on the target.
  faqs:
  - question: What should I see after running `topo clone` on the Hello World project?
    answer: >-
      You should see a new directory at the path you provided (for example, `~/topo-welcome`) and
      clone output that includes lines like `Copy files` and `Cloning into ...`. After cloning,
      the project’s services can be deployed to the Arm-based Linux target as shown in the steps.
  - question: Where do I add a new clone-time argument such as a greeting emoji?
    answer: >-
      Add it under the `x-topo` parameters section in `compose.yaml`, alongside the existing `GREETING_NAME`
      parameter. Define the parameter name and metadata there so Topo can surface it during cloning.
  - question: How do I confirm that my new argument is being used?
    answer: >-
      Clone and deploy the updated project, then check the running service’s behavior for your
      change. For example, the Hello World greeting should include the emoji you configured, or
      the sample webpage should reflect your chosen text and color.
  - question: What are the essential parts of a minimal Topo Project I create from scratch?
    answer: >-
      Include a `compose.yaml` with standard Compose services, an `x-topo` metadata block, and project
      parameters wired to Docker build arguments when needed. The container image should be built for
      Arm Linux targets.
  - question: When should I use Agent Skills, and which ones are available for projects?
    answer: >-
      Use Agent Skills as optional aids when you want help creating or converting a project into
      a Topo Project. Topo provides `topo-project-context` for reference about `x-topo`
      and CLI behavior and `topo-project-bootstrap` to help convert a repository into a Topo Project.
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
        title: Topo Project specification
        link: https://github.com/arm/topo/tree/main/docs/project-specification
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
