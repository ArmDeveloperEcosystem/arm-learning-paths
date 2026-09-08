---
title: Discover and deploy AI models with the Arm AI Portal MCP server
description: Connect an MCP-compatible AI harness to the Arm AI Portal MCP server to find models, compare deployment targets, and plan deployment workflows.

minutes_to_complete: 20

who_is_this_for: This Learning Path is for developers who want to use the Arm AI Portal Model Context Protocol (MCP) server to discover models and plan deployments for Arm-based cloud or edge targets.

learning_objectives:
    - Connect the Arm AI Portal Model Context Protocol (MCP) server to an MCP-compatible AI harness
    - Search and compare models by task, runtime, performance, memory usage, and Arm target, and find relevant documentation
    - Deploy and validate a selected model on an Arm-based edge target
    - Identify the supported workflow for cloud deployment and the current limits of mobile deployment

prerequisites:
    - An MCP-compatible AI client, such as Codex, Claude Code, or GitHub Copilot
    - Basic familiarity with AI model tasks, runtimes, and deployment targets
    - For edge deployment, a Docker-capable `arm64` Linux device reachable over SSH

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-02T19:01:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: false
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a90c72ee8c3b6996c013bf01aec4ff76d1bdbac455bf08a63fc701e2458ae53b
  summary_generated_at: '2026-09-02T19:01:07Z'
  summary_source_hash: a90c72ee8c3b6996c013bf01aec4ff76d1bdbac455bf08a63fc701e2458ae53b
  faq_generated_at: '2026-09-02T19:01:07Z'
  faq_source_hash: a90c72ee8c3b6996c013bf01aec4ff76d1bdbac455bf08a63fc701e2458ae53b
  summary: >-
    You'll connect an MCP-compatible AI harness to the Arm AI Portal MCP server using the server's URL. After setting up the MCP server, you'll search the model
    catalog with natural-language prompts and compare candidates by task, runtime, latency,
    performance, memory usage, and Arm target. You'll also find related documentation and explore deployment
    paths for cloud and Arm-based edge targets. Finally, you'll learn best practices for deploying with the MCP server.
  faqs:
  - question: Do I need to install the Arm AI Portal MCP server locally?
    answer: >-
      No. The server uses Streamable HTTP. Add it to your AI harness by specifying the
      MCP server's URL.
  - question: How do I know the MCP server is connected to my AI harness?
    answer: >-
      List the configured MCP servers and confirm that `arm-ai` appears as connected. Then, ask your
      harness to use the Arm AI Portal MCP server and call `find_model`. If it uses web search
      instead, explicitly ask it to use the `arm-ai` MCP tools.
  - question: What kind of query helps me narrow to the right model?
    answer: >-
      Start with your goal, then add constraints such as model task, Arm target, runtime, latency,
      memory, and performance. If you're unsure of the task, begin with a broad question and
      refine based on the returned options.
  - question: How do I use the MCP server to plan a deployment?
    answer: >-
      Prompt your harness the model and target that you selected and how you can access the target. Ask
      it to separate prerequisites, target preparation, deployment, validation, and cleanup. Review
      the plan and approve it before the harness runs commands or changes the target.
  - question: How do I validate a deployment guided by the MCP server?
    answer: >-
      Ask your harness to check the deployment status and run a representative inference test. Use
      input and success criteria that match the model task. A running process or successful network
      response doesn't prove that the model produces a correct result.
# END generated_summary_faq

author: Pinru Wang

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
    # - Cortex-A
tools_software_languages:
    - MCP
    - Arm AI Portal
    - Arm Topo
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: Arm AI Portal
        link: https://developer.arm.com/ai
        type: website
    - resource:
        title: Model Context Protocol documentation
        link: https://modelcontextprotocol.io/docs/getting-started/intro
        type: documentation
    - resource:
        title: Arm Topo GitHub repository
        link: https://github.com/arm/topo
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
