---
title: Connect your AI harness to the Arm AI Portal MCP server
description: Configure Codex, Claude Code, or GitHub Copilot to connect to the Arm AI Portal MCP server over Streamable HTTP and verify that its tools are available.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose an AI harness

The Arm AI Portal Model Context Protocol (MCP) server gives an AI harness access to AI Portal models, documentation, and deployment guidance. The server uses Streamable HTTP, so you can connect your harness to a URL instead of installing the server locally.

Run one of the following CLI commands to add the MCP server to your chosen AI harness:

{{< tabpane code=true >}}
  {{< tab header="Codex" language="bash" >}}
# Run this command in your terminal
codex mcp add arm-ai --url https://mcp.api.devplatform.arm.com/ai-portal
  {{< /tab >}}
  {{< tab header="Claude Code" language="bash" >}}
# Run this command in your terminal
claude mcp add --transport http arm-ai https://mcp.api.devplatform.arm.com/ai-portal
  {{< /tab >}}
  {{< tab header="GitHub Copilot" language="bash" >}}
# Run this command in your terminal
copilot mcp add --transport http arm-ai https://mcp.api.devplatform.arm.com/ai-portal
  {{< /tab >}}
  {{< tab header="Other client" language="bash" >}}
# Add the MCP URL to your client, and set `Transport: Streamable HTTP`
https://mcp.api.devplatform.arm.com/ai-portal
  {{< /tab >}}
{{< /tabpane >}}

For desktop applications, open the settings and add the MCP server using the MCP URL.

## Verify the connection

Run the following command to confirm that the MCP server appears in your harness's MCP server list:

{{< tabpane code=true >}}
  {{< tab header="Codex" language="bash" >}}
codex mcp list
  {{< /tab >}}
  {{< tab header="Claude Code" language="bash" >}}
claude mcp list
  {{< /tab >}}
  {{< tab header="GitHub Copilot" language="bash" >}}
copilot mcp list
  {{< /tab >}}
{{< /tabpane >}}

For other command-line clients, use the equivalent command to list configured MCP servers. For desktop applications, check the MCP server settings.

You should see `arm-ai` listed as a connected MCP server. If it doesn't appear, verify the URL and confirm that your machine can access the development network.

Open a new session in your AI harness and ask it to use the Arm AI Portal MCP server:

```text
Use the Arm AI Portal MCP server to list the types of AI models available in the catalogue.
```

The harness should select the AI Portal `find_model` tool and summarize the returned model task types. 

Some harnesses might sometimes use web searches rather than the configured MCP. If that happens, make your prompt more specific:

```text
Use the arm-ai MCP tools, not web search, to answer this question.
```
The output is similar to:

```output
• The Arm AI Portal catalogue currently contains 74 models across 11 task types:

  - Image classification — 23
  - Text generation — 16
  - Object detection — 10
  - Image segmentation — 6
  - Automatic speech recognition — 5
  - Image-to-image — 4
  - Text-to-speech — 4
  - Feature extraction / embeddings — 3
  - Image-to-text / OCR — 1
  - Text-to-image — 1
  - Zero-shot image classification — 1

  These are the catalogue’s current task classifications, queried through the Arm AI Portal MCP server.
```
## What you've accomplished and what's next

You've connected an AI harness of your choice to the Arm AI Portal MCP server and confirmed that it can search its catalog. 

Next, you'll use prompts with different levels of detail to search models, compare results, and find documentation.
