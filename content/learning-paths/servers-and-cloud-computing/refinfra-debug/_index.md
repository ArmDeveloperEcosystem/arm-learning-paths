---
title: Debug Neoverse N2 Reference Design with Arm Development Studio

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who are interested in debugging the Arm Neoverse N2 Reference Firmware Stack.

learning_objectives: 
    - Create a debug connection.
    - Debug a System Control Processor (SCP).
    - Debug Arm TF-A (Trusted Firmware-A).

prerequisites:
    - Arm Development Studio, and a license to use it
    - An Arm Neoverse Reference Design (RD) Software Stack
    - A Fixed Virtual Platform (FVP)
    - A basic understanding of Neoverse Reference Design (RD) platform boot

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:54:48Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ec7e276bee542acf3947c51b879ef5b3ac4fad3c09bed33c1020c08a03a7be17
  summary_generated_at: '2026-11-23T20:54:48Z'
  summary_source_hash: ec7e276bee542acf3947c51b879ef5b3ac4fad3c09bed33c1020c08a03a7be17
  faq_generated_at: '2026-11-23T20:54:48Z'
  faq_source_hash: ec7e276bee542acf3947c51b879ef5b3ac4fad3c09bed33c1020c08a03a7be17
  summary: You'll use Arm Development Studio to debug Neoverse N2 Reference Design firmware on an
    FVP. After starting the model and creating a connection, you'll inspect SCP,
    Local Control Processor (LCP), and RSE firmware. You'll adjust build flags to inspect variables, pause BL1 to attach
    the debugger, and set a BL31 breakpoint. Finally, you'll capture UEFI relocation addresses to
    load the correct symbols during BL33 debugging.
  faqs:
  - question: What do I need to start before creating a debug connection?
    answer: Start the Fixed Virtual Platform (FVP) model for the RD-N2 software stack before creating the debug connection.
  - question: How do I inspect SCP variables that appear optimized away?
    answer: Replace `-Og` with `-O0` in the appropriate `<compiler>-Baremetal.cmake` file under
      `rd-infra/scp/cmake/Toolchain`. Rebuild before inspecting variables in the debugger.
  - question: How do I attach the debugger before BL1 continues?
    answer: Add a branch-to-self instruction, `b .`, in `bl1_entrypoint` at `<workspace>/rd-infra/tf-a/bl1/aarch64/bl1_entrypoint.S`.
      The primary CPU spins there so you can attach and set breakpoints.
  - question: How do I set a breakpoint on BL31?
    answer: Open the **Functions** view, find `bl31_entrypoint`, and set a breakpoint. Continue
      execution until the processor stops at BL31.
  - question: How do I reuse UEFI symbol addresses for BL33 debugging?
    answer: Boot the FVP without debugging and record the relocated driver addresses from the
      Non-secure AP console. Repeat the same boot actions in the same order when debugging so
      that the module locations match.
# END generated_summary_faq

author: Daniel Nguyen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Development Studio

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Neoverse Reference Design Platform Software Documentation
        link: https://neoverse-reference-design.docs.arm.com/en/latest/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

