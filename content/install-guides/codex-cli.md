---
title: Codex CLI

author: Joe Stech
minutes_to_complete: 10
official_docs: https://developers.openai.com/codex/cli/

test_maintenance: true
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

Codex CLI is a lightweight coding agent from OpenAI that runs locally in your terminal. It can help you with coding tasks, understand your codebase, run commands, and assist with development workflows.

It supports multiple operating systems, including Arm-based Linux distributions and macOS.

This guide explains how to install Codex CLI on macOS and Arm Linux.

## What should I do before installing Codex CLI?

You need an OpenAI account to use Codex CLI. You can either sign in with your [ChatGPT](https://chatgpt.com/) account (Plus, Pro, Team, Edu, or Enterprise plan) or use an OpenAI API key.

Codex CLI requires Node.js 18 or later.

## How do I download and install Codex CLI?

On most systems, install Codex CLI using npm. On macOS, there is also the option for you to use Homebrew.

### How do I use npm to install Codex CLI?

The easiest way to install Codex CLI is with npm:

```console
npm install -g @openai/codex
```

### Can I use Homebrew to install Codex CLI on macOS?

Yes. Install [Homebrew](https://brew.sh/) if it's not already available on your computer.

Install Codex CLI using Homebrew:

```console
brew install --cask codex
```

## How do I install Codex CLI on Arm Linux?

You can install Codex CLI on Arm Linux distributions using npm. This method works on all major Arm Linux distributions including Ubuntu, Debian, CentOS, and others.

### What packages do I need before installing Codex CLI on Arm Linux?

Before installing Codex CLI, install prerequisite packages and Node.js.

Install the required packages on Ubuntu/Debian systems:

```bash
sudo apt update && sudo apt install -y curl
```

If you're not using Ubuntu/Debian, use your package manager to install curl.

### How do I install Node.js on Arm Linux?

Codex CLI requires Node.js version 18 or higher. The easiest way to install Node.js on Arm Linux is using the NodeSource repository.

Download and run the Node.js setup script. For example, for Node.js 22.x:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
```

Install Node.js:

```bash
sudo apt install nodejs -y
```

Verify Node.js is installed correctly:

```bash
node --version
```

The output should show version 18 or higher:

```output
v22.21.0
```

Verify npm is available:

```bash
npm --version
```

The output shows the npm version:

```output
10.9.4
```

### How do I install Codex CLI using npm on Arm Linux?

With Node.js installed, install Codex CLI globally using npm.

Install Codex CLI globally:

```bash
sudo npm install -g @openai/codex
```

This downloads and installs the latest version of Codex CLI.

### How do I confirm Codex CLI is working?

You now have the latest version of Codex CLI installed.

Confirm the CLI is available by printing the version:

```console
codex --version
```

The output shows the version:

```output
@openai/codex, 0.77.0
```

### How do I authenticate with OpenAI?

There are two ways to authenticate with Codex CLI.

**Option 1: Sign in with ChatGPT**

Run the `codex` command and select **Sign in with ChatGPT** to authenticate:

```console
codex
```
This opens a browser window to complete authentication. This option is recommended if you have a ChatGPT Plus, Pro, Team, Edu, or Enterprise plan.

**Option 2: Use an OpenAI API key**

You can also use an OpenAI API key for authentication. This is useful for developers who prefer API-based access or need to use Codex in automated workflows.

Set the `OPENAI_API_KEY` environment variable:

```console
export OPENAI_API_KEY=your-api-key-here
```

Add this command to your shell configuration file (such as ~/.bashrc or ~/.zshrc) to make it permanent.

You can generate an API key from the [OpenAI Platform](https://platform.openai.com/api-keys).

{{% notice Note %}}
When using an API key, usage is billed to your OpenAI API account rather than being included in your ChatGPT subscription.
{{% /notice %}}

## How do I configure Codex CLI?

Codex CLI stores preferences in `~/.codex/config.toml`.

You can configure various options including the default model, approval mode, and MCP servers.

To see all configuration options, refer to the [Configuration documentation](https://developers.openai.com/codex/cli/reference/).


## Install the Arm MCP server

The Arm MCP Server is an MCP server providing AI assistants with tools and knowledge for Arm architecture development, migration, and optimization. This section shows how to configure the Arm MCP server locally using Docker.

First, pull the MCP server image to your local machine:

```console
docker pull armlimited/arm-mcp:latest
```
Ensure Docker is installed and running. See the [Docker install guide](/install-guides/docker/) for instructions.

### How do I configure the Arm MCP server?

Codex CLI uses a TOML configuration file for MCP servers. Modify the file `~/.codex/config.toml` to add the Arm MCP server using Docker.

To analyze a local codebase, use a `-v` argument to mount a volume to the Arm MCP server `/workspace` folder so it can access code you want to analyze with migrate-ease and other tools.

Replace the path `/Users/yourname01/yourlocalcodebase` with the path to your local codebase.

Add the following to your `~/.codex/config.toml` file:

```toml
[mcp_servers.arm-mcp]
command = "docker"
args = [
    "run",
    "--rm",
    "-i",
    "-v", "/Users/yourname01/yourlocalcodebase:/workspace",
    "--name", "arm-mcp",
    "armlimited/arm-mcp:latest"
]
startup_timeout_sec = 60
```

{{% notice Note %}}
The section must be named `mcp_servers` with an underscore. Using `mcp-servers` or `mcpservers` will cause Codex to ignore the configuration.
{{% /notice %}}

### How do I verify the Arm MCP server is working?

Start Codex CLI and list the tools from the MCP server to verify it is working:

```console
codex
```

At the Codex prompt, run the `/mcp` command to view active MCP servers and their status:

```console
/mcp
```

The Arm MCP server is listed in the output. If the arm-mcp server indicates it's still loading, wait a moment and check again.

You can also verify the tools are available by asking Codex to list the available Arm MCP tools.

If you're facing issues or have questions, reach out to mcpserver@arm.com.

You're now ready to use Codex CLI with Arm-specific development assistance.
