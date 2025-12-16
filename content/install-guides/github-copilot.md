---
title: GitHub Copilot

draft: true 

author: Pareena Verma
minutes_to_complete: 10
official_docs: https://docs.github.com/en/copilot

test_maintenance: true
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort. It suggests whole lines or entire functions based on your comments and code context.

Copilot works seamlessly on Arm-based systems, including Linux distributions running on Arm servers, macOS on Apple Silicon, and Windows on Arm devices. This guide shows you how to install GitHub Copilot in Visual Studio Code and extend it with the Arm MCP Server for Arm-specific development assistance.

{{% notice Note %}}
For installation instructions for other editors (JetBrains IDEs, Neovim, Vim), see the [GitHub Copilot documentation](https://docs.github.com/en/copilot).
{{% /notice %}}

## What should I do before installing GitHub Copilot?

You need a GitHub account with an active GitHub Copilot subscription to use GitHub Copilot. 

If you don't have a GitHub account, visit [GitHub](https://github.com/) and sign up.

### Subscribe to GitHub Copilot

GitHub Copilot offers several subscription plans:

- **Individual** — For personal development
- **Business** — For teams and organizations  
- **Enterprise** — For large-scale deployments
- **Free tier** — For verified students, teachers, and maintainers of popular open source projects

[Select your GitHub Copilot subscription plan](https://github.com/features/copilot/plans) to get started.

### Verify your subscription

After subscribing, verify your subscription is active:

1. Sign in to your GitHub account
2. Navigate to **Settings** → **Copilot**
3. Confirm your subscription status shows as **Active**

## Install Visual Studio Code

Visual Studio Code runs natively on Arm systems and provides the best experience for GitHub Copilot.

Download Visual Studio Code from the [Visual Studio Code download page](https://code.visualstudio.com/download). Select the version for your operating system:

- **macOS (Apple Silicon)** — Download the Apple Silicon version
- **Linux (Arm)** — Download the Arm64 `.deb` or `.rpm` package
- **Windows on Arm** — Download the Arm64 installer

After downloading, run the installer and follow the installation prompts.

For Linux systems, install VS Code using your package manager. On Ubuntu and Debian-based distributions:

```bash { target="ubuntu:latest" }
curl -L "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64" -o vscode-arm64.deb
sudo dpkg -i vscode-arm64.deb
sudo apt-get install -f 
```

### Verify the installation

Open a terminal and verify the installation:

```bash
code --version
```

The output is similar to:

```output
1.95.3
f1a4fb101478ce6ec82fe9627c43efbf9e98c813
arm64
```


## Install GitHub Copilot extensions

### Install the main extension

Open Visual Studio Code and install the GitHub Copilot extension:

1. Open the Extensions view by selecting the Extensions icon in the Activity Bar or press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS)
2. Search for **GitHub Copilot**
3. Select **Install** on the GitHub Copilot extension by GitHub

Alternatively, install from the command line:

```console
code --install-extension GitHub.copilot
```

### Install Copilot Chat

For conversational AI assistance, install the GitHub Copilot Chat extension:

```console
code --install-extension GitHub.copilot-chat
```

You can also search for **GitHub Copilot Chat** in the Extensions view and select **Install**.

### Authorize GitHub Copilot

After installing the extensions, authorize GitHub Copilot:

1. In VS Code, select the GitHub Copilot icon in the status bar (bottom right)
2. Select **Sign in to GitHub**
3. Follow the prompts to authorize the extension in your browser
4. Return to VS Code to complete the setup

### Verify Copilot is working

Test that GitHub Copilot is generating suggestions:

1. Create a new file (**File** → **New File** or press `Ctrl+N` on Windows/Linux or `Cmd+N` on macOS)
2. Save the file with a programming language extension (`test.py` for Python, `test.js` for JavaScript, or `test.go` for Go)
3. Type a comment describing a function:
   ```python
   # Function to calculate fibonacci numbers
   ```
4. Press Enter to start a new line

Copilot analyzes your comment and suggests code as gray text in the editor.

5. Press Tab to accept the suggestion or Esc to dismiss it
6. Continue typing to see more suggestions as you work

If you don't see suggestions:

- Verify you're working in the VS Code editor window (not a terminal)
- Check that the GitHub Copilot icon in the status bar shows it's active
- Confirm you're signed in to your GitHub account
- Verify your subscription is active

## Work with GitHub Copilot modes

GitHub Copilot Chat in Visual Studio Code offers three modes: Agent, Edit, and Ask. Each mode helps you work with code in different ways.

### Agent Mode

Agent Mode enables Copilot to take autonomous actions in your workspace. Copilot can read and analyze multiple files, make changes across your project, and create new files.

To use Agent Mode:

1. Open the Copilot Chat panel by selecting the chat icon in the Activity Bar or press `Ctrl+Enter` (Windows/Linux) or `Cmd+Ctrl+I` (macOS)
2. Type `@workspace` followed by your request

Example prompts:
- `Create a Python application to calculate fibonacci numbers`
- `@workspace add error handling throughout the application`

### Edit Mode

Edit Mode focuses on making targeted changes to your current file or selected code. This mode is useful when you want Copilot to modify existing code without creating new files.

To use Edit Mode with selected code:

1. Select the code you want to modify in your editor
2. Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (macOS) to open inline chat
3. Describe the changes you want
4. Copilot shows a preview before applying changes

Example prompts:
- Select a function and ask: `Add input validation and error handling`
- Select a code block and ask: `Optimize this code for Arm architecture`

### Ask Mode

Ask Mode helps you understand code and learn concepts without making changes to your files.

To use Ask Mode:

1. Open the Copilot Chat panel
2. Type your question directly without any special prefixes

Example prompts:
- `How does this function work?` (with code selected)
- `What are the best practices for error handling in Python?`
- `Explain the difference between Arm64 and x86 architectures`

## Extend with the Arm MCP Server

Model Context Protocol (MCP) Servers extend GitHub Copilot's capabilities by providing specialized tools and knowledge bases. The Arm MCP Server provides AI assistants with tools and knowledge for Arm architecture development, migration, and optimization.

### About the Arm MCP Server

The Arm MCP Server includes several tools for Arm development:

- **migrate-ease scan** — Analyzes codebases for x86-specific code that needs updating for Arm compatibility
- **skopeo** — Inspects container images to check for ARM64 architecture support
- **knowledge_base_search** — Searches Arm documentation and learning resources
- **mca (Machine Code Analyzer)** — Analyzes assembly code for performance on Arm architectures
- **check_image** — Verifies Docker image architecture compatibility

### Install the Arm MCP Server

You need Docker running on your system to use the Arm MCP Server. See the [Docker install guide](/install-guides/docker/) for instructions.

You can configure the MCP server using one of these methods:

Method 1: Install from GitHub MCP Registry (recommended)

The easiest way to install the Arm MCP Server is through the GitHub MCP Registry:

1. Visit the [Arm MCP Server registry page](https://github.com/mcp/arm/arm-mcp)
2. Select the **Install MCP Server** button
3. From the dropdown, choose **Install in VSCode**
4. VS Code opens with the Arm MCP Server installation page
5. Select **Install** as you would with other extensions

![Screenshot of the Arm MCP Server installation page in Visual Studio Code showing the Install button and server description alt-text#center](/install-guides/_images/mcp-server-install.png "Install Arm MCP Server")

This method automatically installs the Arm MCP Server and pulls the Docker image. No manual configuration is required.

### Configure manually (alternative method)

You can also configure the Arm MCP Server manually for more control over the installation.

First, ensure Docker is running on your system. Pull the Arm MCP Server image:

```console
docker pull armlimited/arm-mcp:latest
```

Create a `.vscode` directory in your project root if it doesn't exist, then create an `mcp.json` file:

```console
mkdir -p .vscode
```

Create an `mcp.json` file in the `.vscode` directory with the following configuration:

```json
{
  "servers": {
    "arm-mcp": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-v", "/path/to/your/codebase:/workspace",
        "armlimited/arm-mcp:latest"
      ]
    }
  }
}
```

Method 3: User configuration (available in all workspaces)

Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS) and select **MCP: Open User Configuration**. This opens your user-level `mcp.json` file located at `~/Library/Application Support/Code/User/mcp.json` (macOS) or `%APPDATA%\Code\User\mcp.json` (Windows).

Add the following configuration to the user-level `mcp.json` file:

```json
{
  "servers": {
    "arm-mcp": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-v", "/path/to/your/codebase:/workspace",
        "armlimited/arm-mcp:latest"
      ]
    }
  }
}
```

Save the file. A **Start** button appears at the top of the servers list in your `mcp.json` file. Select **Start** to start the Arm MCP Server.

### How do I analyze a local codebase with the Arm MCP Server?

To analyze code in your workspace, mount your local directory to the MCP server's `/workspace` folder using a volume mount.

Update your `.vscode/mcp.json` configuration to include the volume mount. Replace `/path/to/your/codebase` with the actual path to your project

For example, if your project is at `/Users/username/myproject`, the volume mount configuration is:

```json
"-v",
"/Users/username/myproject:/workspace",
```

{{% notice Note %}}
The volume mount (`-v` flag) connects your local directory to the MCP server's `/workspace` folder. This enables the server to analyze code in your workspace. Use absolute paths for the source directory to avoid mounting errors.
{{% /notice %}}

After saving the `.vscode/mcp.json` file, select the **Start** button that appears at the top of the servers list to start the MCP server.

### Verify the installation

After starting the MCP server, confirm it's running:

1. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS)
2. Type and select **MCP: List Servers**
3. Verify `arm-mcp` appears as a Running configured server

Open the GitHub Copilot Chat panel by selecting the chat icon in the Activity Bar. In the chat box, select **Agent** from the mode dropdown.

To view available MCP tools, select the tools icon in the top left corner of the chat box. This opens the MCP server list showing all available tools from the Arm MCP Server.

![Screenshot of the MCP Server Tools panel in Visual Studio Code showing available tools from the Arm MCP Server alt-text#center](/install-guides/_images/new-mcp-server-tools.png "Tools from the Arm MCP Server")

### Use the Arm MCP Server

Ask Copilot to use specific Arm MCP tools in your prompts:

```
Use the Arm MCP Server to scan my codebase for x86-specific code
```

or

```
Check if the nginx:latest Docker image supports Arm64
```

Example prompts that use the Arm MCP Server:

- `Scan my workspace for code that needs updating for Arm compatibility`
- `Check if the postgres:latest container image supports Arm64 architecture`
- `Search the Arm knowledge base for NEON intrinsics examples`
- `Find learning resources about migrating from x86 to Arm`

## Troubleshooting

### MCP Server doesn't connect

If the Arm MCP Server doesn't connect:

- Verify Docker is running: `docker ps`
- Check that the image was pulled successfully: `docker images | grep arm-mcp`
- Review the VS Code Output panel (**View** → **Output** → **GitHub Copilot Chat**) for error messages
- Restart VS Code after making configuration changes

### Copilot suggestions don't appear

If you don't see Copilot suggestions:

- Verify you're in the editor window (not a terminal or output panel)
- Check that the GitHub Copilot icon in the status bar is active (not grayed out)
- Confirm you're signed in to GitHub (**View** → **Command Palette** → **GitHub: Sign In**)
- Verify your subscription is active in GitHub settings

### Volume mount errors

If you see volume mount errors when starting the MCP server:

- Ensure you're using absolute paths (not relative paths like `./myproject`)
- Verify the directory exists and you have read permissions
- On Linux, ensure your user has permission to run Docker commands

For support, contact [mcpserver@arm.com](mailto:mcpserver@arm.com).

You're ready to use GitHub Copilot with the Arm MCP Server to enhance your Arm development workflow.
