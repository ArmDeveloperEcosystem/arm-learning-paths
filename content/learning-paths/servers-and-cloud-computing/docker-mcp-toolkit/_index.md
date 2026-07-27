---
title: Automate x86 to Arm Migration with Docker MCP Toolkit, VS Code and GitHub Copilot

description: Learn how to use the Docker MCP Toolkit with the Arm MCP Server and GitHub Copilot to automate container and code migration from x86 to Arm64. Through a hands-on example, migrate a legacy C++ application with AVX2 intrinsics to Arm Neon.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers and DevOps engineers who want to automate the migration of containerized applications from x86 to Arm64 using AI-powered tools in the Docker MCP Toolkit.

learning_objectives:
  - Describe how the Model Context Protocol (MCP) enables AI coding assistants to invoke structured migration tools through the Arm MCP server
  - Explain how the Docker MCP Toolkit connects AI coding assistants to Arm MCP server
  - Install and configure the Docker MCP Toolkit with the Arm MCP Server, GitHub MCP Server, and Sequential Thinking MCP Server
  - Connect the MCP Gateway to VS Code with GitHub Copilot
  - Use AI agents to scan codebases for x86-specific dependencies and intrinsics
  - Automate the conversion of x86 AVX2 intrinsics to Arm Neon equivalents using the Arm MCP Server knowledge base
  - Create and manage pull requests with migrated code using the GitHub MCP Server

prerequisites:
    - Docker Desktop 4.59 or later with MCP Toolkit enabled
    - VS Code with the GitHub Copilot extension
    - A GitHub account with a personal access token
    - A machine with at least 8 GB RAM (16 GB recommended)
    - Basic familiarity with Docker, C++, and SIMD intrinsics concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:52:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 80785022032bf4e3c65da682e698940a212ee1ee77386698889a9fafbed9f823
  summary_generated_at: '2026-07-27T18:52:34Z'
  summary_source_hash: 80785022032bf4e3c65da682e698940a212ee1ee77386698889a9fafbed9f823
  faq_generated_at: '2026-07-27T18:52:34Z'
  faq_source_hash: 80785022032bf4e3c65da682e698940a212ee1ee77386698889a9fafbed9f823
  summary: >-
    You'll use Docker MCP Toolkit, the Arm MCP Server, and GitHub Copilot in VS Code to migrate an
    x86-optimized C++ container to Arm64. You'll configure the MCP servers and Gateway, use a provided
    prompt to find x86-specific code and propose Arm Neon conversions, update the Dockerfile, and
    build the container with `docker buildx`. Finally, you'll run the container and verify Arm64
    execution with NEON.
  faqs:
  - question: How do I know the MCP_DOCKER server is running and connected to Copilot?
    answer: >-
      In VS Code, select **Extensions**, then **MCP_DOCKER** and **Start Server**.
      When it is running, GitHub Copilot can invoke the configured MCP servers through the MCP
      Gateway.
  - question: Which repository do I clone, and where should I run the commands?
    answer: >-
      Clone `https://github.com/JoeStech/docker-blog-arm-migration` and change into that directory.
      Open it in VS Code and run the build and run commands from the repository root.
  - question: What should I change in the Dockerfile for Arm64 builds?
    answer: >-
      Update two areas for Arm compatibility, including adding Arm64 support in the base image.
      Follow the migration steps to apply the remaining `Dockerfile` adjustments identified
      during the review.
  - question: How do I trigger the migration with Copilot, and what should I expect it to do?
    answer: >-
      Open GitHub Copilot Chat in VS Code and paste the provided migration prompt. Copilot uses
      the Arm MCP Server tools to scan for x86-specific dependencies and AVX2 intrinsics, propose
      Neon equivalents, and can prepare a pull request via the GitHub MCP Server.
  - question: What result should I expect when I run the Arm64 container?
    answer: >-
      The benchmark output shows Arm64 execution with NEON optimizations and prints
      benchmark details. Look for lines such as the architecture notice, the matrix size, and
      a result sum to confirm a successful run.
# END generated_summary_faq

author: Ajeet Singh Raina

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - Docker
    - MCP
    - GitHub Copilot
    - C++
    - VS Code
operatingsystems:
    - Linux
    - macOS

further_reading:
    - resource:
        title: Docker MCP Toolkit Documentation
        link: https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/
        type: documentation
    - resource:
        title: Arm MCP Server on Docker Hub
        link: https://hub.docker.com/mcp/server/arm-mcp/overview
        type: website
    - resource:
        title: Docker MCP Gateway on GitHub
        link: https://github.com/docker/mcp-gateway
        type: website
    - resource:
        title: Introducing the Arm MCP Server
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/introducing-the-arm-mcp-server-simplifying-cloud-migration-with-ai
        type: blog
    - resource:
        title: Arm MCP Server Learning Path
        link: /learning-paths/servers-and-cloud-computing/arm-mcp-server/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
