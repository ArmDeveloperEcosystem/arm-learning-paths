---
title: Understand AI-driven profiling with Arm Performix MCP
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why AI-driven profiling with Arm Performix

The Arm MCP Server exposes Arm Performix as a first-class tool that AI coding assistants can invoke directly. Rather than switching between your IDE and the Performix GUI to analyze results and then back again to apply code changes, an AI agent can orchestrate the entire profiling pipeline — configuring the recipe, launching the collection run, retrieving hotspot data, and proposing optimizations — all in a single agentic workflow.

## What is the Arm Performix tool in the MCP Server?

Arm Performix is a performance profiling tool that simplifies the workflow of collecting CPU samples, building flame graphs, and identifying the functions that dominate application runtime. When integrated into the MCP server, it lets an AI agent orchestrate the entire profiling pipeline — configuring the recipe, launching the collection run, and retrieving the resulting hotspot data — without manual interaction with the Performix engine.

Context switching for profiling is removed. Rather than switching between your IDE and the Performix GUI to analyze results and then back again to apply code changes, an AI agent can do all of this for you in a single agentic workflow.

## How the MCP tool works

The `apx_recipe_run` tool in the Arm MCP Server accepts a recipe name, a binary path on the remote target, and SSH connection details. It starts the Performix collection run on the configured remote target, waits for the application to finish, and then returns a structured summary of the profiling results. The summary includes the top CPU-time-consuming functions ordered by sample percentage, call stack context for each hotspot, and any relevant observations about the application's runtime behavior.

The agent uses this data to cross-reference hotspot function names against the source files in your workspace, reason about why those functions are expensive, and propose specific code changes. Because the AI can see both the profiling output and the source code simultaneously, it avoids the guesswork that is common in manual profiling workflows.

**Use case:** Automating the Code Hotspots recipe on a C++ application running on an Arm Neoverse target to identify and fix the most CPU-intensive functions. In this Learning Path, the agent drives three successive optimization passes — each validated by a re-profile before moving to the next — to achieve a measured ~12x runtime improvement.

## How to interact with the Arm MCP Server for profiling

The Arm MCP Server supports the same interaction styles as the rest of its tool suite: direct chat, prompt files, and agentic workflows. For profiling tasks, prompt files are the recommended approach. Profiling workflows typically involve multiple sequential steps — building the application, running a recipe, reading results, editing code, and repeating. Encoding this sequence in a prompt file makes it repeatable, shareable, and easy to version-control alongside the application.

### Direct AI chat

You can ask your AI assistant direct questions and it will invoke the `apx_recipe_run` tool when appropriate. For example:

```text
Run the Code Hotspots recipe on /home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread_debug and tell me which functions are the hottest
```

This is useful for quick, exploratory checks. It works well when you already know the binary path and just want a fast hotspot summary before committing to deeper analysis.

### Prompt files

For repeatable workflows, a prompt file encodes the full profiling sequence as a structured instruction set. Prompt files reference the `arm-mcp/apx_recipe_run` tool alongside other tools such as `edit/editFiles`, which allows the agent to profile the application and then immediately propose source edits based on what it finds. You'll create a prompt file in the next sections to run the Code Hotspots recipe on the Mandelbrot example.

### Agentic workflows

Tools like GitHub Copilot Agent Mode, Claude Code, Kiro, and OpenAI Codex support autonomous multi-step execution. When you combine a prompt file with an agentic workflow, the profiling step is deterministic: the agent calls `arm-mcp/apx_recipe_run` through the Arm MCP Server, which runs the Performix recipe on your target and returns the identified hotspots as structured, reproducible data. The agent then reasons over those hotspots, locating the corresponding source code, forming a hypothesis about why each function is expensive, and proposing a targeted change — before rebuilding and calling `arm-mcp/apx_recipe_run` again to measure the delta. Every decision in the loop is grounded in the hotspot data returned by the tool; the AI never guesses at performance characteristics.

## Setting up the Arm MCP Server

To use the Arm MCP Server with an AI coding assistant, you need to configure the assistant to connect to the MCP server. Connecting your assistant allows it to query Arm-specific tools, documentation, and capabilities exposed through the Model Context Protocol (MCP).

The required configuration steps vary by AI coding assistant. Refer to the installation guides below for step-by-step instructions on connecting the following AI coding assistants to the Arm MCP server:

- [GitHub Copilot](/install-guides/github-copilot/)
- [Gemini CLI](/install-guides/gemini/)
- [Kiro CLI](/install-guides/kiro-cli/)
- [Codex CLI](/install-guides/codex-cli/)
- [Claude Code](/install-guides/claude-code)

In the next section, you'll build the Mandelbrot example application on your remote Arm server and confirm that Arm Performix can reach the target.
