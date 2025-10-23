---
title: Install CircleCI CLI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install CircleCI CLI on AWS Graviton2 (Neoverse N1) Instance
This guide explains installing the **CircleCI Command Line Interface (CLI)** on an **AWS Graviton2 (Neoverse N1) Arm64 EC2 instance**.  
The CLI enables you to interact with CircleCI directly from your terminal — for validating configuration files, managing pipelines, and operating self-hosted runners on your EC2 instance.

### Install Required Packages
Before installing the CircleCI CLI, ensure your system has the necessary tools for downloading and extracting files.

```console
sudo apt update && sudo apt install -y curl tar gzip coreutils gpg git
```
### Download and Extract the CircleCI CLI

Next, download the CircleCI CLI binary for **Linux arm64** and extract it.

```console
curl -fLSs https://github.com/CircleCI-Public/circleci-cli/releases/download/v0.1.33494/circleci-cli_0.1.33494_linux_arm64.tar.gz | tar xz
sudo mv circleci-cli_0.1.33494_linux_arm64/circleci /usr/local/bin/
```
- The `curl` command fetches the official **CircleCI CLI archive** from GitHub.  
- The `| tar xz` command extracts the compressed binary in a single step.  
- After extraction, a new folder named **`circleci-cli_0.1.33494_linux_arm64`** appears in your current directory.

### Verify the Installation

To ensure that the CLI is installed successfully, check its version:

```console
circleci version
```
You should see an output similar to:

```output
0.1.33494+7cc6570 (release)
```

If this version number appears, the CircleCI CLI installation on your AWS Graviton2 instance was successful!
