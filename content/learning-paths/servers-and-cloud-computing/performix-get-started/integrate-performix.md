---
title: Integrate Arm Performix into your workflow

weight: 20

layout: learningpathall
---

{{% notice Note %}}
Editorial review needed: Decide whether to keep, shorten, or remove this page.
{{% /notice %}}

## How Performix compares to other tools

If you're familiar with tools such as Perf, you recognize the value of hardware performance counters, but also the cost of interpreting them. Performix differs in the following ways:

- **Guided analysis:** applies Arm's standardized performance methodologies and presents results with context and suggested next steps
- **Function attribution:** attributes performance metrics directly to functions and call paths, making results immediately actionable
- **Low-overhead sampling:** preserves realistic application behavior, allowing analysis on representative runs
- **[Agentic dynamic insights](https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/):** exposes results to your preferred AI coding assistant so you can query data and discover ways to improve performance

## CI/CD and AI-assisted workflows

Performix can be driven entirely from the command line and results can be exported in machine-readable formats. Results can be compared across runs, making it easier to detect regressions and track performance changes over time. This makes Performix suitable for CI/CD pipelines where performance regressions need to be detected early.

Performix can also be integrated into AI-assisted workflows using the [Arm MCP Server](https://developer.arm.com/servers-and-cloud-computing/arm-mcp-server), which implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) to expose system and performance tooling through a structured interface. This allows AI assistants such as GitHub Copilot or Codex to invoke Performix analysis workflows, query profiling data, and retrieve insights programmatically.

For a walkthrough of the Performix GUI and setup process, see this video on [getting started with Arm Performix](https://youtu.be/_eX8ZpNT0kc?si=WrQg5daHxUc0MFbR).
