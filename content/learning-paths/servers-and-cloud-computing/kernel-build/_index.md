---
title: Build Linux kernels for Arm cloud instances

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers building custom Linux kernels on Arm servers and cloud instances.

description: Compile and install custom Linux kernels on Arm cloud instances using TuxMake with configurations for 64 KB page sizes and Fastpath testing.

learning_objectives:
    - Set up a build environment for compiling Linux kernels on Arm cloud instances.
    - Build custom Linux kernels with various configurations using TuxMake.
    - Install and verify custom-built kernels.
    - Configure kernels for specific use cases, including 64 KB page sizes and Fastpath testing.

prerequisites:
    - An Arm cloud instance with at least 24 vCPUs and 200 GB of free storage running Ubuntu 24.04 LTS
    - Understanding of kernel images and modules
    - Familiarity with GRUB bootloader and initramfs

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:22:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2610a92c54a3f084b1f70aa007979898cc0931e75061582cb0acf2ef9e810f43
  summary_generated_at: '2026-09-15T21:22:08Z'
  summary_source_hash: 2610a92c54a3f084b1f70aa007979898cc0931e75061582cb0acf2ef9e810f43
  faq_generated_at: '2026-09-15T21:22:08Z'
  faq_source_hash: 2610a92c54a3f084b1f70aa007979898cc0931e75061582cb0acf2ef9e810f43
  summary: >-
    You'll prepare an Arm-based cloud instance running Ubuntu, and use TuxMake to compile custom Linux kernels
    with selectable versions and configurations. First, you'll choose between installing a kernel
    directly and generating packages, then verify the bootloader, modules, and build
    artifacts. You can configure 64 KB pages or create Fastpath-ready, build-only outputs,
    copying the flat artifacts to a test environment for validation.
  faqs:
  - question: How do I choose the kernel version tag when building with TuxMake?
    answer: >-
      The examples use valid Linux version tags such as `v6.18.1`, but you can select any other
      valid tag. Pass your chosen tag to the `--tags` flag and TuxMake builds that version.
  - question: What result should I expect after installing a custom kernel?
    answer: >-
      You should see a new GRUB entry for the installed kernel. After reboot, the running kernel
      version should match the one you built, and the corresponding modules should be available.
  - question: What should I check if my build is very slow or runs out of memory?
    answer: >-
      Use a sufficiently large Arm instance, as smaller instances take longer and can run out of
      memory during compilation. Confirm that you have ample free storage before starting the
      build.
  - question: Can I combine --fastpath true with --kernel-install?
    answer: >-
      No. Fastpath is a build-only workflow, so don't combine `--fastpath true` (or its demo shortcut)
      with `--kernel-install` or any `--install-from` commands. Build the kernel, then copy the flat
      artifacts to your test environment.
  - question: Which workflow should I use if I want packages instead of installing directly?
    answer: >-
      Run `./scripts/kernel_build_and_install.sh --tags v6.18.1 --include-bindeb-pkg` to produce
      Debian packages alongside the flat kernel artifacts. The `.deb` files are written under
      `~/kernels/v6.18.1` for later transfer and installation.
# END generated_summary_faq

author: Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - TuxMake

further_reading:
    - resource:
        title: TuxMake documentation
        link: https://tuxmake.org/
        type: documentation
    - resource:
        title: Linux kernel documentation
        link: https://www.kernel.org/doc/html/latest/
        type: documentation
    - resource:
        title: Arm kernel build repository
        link: https://github.com/geremyCohen/arm_kernel_install_guide
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
