---
title: Prepare your local machine for Agent Sandbox on GKE
description: Prepare the required tools on Ubuntu Linux or macOS used to manage remote GKE sandboxes.
weight: 2
layout: learningpathall
---

## Run agent-generated code in an isolated remote sandbox

Coding agents can write useful programs, but running agent-generated code on your local machine gives untrusted code direct access to your files, credentials, and network. Agent Sandbox on Google Kubernetes Engine (GKE) is purpose-built for this problem: it executes untrusted, model-generated code in a secure, isolated environment away from your local machine. Each sandbox Pod runs under gVisor, which places a user-space application kernel between the workload and the host kernel. Agent Sandbox applies a default-deny network posture to sandboxed workloads.

To use agent sandboxes, you can create a Google Kubernetes Engine (GKE) Standard cluster and enable Agent Sandbox on a Google Axion node pool. 

You'll create a cluster with a pool of pre-warmed sandboxes. When you need to run code, you'll allocate a sandbox from the pool and submit your code to it from your local machine.

Your agent and your terminal stay on your local machine, and the generated code runs remotely.

## Set up your local machine

Your local machine manages the Kubernetes resources. The Python workloads run on the remote Arm node. You don't need local Docker, KVM, or a local gVisor installation.

Use Ubuntu Linux or macOS. The examples were tested on an Arm Linux system and on macOS.

### Install the required tools

Install the Google Cloud CLI (with `gke-gcloud-auth-plugin`) and Python 3.

The Google Cloud CLI provisions and manages the GKE cluster and authenticates kubectl. Python 3 runs the helper scripts used on later pages.

#### Ubuntu Linux

On Ubuntu Linux, add the Google Cloud APT repository and install the packages:

```bash
sudo apt-get update
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg -o /tmp/gke-cloud-apt-key.gpg
sudo gpg --dearmor --yes --output /usr/share/keyrings/cloud.google.gpg /tmp/gke-cloud-apt-key.gpg
printf '%s\n' 'deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main' \
  | sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update
sudo apt-get install -y google-cloud-cli google-cloud-cli-gke-gcloud-auth-plugin python3 python3-venv jq
```

#### macOS

On macOS, install [Homebrew](https://brew.sh/) if needed, then install the Cloud CLI, its authentication plugin, and Python:

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
brew update
brew install --cask gcloud-cli
brew install python jq
export PATH="$(brew --prefix)/share/google-cloud-sdk/bin:$PATH"
gcloud components install beta gke-gcloud-auth-plugin
```

### Authenticate and confirm the tools are ready

Find your project ID on the front page of the Google Cloud console. Set the `PROJECT_ID` environment variable and sign in:

```bash
export PROJECT_ID="REPLACE_WITH_YOUR_PROJECT_ID"
gcloud auth login
gcloud config set project "$PROJECT_ID"
gcloud projects describe "$PROJECT_ID" --format='value(projectId)'
command -v gcloud gke-gcloud-auth-plugin python3
gcloud beta container clusters update --help 2>/dev/null | grep -q enable-agent-sandbox \
  && echo "enable-agent-sandbox flag: present" \
  || echo "enable-agent-sandbox flag: NOT FOUND — upgrade the Cloud CLI"
```

The final command in the set checks that your Cloud CLI version supports Agent Sandbox. If it reports `NOT FOUND`, upgrade the CLI before continuing.

If you don't have a browser available, use `gcloud auth login --no-launch-browser` and follow the instructions.

### Create a working directory

Create a working directory and set `LP_WORKDIR`. You can use `LP_WORKDIR` to return to this directory:

```bash
mkdir -p ~/gke-agent-sandbox
cd ~/gke-agent-sandbox
export LP_WORKDIR="$PWD"
mkdir -p output runs
```

`output/` stores command output you save for reference, such as cluster configuration, pod specs, and workload results. `runs/` holds per-task subdirectories created by the helper scripts, one for each sandbox claim lifecycle.

If you want to be able to restore your session in a new terminal, save `LP_WORKDIR` and `PROJECT_ID` to a file called `env.sh`:

```bash
cat > "$LP_WORKDIR/env.sh" << EOF
export LP_WORKDIR="$LP_WORKDIR"
export PROJECT_ID="$PROJECT_ID"
EOF
```
You can skip this step and manage the variables yourself if you prefer to use the same terminal throughout.

If you save the variables to `env.sh`, source them at the start of any new terminal with `source ~/gke-agent-sandbox/env.sh`.

## What you've accomplished and what's next

You've installed the Google Cloud CLI and Python, created the working directory, and confirmed the Cloud CLI supports Agent Sandbox. 

Next, you'll create the dedicated GKE cluster and its Arm sandbox node pool, then install the matching kubectl.
