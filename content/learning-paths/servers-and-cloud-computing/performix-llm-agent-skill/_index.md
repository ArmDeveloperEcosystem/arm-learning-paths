---
title: Get started with the arm-performix agent skill for profiling and improving Arm workloads

description: Install the arm-performix skill to provide an AI coding assistant profiling context so it can drive Arm Performix, find code hotspots, diagnose pipeline stalls, and propose measured improvements on Arm Neoverse.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who use an AI coding assistant with Agent Skills support, such as GitHub Copilot in VS Code or Claude Code, and want the arm-performix skill to drive Arm Performix profiling workflows without memorizing the apx command-line interface.

learning_objectives:
    - Install and enable the arm-performix skill in your AI assistant
    - Trigger the skill with phrasing that activates the profiling workflow
    - Provide the context the skill needs to profile (target, binary, workload)
    - Read the analysis report the skill produces and drive the improvement loop

prerequisites:
    - An AI assistant with Agent Skills support enabled, such as [GitHub Copilot in VS Code](/install-guides/github-copilot/) or [Claude Code](/install-guides/claude-code/)
    - An Arm Neoverse-based Linux instance reachable from the assistant's environment. If you need an instance, complete the [Get started with Arm-based cloud instances Learning Path](/learning-paths/servers-and-cloud-computing/csp/)
    - Arm Performix installed with access to a supported execution method, such as the `apx` CLI, on the host `PATH`. For more information, see the [Arm Performix install guide](/install-guides/performix/). The skill guides AI assistants to use the `apx` CLI by default.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-23T15:07:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 33576a961d9992d8b8e5a6ef65080d58561f4d98d226b0a0dfa990bceffed0bf
  summary_generated_at: '2026-07-23T15:07:40Z'
  summary_source_hash: 33576a961d9992d8b8e5a6ef65080d58561f4d98d226b0a0dfa990bceffed0bf
  faq_generated_at: '2026-07-23T15:07:40Z'
  faq_source_hash: 33576a961d9992d8b8e5a6ef65080d58561f4d98d226b0a0dfa990bceffed0bf
  summary: >-
    You’ll install the `arm-performix` skill and learn how to activate it with a performance-focused prompt. You’ll learn that you need to provide an Arm Neoverse target, an absolute binary path, a repeatable workload, and a profiling goal in your prompts. Then, you'll interpret an example structured analysis report and learn how to use a report's recommendations to guide measured improvements.
  faqs:
  - question: How do I install the arm-performix skill using Git?
    answer: >-
      Clone the skills repository, then copy the `arm-performix` folder into your project’s skills directory.
  - question: Do I need to run the apx CLI myself, or does the skill handle it?
    answer: >-
      You don't need to run `apx` CLI commands manually. The skill guides AI assistants to use the `apx` CLI by default. Ensure Arm Performix is installed
      and `apx` is available on the host `PATH`.
  - question: How do I write prompts to activate the arm-performix skill?
    answer: >-
      Use clear profiling intent, for example: "Profile this workload on Arm and find the hotspots",
      "Why is this binary slow on my Arm Neoverse server?", "Use Performix to check whether my
      hot loop uses vector instructions", or "Investigate cache and translation lookaside buffer
      stalls on my Neoverse target". Vague prompts are less effective.
  - question: What context should I include so the skill can profile correctly?
    answer: >-
      State the target (Arm Neoverse-based Linux instance), an absolute path to the binary to analyze, how to run the workload, and the profiling goal. Provide any run arguments the assistant needs to execute the
      binary.
  - question: What should I expect after the skill completes a profiling run?
    answer: >-
      Expect a structured analysis report with sections such as "Bottleneck Summary", "Key Metrics",
      "Hot Functions", "Recommended Actions", "Ruled Out", and "Next Step". Use "Recommended Actions"
      and "Next Step" to drive code changes, then ask the assistant to rerun the recipe to validate
      the result.
# END generated_summary_faq

author:
    - Henry Wang

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - GitHub Copilot
    - MCP
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: Arm Performix product page
        link: https://developer.arm.com/servers-and-cloud-computing/arm-performix
        type: website
    - resource:
        title: Find Code Hotspots with Arm Performix
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: learning-path
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: /learning-paths/servers-and-cloud-computing/performix-microarchitecture/
        type: learning-path
    - resource:
        title: Optimize memory access behavior using Arm Performix and the Arm MCP Server
        link: /learning-paths/servers-and-cloud-computing/performix-memory-access/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

