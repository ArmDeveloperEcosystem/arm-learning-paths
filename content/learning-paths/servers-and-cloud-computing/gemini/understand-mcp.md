
---
title: Understand the Arm Model Context Protocol
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you learn what the Arm Model Context Protocol (MCP) is and how it extends Gemini CLI with Arm-specific tools and knowledge.

This page focuses on concepts only. You do not configure or run MCP yet.

## What is the Model Context Protocol (MCP)?

The Model Context Protocol allows Gemini CLI to interact with external tools that provide structured data, documentation, and analysis capabilities.

Instead of relying only on a language model, Gemini can call MCP tools to retrieve authoritative information or perform targeted analysis.

## Why use MCP for Arm development?

The Arm MCP server provides:
- Access to Arm-specific documentation
- Architecture-aware guidance
- Tools for reasoning about migration and optimization

MCP is most useful when you want deeper, architecture-aware assistance beyond general development advice.

## When MCP is not required

You do not need MCP for:
- General programming questions
- Language syntax help
- Non-architecture-specific tasks

In the next section, you configure Gemini CLI to use the Arm MCP server.
