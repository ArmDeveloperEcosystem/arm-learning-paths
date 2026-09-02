---
title: Understand AI-driven profiling with the Arm Performix MCP server
description: Understand how the dedicated Arm Performix MCP server enables an AI agent to run Code Hotspots and propose evidence-based optimizations.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why profile with Arm Performix using AI

The dedicated Arm Performix MCP server lets AI coding assistants invoke Performix tools directly. An agent can select a configured target, run a recipe, retrieve measured evidence, and propose optimizations as part of one workflow.

## What the Arm Performix MCP server is

Arm Performix is a performance profiling tool that collects CPU samples, builds flame graphs, and identifies the functions that dominate application runtime.

Arm Performix includes a local Model Context Protocol (MCP) server. The installed `apx` executable starts the server with the `mcp start` arguments and gives a compatible AI assistant access to Performix targets, recipes, runs, queries, and AI insights.

You can still open a run in the Performix GUI to inspect its flame graph and source attribution. The MCP workflow complements that interface by keeping the run evidence alongside your source code and agent conversation.

## How the MCP workflow works

The agent uses separate Performix tools for collection and analysis:

- `list_targets` identifies targets that are already configured in Performix
- `run_recipe` runs Code Hotspots against a selected target and returns a run ID and status
- `generate_ai_insights` prepares measured evidence and recipe guidance for a successful run
- `run_query` supports focused queries when deeper analysis needs raw rendered data

Keeping collection and analysis separate lets you confirm the target and workload before remote execution. It also ties every analysis request to a stable run ID.

The agent can cross-reference hotspot functions against source files in its workspace, explain what the profile establishes, and propose focused changes. You should still distinguish measured observations from hypotheses and validate each change with a new run and elapsed-time measurement.

## Interact with the Arm Performix MCP server

### Direct AI chat

Ask your AI assistant to name the server and task explicitly. For example:

```text
Use the Arm Performix MCP server to list the configured targets.
```

After you select a target, provide the absolute workload command and require confirmation before collection. When the run completes, use its run ID in a separate request for AI insights.

### Repeatable prompts

Store your collection and analysis prompts with the project when you want a repeatable workflow. Include the target name, absolute workload command, confirmation requirement, and run ID rather than binding the prompt to internal MCP tool names. This keeps the prompt portable across compatible AI assistants.

### Agentic workflows

An agentic workflow can combine Performix evidence with source inspection and code editing when the assistant has access to the relevant development environment. The Performix MCP server runs and analyzes recipes; it doesn't by itself provide remote source-editing or deployment tools.

Review proposed changes and command approvals before the agent acts. Apply one performance-relevant change at a time, rebuild the workload, and profile it again with the same target and settings.

## Set up the Arm Performix MCP server

Configure your AI coding assistant to start the installed `apx` executable with `mcp start`. The server name is `arm-performix`.

For a tested configuration and verification workflow, complete [Generate Arm Performix AI insights in Visual Studio Code with Codex](/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/) before continuing.

## What you've learned and what's next

You've learned how the dedicated Arm Performix MCP server separates collection from evidence-based analysis.

Next, you'll build the Mandelbrot example application on your remote Arm server and confirm that Arm Performix can reach the target.
