
---
title: Explore the Arm Model Context Protocol
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you learn what the Arm Model Context Protocol (MCP) is and how it extends Gemini CLI with Arm-specific tools and knowledge.

{{% notice Note %}}
This page focuses on concepts only. You do not configure or run MCP yet.
{{% /notice %}}

## What is the Model Context Protocol (MCP)?

The Model Context Protocol allows Gemini CLI to interact with external tools that provide structured data, documentation, and analysis capabilities.

Instead of relying only on a language model, Gemini CLI can call MCP tools to retrieve authoritative information or perform targeted analysis.

{{% notice Tip %}}
You can think of MCP as a bridge between Gemini CLI and external, authoritative tools. Instead of relying solely on generated responses, Gemini CLI can use MCP to query structured sources and tools that are specifically designed for Arm development.
{{% /notice %}}

## Why use MCP for Arm development?

When MCP is enabled, Gemini CLI can:
- Reference Arm-specific documentation and guidance more reliably
- Provide architecture-aware reasoning instead of generic advice
- Use specialized tools to support migration and optimization discussions

MCP is most useful when you want deeper, architecture-aware assistance beyond general development advice.

## When MCP is not required

You do not need MCP for:
- General programming questions
- Language syntax help
- Non-architecture-specific tasks

MCP does not replace compilers, profilers, or benchmarking tools. It augments Gemini CLI by providing better context and tooling for reasoning about Arm-specific development challenges.

In the next section, you configure Gemini CLI to use the Arm MCP server.
