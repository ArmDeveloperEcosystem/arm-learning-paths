---
title: Set up and test the Neoverse Reference Design software stack

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in testing the Neoverse Reference Design firmware stack.

learning_objectives: 
    - Set up your environment.
    - Build the reference firmware stack.
    - Test the reference firmware stack.

prerequisites:
    - Some understanding of the [Reference Design software stack architecture](https://neoverse-reference-design.docs.arm.com/en/latest/about/software_stack.html)
    - Some understanding of the Linux command line
    - (Optional) A basic understanding of Docker and containers

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:55:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2b57893c6152769ff7cf1e9c37a869eebeff847fa634ea46732e28cca2193f09
  summary_generated_at: '2026-11-23T20:55:18Z'
  summary_source_hash: 2b57893c6152769ff7cf1e9c37a869eebeff847fa634ea46732e28cca2193f09
  faq_generated_at: '2026-11-23T20:55:18Z'
  faq_source_hash: 2b57893c6152769ff7cf1e9c37a869eebeff847fa634ea46732e28cca2193f09
  summary: You'll build and test the Neoverse N2 Reference Design software stack on a Fixed Virtual
    Platform (FVP). First, you'll prepare an Ubuntu host, fetch the source, and enter the build container.
    You'll build and package the firmware and BusyBox Linux image, then install the RD-N2 FVP and
    set `MODEL` to its binary. Finally, you'll run the model and check that Linux reaches a shell.
  faqs:
  - question: What should I check before starting a full build?
    answer: Use an AArch64 or x86_64 host running Ubuntu 22.04. Ensure at least 64 GB of free
      disk space and a minimum of 32 GB of RAM (48 GB recommended). The disk space and RAM is necessary to sync and build the platform
      software stack.
  - question: Where do I run the build script?
    answer: From the workspace inside the container, run `./build-scripts/rdinfra/build-test-busybox.sh
      -p rdn2 build`. Keep the `./build-scripts/` prefix; the command is run from the workspace.
  - question: How do I verify that the images are ready for the FVP?
    answer: After packaging, run `ls output/rdn2/`. Check that `grub-busybox.img`,
      `ramdisk-busybox.img`, and the `rdn2` directory are present. Run `ls output/rdn2/rdn2/ -l`
      to inspect the firmware files, including `fip-uefi.bin` and `tf-bl1.bin`.
  - question: How do I point the test at the RD-N2 model?
    answer: Install the RD-N2 FVP, then export `MODEL` with the path to the installed `FVP_RD_N2`
      binary.
  - question: What shows that the FVP test completed?
    answer: Check the model consoles for firmware and Linux boot messages. Reaching the BusyBox
      shell shows that the built stack booted on the RD-N2 Fixed Virtual Platform (FVP).
# END generated_summary_faq

author: 
    - Tom Pilar
    - Daniel Nguyen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Docker
    - FVP
    - Arm Development Studio
    - Runbook

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

