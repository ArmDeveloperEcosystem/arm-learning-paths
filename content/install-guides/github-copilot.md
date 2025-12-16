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

GitHub Copilot works seamlessly on Arm-based systems, including Linux distributions running on Arm servers, macOS on Apple Silicon, and Windows on Arm devices.

This guide focuses on installing GitHub Copilot in Visual Studio Code. GitHub Copilot also supports other editors including JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm), Neovim, and others. Visit the [official GitHub Copilot documentation](https://docs.github.com/en/copilot) for installation instructions for other editors.

## What should I do before installing GitHub Copilot?

You need a GitHub account with an active GitHub Copilot subscription to use GitHub Copilot. 

If you don't have a GitHub account, visit [GitHub](https://github.com/) and sign up.

To subscribe to GitHub Copilot, visit [GitHub Copilot pricing](https://github.com/features/copilot/plans) and choose a plan that fits your needs. GitHub Copilot offers individual, business, and enterprise plans, plus a free tier for verified students, teachers, and maintainers of popular open source projects.

## How do I install GitHub Copilot in Visual Studio Code?

Visual Studio Code is one of the most popular editors for using GitHub Copilot, and it works natively on Arm systems.

### Install Visual Studio Code

If you don't have Visual Studio Code installed, download and install it from the [offical download page]((https://code.visualstudio.com/download) for your operating system:

- macOS (Apple Silicon): Download the the Apple Silicon version
- Linux (Arm): Download the Arm64 `.deb` or `.rpm` package
- Windows on Arm: Download the Arm64 installer

For Linux, you can install VS Code using the package manager. On Ubuntu and Debian-based distributions:

```bash { target="ubuntu:latest" }
curl -L "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64" -o vscode-arm64.deb
sudo dpkg -i vscode-arm64.deb
sudo apt-get install -f 
```

### Install the GitHub Copilot extension

Open Visual Studio Code and install the GitHub Copilot extension:

1. Open VS Code
2. Select the Extensions view by selecting the Extensions icon in the Activity Bar on the left side or pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS)
3. Search for "GitHub Copilot"
4. Select **Install** on the "GitHub Copilot" extension by GitHub

Alternatively, install from the command line:

```console
code --install-extension GitHub.copilot
```

### Install the GitHub Copilot Chat extension 

For an enhanced experience with conversational AI assistance, install the GitHub Copilot Chat extension:

```console
code --install-extension GitHub.copilot-chat
```

Or search for "GitHub Copilot Chat" in the Extensions view and install it.

### Sign in to GitHub Copilot

After installing the extension, you need to authorize it:

1. In VS Code, select the GitHub Copilot icon in the status bar (bottom right)
2. Select **Sign in to GitHub**
3. Follow the prompts to authorize the extension in your browser
4. Return to VS Code to complete the setup

## How do I confirm GitHub Copilot is working?

You now have GitHub Copilot installed in Visual Studio Code. 

Confirm it's working by testing code suggestions:

1. In VSCode, create a new file by selecting **File** → **New File** or pressing `Ctrl+N` (Windows/Linux) or `Cmd+N` (macOS)
2. Save the file with a programming language extension by selecting **File** → **Save As** (for example, `test.py` for Python, `test.js` for JavaScript, or `test.go` for Go)
3. In the VS Code editor window, type a comment describing a function:
   - For Python: `# Function to calculate fibonacci numbers`
   - For JavaScript: `// Function to calculate fibonacci numbers`
   - For Go: `// Function to calculate fibonacci numbers`
4. Press Enter to start a new line

GitHub Copilot analyzes your comment and suggests code. The suggestion appears as gray text in the editor.

5. Press Tab to accept the suggestion, or press Esc to dismiss it
6. Continue typing to see more suggestions as you work

If you don't see suggestions, check that:
- You're working in the Visual Studio Code editor window (not a terminal)
- The GitHub Copilot icon in the status bar (bottom right) shows it's active
- You're signed in to your GitHub account
- Your subscription is active

## What are the different GitHub Copilot modes?

GitHub Copilot Chat in Visual Studio Code offers three modes to help you work with code in different ways: Agent, Edit, and Ask modes. Each mode is designed for specific tasks.

### Agent Mode

Agent Mode enables GitHub Copilot to take autonomous actions in your workspace. In this mode, Copilot can:

- Read and analyze multiple files in your project
- Make changes across different files
- Create new files and directories
- Execute tasks that require understanding your entire codebase

To use Agent Mode:

1. Open the GitHub Copilot Chat panel by selecting the chat icon in the Activity Bar or pressing `Ctrl+Enter` (Windows/Linux) or `Cmd+Ctrl+I` (macOS)
2. Type `@workspace` followed by your request or prompt to engage Agent Mode
3. Copilot analyzes your workspace and takes appropriate actions

Example prompts for Agent Mode:
- `Create a python application to calculate fibonacci numbers on my arm machine`
- `@workspace add error handling throughout the application`

### Edit Mode

Edit Mode focuses on making targeted changes to your current file or selected code. This mode is useful when you want Copilot to modify existing code without creating new files.

To use Edit Mode:

1. Select the code you want to modify in your editor
2. Open the Copilot Chat panel
3. Type your request describing the changes you want

Alternatively, use the inline chat:

1. Select the code you want to modify
2. Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (macOS) to open inline chat
3. Describe the changes you want to make
4. Copilot shows a preview of the changes before applying them

Example prompts for Edit Mode:
- Select a function and ask: `Add input validation and error handling`
- Select a code block and ask: `Optimize this code for better performance on my arm machine`

### Ask Mode

Ask Mode is designed for questions and explanations. Use this mode when you want to understand code, learn about concepts, or get guidance without making changes to your files.

To use Ask Mode:

1. Open the GitHub Copilot Chat panel
2. Type your question directly without any special prefixes

Example prompts for Ask Mode:
- `How does this function work?` (with code selected)
- `What are the best practices for error handling in Python?`

## How do I use MCP Servers with GitHub Copilot?

Model Context Protocol (MCP) Servers extend GitHub Copilot's capabilities by providing specialized tools and knowledge bases. GitHub Copilot can connect to MCP servers to access domain-specific expertise and functionality.

The Arm MCP Server provides AI assistants with tools and knowledge for Arm architecture development, migration, and optimization. This is particularly useful when working on Arm-based systems.

### What tools does the Arm MCP Server provide?

The Arm MCP Server includes several tools designed for Arm development:

- migrate-ease scan: Analyzes codebases for x86-specific code that needs updating for Arm compatibility
- skopeo: Inspects container images to check for ARM64 architecture support
- knowledge_base_search: Searches Arm documentation and learning resources
- mca (Machine Code Analyzer): Analyzes assembly code for performance on Arm architectures
- check_image: Verifies Docker image architecture compatibility

### How do I configure the Arm MCP Server with GitHub Copilot?

You need Docker running on your system to use the Arm MCP Server. See the [Docker install guide](/install-guides/docker/) for instructions.

You can configure the MCP server using one of these methods:

Method 1: Install from GitHub MCP Registry (recommended)

The easiest way to install the Arm MCP Server is through the GitHub MCP Registry:

1. Visit the [Arm MCP Server registry page](https://github.com/mcp/arm/arm-mcp)
2. Select the **Install MCP Server** button
3. From the dropdown, choose **Install in VSCode**
4. VS Code opens with the Arm MCP Server installation page
5. Select **Install** as you would with other extensions

![MCP Server Install](/install-guides/_images/mcp-server-install.png "Figure 1. Install Arm MCP Server")

This method automatically installs the Arm MCP Server and pulls the Docker image. No manual configuration is required.

Method 2: Workspace configuration (recommended for sharing)

For manual configuration, you can create a configuration file in your workspace. MCP servers can be configured in two locations:

- For a specific repository: Create a `.vscode/mcp.json` file in the root of your repository. This enables you to share MCP server configuration with anyone who opens the project.
- For your personal VS Code instance: Add the configuration to your `settings.json` file. This makes the server available in all workspaces.

{{% notice Note %}}
Use only one location per server to avoid conflicts and unexpected behavior.
{{% /notice %}}

First, pull the Arm MCP Server image:

```console
docker pull armlimited/arm-mcp:latest
```

Create a `.vscode` directory in your project root if it doesn't exist, then create an `mcp.json` file:

```console
mkdir -p .vscode
```

Add the following configuration to `.vscode/mcp.json`:

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

For example, if your project is at `/Users/username/myproject`, the volume mount args in your `mcp.json` would be:

```json
"-v",
"/Users/username/myproject:/workspace",
```

### How do I verify the Arm MCP Server is working?

After saving the `.vscode/mcp.json` file, the **Start** button appears at the top of the servers list. Select **Start** to start the MCP server.

To confirm the server is running:

1. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS)
2. Type and select **MCP: List Servers**
3. You should see `arm-mcp` listed as a Running configured server

Open the GitHub Copilot Chat panel by selecting the chat icon in the Activity Bar. In the chat box, select **Agent** from the mode dropdown.

To view available MCP tools, select the tools icon in the top left corner of the chat box. This opens the MCP server list showing all available tools from the Arm MCP Server.

![MCP Server Tools](/install-guides/_images/new-mcp-server-tools.png "Figure 2. Tools loaded from the Arm MCP Server")

You can also ask Copilot to use specific Arm MCP tools:

```
Use the Arm MCP Server to scan my codebase for x86-specific code
```

or

```
Check if the nginx:latest Docker image supports Arm64
```

### Example prompts using the Arm MCP Server

Here are some example prompts that use the Arm MCP Server tools:

- `Scan my workspace for code that needs updating for Arm compatibility`
- `Check if the postgres:latest container image supports Arm64 architecture`
- `Search the Arm knowledge base for NEON intrinsics examples`
- `Find learning resources about migrating from x86 to Arm`

### Troubleshooting MCP Server connections

If the Arm MCP Server doesn't connect:

- Verify Docker is running: `docker ps`
- Check that the image was pulled successfully: `docker images | grep arm-mcp`
- Ensure the timeout value (60000ms) is sufficient for your system
- Check VS Code Output panel (select **Output** → **GitHub Copilot Chat**) for error messages
- Restart VS Code after making configuration changes

If you encounter issues or have questions, reach out to mcpserver@arm.com.

You're ready to use GitHub Copilot with the Arm MCP Server to enhance your Arm development workflow.
