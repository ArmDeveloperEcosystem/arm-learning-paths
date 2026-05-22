---
title: Antigravity CLI
author: Jason Andrews
minutes_to_complete: 15
official_docs: https://antigravity.google/

draft: true

test_maintenance: true
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

Antigravity CLI is Google's terminal-based interface for interacting with the Antigravity 2.0 agent-first development platform. You can use it to ask questions, perform multi-file code editing, and invoke AI agents directly from your terminal.

It supports multiple operating systems, including Arm Linux distributions and macOS, and provides powerful AI assistance for developers working on Arm platforms.

In this guide, you'll learn how to install Antigravity CLI on macOS and Arm Linux.

## Before you begin

You need a Google account to use Antigravity CLI. If you don't have one, visit [Google Account Creation](https://accounts.google.com/signup) to create an account.

After installation, running the tool (via the `agy` command) will initiate the authentication process:
- **Local Machine:** It will automatically open your default browser for Google Sign-In.
- **Remote/SSH Sessions:** It will detect the environment and print a secure authorization URL that you can copy and open in your local browser to complete the login.


## Install Antigravity CLI on macOS

You can install Antigravity CLI on macOS using either the official one-liner script or Homebrew.

### Option 1: Install using the official installer script (Recommended)

First, verify that `curl` is available on your system, then run the installer:

