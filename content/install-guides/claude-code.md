---
title: Claude Code

draft: true

author: Pareena Verma
minutes_to_complete: 10
official_docs: https://code.claude.com/docs

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

Claude Code is an AI-powered command-line tool that helps you build features, debug code, and navigate codebases directly from your terminal. It provides autonomous coding assistance and integrates with your existing development workflow.

Claude Code works seamlessly on Arm-based systems, including Linux distributions running on Arm servers, macOS on Apple Silicon, and Windows on Arm devices.

## What should I do before installing Claude Code?

You need a Claude account to use Claude Code. A Claude.ai account is recommended, though you can also use a Claude Console account.

If you don't have a Claude account, visit [Claude.ai](https://claude.ai/) and sign up.

Claude Code is only available for paid Pro and Max accounts, if not using API credits. Visit [Claude pricing](https://www.anthropic.com/pricing) to review the options.

## How do I install Claude Code?

Claude Code is a terminal application that works on macOS, Linux, and Windows systems, including Arm-based platforms.

### Install on Linux (Arm)

The recommended installation method for Linux uses the installation script:

```bash { target="ubuntu:latest" }
curl -fsSL https://claude.ai/install.sh | bash
```

This script automatically detects your system architecture and installs the appropriate version for Arm64 systems.

Add Claude Code to your PATH:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
```

### Install on macOS (Apple Silicon)

On macOS, you can use the installation script:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Or install using Homebrew:

```bash
brew install --cask claude-code
```

### Install on Windows on Arm

On Windows systems, including Windows on Arm, run the following PowerShell command:

```console
irm https://claude.ai/install.ps1 | iex
```

For other options, please [see the Claude Code setup page](https://code.claude.com/docs/en/setup).

### Verify installation

Confirm Claude Code is installed by checking the version:

```console
claude --version
```

The output shows the installed version:

```output
2.1.7 (Claude Code)
```

## How do I authenticate Claude Code?

After installing Claude Code, you need to authenticate:

1. Navigate to a project directory:

```console
cd your-project
```

2. Start Claude Code:

```console
claude
```

3. Choose your configuration options from the wizard (dark mode, etc).
4. On first use, Claude Code prompts you to log in through your browser if you are using your Claude account. If you are on a remote machine, Claude Code will give you a link to paste into a local browser, which will then provide you with a code to paste into Claude Code.
5. Accept the acknowledgements in Claude Code and the application will be ready to use.

Claude Code automatically saves your authentication credentials for future sessions.

## How do I confirm Claude Code is working?

Test Claude Code by asking it to perform a simple task:

1. In your terminal, start Claude Code in a project directory:

```console
claude
```

2. Type a request, for example:

```console
> Create a Python function to calculate fibonacci numbers for my Arm machine
```

3. Claude Code analyzes your request, creates a plan, and generates the code
4. Review the proposed changes before accepting them

Claude Code shows you a preview of changes before applying them, giving you control over what gets modified in your codebase.

If Claude Code doesn't respond:
- Verify you're authenticated (run `claude` and check for authentication prompts)
- Check your internet connection
- Ensure your Claude account is active
- Try restarting Claude Code


## How do I use MCP Servers with Claude Code?

Model Context Protocol (MCP) Servers extend Claude Code's capabilities by providing specialized tools and knowledge bases. Claude Code can connect to MCP servers to access domain-specific expertise and functionality.

The Arm MCP Server provides AI assistants with tools and knowledge for Arm architecture development, migration, and optimization. This is particularly useful when working on Arm-based systems.

### What tools does the Arm MCP Server provide?

The Arm MCP Server includes several tools designed for Arm development:

- migrate-ease scan: Analyzes codebases for x86-specific code that needs updating for Arm compatibility
- skopeo: Inspects container images to check for ARM64 architecture support
- knowledge_base_search: Searches Arm documentation and learning resources
- mca (Machine Code Analyzer): Analyzes assembly code for performance on Arm architectures
- check_image: Verifies Docker image architecture compatibility

### How do I configure the Arm MCP Server with Claude Code?

You need Docker running on your system to use the Arm MCP Server. See the [Docker install guide](/install-guides/docker/) for instructions.

First, pull the Arm MCP Server image:

```console
docker pull armlimited/arm-mcp:latest
```

Configure the Arm MCP Server using the `claude mcp add` command. You can configure MCP servers at three different scopes:

- Local scope (default): Available only to you in the current project
- Project scope: Shared with everyone in the project via `.mcp.json` file
- User scope: Available to you across all projects

{{% notice Note %}}
Choose the appropriate scope based on your needs. Project scope is recommended for team collaboration, while user scope is useful for personal tools you use across multiple projects.
{{% /notice %}}

#### Configure for a specific project (local scope)

Navigate to your project directory and add the Arm MCP Server:

```console
cd your-project
claude mcp add --transport stdio arm-mcp -- docker run --rm -i --pull=always -v "$(pwd):/workspace" armlimited/arm-mcp:latest
```

This configuration is stored in `~/.claude.json` under your project's path and is only accessible when working in this directory.

#### Configure for all projects (user scope)

To make the Arm MCP Server available across all your projects:

```console
claude mcp add --scope user --transport stdio arm-mcp -- docker run --rm -i --pull=always -v "$(pwd):/workspace" armlimited/arm-mcp:latest
```

This configuration is stored in `~/.claude.json` and is accessible from any project directory.

#### Configure for team sharing (project scope)

To share the MCP server configuration with your team via version control:

```console
cd your-project
claude mcp add --scope project --transport stdio arm-mcp -- docker run --rm -i --pull=always -v "$(pwd):/workspace" armlimited/arm-mcp:latest
```

This creates a `.mcp.json` file in your project root that can be committed to version control.

### How do I analyze a local codebase with the Arm MCP Server?

The Arm MCP Server automatically mounts your current working directory to the `/workspace` folder inside the Docker container when you use the configuration commands shown above.

To analyze a different directory, modify the volume mount in the `docker run` command. For example, to analyze `/Users/username/myproject`:

```console
claude mcp add --transport stdio arm-mcp -- docker run --rm -i -v "/Users/username/myproject:/workspace" armlimited/arm-mcp:latest
```

### How do I verify the Arm MCP Server is working?

List configured MCP servers:

```console
claude mcp list
```

You should see `arm-mcp` in the list of configured servers.

Get details about the Arm MCP Server configuration:

```console
claude mcp get arm-mcp
```

To test the server's functionality, start Claude Code and ask it to use the Arm MCP tools:

```console
claude
```

Then try one of these prompts:

```console
> Use the Arm MCP Server to scan my codebase for x86-specific code
```

or

```console
> Check if the nginx:latest Docker image supports Arm64
```

You can also use the `/mcp` command within Claude Code to see the status of all connected MCP servers and their available tools.

### Example prompts using the Arm MCP Server

Here are some example prompts that use the Arm MCP Server tools:

- `Scan my workspace for code that needs updating for Arm compatibility`
- `Check if the postgres:latest container image supports Arm64 architecture`
- `Search the Arm knowledge base for NEON intrinsics examples`
- `Find learning resources about migrating from x86 to Arm`
- `Analyze this assembly code for performance on Arm processors`

### Managing MCP servers

Remove an MCP server:

```console
claude mcp remove arm-mcp
```

Update an MCP server configuration by removing and re-adding it with new settings.

Check MCP server status within Claude Code:

```console
> /mcp
```

### Troubleshooting MCP Server connections

If the Arm MCP Server doesn't connect:

- Verify Docker is running: `docker ps`
- Check that the image was pulled successfully: `docker images | grep arm-mcp`
- Ensure the volume mount path exists and is accessible
- Check that the Docker daemon is running and accessible
- Try restarting Claude Code after configuration changes
- Review the output of `claude mcp get arm-mcp` for configuration errors

If you encounter issues or have questions, reach out to mcpserver@arm.com.


## Custom prompts and workflows

Create custom prompts for common tasks in your workflow. Refer to the [Claude Code documentation](https://code.claude.com/docs) for advanced configuration options.

You're ready to use Claude Code with the Arm MCP Server to enhance your Arm development workflow.
