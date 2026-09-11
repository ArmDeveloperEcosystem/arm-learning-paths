---
title: Understand AI-driven profiling with the Arm Performix MCP server
description: Understand how the Arm Performix MCP server enables an AI agent to run Code Hotspots profiling and propose evidence-based optimizations.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why profile with Arm Performix using AI

The Arm Performix MCP server exposes Performix tools that AI coding assistants can invoke directly. Rather than switching between your IDE and the Performix GUI to analyze results and then back again to apply code changes, an AI agent can orchestrate the entire profiling pipeline. Configuring the recipe, launching the collection run, retrieving hotspot data, and proposing optimizations can all be part of a single agentic workflow.

## What the Arm Performix MCP server is

Arm Performix is a performance profiling tool that simplifies the workflow of collecting CPU samples, building flame graphs, and identifying the functions that dominate application runtime.

Arm Performix includes a local Model Context Protocol (MCP) server. The installed `apx` executable starts the server with the `mcp start` arguments and gives a compatible AI assistant access to Performix targets, recipes, runs, and AI insights.

You don't need to context switch between your IDE and the Performix GUI to analyze results and then back again to apply code changes. An AI agent can do all of this for you in a single agentic workflow.

## How the MCP workflow works

The agent uses separate Performix tools for collection and analysis:

- `list_recipes` identifies the recipes available in the installed Performix version.
- `list_targets` identifies targets that are already configured in Performix.
- `recipe_info` checks the selected recipe's parameters and support for a target.
- `run_recipe` runs Code Hotspots against a selected target and returns a run ID and status.
- `generate_ai_insights` prepares measured evidence and recipe guidance for a successful run.

The agent uses this data to cross-reference hotspot function names against the source files in your workspace, reason about why those functions are expensive, and propose specific code changes. Because the AI can see both the profiling output and the source code simultaneously, it avoids the guesswork that's common in manual profiling workflows.

You'll use the Arm Performix MCP server in the following sections to automate the Code Hotspots recipe on a C++ application running on an Arm Neoverse target and identify and fix the most CPU-intensive functions. The agent will drive three successive optimization passes — each validated by a re-profile before moving to the next — to achieve a measured ~12x runtime improvement.

## How to interact with the Arm Performix MCP server for profiling

The Arm Performix MCP server supports direct chat, prompt files, and agentic workflows. For profiling tasks, prompt files are the recommended approach. Profiling workflows typically involve multiple sequential steps — building the application, running a recipe, reading results, editing code, and repeating. Encoding this sequence in a prompt file makes it repeatable, shareable, and easy to version-control alongside the application.

### Direct AI chat

You can ask your AI assistant direct questions and it'll invoke the Arm Performix MCP tools when appropriate. For example:

```text
Use the Arm Performix MCP server to list the configured targets.
```

Direct chat is useful for quick, exploratory checks. It works well when you already know the target and binary path and just want a fast hotspot summary before committing to deeper analysis.

### Prompt files

For repeatable workflows, a prompt file encodes the full profiling sequence as a structured instruction set. Include the target name, absolute workload command, confirmation requirement, and run ID rather than binding the prompt to internal MCP tool names. This keeps the prompt portable across compatible AI assistants and allows the agent to profile the application and then propose source edits based on what it finds.

### Agentic workflows

Tools such as GitHub Copilot Agent Mode, Claude Code, Kiro, and OpenAI Codex support autonomous multi-step execution. When you combine a prompt file with an agentic workflow, the profiling step is deterministic: the agent uses the Arm Performix MCP server to run the recipe on your target and receives a run ID, then generates AI insights for that run. The agent then reasons over those hotspots, locating the corresponding source code, forming a hypothesis about why each function is expensive, and proposing a targeted change — before rebuilding and running the recipe again to measure the delta.

Every decision in the loop is grounded in the hotspot data returned by the tool; the AI never guesses at performance characteristics.

## Set up the Arm Performix MCP server

Configure your AI coding assistant to start the installed `apx` executable with `mcp start`. The server name is `arm-performix`.

For a tested configuration and verification workflow, complete [Generate Arm Performix AI insights in Visual Studio Code with Codex](/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/) before continuing.

## What you've learned and what's next

You've now learned what the Arm Performix MCP server is and how it works. You've also learned why the server is useful and how you can interact with it.

Next, you'll build the Mandelbrot example application on your remote Arm server and confirm that Arm Performix can reach the target.
