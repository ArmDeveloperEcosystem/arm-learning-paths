---
title: Set up Docker MCP Toolkit with Arm, GitHub, and Sequential Thinking servers
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

You need:

- Docker Desktop 4.59 or later.
- VS Code with the GitHub Copilot extension.
- A GitHub account with a personal access token.
- A machine with at least 8 GB RAM (16 GB recommended).

## Enable the Docker MCP Toolkit

1. Open Docker Desktop.
2. Go to **Settings** > **Beta features**.
3. Toggle **Enable Docker MCP Toolkit** on.
4. Click **Apply**.

After a few seconds, the **MCP Toolkit** tab appears in the left sidebar.

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

1. Select the GitHub Official server.
2. Choose **Personal Access Token** as the authentication method.
3. Enter your GitHub token from **GitHub Settings** > **Developer Settings** > **Personal access tokens**.

This server lets GitHub Copilot create pull requests, manage issues, and commit changes directly to your repositories.

### Sequential Thinking MCP Server

Search for **Sequential Thinking** in the catalog and add the [Sequential Thinking MCP Server](https://hub.docker.com/mcp/server/sequentialthinking/overview).

No configuration is needed. This server helps GitHub Copilot break down complex migration decisions into logical steps.

## Connect VS Code to the MCP Gateway

1. In Docker Desktop, go to **MCP Toolkit** > **Clients** tab.
2. Scroll to **Visual Studio Code** and click **Connect**.
3. Open VS Code and click the **Extensions** icon in the left toolbar.
4. Find **MCP_DOCKER**, click the gear icon, and click **Start Server**.

## Verify the connection

Open GitHub Copilot Chat in VS Code and ask:

```text
What Arm migration tools do you have access to?
```

You should see tools from all three servers listed. If they appear, your setup is complete.

In the next section, you will examine the demo application to understand what blocks its migration to Arm64.
