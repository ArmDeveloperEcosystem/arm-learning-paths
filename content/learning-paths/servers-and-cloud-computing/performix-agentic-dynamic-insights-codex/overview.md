---
title: Overview

weight: 2

layout: learningpathall
---
[Arm Performix](https://developer.arm.com/servers-and-cloud-computing/arm-performix) is a performance toolkit designed to help developers identify bottlenecks and validate improvements on Arm-based systems. It simplifies the process of turning low-level performance data into actionable insights through guided analysis paths called recipes. These recipes help you answer common performance questions and move quickly from observation to root cause.

Arm Performix can expose performance-analysis capabilities to an AI coding assistant through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). This lets you ask focused performance questions from your development environment while using Arm Performix profile data as the evidence behind the answer.

This tutorial shows how to configure the Arm Performix MCP server with the Codex extension in Visual Studio Code, then generate AI Insights for an existing Arm Performix profiling run.

Use AI-generated responses to support performance investigation. Validate important findings by reviewing the relevant data in Arm Performix and by rerunning the workload after making changes.

## How it works

Arm Performix stores profiling runs, target information and rendered analysis data. The Arm Performix MCP server exposes selected Arm Performix capabilities as tools that an MCP-compatible assistant can call.

When you ask for insights, the flow is:

1. You ask an AI assistant in VS Code for Arm Performix insights.
2. The assistant calls the Arm Performix MCP server. 
3. Arm Performix gathers relevant run data and profile evidence.
4. The assistant uses that evidence to identify likely bottlenecks, explain why they matter, and suggest next steps.
The assistant does not need to infer everything from source code alone. It can use Arm Performix data as context, including information about runs, functions, call paths, source code, disassembly, or performance metrics, depending on what is available for the selected run.

