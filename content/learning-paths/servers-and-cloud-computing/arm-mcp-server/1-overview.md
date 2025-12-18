---
title: Arm MCP Server Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is the Arm MCP Server?

The Arm MCP Server is a tool that enables AI-powered developer tools to become Arm cloud migration and optimization experts. It implements the Model Context Protocol (MCP), an open standard that allows AI assistants to access external tools and data sources.

By connecting your AI coding assistant to the Arm MCP Server, you gain access to Arm-specific knowledge, container image inspection tools, and code analysis capabilities that streamline the process of migrating applications from x86 to Arm.

## How to interact with the Arm MCP Server

There are multiple ways to interact with the Arm MCP Server, depending on your development environment and workflow:

### 1. Direct AI Chat

You can ask your AI assistant natural language questions, and it will automatically use the MCP tools when appropriate. For example:

```text
Check if the nginx:latest Docker image supports Arm architecture
```

### 2. Prompt Files

Many AI coding tools support prompt files that provide structured instructions. These files can reference MCP tools and guide the AI through complex workflows like full codebase migrations.

### 3. Agentic Workflows

Tools like GitHub Copilot Agent Mode, Claude Code, Kiro, and OpenAI Codex support autonomous agent workflows where the AI can execute multi-step migration tasks with minimal intervention. These fully agentic workflows can be combined with prompt files and direct chat to create an extremely powerful development system.

## Available Arm MCP Server Tools

The Arm MCP Server provides several specialized tools for migration and optimization:

### knowledge_base_search

Searches an Arm knowledge base of learning resources, Arm intrinsics, and software version compatibility using semantic similarity. Given a natural language query, it returns matching resources with URLs, titles, and content snippets ranked by relevance.

**Use case:** Finding documentation, tutorials, or version compatibility information for Arm migration.

### check_image

Checks Docker image architectures. Provide an image in `name:tag` format and get a report of supported architectures.

**Use case:** Quickly verify if a container base image supports `arm64` before starting a migration.

### skopeo

A container image architecture inspector that inspects container images remotely without downloading them to check architecture support (especially ARM64 compatibility).

**Use case:** Detailed inspection of container manifests and multi-architecture support before migrating workloads to Arm-based infrastructure.

### migrate_ease_scan

Runs a migrate-ease scan against a workspace or remote Git repository. Supported scanners include: cpp, python, go, js, and java. Returns analysis results identifying x86-specific code that needs attention.

**Use case:** Automated scanning of codebases to identify architecture-specific dependencies, build flags, intrinsics, and libraries that need to be changed for Arm.

### mca (Machine Code Analyzer)

An assembly code performance analyzer that predicts performance on different CPU architectures and identifies bottlenecks. It estimates Instructions Per Cycle (IPC), execution time, and resource usage.

**Use case:** Analyzing and optimizing performance-critical assembly code when migrating between processor types.

### sysreport_instructions

Provides instructions for installing and using sysreport, a tool that obtains system information related to system architecture, CPU, memory, and other hardware details.

**Use case:** Understanding the target Arm system's capabilities before deployment.

## Setting up the Arm MCP Server

To use the Arm MCP Server with an AI coding assistant, you must configure the assistant to connect to the MCP server. This connection allows the assistant to query Arm-specific tools, documentation, and capabilities exposed through the Model Context Protocol (MCP).
The required configuration steps vary by AI coding assistant. Refer to the installation guides below for step-by-step instructions on connecting the following AI coding assistants to the Arm MCP server:

  [GitHub Copilot](/install-guides/github-copilot/)
  [Gemini CLI](/install-guides/gemini/)
  [Kiro CLI](/install-guides/kiro-cli/)

Continue to the next section to see the Arm MCP Server in action.
