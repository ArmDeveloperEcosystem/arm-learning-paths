---
title: Automate x86 to Arm Migration with Docker MCP Toolkit, VS Code and GitHub Copilot
    
description: Learn how to use the Docker MCP Toolkit with the Arm MCP Server and GitHub Copilot to automate container and code migration from x86 to Arm64. Through a hands-on example, migrate a legacy C++ application with AVX2 intrinsics to Arm NEON.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers and DevOps engineers who want to automate the migration of containerized applications from x86 to Arm64 using AI-powered tools in the Docker MCP Toolkit.

learning_objectives:
  - Describe how the Model Context Protocol (MCP) enables AI coding assistants to invoke structured migration tools through the Arm MCP server
  - Explain how the Docker MCP Toolkit connects AI coding assistants to Arm MCP server
  - Install and configure the Docker MCP Toolkit with the Arm MCP Server, GitHub MCP Server, and Sequential Thinking MCP Server
  - Connect the MCP Gateway to VS Code with GitHub Copilot
  - Use AI agents to scan codebases for x86-specific dependencies and intrinsics
  - Automate the conversion of x86 AVX2 intrinsics to Arm NEON equivalents using the Arm MCP Server knowledge base
  - Create and manage pull requests with migrated code using the GitHub MCP Server

prerequisites:
    - Docker Desktop 4.59 or later with MCP Toolkit enabled
    - VS Code with the GitHub Copilot extension
    - A GitHub account with a personal access token
    - A machine with at least 8 GB RAM (16 GB recommended)
    - Basic familiarity with Docker, C++, and SIMD intrinsics concepts
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
