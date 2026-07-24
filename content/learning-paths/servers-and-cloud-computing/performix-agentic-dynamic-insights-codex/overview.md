---
title: Overview

weight: 2

description: Learn how Codex uses the Arm Performix MCP server to turn profiling data into evidence-based performance recommendations.

layout: learningpathall
---
## Understand the AI-assisted profiling workflow

[Arm Performix](https://developer.arm.com/servers-and-cloud-computing/arm-performix) is a performance toolkit designed to help developers identify bottlenecks and validate improvements on Arm-based systems. It simplifies the process of turning low-level performance data into actionable insights through guided analysis paths called recipes. These recipes help you answer common performance questions and move quickly from observation to root cause.

Arm Performix includes a local Model Context Protocol (MCP) server. MCP is a standard way for an AI assistant to discover and call tools. The server lets Codex query Performix recipes, targets, and runs from Visual Studio Code instead of relying on source-code analysis alone.

You will connect the server to Codex, select or create a Code Hotspots run, and ask for an AI Insight. The response should connect each recommendation to evidence from the selected run.

The MCP server runs on the same host as Codex. It can make profile data, symbols, source excerpts, disassembly excerpts, and performance metrics available to the assistant. Confirm that this use complies with your organization's data-handling policy before you continue.

Use AI-generated responses to support performance investigation. Validate important findings by reviewing the relevant data in Arm Performix and by rerunning the workload after making changes.

## How it works

Arm Performix stores profiling runs, target information, and rendered analysis data. Its MCP server exposes select Performix capabilities as tools that an MCP-compatible assistant can call.

When you ask for insights, the flow is:

1. You ask an AI Assisant, in this case, Codex in VS Code for an Arm Performix insight.
2. Codex calls the Arm Performix MCP server.
3. Arm Performix gathers relevant run data and profile evidence.
4. Codex uses that evidence to identify likely bottlenecks, explain why they matter, and suggest the next investigation step.

The available evidence depends on how the run was collected. Debug symbols and source mappings improve function and source-line attribution, while a representative profiling duration improves sampling quality.

 Next, configure the local MCP server and verify that Codex can use its tools.
