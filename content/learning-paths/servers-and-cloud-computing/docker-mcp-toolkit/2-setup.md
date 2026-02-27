---
title: Set up Docker MCP Toolkit with Arm, GitHub, and Sequential Thinking servers
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

Make sure the following tools are installed:

- Docker Desktop 4.59 or later
- VS Code with the GitHub Copilot extension
- A GitHub account with a Personal Access Token (PAT) that allows repository access
- A machine with at least 8 GB RAM (16 GB recommended)

You'll use Docker Desktop to host MCP servers locally, and VS Code with GitHub Copilot to invoke those servers through the MCP Gateway.

## Enable the Docker MCP Toolkit

The MCP Toolkit allows Docker Desktop to run and manage MCP (Model Context Protocol) servers, which expose structured tools that AI assistants can call.

- Open Docker Desktop
- Go to **Settings** > **Beta features**
- Toggle **Enable Docker MCP Toolkit** on
- Select **Apply**

The **MCP Toolkit** tab appears in the left sidebar.

## Add the required MCP servers

Open the **MCP Toolkit** in Docker Desktop and select the **Catalog** tab. Add the following three servers:

### Arm MCP Server

Search for **Arm** in the catalog and add the [Arm MCP Server](https://hub.docker.com/mcp/server/arm-mcp/overview).

Configure it by setting the directory path to your local code. This allows the `migrate_ease_scan` and `mca` tools to access your source files. Click **Save** after setting the path.

The Arm MCP Server provides six tools:

| Tool | Description |
|------|-------------|
| `knowledge_base_search` | Semantic search of Arm learning resources, intrinsics documentation, and software compatibility |
| `migrate_ease_scan` | Code scanner for C++, Python, Go, JavaScript, and Java Arm compatibility analysis |
| `check_image` | Docker image architecture verification for Arm64 support |
| `skopeo` | Remote container image inspection without downloading |
| `mca` | Machine Code Analyzer for assembly performance and IPC predictions |
| `sysreport_instructions` | System architecture information gathering |

### GitHub Official MCP Server

Search for **GitHub Official** in the catalog and add the [GitHub MCP Server](https://hub.docker.com/mcp/server/github-official/overview).

Configure authentication:

- Select the GitHub Official server
- Choose **Personal Access Token** as the authentication method
- Enter your GitHub token from **GitHub Settings** > **Developer Settings** > **Personal access tokens**

This server lets GitHub Copilot create pull requests, manage issues, and commit changes directly to your repositories.

### Sequential Thinking MCP Server

Search for **Sequential Thinking** in the catalog and add the [Sequential Thinking MCP Server](https://hub.docker.com/mcp/server/sequentialthinking/overview).

No configuration is needed. This server helps GitHub Copilot break down complex migration decisions into logical steps.

## Connect VS Code to the MCP Gateway

- In Docker Desktop, go to **MCP Toolkit** > **Clients** tab
- Scroll to **Visual Studio Code** and select **Connect**
- Open VS Code and select the **Extensions** icon in the left toolbar
- Find **MCP_DOCKER**, select the gear icon, and select **Start Server**

## Verify the connection

Open GitHub Copilot Chat in VS Code and ask:

```text
What Arm migration tools do you have access to?
```

If the setup is correct, Copilot lists tools from:

- Arm MCP Server
- GitHub MCP Server
- Sequential Thinking MCP Server

This confirms that tool invocation through the MCP Gateway is working.

## What you've learned and what's next

You have:
- Enabled the Docker MCP Toolkit in Docker Desktop
- Configured three MCP servers: Arm MCP Server, GitHub MCP Server, and Sequential Thinking MCP Server
- Connected VS Code with GitHub Copilot to the MCP Gateway
- Verified that Copilot can access migration tools

Next, you'll examine the demo application to identify x86-specific code that needs adaptation for Arm64.