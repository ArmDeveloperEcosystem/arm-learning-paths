---
title: Understand the AI-assisted Arm Performix insight workflow

weight: 2

description: Learn how Codex uses the Arm Performix MCP server to turn profiling data into evidence-based performance recommendations.

layout: learningpathall
---
## Arm Performix local MCP server

[Arm Performix](https://developer.arm.com/servers-and-cloud-computing/arm-performix) is a performance toolkit designed to help developers identify bottlenecks and validate improvements on Arm-based systems. The toolkit turns low-level performance data into actionable insights through guided analysis paths called recipes. You can use these recipes to answer common performance questions and move quickly from observation to root cause.

Arm Performix includes a local Model Context Protocol (MCP) server. MCP is a standard way for an AI assistant to discover and call tools. The server lets Codex query Performix recipes, targets, and runs from Visual Studio Code instead of relying on source-code analysis alone.

You'll connect the server to Codex, select or create a Code Hotspots run, and ask for an AI insight. The response should connect each recommendation to evidence from the selected run.

{{% notice Important %}}
The MCP server runs on the same host as Codex. It can make profile data, symbols, source excerpts, disassembly excerpts, and performance metrics available to the assistant. Before you continue, confirm that this use complies with your organization's data-handling policy.
{{% /notice %}}

Use AI-generated responses to support performance investigation. Validate important findings by reviewing the relevant data in Arm Performix and by rerunning the workload after making changes.

## How AI-assisted Arm Performix insights are generated

Arm Performix stores profiling runs, target information, and rendered analysis data. The local MCP server exposes specific Performix capabilities as tools that an MCP-compatible assistant can call.

When you ask for insights, the flow is:

1. You ask an AI assistant — in this case, Codex in VS Code — for an Arm Performix insight.
2. Codex calls the Arm Performix MCP server.
3. Arm Performix gathers relevant run data and profile evidence.
4. Codex uses that evidence to identify likely bottlenecks, explain why they matter, and suggest the next investigation step.

The available evidence depends on how the run was collected. Debug symbols and source mappings improve function and source-line attribution, while a representative profiling duration improves sampling quality.

## What you've learned and what's next

You've learned about Arm Performix's local MCP server and how AI-assisted insights are generated. 

Next, you'll configure the local MCP server and verify that Codex can use its tools.
