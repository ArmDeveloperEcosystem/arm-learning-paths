---
title: Gemini CLI

author: Jason Andrews
minutes_to_complete: 15
official_docs: https://ai.google.dev/gemini-api/docs/cli

test_maintenance: true
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

Gemini CLI is Google's command-line interface for interacting with the Gemini AI assistant. You can use it to ask questions about software development, architecture, and general programming tasks with advanced AI capabilities.

It supports multiple operating systems, including Arm Linux distributions and macOS, and provides powerful AI assistance for developers working on Arm platforms.

This guide explains how to install Gemini CLI on macOS and Arm Linux.

## What should I do before installing Gemini CLI?

You need a Google account to use Gemini CLI. If you don't have one, visit [Google Account Creation](https://accounts.google.com/signup) to create your account.

You'll also need to set up authentication for the Gemini API. Gemini CLI supports multiple authentication methods, with Google OAuth login being the recommended approach for most users.

## How do I set up authentication for Gemini CLI?

Gemini CLI offers three authentication methods. Choose the one that best fits your needs.

### Option 1: Google OAuth login 

This is your Google account, and is the easiest method for most users. After installing Gemini CLI, run the tool and select "Login with Google" when prompted. This opens your browser for authentication.

Benefits of using Google OAuth:
- Free tier includes 60 requests per minute and 1,000 requests per day
- Access to Gemini with 1M token context window
- No manual API key management required

### Option 2: Gemini API key

If you prefer using an API key, you can generate one from Google AI Studio.

To get your API key:
1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

Set the API key in your environment:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

Benefits of using an API key:
- Free tier includes 250 requests per day
- Works well for automated scripts and CI/CD environments
- No interactive authentication required

### Option 3: Vertex AI for enterprise users

For enterprise users with Google Cloud accounts, you can use Vertex AI authentication.

Set up Vertex AI authentication:

```bash
export GOOGLE_API_KEY="YOUR_GOOGLE_CLOUD_API_KEY"
export GOOGLE_GENAI_USE_VERTEXAI=true
```

Benefits of using Vertex AI:
- Enterprise-grade features and support
- Integration with Google Cloud billing and management
- Higher rate limits and advanced features

## How do I install Gemini CLI on macOS?

The easiest way to install Gemini CLI on macOS is using Homebrew, which handles all dependencies.

### Install Gemini CLI on macOS using Homebrew

