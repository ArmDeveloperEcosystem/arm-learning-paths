---
title: Set-up Buildkite
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Buildkite Agent Setup 
This guide describes the steps to configure a Buildkite agent and queue after installing the Buildkite agent binary on a Google Axion C4A Arm VM.

## 1. Create an Agent Token

Before configuring the agent, you need an agent token from your Buildkite organization.

1. Log in to your **Buildkite** account (you can login with GitHub), and go to your **Organization Settings**.  
2. Click **Agents** in the left menu.
3. Click **Create Agent Token**.  
4. Enter a **name** for your token, e.g., `buildkite-arm`.  
5. Click **Create Token**.  
6. **Copy the token** immediately – you won’t be able to see it again after leaving the page.

![Buildkite Dashboard alt-text#center](images/agent-token.png "Figure 1: Create Buildkite agent Token")


## 2. Configure Buildkite Agent

Create the configuration directory and file on your local system:

```console
sudo tee /root/.buildkite-agent/buildkite-agent.cfg > /dev/null <<EOF
token="YOUR_AGENT_TOKEN"
tags="queue=buildkite-queue1"
EOF
```
- Replace `YOUR_AGENT_TOKEN` with the token you generated from your **Buildkite Agents page**.  
- `tags` in Buildkite are key-value labels that let you match pipeline steps to specific agents, ensuring jobs run only on agents with the required tag.
- The `name` field is optional; if omitted, Buildkite will assign a default name.


Verify the configuration:

```console
sudo cat /root/.buildkite-agent/buildkite-agent.cfg
```
You should see output similar to:

```output
# The token from your Buildkite "Agents" page
token="YOUR-GENERATED-TOKEN-VALUE"
tags="queue=buildkite-queue1"

# The name of the agent
name="%hostname-%spawn"

# The number of agents to spawn in parallel (default is "1")
# spawn=1

# The priority of the agent (higher priorities are assigned work first)
# priority=1
```
## 3. Create a Queue in Buildkite

1. Go to your **Buildkite Organization → Queues → Create Queue**.  
2. Name it: `buildkite-queue1`.  
3. Save it.  

{{% notice Note %}}Make sure the queue name matches the `tags` field in the agent configuration.{{% /notice %}}

![Buildkite Dashboard alt-text#center](images/queue.png "Figure 2: Create Buildkite Queue")

## 4. Verify Agent in Buildkite UI

First, you need to run locally:

```console
sudo /root/.buildkite-agent/bin/buildkite-agent start
```

Then, Verify by UI:

Go to **Buildkite → Agents.**

Confirm that the agent is online and connected to the queue buildkite-queue1.

![Buildkite Dashboard alt-text#center](images/agent.png "Figure 3: Verify Agent")

Buildkite-agent setup is complete, you can now proceed with the multi-arch build using Buildkite.
