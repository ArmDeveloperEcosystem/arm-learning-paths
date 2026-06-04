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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:43:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 80785022032bf4e3c65da682e698940a212ee1ee77386698889a9fafbed9f823
  summary_generated_at: '2026-06-02T03:37:07Z'
  summary_source_hash: 80785022032bf4e3c65da682e698940a212ee1ee77386698889a9fafbed9f823
  faq_generated_at: '2026-06-03T00:43:28Z'
  faq_source_hash: 80785022032bf4e3c65da682e698940a212ee1ee77386698889a9fafbed9f823
  summary: >-
    This advanced path shows how to use the Docker MCP Toolkit with the Arm MCP Server and GitHub
    Copilot in VS Code to automate migration of a containerized C++ app from x86 AVX2 intrinsics
    to Arm64 Neon. You will enable the MCP Toolkit in Docker Desktop, connect the MCP Gateway
    to VS Code, and configure the Arm, GitHub, and Sequential Thinking MCP servers. Using a provided
    demo repository, you will scan for x86-specific code, generate Neon equivalents, create a
    pull request, and review changes. Finally, you will build for linux/arm64 with docker buildx
    and run the benchmark to validate output on Arm64. Prerequisites include Docker Desktop 4.59+,
    VS Code with GitHub Copilot, a GitHub PAT, and basic Docker/C++ and SIMD knowledge. Estimated
    time: 45 minutes on Linux or macOS.
  faqs:
  - question: What do I need before starting the migration steps?
    answer: >-
      You need Docker Desktop 4.59 or later with MCP Toolkit enabled, VS Code with the GitHub
      Copilot extension, a GitHub account with a Personal Access Token that allows repository
      access, a machine with at least 8 GB RAM (16 GB recommended), and basic familiarity with
      Docker, C++, and SIMD intrinsics concepts.
  - question: Which MCP servers should I configure, and how do I make them available to Copilot
      in VS Code?
    answer: >-
      Configure the Arm MCP Server, GitHub MCP Server, and Sequential Thinking MCP Server in the
      Docker MCP Toolkit. In VS Code, ensure the MCP_DOCKER server is running (Extensions > MCP_DOCKER
      > Start Server) so GitHub Copilot can invoke these servers through the MCP Gateway.
  - question: Where do I get the demo application and open it in VS Code?
    answer: >-
      Clone the repository with: git clone https://github.com/JoeStech/docker-blog-arm-migration
      and cd into docker-blog-arm-migration. Open it in VS Code with: code .
  - question: How do I direct GitHub Copilot to perform the x86-to-Arm64 migration?
    answer: >-
      Open GitHub Copilot Chat in VS Code and paste the provided prompt that instructs it to use
      the Arm MCP Server tools for migration. Copilot will scan for x86-specific dependencies
      and intrinsics, automate AVX2-to-Neon conversions using the Arm MCP Server knowledge base,
      and propose changes via a pull request using the GitHub MCP Server.
  - question: What result should I expect after building and running the Arm64 container?
    answer: >-
      After building with docker buildx for --platform linux/arm64 and running the container,
      the benchmark output should indicate it’s running on Arm64 with NEON optimizations and display
      matrix multiplication timings and a result sum. This confirms the migrated code executes
      on Arm64 as intended.
# END generated_summary_faq

author: Ajeet Singh Raina

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