You can install [Homebrew](https://brew.sh/) if it isn't already available on your computer.

Install Gemini CLI using Homebrew:

```console
brew install gemini-cli
```

This installs Gemini CLI and automatically handles the Node.js dependency. The Homebrew version is currently at 0.19.4 (stable) and receives regular updates.

### Install Gemini CLI on macOS using npm

If you prefer to use npm or need the latest version, you can install Gemini CLI globally using npm.

First, make sure you have Node.js version 20 or higher installed. Install Node.js using Homebrew:

```console
brew install node
```

Verify Node.js is installed correctly:

```console
node --version
```

The output is similar to:

```output
v25.2.1
```

Install Gemini CLI globally using npm:

```console
npm install -g @google/gemini-cli
```

This installs the latest version, such as 0.20.0, directly from npm. Homebrew can lag behind npm, so versions might differ.

### How do I confirm Gemini CLI is working on macOS?

You now have Gemini CLI installed on your macOS system.

Confirm the CLI is available by checking the version:

```console
gemini --version
```

The output is similar to:

```output
0.20.0
```

Start an interactive session to test basic functionality:

```console
gemini
```

This opens the Gemini CLI interface where you can authenticate and start asking questions. On first run, you'll be prompted to choose your authentication method.

## How do I install Gemini CLI on Arm Linux?

You can install Gemini CLI on Arm Linux distributions using npm. This method works on all major Arm Linux distributions including Ubuntu, Debian, CentOS, and others.

### What packages do I need before installing Gemini CLI on Arm Linux?

Before installing Gemini CLI, install prerequisite packages and Node.js.

Install the required packages on Ubuntu/Debian systems:

```bash
sudo apt update && sudo apt install -y curl
```

If you're not using Ubuntu/Debian, use your package manager to install curl.

### How do I install Node.js on Arm Linux?

Gemini CLI requires Node.js version 20 or higher. The easiest way to install Node.js on Arm Linux is using the NodeSource repository.

Download and run the Node.js 20.x setup script:

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```

Verify Node.js is installed correctly:

```bash
node --version
```

The output should show version 20 or higher:

```output
v20.19.4
```

Verify npm is available:

```bash
npm --version
```

The output is similar to:

```output
10.2.4
```

### How do I install Gemini CLI using npm on Arm Linux?

With Node.js installed, install Gemini CLI globally using npm.

Install Gemini CLI globally:

```bash
sudo npm install -g @google/gemini-cli
```

This downloads and installs the latest version of Gemini CLI. The installation may take a few minutes as it downloads dependencies.

### How do I confirm Gemini CLI is working on Arm Linux?

You now have Gemini CLI installed on your Arm Linux system.

Confirm the CLI is available by checking the version:

```bash
gemini --version
```

The output shows the version:

```output
0.20.0
```

### How do I view the available command-line options?

To print the available commands and options, use the `--help` flag:

```bash 
gemini --help
```

The output shows the available commands and options:

```output
Usage: gemini [options] [command]

Gemini CLI - Launch an interactive CLI, use -p/--prompt for non-interactive mode

Commands:
  gemini [query..]             Launch Gemini CLI                                                                         [default]
  gemini mcp                   Manage MCP servers
  gemini extensions <command>  Manage Gemini CLI extensions.                                                  [aliases: extension]

Positionals:
  query  Positional prompt. Defaults to one-shot; use -i/--prompt-interactive for interactive.

Options:
  -d, --debug                     Run in debug mode?                                                    [boolean] [default: false]
  -m, --model                     Model                                                                                   [string]
  -p, --prompt                    Prompt. Appended to input on stdin (if any).
                          [deprecated: Use the positional prompt instead. This flag will be removed in a future version.] [string]
  -i, --prompt-interactive        Execute the provided prompt and continue in interactive mode                            [string]
  -s, --sandbox                   Run in sandbox?                                                                        [boolean]
  -y, --yolo                      Automatically accept all actions (aka YOLO mode, see https://www.youtube.com/watch?v=xvFZjo5PgG0
                                  for more details)?                                                    [boolean] [default: false]
      --approval-mode             Set the approval mode: default (prompt for approval), auto_edit (auto-approve edit tools), yolo
                                  (auto-approve all tools)                      [string] [choices: "default", "auto_edit", "yolo"]
      --experimental-acp          Starts the agent in ACP mode                                                           [boolean]
      --allowed-mcp-server-names  Allowed MCP server names                                                                 [array]
      --allowed-tools             Tools that are allowed to run without confirmation                                       [array]
  -e, --extensions                A list of extensions to use. If not provided, all extensions are used.                   [array]
  -l, --list-extensions           List all available extensions and exit.                                                [boolean]
  -r, --resume                    Resume a previous session. Use "latest" for most recent or index number (e.g. --resume 5)
                                                                                                                          [string]
      --list-sessions             List available sessions for the current project and exit.                              [boolean]
      --delete-session            Delete a session by index number (use --list-sessions to see available sessions).       [string]
      --include-directories       Additional directories to include in the workspace (comma-separated or multiple
                                  --include-directories)                                                                   [array]
      --screen-reader             Enable screen reader mode for accessibility.                                           [boolean]
  -o, --output-format             The format of the CLI output.                  [string] [choices: "text", "json", "stream-json"]
  -v, --version                   Show version number                                                                    [boolean]
  -h, --help                      Show help               
```

Your Gemini CLI installation on Arm Linux is now complete and ready to use.

## How do I configure context for Arm development?

Context configuration allows you to provide Gemini with persistent information about your development environment, preferences, and project details. This helps Gemini give more relevant and tailored responses for Arm architecture development.

### How do I create a context file for Gemini CLI?

Gemini CLI looks for context files in your home directory's `.gemini` configuration folder. Create this directory and add your context file.

Create the Gemini configuration directory:

```bash
mkdir -p ~/.gemini
```

Create a context file with Arm development information:

```bash
cat > ~/.gemini/GEMINI.md << 'EOF'
I am an Arm Linux developer. I prefer Ubuntu and other Debian based distributions. I don't use any x86 computers so please provide all information assuming I'm working on Arm Linux. Sometimes I use macOS and Windows on Arm, but please only provide information about these operating systems when I ask for it.
EOF
```

This creates a context file that tells Gemini about your Arm development focus and preferences.

### How do I verify that context is being loaded?

Verify that Gemini is loading your context file by starting a chat session and asking a development question.

Start Gemini CLI:

```console
gemini 
```

Ask a question that should trigger context-aware responses:

```output
How do I install gcloud?
```

If context is loaded correctly, Gemini should provide Arm-specific recommendations.

## How do I integrate the Arm MCP server with Gemini CLI?

The Arm MCP (Model Context Protocol) server provides Gemini CLI with specialized tools and knowledge for Arm architecture development, migration, and optimization. By integrating the Arm MCP server, you gain access to Arm-specific documentation, code analysis tools, and optimization recommendations directly through your Gemini conversations.

### How do I set up the Arm MCP server with Docker?

The Arm MCP server runs as a Docker container that Gemini CLI connects to via the Model Context Protocol. You need Docker installed on your system to use the MCP server.

First, ensure Docker is installed and running on your system. Install Docker by following the [Docker installation guide](/install-guides/docker/).

Pull the Arm MCP server Docker image:

```console
docker pull armlimited/arm-mcp:latest
```

### How do I configure Gemini CLI to use the Arm MCP server?

Gemini CLI uses a configuration file to connect to MCP servers. Create or update this configuration to include the Arm MCP server.

Use an editor to modify the file `~/.gemini/settings.json` to add an MCP object. 

You may have other objects already in the file so make sure to use a `,` at the end of each object that is not the last one. For example, the code below shows both the `security` and the `mcpServers` objects.

```json
{
  "security": {
    "auth": {
      "selectedType": "oauth-personal"
    }
  },
  "mcpServers": {
    "arm_mcp_server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-v", "$HOME/workspace:/workspace",
        "--name", "arm-mcp",
        "armlimited/arm-mcp:latest"
      ],
      "env": {},
      "timeout": 60000
    }
  }
}
```

This configuration tells Gemini CLI to connect to the Arm MCP server running in the Docker container.

### How do I verify the Arm MCP server is working?

Start the Gemini CLI and list the tools from the MCP server to verify it's working:

```console
gemini
```

Use the `/tools` command to list the available tools:

```console
/tools
```

The Arm MCP server tools are listed in the output. If the arm-mcp server indicates it's still loading, wait a moment and run `/tools` again.

If you're facing issues or have questions, reach out to mcpserver@arm.com.

You're now ready to use Gemini CLI with the Arm MCP server for Arm-specific development assistance.