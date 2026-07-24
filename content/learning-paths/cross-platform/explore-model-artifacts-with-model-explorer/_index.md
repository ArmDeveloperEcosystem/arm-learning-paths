---
title: Inspect model artifacts and runtime profiles with Google Model Explorer and Arm extensions
    
description: Inspect ExecuTorch PTE, TOSA, VGF, ETRecord, and ETDump model artifacts with Google Model Explorer and Arm extensions.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for Edge AI developers who need to inspect model artifacts after backend delegation, understand graph structure and delegate coverage, and use those insights to reason about performance and behavior.

learning_objectives:
  - Set up Google Model Explorer with the combined ExecuTorch extension and separate Tensor Operator Set Architecture (TOSA) and VGF adapters. 
  - Open ExecuTorch deployment graphs and inspect delegate regions, work outside delegates, graph fragmentation, and backend-specific changes
  - Trace model transformations across PTE, TOSA, and VGF artifacts
  - Use ETRecord and ETDump overlays to connect exported graph structure with runtime profiling data

prerequisites:
  - Python 3.10, 3.11, or 3.12
  - Basic familiarity with PyTorch, ExecuTorch, or model deployment workflows
  - Git Large File Storage (LFS)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-24T17:13:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 27a823fec7ad01beca56b6ad1d6ee8a07085686f5fbffb0b361ccb4f573ecf6e
  summary_generated_at: '2026-07-24T17:13:27Z'
  summary_source_hash: 27a823fec7ad01beca56b6ad1d6ee8a07085686f5fbffb0b361ccb4f573ecf6e
  faq_generated_at: '2026-07-24T17:13:27Z'
  faq_source_hash: 27a823fec7ad01beca56b6ad1d6ee8a07085686f5fbffb0b361ccb4f573ecf6e
  summary: >-
    You'll use pre-generated `.pte`, `.tosa`, `.vgf`, `.etrecord`, and `.etdp`
    artifacts to understand how Google Model Explorer and Arm extensions expose
    model export, lowering, backend delegation, and runtime behavior. After
    installing the ExecuTorch extension and the TOSA and VGF adapters, you'll use
    a Cortex-M PTE to learn graph navigation, compare portable and XNNPACK
    Cortex-A programs, and diagnose no, clean, and fragmented Ethos-U delegation.
    You'll then inspect TOSA intermediate graphs, relate TOSA fragments to
    delegation boundaries, and compare a VGF-backed PTE with the standalone VGF
    graph used by workflows with the ML extensions for Vulkan. Finally, you'll
    open ETRecord files and load their matching ETDump data to identify whether
    delegate calls or non-delegated operators dominate runtime.
  faqs:
  - question: Which extensions should I enable to load the artifacts used here?
    answer: >-
      Enable the ExecuTorch extension to open `.pte` and `.etrecord` files and add `.etdp` profiling
      overlays. Enable the TOSA adapter for `.tosa` files and the VGF adapter for `.vgf` files. By running all three, you can switch between formats in one session.
  - question: How do I recognize delegate regions and fragmentation in a PTE?
    answer: >-
      Inspect the graph for a single contiguous delegate region, multiple smaller delegate regions,
      or nodes that remain outside the delegate. Use this view to see how much of the model
      is delegated and where non-delegated work occurs.
  - question: What result should I expect when opening the Cortex-M .pte example?
    answer: >-
      The deployment graph renders in the browser with expandable nodes and metadata. Seeing
      the graph confirms the installation and that the ExecuTorch extension is active.
  - question: How do I compare portable and XNNPACK PTEs for Cortex-A CPU paths?
    answer: >-
      Open both PTE files and examine operator nodes and backend-specific changes. Look for differences
      in how operators are implemented and where execution paths differ from portable kernels.
  - question: How do I connect runtime data to the exported graph?
    answer: >-
      Open the matching `.etrecord` file and its `.etdp` profiling data with the ExecuTorch extension enabled.
      Model Explorer overlays align these data with graph nodes so you can correlate structure
      with runtime behavior.
# END generated_summary_faq

author:
  - Matt Cossins

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
  - Cortex-A
  - Cortex-M
  - Ethos-U
  - Mali
tools_software_languages:
  - Model Explorer
  - ExecuTorch
  - PyTorch
  - Python
  - TOSA
  - VGF
  - ETRecord
  - ETDump
  
operatingsystems:
  - Linux
  - macOS
  - Windows

shared_path: true
shared_between:
  - embedded-and-microcontrollers
  - mobile-graphics-and-gaming

further_reading:
  - resource:
      title: Google Model Explorer
      link: https://github.com/google-ai-edge/model-explorer
      type: repository
  - resource:
      title: ExecuTorch extension for Model Explorer
      link: https://github.com/arm/executorch-extension-model-explorer
      type: repository
  - resource:
      title: PTE adapter for Model Explorer
      link: https://github.com/arm/pte-adapter-model-explorer
      type: repository
  - resource:
      title: ETRecord adapter for Model Explorer
      link: https://github.com/arm/etrecord-adapter-model-explorer
      type: repository
  - resource:
      title: ETDump data provider for Model Explorer
      link: https://github.com/arm/etdump-data-provider-model-explorer
      type: repository
  - resource:
      title: TOSA adapter for Model Explorer
      link: https://github.com/arm/tosa-adapter-model-explorer
      type: repository
  - resource:
      title: VGF adapter for Model Explorer
      link: https://github.com/arm/vgf-adapter-model-explorer
      type: repository
  - resource:
      title: ExecuTorch documentation
      link: https://docs.pytorch.org/executorch/stable/index.html
      type: documentation
  - resource:
      title: ExecuTorch ETRecord
      link: https://docs.pytorch.org/executorch/stable/etrecord.html
      type: documentation
  - resource:
      title: ExecuTorch ETDump
      link: https://docs.pytorch.org/executorch/stable/etdump.html
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
