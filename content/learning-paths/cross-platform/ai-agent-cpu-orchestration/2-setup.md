---
title: Set up your environment before running the agent
description: Set up a Python virtual environment, Serper API key, required packages, and the concierge agent script before running the local AI agent on Arm.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install and configure prerequisites for the agent

Prepare the following before running the agent: a Serper API key for web search, a Python virtual environment, the required packages, and the agent script.

These steps are identical on an Apple silicon MacBook, an Arm Linux machine, and an NVIDIA DGX Spark.

### Create a project directory and virtual environment

A virtual environment keeps the agent's dependencies isolated from your system Python, so you always run against the right package versions.

Create and enter a project directory:

```bash
mkdir concierge-agent
cd concierge-agent
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Your shell prompt will now show `(.venv)`, which confirms the environment is active.

### Install the required packages

The agent uses `requests` for HTTP calls and `beautifulsoup4` to parse web pages.

Install the two packages:

```bash
pip install requests beautifulsoup4
```

## Set your Serper API key

The agent searches the web through [Serper](https://serper.dev/), a Google Search API. The free tier is enough to complete this Learning Path.

1. Go to [serper.dev](https://serper.dev/) and create a free account.
2. After logging in, you'll see the dashboard. On the left, select **API Keys**.
3. Copy the Default key.
4. Export your API key as an environment variable in the same terminal session as your virtual environment:

    ```bash
    export SERPER_API_KEY="your-serper-api-key"
    ```

{{% notice Tip %}}
This variable only lasts for the current terminal session. To keep it across sessions, add the same line to your shell profile, for example `~/.zshrc` on macOS or `~/.bashrc` on Linux.
{{% /notice %}}

### Download the agent script

Download the complete agent script <a href="/learning-paths/cross-platform/ai-agent-cpu-orchestration/concierge_agent.py" download>concierge_agent.py</a>, and move it into your `concierge-agent` directory.

Alternatively, download it directly from the command line:

```bash
curl -O https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/cross-platform/ai-agent-cpu-orchestration/concierge_agent.py
```

Confirm the file is in your project directory:

```bash
ls concierge_agent.py
```

## What you've accomplished and what's next

You've now obtained and set a Serper API key, created a virtual environment, and downloaded the agent script. 

Next, you'll serve the model locally with Ollama.
