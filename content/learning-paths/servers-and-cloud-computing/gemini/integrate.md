
---
title: Integrate the Arm MCP server with Gemini CLI
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you integrate the Arm Model Context Protocol (MCP) server with Gemini CLI.

This enables Gemini to access Arm-specific tools and documentation during interactive sessions.

## Prerequisites

Before continuing, ensure:
- Gemini CLI is installed and working
- Docker is installed and running on your system

## Pull the Arm MCP server image

Pull the latest Arm MCP server container image:

```console
docker pull armlimited/arm-mcp:latest
```

## Configure Gemini CLI to use MCP

Edit the Gemini CLI settings file:

```console
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

Add the following configuration:

```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-v", "/path/to/your/code:/workspace",
        "armlimited/arm-mcp:latest"
      ],
      "timeout": 60000
    }
  }
}
```

Replace `/path/to/your/code` with the path to your local source directory.

## Verify MCP integration

Start Gemini CLI:

```console
gemini
```

List available tools:

```text
/tools
```

If the Arm MCP server is configured correctly, Arm-related tools appear in the output.

Next, you use Gemini CLI with MCP to analyze Arm code and migration scenarios.
