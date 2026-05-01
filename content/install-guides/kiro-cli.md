---
title: Kiro CLI

author: Jason Andrews
minutes_to_complete: 10
official_docs: https://kiro.dev/docs/cli/

test_maintenance: true
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

Kiro CLI is a command-line tool powered by a generative AI assistant. You can use it to ask questions about AWS architecture, resources, and general development tasks. 

It supports multiple operating systems, including Arm-based Linux distributions and macOS, and you can install it in several ways.

## What should I do before installing Kiro CLI?

You need a Builder ID to use Kiro CLI. If you don't have one, visit [Do more with AWS Builder ID](https://community.aws/builderid) and select **Sign up with Builder ID** to create your AWS Builder ID.

This guide explains how to install Kiro CLI on macOS and Arm Linux.

## How do I download and install Kiro CLI?

The CLI is invoked using the `kiro-cli` command. 

The easiest way to install Kiro CLI on Linux and macOS is with a single command:

```console
curl -fsSL https://cli.kiro.dev/install | bash
```

### Can I use Homebrew to install Kiro CLI on macOS?

Yes, you can install [Homebrew](https://brew.sh/) if it's not already available on your computer.

Install Kiro CLI using Homebrew:

```console
brew install kiro-cli
```

### Can I install Kiro CLI on Arm Linux by downloading a ZIP file?

Yes, you can download and install Kiro CLI on any Arm Linux distribution using the installer.

Before starting, ensure that `curl` and `unzip` are available on your computer. 

{{% notice Note %}}
For Debian-based distributions such as Ubuntu, use the commands below. For other Linux distributions, use the appropriate package manager to install `curl` and `unzip`.
{{% /notice %}} 

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install curl unzip -y
```

Download the ZIP file with `curl`:

```bash { target="ubuntu:latest" }
curl --proto '=https' --tlsv1.2 -sSf 'https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-aarch64-linux.zip' -o 'kirocli.zip'
```

Extract the installer and run it:

```console
unzip kirocli.zip
bash ./kirocli/install.sh
```

The installer prompts you about updating your shell configuration:

```output
✔ Do you want kiro to modify your shell config (you will have to manually do this otherwise)? 
```

To automate the install, add the `--no-confirm` flag to the `install.sh` command. 

{{% notice Note %}}
If you're using a Linux distribution with an older version of the GNU C Library, or one that doesn't use it at all (such as Alpine), you can download an alternative package. This package is built with the musl C library and has no external dependencies. 

Substitute the `curl` command above with this one and use the same install instructions:

```bash { target="ubuntu:latest" }
curl --proto '=https' --tlsv1.2 -sSf 'https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-aarch64-linux-musl.zip' -o 'kirocli.zip'
```

{{% /notice %}}

### How do I confirm Kiro CLI is working?

You now have the latest version of Kiro CLI installed. 

Confirm the CLI is available by printing the version:

```console
kiro-cli version
```

The output shows the version:

```output
kiro-cli 1.28.1
```

## How can I configure my AWS account to get the most from Kiro CLI?

Kiro CLI can answer questions and solve problems related to your AWS resources and help you develop faster on AWS. To get the maximum benefit, you can configure the AWS CLI to use your account.

Follow the [AWS CLI Install Guide](/install-guides/aws-cli/) and the [AWS Credentials Install Guide](/install-guides/aws_access_keys/) to set up the AWS CLI and generate and configure access keys.

This allows you to use Kiro CLI to ask questions and solve issues specific to your AWS account.

For example, you can ask for the IP address of an EC2 instance instead of going to the AWS console or looking up the AWS CLI command to get it.

Kiro accesses your AWS resources and prints the information you ask for.

## How can I set the Kiro CLI context to tailor responses?

Kiro CLI can read your context. If you provide more information about yourself, you get tailored responses that match your development environment.

There are multiple options to store context.

Use the `/context` command to see the possible locations to store your context.

```console
/context show
```

The help information is printed.

```output

Agent (kiro_default)
  - AmazonQ.md (no matches)
  - AGENTS.md (no matches)
  - README.md (no matches)

Session (temporary)
  <none>

No files in the current directory matched the rules above.
```

For example, you can create a new file to store your context as shown below:

```console
echo "I am an Arm Linux developer. I prefer Ubuntu and other Debian based distributions. I don't use any x86 computers so please provide all information assuming I'm working on Arm Linux. Sometimes I use macOS and Windows on Arm, but please only provide information about these operating systems when I ask for it." > ~/.kiro/context.md
```

When you invoke `kiro-cli chat`, you can confirm your context information was read by loading it and asking about it.

Load the context file:

```console
/context add ~/.kiro/context.md
```

Confirm it was read:

```console
did you read my context information?
```

The response confirms the context file was read:

```output
Yes, I read your context information. You're an Arm Linux developer who prefers Ubuntu and other Debian-based
distributions, and you don't use x86 computers. You also sometimes use macOS and Windows on Arm, but only want
information about those when you specifically ask for them.
```

Ask questions like "How do I install the AWS CLI?" to verify that the answers match the provided context.

## How do I change the model Kiro uses?

When you start `kiro-cli chat`, the model is printed:

```output
Model: Auto (/model to change)
```

Use the `/model` command to list other available models:

```console
/model
```

The model options are displayed:

```output
 Press (↑↓) to navigate · Enter(⏎) to select model
❯ Auto (current) | 1x credit | Models chosen by task for optimal usage and consistent quality
  claude-sonnet-4.5 | 1.3x credit | The latest Claude Sonnet model
  claude-sonnet-4 | 1.3x credit | Hybrid reasoning and coding for regular use
  claude-haiku-4.5 | 0.4x credit | The latest Claude Haiku model
```

Use the arrow keys to select the model you want to use. 

You can ask Kiro to set the default model for future sessions.

## Install a local MCP server

The Arm MCP Server is an MCP server providing AI assistants with tools and knowledge for Arm architecture development, migration, and optimization. This section shows how to configure the Arm MCP server locally using Docker.

First, pull the MCP server image to your local machine:

```console
docker pull armlimited/arm-mcp:latest
```

You also need Docker running on the system. See the [Docker install guide](/install-guides/docker/) for instructions.

### How do I configure the Arm MCP server?

Modify the file `~/.kiro/settings/mcp.json` to add the Arm MCP server via a Docker container.

To analyze a local codebase, use a `-v` command to mount a volume to the Arm MCP server `/workspace` folder so it can access code you want to analyze with migrate-ease and other tools.

Replace the path `/path/to/your/workspace` with the path to your local codebase:

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
      "env": {},
      "timeout": 60000
    }
  }
}
```

To enable Arm Performix features through the Arm MCP Server, replace `/path/to/your/ssh/private_key` and `/path/to/your/ssh/known_hosts` with the SSH private key and `known_hosts` file used for your target device.

### Optional: Use a Docker replacement containerization tool

You can use other containerization tools besides Docker that are free and do not require licenses, such as Podman, Finch, Colima, and Rancher Desktop. Choose one of the options below and use its CLI in place of `docker`.

{{< tabpane-normal >}}
  {{< tab header="Podman" >}}
Install: [Podman](https://podman.io/docs/installation)

Pull the Arm MCP Server image:
```console
podman pull armlimited/arm-mcp:latest
```

Add the following configuration to the user-level `~/.kiro/settings/mcp.json` file:
```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "podman",
      "args": [
        "run",
        "--rm",
        "-i",
        "-v", "/Users/yourname01/yourlocalcodebase:/workspace",
        "--name", "arm-mcp",
        "armlimited/arm-mcp:latest"
      ],
      "env": {},
      "timeout": 60000
    }
  }
}
```
  {{< /tab >}}
  {{< tab header="Finch" >}}
Install: [Finch](https://runfinch.com/docs/getting-started/installation/)

Pull the Arm MCP Server image:
```console
finch pull armlimited/arm-mcp:latest
```

Add the following configuration to the user-level `~/.kiro/settings/mcp.json` file:
```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "finch",
      "args": [
        "run",
        "--rm",
        "-i",
        "-v", "/Users/yourname01/yourlocalcodebase:/workspace",
        "--name", "arm-mcp",
        "armlimited/arm-mcp:latest"
      ],
      "env": {},
      "timeout": 60000
    }
  }
}
```
  {{< /tab >}}
  {{< tab header="Colima" >}}
Install: [Colima](https://github.com/abiosoft/colima#installation)

Colima provides a Docker-compatible CLI via Docker contexts.

Pull the Arm MCP Server image:
```console
docker pull armlimited/arm-mcp:latest
```

Add the following configuration to the user-level `~/.kiro/settings/mcp.json` file:
```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-v", "/Users/yourname01/yourlocalcodebase:/workspace",
        "--name", "arm-mcp",
        "armlimited/arm-mcp:latest"
      ],
      "env": {},
      "timeout": 60000
    }
  }
}
```
  {{< /tab >}}
  {{< tab header="Rancher Desktop" >}}
Install: [Rancher Desktop](https://docs.rancherdesktop.io/getting-started/installation/)

Rancher Desktop uses the Docker container engine via Morby.

Pull the Arm MCP Server image:
```console
docker pull armlimited/arm-mcp:latest
```

Add the following configuration to the user-level `~/.kiro/settings/mcp.json` file:
```json
{
  "mcpServers": {
    "arm_mcp_server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-v", "/Users/yourname01/yourlocalcodebase:/workspace",
        "--name", "arm-mcp",
        "armlimited/arm-mcp:latest"
      ],
      "env": {},
      "timeout": 60000
    }
  }
}
```
  {{< /tab >}}
{{< /tabpane-normal >}}

### How do I verify the Arm MCP server is working?

Start Kiro CLI chat from your local shell and list the tools from the MCP server to verify it is working:

```console
kiro-cli chat
```

Use the `/tools` command to list the available tools:

```console
/tools
```

You should see the Arm MCP server tools listed in the output. If the arm-mcp server says it's still loading, wait a moment and run `/tools` again.

### Use Arm prompt files with the MCP Server

The Arm MCP Server provides a rich set of tools and knowledge base, but to make the best use of it, you should pair it with Arm-specific prompt files. These prompt files supply task-oriented context, best practices, and structured workflows that guide the agent in using MCP tools more effectively across common Arm development tasks.

#### Get the prompt files

Browse the [agent integrations directory for Kiro](https://github.com/arm/mcp/tree/main/agent-integrations/kiro) to find prompt files for specific use cases:

- **Arm migration** ([arm-migration.md](https://github.com/arm/mcp/blob/main/agent-integrations/kiro/arm-migration.md)): Helps the agent systematically migrate applications from x86 to Arm, including dependency analysis, compatibility checks, and optimization recommendations.

Each prompt file is a Markdown configuration that you can reference in your Kiro CLI sessions to enable more targeted, task-specific assistance.

If you're facing issues or have questions, reach out to mcpserver@arm.com.

You're now ready to use Kiro CLI with the Arm MCP server for Arm-specific development assistance.
