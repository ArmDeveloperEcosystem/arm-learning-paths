---
title: About Arm Performix

weight: 2

layout: learningpathall
---
[Arm Performix](https://developer.arm.com/servers-and-cloud-computing/arm-performix) is a performance toolkit designed to help developers identify bottlenecks and validate improvements on Arm-based systems. It simplifies the process of turning low-level performance data into actionable insights through guided analysis paths that help you answer common performance questions and move quickly from observation to root cause.

Working with Arm Performix is designed to be quick and straightforward. The intuitive GUI guides you through the setup process, from connecting to a target system to running your first analysis. In most cases, you can go from installation to your first useful results in just a few minutes. Simply connect to your target, select a recipe and run your workload. Performix handles data collection and analysis automatically, presenting results as visualizations and guided explanations. Here's a video describing how to [get started with Arm Performix](https://youtu.be/_eX8ZpNT0kc?si=WrQg5daHxUc0MFbR).

## Why Arm Performix is different 
If you’re familiar with tools such as perf, you will recognize the value of hardware performance counters, but also the cost of interpreting them.

Performix differs in the following ways:

- Guided analysis: Performix applies Arm’s standardized performance methodologies and presents results with context and suggested next steps.
- Function attribution: Performance metrics are attributed directly to functions and call paths, making results immediately actionable.
- Low-overhead sampling: Performix is designed to preserve realistic workload behavior, allowing analysis on representative runs.
- [Agentic dynamic insights](https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/): Expose Performix results to your preferred AI coding assistant so you can query the data and discover ways to improve performance problems.
- Fast to get started: Go from setup to useful results in minutes, without stitching together multiple tools or workflows.

The result is a faster path to understanding performance, especially if you are not a performance expert.

## Integrate Arm Performix into developer workflows

Performix is designed to fit into modern development environments. It can be driven entirely from the command-line and results can be exported in machine-readable formats. Results can then be compared across runs, making it easier to detect regressions and track performance changes over time. This makes Performix suitable not only for interactive analysis, but also for CI/CD pipelines where performance regressions need to be detected early. 

Performix can also be integrated into AI-assisted workflows using the [Arm MCP Server](https://developer.arm.com/servers-and-cloud-computing/arm-mcp-server), which implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) to expose system and performance tooling through a structured interface. This allows AI assistants such as GitHub Copilot or Codex to invoke Performix analysis workflows, query profiling data, and retrieve insights programmatically. For example, you can request hotspot analysis, inspect Topdown metrics, or explore instruction mix results directly from your editor. By exposing performance data through MCP, Performix integrates code, tooling, and analysis, enabling more iterative and automated optimization without manual navigation of profiling tools. Here is a learning path that walks you through [how to generate Performix insights in VS Code with Codex](https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/)