```console
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

The installer detects your macOS environment and downloads the appropriate binary. By default, the binary is installed to `~/.local/bin`. 

To run the command globally, ensure this directory is included in your system's `PATH`. Add the following line to your shell configuration file (e.g., `~/.zshrc` or `~/.bash_profile`):

```console
export PATH="$HOME/.local/bin:$PATH"
```

Apply the changes to your current terminal session:

```console
source ~/.zshrc
```

### Option 2: Install using Homebrew

If you prefer using Homebrew for package management, you can install the CLI using the Homebrew cask:

```console
brew install --cask antigravity-cli
```

## Install Antigravity CLI on Arm Linux

You can install Antigravity CLI on Arm Linux distributions using the official installer script. This method works on all major Arm Linux distributions including Ubuntu, Debian, and CentOS.

### Prerequisite packages

Before running the installer, make sure you have `curl` installed on your system.

Install `curl` on Ubuntu/Debian systems:

```bash
sudo apt update && sudo apt install -y curl
```

If you are not using Ubuntu/Debian, use your distribution's package manager to install `curl`.

### Install using the installer script

With `curl` installed, run the installation script:

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

The script automatically detects the CPU architecture (such as `aarch64` / `arm64`) and installs the compatible Arm Linux binary to `~/.local/bin`.

Ensure the installation directory is in your `PATH` by adding it to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Apply the changes:

```bash
source ~/.bashrc
```

## Confirm Antigravity CLI is working

Verify the installation is successful by checking the version of the `agy` binary:

```bash
agy --version
```

The output is similar to:

```output
1.0.1
```

Start an interactive session to authenticate and test basic functionality:

```console
agy
```

This launches the terminal user interface (TUI). On your first run, follow the prompt to authenticate with your Google account. Once authenticated, you can immediately begin asking questions.

### View the available command-line options

To print the available commands and options, use the `--help` flag:

```bash
agy --help
```

Inside the interactive TUI session, you can type `?` to list all available slash commands (e.g., `/settings`, `/clear`, `/fork`, `/logout`).

If you are migrating from the older Gemini CLI, you can use the built-in migration command to import your existing settings, skills, and configuration:

```console
agy plugin import gemini
```

## Configure context for Arm development

Context configuration allows you to provide the Antigravity agent with persistent information about your development environment, preferences, and project details. This helps it generate highly relevant and tailored responses for Arm architecture development.

### Create a context file

Antigravity CLI respects both global and workspace-level context files to guide agent behavior:
- **Global Context:** The CLI automatically loads and enforces user-wide rules located at `~/.gemini/GEMINI.md` across all workspaces.
- **Workspace Context:** The CLI reads `.antigravity.md` (recommended for Antigravity CLI) or `GEMINI.md` (fully supported for backward compatibility) as well as `AGENTS.md` from your active project directory. If both `.antigravity.md` and `GEMINI.md` are present, `.antigravity.md` takes precedence.

Create the global configuration directory if it does not exist:

```console
mkdir -p ~/.gemini
```

Create a global context file with your Arm development preferences:

```console
cat > ~/.gemini/GEMINI.md << 'EOF'
I am an Arm Linux developer. I prefer Ubuntu and other Debian based distributions. I don't use any x86 computers so please provide all information assuming I'm working on Arm Linux. Sometimes I use macOS and Windows on Arm, but please only provide information about these operating systems when I ask for it.
EOF
```

### Managing settings

Antigravity CLI settings are stored in `~/.gemini/antigravity-cli/settings.json`. You can manage settings in two ways:
1. **Interactive Menu:** Run `agy` and type `/settings` or `/config` to open a full-screen overlay menu to browse and modify settings.
2. **Manual Editing:** Open `~/.gemini/antigravity-cli/settings.json` in a text editor to update your preferences manually.

---

## Integrate the Arm MCP server with Antigravity CLI

The Arm Model Context Protocol (MCP) server provides Antigravity CLI with specialized tools and knowledge for Arm architecture development, migration, and optimization. By integrating the Arm MCP server, you gain access to Arm-specific documentation, code analysis tools, and optimization recommendations.

Unlike the older Gemini CLI which stored MCP settings inline inside `settings.json`, Antigravity CLI uses a dedicated configuration file for managing MCP servers.

### Set up the Arm MCP server with Docker

The Arm MCP server runs as a Docker container that Antigravity CLI connects to via the Model Context Protocol. 

First, ensure Docker is installed and running on your system. If needed, follow the [Docker installation guide](/install-guides/docker/).

Pull the Arm MCP server Docker image:

```console
docker pull armlimited/arm-mcp:latest
```

### Configure Antigravity CLI to use the Arm MCP server

Create or update the dedicated global MCP configuration file at `~/.gemini/antigravity-cli/mcp_config.json` (or `.agents/mcp_config.json` inside your active workspace to enable it only for a specific project).

Add the following JSON configuration to `~/.gemini/antigravity-cli/mcp_config.json`:

```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--pull=always",
        "-v",
        "/path/to/your/workspace:/workspace",
        "-v",
        "/path/to/your/ssh/private_key:/run/keys/ssh-key.pem:ro",
        "-v",
        "/path/to/your/ssh/known_hosts:/run/keys/known_hosts:ro",
        "armlimited/arm-mcp:latest"
      ],
      "env": {}
    }
  }
}
```

Replace `/path/to/your/workspace`, `/path/to/your/ssh/private_key`, and `/path/to/your/ssh/known_hosts` with your actual workspace directory, SSH private key, and `known_hosts` file to enable remote testing features on your target device.

### Optional: Use alternative container tools

If you prefer not to use Docker, you can run the Arm MCP server using other compatible container tools such as Podman, Finch, Colima, or Rancher Desktop. 

Select your container tool from the tabs below to view setup instructions and configuration for `~/.gemini/antigravity-cli/mcp_config.json`:

{{< tabpane-normal >}}
  {{< tab header="Podman" >}}
Install: [Podman](https://podman.io/docs/installation)

Pull the Arm MCP Server image:
```console
podman pull armlimited/arm-mcp:latest
```

Add the following configuration to `~/.gemini/antigravity-cli/mcp_config.json`:
```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "podman",
      "args": [
        "run",
        "--rm",
        "-i",
        "--pull=always",
        "-v",
        "/path/to/your/workspace:/workspace",
        "-v",
        "/path/to/your/ssh/private_key:/run/keys/ssh-key.pem:ro",
        "-v",
        "/path/to/your/ssh/known_hosts:/run/keys/known_hosts:ro",
        "armlimited/arm-mcp:latest"
      ],
      "env": {}
    }
  }
}
```
  {{< /tab >}}
  {{< tab header="Finch" >}}
Install: [Finch](/install-guides/finch/)

Pull the Arm MCP Server image:
```console
finch pull armlimited/arm-mcp:latest
```

Add the following configuration to `~/.gemini/antigravity-cli/mcp_config.json`:
```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "finch",
      "args": [
        "run",
        "--rm",
        "-i",
        "--pull=always",
        "-v",
        "/path/to/your/workspace:/workspace",
        "-v",
        "/path/to/your/ssh/private_key:/run/keys/ssh-key.pem:ro",
        "-v",
        "/path/to/your/ssh/known_hosts:/run/keys/known_hosts:ro",
        "armlimited/arm-mcp:latest"
      ],
      "env": {}
    }
  }
}
```
  {{< /tab >}}
  {{< tab header="Colima" >}}
Install: [Colima](https://github.com/abiosoft/colima#installation)

Colima is a lightweight, open-source command-line alternative to Docker Desktop (primarily for macOS). It runs a minimal virtual machine in the background, allowing you to use your standard `docker` command-line tool without installing Docker Desktop.

Pull the Arm MCP Server image:
```console
docker pull armlimited/arm-mcp:latest
```

Add the following configuration to `~/.gemini/antigravity-cli/mcp_config.json`:
```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--pull=always",
        "-v",
        "/path/to/your/workspace:/workspace",
        "-v",
        "/path/to/your/ssh/private_key:/run/keys/ssh-key.pem:ro",
        "-v",
        "/path/to/your/ssh/known_hosts:/run/keys/known_hosts:ro",
        "armlimited/arm-mcp:latest"
      ],
      "env": {}
    }
  }
}
```
  {{< /tab >}}
  {{< tab header="Rancher Desktop" >}}
Install: [Rancher Desktop](https://docs.rancherdesktop.io/getting-started/installation/)

Rancher Desktop uses Docker via Moby.

Pull the Arm MCP Server image:
```console
docker pull armlimited/arm-mcp:latest
```

Add the following configuration to `~/.gemini/antigravity-cli/mcp_config.json`:
```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--pull=always",
        "-v",
        "/path/to/your/workspace:/workspace",
        "-v",
        "/path/to/your/ssh/private_key:/run/keys/ssh-key.pem:ro",
        "-v",
        "/path/to/your/ssh/known_hosts:/run/keys/known_hosts:ro",
        "armlimited/arm-mcp:latest"
      ],
      "env": {}
    }
  }
}
```
  {{< /tab >}}
{{< /tabpane-normal >}}

### Verify the Arm MCP server is working

Start an interactive Antigravity CLI session:

```console
agy
```

Use the `/mcp` command to list the active MCP servers and verify that `arm_mcp_server` is running and ready:

```console
/mcp
```

The Arm MCP server tools are listed in the output:

```output
MCP Servers

Plugins (~/.gemini/antigravity-cli/plugins)
>  ✓ arm_mcp_server  Tools: knowledge_base_search, check_image, sysreport_instructions,
                     migrate_ease_scan, apx_recipe_run, +2 more
```


### Use Arm prompt files with the MCP Server

To guide the agent in using MCP tools effectively across common Arm development tasks, pair the server with Arm-specific prompt files. 

Browse the [agent integrations directory](https://github.com/arm/mcp/tree/main/agent-integrations/gemini) to find prompt files for specific use cases, such as:
- **Arm migration** ([arm-migration.toml](https://github.com/arm/mcp/blob/main/agent-integrations/gemini/arm-migration.toml)): Helps the agent systematically migrate applications from x86 to Arm, including dependency analysis, compatibility checks, and optimization recommendations.

If you are facing issues or have questions, reach out to mcpserver@arm.com.
