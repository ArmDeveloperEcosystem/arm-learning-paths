---
title: Convert uvprojx-based projects to csolution

description: Learn how to import, convert, and build uvprojx-based projects to csolution format using Keil Studio, µVision, and command-line tools for CMSIS-Toolbox compatibility.

minutes_to_complete: 10

who_is_this_for: This is a topic for users of µVision who want to migrate to the new project format (csolution) required by CMSIS-Toolbox.

learning_objectives:
    - Import, convert, and build uvprojx-based projects in Keil Studio.
    - Convert uvprojx-based projects in µVision.
    - Convert and build uvprojx-based projects on the command line.

prerequisites:
    - Install [Keil Studio](/install-guides/keilstudio_vs/) on your machine.
    - Install [µVision](/install-guides/mdk/) on your machine.
    - The &micro;Vision project must use Arm Compiler 6 as the default toolchain. Arm Compiler 5 is not supported.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:56:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 504b9156c3412760370a179068177441503408806f677f1beb8790e70fe95fff
  summary_generated_at: '2026-08-13T18:56:59Z'
  summary_source_hash: 504b9156c3412760370a179068177441503408806f677f1beb8790e70fe95fff
  faq_generated_at: '2026-08-13T18:56:59Z'
  faq_source_hash: 504b9156c3412760370a179068177441503408806f677f1beb8790e70fe95fff
  summary: >-
    You'll convert a µVision `uvprojx` project to the CMSIS-Toolbox `csolution` format. First, you'll
    use Keil Studio for VS Code to generate `.csolution.yaml`, `.cproject.yaml`, and `vcpkg-configuration.json`
    files. Alternatively, you'll export from µVision or run `uv2csolution` on the command line. Then,
    you'll confirm the conversion output and open the project in CMSIS-Toolbox or Keil Studio.
  faqs:
  - question: How do I start the conversion in Keil Studio?
    answer: >-
      In VS Code, open the folder that contains the .uvprojx file, then right-click the .uvprojx
      and select "Convert µVision project to csolution." Keil Studio generates the csolution and
      related files in the same workspace.
  - question: What result should I expect after a successful conversion?
    answer: >-
      You should see files such as `<project>.csolution.yaml`, `<project>.cproject.yaml`, and `vcpkg-configuration.json`.
      In Keil Studio, the **Output** window reports success and the `vcpkg` configuration is activated.
  - question: How do I verify the export from µVision worked?
    answer: >-
      Check the **Build Output** window for a successful conversion message. The generated `csolution`
      files appear alongside your project and can be opened by CMSIS-Toolbox or Keil Studio.
  - question: What should I check if the conversion option is missing or fails?
    answer: >-
      Confirm the µVision project uses Arm Compiler 6 as the default toolchain. Projects that
      use Arm Compiler 5 aren't supported for conversion.
  - question: Can I convert from the command line and what should I do next?
    answer: >-
      Yes. Install the `uv2csolution` tool and follow its command-line usage. The tool is available for
      macOS, Linux, and Windows. After conversion, use the generated `csolution` with CMSIS-Toolbox
      or open it in Keil Studio.
# END generated_summary_faq

author: Christopher Seidl

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-M
tools_software_languages:
    - Keil MDK
    - CMSIS-Toolbox
operatingsystems:
    - Windows
    - Linux
    - macOS

further_reading:
    - resource:
        title: Keil Studio User's Guide
        link: https://mdk-packs.github.io/vscode-cmsis-solution-docs/index.html
        type: documentation
    - resource:
        title: Introducing Keil MDK Version 6
        link: https://community.arm.com/arm-community-blogs/b/internet-of-things-blog/posts/keil-mdk-version-6
        type: blog
    - resource:
        title: keil.arm.com
        link: https://keil.arm.com
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
