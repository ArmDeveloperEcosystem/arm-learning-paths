---
title: Disassemble macOS binaries to check for SME and SME2 instructions

description: Use otool and llvm-objdump on macOS to verify that a compiled binary contains SME and SME2 instructions.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to disassemble binaries on macOS and check for Scalable Matrix Extension (SME) and SME2 instructions.

learning_objectives:
    - Identify the architecture, executable code, symbols, and supporting strings in a macOS binary.
    - Use two disassemblers to inspect instruction bytes, names, operands, and addresses.
    - Identify what disassembly can and can't tell you about SME and SME2 instructions.

prerequisites:
    - An Apple silicon Mac
    - Xcode 26.6 or newer, which includes `clang`, `otool`, `nm`, and `llvm-objdump`
    - Basic familiarity with C, assembly language, and the macOS terminal

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-02T15:37:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a97a3dc25f0e6079af133571a970e3ac8a2587589c0ad21e7db60d99f72f2230
  summary_generated_at: '2026-11-02T15:37:47Z'
  summary_source_hash: a97a3dc25f0e6079af133571a970e3ac8a2587589c0ad21e7db60d99f72f2230
  faq_generated_at: '2026-11-02T15:37:47Z'
  faq_source_hash: a97a3dc25f0e6079af133571a970e3ac8a2587589c0ad21e7db60d99f72f2230
  summary: >-
    You'll build a small arm64 Mach-O fixture on macOS. Then, you'll use `otool` and `llvm-objdump` to inspect it for SME and SME2 instructions. You'll compare strings and symbols with decoded executable code, checking instruction bytes, operands, addresses, and surrounding context. You'll also test comparison binaries, then combine the `llvm-objdump` and `awk` checks in a reusable script. 
  # faqs:
  # - question: How do I know I'm inspecting the correct architecture slice?
  #   answer: >-
  #     Select the `arm64` slice when you inspect a universal Mach-O binary. Use options such as
  #     `-arch arm64` with `otool`, `strings`, and `nm`, and confirm the slice with `lipo -info`.
  # - question: Do SME2-related strings or symbols prove that the binary contains SME2 instructions?
  #   answer: >-
  #     No. Strings and symbol names can suggest that the program relates to SME2, but that alone
  #     doesn't establish that SME or SME2 instructions are present. Inspect decoded executable code instead.
  # - question: How can I confirm that a decoded instruction matches its encoding?
  #   answer: >-
  #     Compare the instruction bytes, mnemonic, operands, and address in `llvm-objdump` output.
  #     Cross-check the decoded instruction and address with `otool` for the same binary.
  # - question: What does finding SME2 instructions in the binary tell me about runtime behavior?
  #   answer: >-
  #     It confirms that the instructions are present in the inspected executable code. It doesn't
  #     show whether the application calls that code or whether running it improves performance.
  # - question: How do I use the verification script with a comparison binary?
  #   answer: >-
  #     Put `verify-static-sme2.sh`, `strict-sme2.awk`, and the compiled binaries in the working
  #     directory. Run the script with the binary name; the positive fixture should pass, while
  #     the string-only control should report no matching instructions.
# END generated_summary_faq

author: Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips: []
tools_software_languages:
    - Clang
    - LLVM
    - Assembly
    - Bash
operatingsystems:
    - macOS

further_reading:
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 1)
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: LLVM llvm-objdump command guide
        link: https://llvm.org/docs/CommandGuide/llvm-objdump.html
        type: documentation
    - resource:
        title: SME Insights
        link: /insights/sme/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
