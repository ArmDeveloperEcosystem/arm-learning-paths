---
title: Install Gemini CLI
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you install Gemini CLI on macOS or Arm Linux and verify that it is working.

Gemini CLI is Google’s command-line interface for interacting with the Gemini AI assistant from your terminal.

## Before you begin

To use Gemini CLI, you need:

- A Google account
- An authentication method for Gemini (OAuth login is recommended for most users)
- Node.js 20 or later (Gemini CLI runs on Node.js)

## Set up authentication

Gemini CLI supports multiple authentication methods. Choose one option.

### Option 1: Google OAuth login

This is the simplest option for most users.

After you install Gemini CLI, run:

```console
gemini
```

When prompted, select **Login with Google** and complete authentication in your browser.

### Option 2: Gemini API key

If you prefer using an API key (for example, in scripts or CI), generate one in Google AI Studio:

1. Go to https://aistudio.google.com/apikey
2. Sign in with your Google account
3. Select **Create API Key**
4. Copy the generated key

Set the key as an environment variable:

```console
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Option 3: Vertex AI (enterprise)

If you use Gemini through Vertex AI, set these environment variables:

```console
export GOOGLE_API_KEY="YOUR_GOOGLE_CLOUD_API_KEY"
export GOOGLE_GENAI_USE_VERTEXAI=true
```

## Install Gemini CLI on macOS

You can install Gemini CLI on macOS using Homebrew or npm.

### Install using Homebrew

If you do not have Homebrew installed, see https://brew.sh/.

Install Gemini CLI:

```console
brew install gemini-cli
```

### Install using npm

If you prefer npm, install Gemini CLI globally.

1. Install Node.js 20 or later:

```console
brew install node
```

2. Verify your Node.js version:

```console
node --version
```

3. Install Gemini CLI:

```console
npm install -g @google/gemini-cli
```

## Install Gemini CLI on Arm Linux

This section uses Ubuntu or Debian as the example. For other distributions, use the equivalent package manager.

## Install prerequisites

Install `curl`:

```console
sudo apt update
sudo apt install -y curl
```

### Install Node.js 20 or later

Use the NodeSource setup script:

```console
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

Verify Node.js and npm:

```console
node --version
npm --version
```

### Install Gemini CLI

Install Gemini CLI globally:

```console
sudo npm install -g @google/gemini-cli
```

## Verify the installation

Confirm that the CLI is available:

```console
gemini --version
```

Start an interactive session:

```console
gemini
```

On first run, you are prompted to authenticate if you have not already done so.

## View available CLI options

To print the available commands and options, use:

```console
gemini --help
```

## What you have accomplished and what is next

You have installed Gemini CLI and verified that it runs on your system.

Next, you can configure Gemini CLI with persistent context for Arm development workflows, and optionally integrate additional tooling such as an MCP server.
