---
title: Amazon Q Developer CLI

author: Jason Andrews
minutes_to_complete: 10
official_docs: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line.html

test_maintenance: true
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

Amazon Q Developer CLI is a command-line tool for Amazon Q, a generative AI-powered assistant. You can use it to ask questions about AWS architecture, resources, and general development tasks. 

It supports multiple operating systems, including Arm-based Linux distributions and macOS, supports the Arm architecture, and you can install it in several ways.

## What should I do before installing Amazon Q Developer CLI?

You need a Builder ID to use the Amazon Q Developer CLI. If you don't have one, visit [Do more with AWS Builder ID](https://community.aws/builderid) and click **Sign up with Builder ID** to create your AWS Builder ID. 

This guide explains how to install Amazon Q Developer CLI on macOS and Arm Linux.

## How do I download and install Amazon Q Developer CLI?

The CLI is invoked using the `q` command. 

### How do I install Amazon Q Developer CLI on macOS?

Install [Homebrew](https://brew.sh/) if it's not already available on your computer.

Then install the Q CLI:

```console
brew install amazon-q
```

### How do I install the Q CLI on Arm Linux?

The easiest way to install the Q CLI on any Arm Linux distribution is to download and run the installer. 

Before starting, ensure that `curl` and `unzip` are available on your computer. 

{{% notice Note %}}
For Debian-based distributions such as Ubuntu, use the commands below. For other Linux distributions, use the appropriate package manager to install `curl` and `unzip`.
{{% /notice %}} 

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install curl unzip -y
```

Download the zip file with `curl`:

```bash { target="ubuntu:latest" }
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.codewhisperer.us-east-1.amazonaws.com/latest/q-aarch64-linux.zip" -o "q.zip"
```

Extract the installer and run it:

```console
unzip q.zip
bash ./q/install.sh
```

You'll then be prompted about updating your shell config:

```output
✔ Do you want q to modify your shell config (you will have to manually do this otherwise)? 
```

To automate the install, add the `--no-confirm` flag to the `install.sh` command. 

{{% notice Note %}}
If you're using a Linux distribution with an older version of the GNU C Library - or one that does not use it at all, such as Alpine - you can download an alternative package built with the musl C library and has no external dependencies. 

Substitute the `curl` command above with this one and use the same install instructions:

```bash { target="ubuntu:latest" }
curl "https://desktop-release.codewhisperer.us-east-1.amazonaws.com/latest/q-aarch64-linux-musl.zip" -o "q.zip"
```

{{% /notice %}}

### How do I confirm the Q CLI is working?

You now have the latest version of the Amazon Q Developer CLI installed. 

Confirm the CLI is available by invoking the `q` command to print the version.

```console
q version
```

The version is printed:

```output
q 1.10.1
```

## How can I configure my AWS account to get the most from the Q CLI?

The Q CLI can answer questions and solve problems related to your AWS resources and help you develop faster on AWS. To get the maximum benefit, you can configure the AWS CLI to use your account. 

Follow the [AWS CLI Install Guide](/install-guides/aws_access_keys/) and the [AWS Credentials Install Guide](/install-guides/aws_access_keys/) to set up the AWS CLI and generate and configure access keys. 

This allows you to use the Amazon Q Developer CLI to ask questions and solve issues specific to your AWS account. 

## What is an example of using the Q CLI? 

You can use `q chat` to find information about your AWS resources. 

```console
q chat
```

When the chat session starts you see:

```output
To learn more about MCP safety, see https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-mcp-security.html



    ⢠⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣶⣦⡀⠀
 ⠀⠀⠀⣾⡿⢻⣿⡆⠀⠀⠀⢀⣄⡄⢀⣠⣤⣤⡀⢀⣠⣤⣤⡀⠀⠀⢀⣠⣤⣤⣤⣄⠀⠀⢀⣤⣤⣤⣤⣤⣤⡀⠀⠀⣀⣤⣤⣤⣀⠀⠀⠀⢠⣤⡀⣀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠋⠀⠀⠀⠙⣿⣿⡆
 ⠀⠀⣼⣿⠇⠀⣿⣿⡄⠀⠀⢸⣿⣿⠛⠉⠻⣿⣿⠛⠉⠛⣿⣿⠀⠀⠘⠛⠉⠉⠻⣿⣧⠀⠈⠛⠛⠛⣻⣿⡿⠀⢀⣾⣿⠛⠉⠻⣿⣷⡀⠀⢸⣿⡟⠛⠉⢻⣿⣷⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⢸⣿⣿
 ⠀⢰⣿⣿⣤⣤⣼⣿⣷⠀⠀⢸⣿⣿⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⠀⠀⢀⣴⣶⣶⣶⣿⣿⠀⠀⠀⣠⣾⡿⠋⠀⠀⢸⣿⣿⠀⠀⠀⣿⣿⡇⠀⢸⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⢸⣿⡿
 ⢀⣿⣿⠋⠉⠉⠉⢻⣿⣇⠀⢸⣿⣿⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⠀⠀⣿⣿⡀⠀⣠⣿⣿⠀⢀⣴⣿⣋⣀⣀⣀⡀⠘⣿⣿⣄⣀⣠⣿⣿⠃⠀⢸⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣀⣀⣀⣴⣿⡿⠃
 ⠚⠛⠋⠀⠀⠀⠀⠘⠛⠛⠀⠘⠛⠛⠀⠀⠀⠛⠛⠀⠀⠀⠛⠛⠀⠀⠙⠻⠿⠟⠋⠛⠛⠀⠘⠛⠛⠛⠛⠛⠛⠃⠀⠈⠛⠿⠿⠿⠛⠁⠀⠀⠘⠛⠃⠀⠀⠘⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣿⣿⣋⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⡧

╭─────────────────────────────── Did you know? ────────────────────────────────╮
│                                                                              │
│     You can resume the last conversation from your current directory by      │
│                        launching with q chat --resume                        │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

/help all commands  •  ctrl + j new lines  •  ctrl + s fuzzy search
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
```

For example, you can ask for the IP address of an EC2 instance instead of going to the AWS console or looking up the AWS CLI command to get it. 

An example is shown below:

![Connect #center](/install-guides/_images/q.gif)

## How can I set the Q CLI context to tailor responses? 

The Q CLI reads your context when you start it. If you provide more information about yourself, you will get tailored responses that match your development environment.

There are multiple options to store context.

Use the `/context` command to see the possible locations to store your context.

```console
/context show
```

The help information is printed.

```output

🌍 global:
    .amazonq/rules/**/*.md 
    README.md 
    AmazonQ.md 

👤 profile (default):
    <none>

No files in the current directory matched the rules above.
```

For example, you can create a new file to store your context.

```console
mkdir -p ~/.amazonq/rules/context
echo "I am an Arm Linux developer. I prefer Ubuntu and other Debian based distributions. I don't use any x86 computers so please provide all information assuming I'm working on Arm Linux. Sometimes I use macOS and Windows on Arm, but please only provide information about these operating systems when I ask for it." > ~/.amazonq/rules/context/context.md
```

When you invoke `q chat` you can confirm your context information was read by asking. 

```console
did you read my context information?
```

The response confirms the context file was read:

```output
Yes, I've read your context information. I understand that you're an Arm Linux developer who primarily 
uses Ubuntu and other Debian-based distributions. You don't use x86 computers, so I'll provide all 
information assuming you're working on Arm Linux. You occasionally use macOS and Windows on Arm, but I'
ll only provide information about those operating systems when you specifically ask for it.

I'll tailor my responses to be relevant for Arm Linux development, particularly focusing on Debian-
based distributions like Ubuntu, which is your preference.
```

Give it a try by asking questions like "How do I install the AWS CLI?" and verify that the answers match the provided context.

## How do I change the model Amazon Q uses?

When you start `q chat` the model is printed:

```output
🤖 You are chatting with claude-3.7-sonnet
```

You can use the `/model` command to list other available models.

```console
/model
```

The model options are displayed:

```output
? Select a model for this chat session ›
❯ claude-4-sonnet
  claude-3.7-sonnet (active)
  claude-3.5-sonnet
```

Use the arrow keys and select the model you want to use. 

You can ask Amazon Q to set the default model for future sessions.

## Install an MCP server

As an example of using MCP with Amazon Q, you can configure a local Github MCP server. 

Go to your GitHub account developer settings and create a personal access token with the following permissions:

- repo (Full control of private repositories)
- read:org (Read organization membership)
- read:user (Read user profile data)


Use an editor to add the content below to the file `$HOME/.amazonq/mcp.json`

```console
{
    "mcpServers": {
      "github": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "-e",
          "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"
        ],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "<your-github-pat>"
        }
      }
    }
}
```

Replace `<your-github-pat>` with your GitHub token.

You also need Docker running on the system. Refer to the [Docker install guide](/install-guides/docker/) for instructions. 

Restart `q` with the new MCP configuration:

```console
q chat
```

You see the GitHub MCP server loaded and running:

```output
✓ github loaded in 0.14 s
✓ 1 of 1 mcp servers initialized.

    ⢠⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣶⣦⡀⠀
 ⠀⠀⠀⣾⡿⢻⣿⡆⠀⠀⠀⢀⣄⡄⢀⣠⣤⣤⡀⢀⣠⣤⣤⡀⠀⠀⢀⣠⣤⣤⣤⣄⠀⠀⢀⣤⣤⣤⣤⣤⣤⡀⠀⠀⣀⣤⣤⣤⣀⠀⠀⠀⢠⣤⡀⣀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠋⠀⠀⠀⠙⣿⣿⡆
 ⠀⠀⣼⣿⠇⠀⣿⣿⡄⠀⠀⢸⣿⣿⠛⠉⠻⣿⣿⠛⠉⠛⣿⣿⠀⠀⠘⠛⠉⠉⠻⣿⣧⠀⠈⠛⠛⠛⣻⣿⡿⠀⢀⣾⣿⠛⠉⠻⣿⣷⡀⠀⢸⣿⡟⠛⠉⢻⣿⣷⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⢸⣿⣿
 ⠀⢰⣿⣿⣤⣤⣼⣿⣷⠀⠀⢸⣿⣿⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⠀⠀⢀⣴⣶⣶⣶⣿⣿⠀⠀⠀⣠⣾⡿⠋⠀⠀⢸⣿⣿⠀⠀⠀⣿⣿⡇⠀⢸⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⢸⣿⡿
 ⢀⣿⣿⠋⠉⠉⠉⢻⣿⣇⠀⢸⣿⣿⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⠀⠀⣿⣿⡀⠀⣠⣿⣿⠀⢀⣴⣿⣋⣀⣀⣀⡀⠘⣿⣿⣄⣀⣠⣿⣿⠃⠀⢸⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣀⣀⣀⣴⣿⡿⠃
 ⠚⠛⠋⠀⠀⠀⠀⠘⠛⠛⠀⠘⠛⠛⠀⠀⠀⠛⠛⠀⠀⠀⠛⠛⠀⠀⠙⠻⠿⠟⠋⠛⠛⠀⠘⠛⠛⠛⠛⠛⠛⠃⠀⠈⠛⠿⠿⠿⠛⠁⠀⠀⠘⠛⠃⠀⠀⠘⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣿⣿⣋⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⡧

╭─────────────────────────────── Did you know? ────────────────────────────────╮
│                                                                              │
│      You can execute bash commands by typing ! followed by the command       │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

/help all commands  •  ctrl + j new lines  •  ctrl + s fuzzy search
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
```

You can now use the GitHub MCP server to interact with GitHub repositories and do things like:

**Repository Management**
- Create new repositories
- Fork existing repositories
- List branches and tags
- Create new branches

**Code Management**
- Get file contents from repositories
- Create or update files
- Delete files
- Push multiple files in a single commit
- Search code across repositories

**Pull Requests**
- Create pull requests
- List pull requests
- Get pull request details
- Update pull requests
- Merge pull requests
- Review pull requests
- Request GitHub Copilot reviews
- Get pull request files and comments

**Issues**
- Create issues
- List issues
- Get issue details
- Update issues
- Add comments to issues
- Search issues

**Commits**
- List commits
- Get commit details

You're ready to use the Q CLI.
