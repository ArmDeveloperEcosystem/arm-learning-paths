---
title: Install CircleCI CLI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install CircleCI CLI on AWS Graviton2 (Neoverse N1) instance
This guide walks you through how to install the CircleCI command line interface (CLI). With the CLI, you can work with CircleCI from your terminal to check configuration files, manage pipelines, and run self-hosted runners on your EC2 instance.

## Install the required packages
Before installing the CircleCI CLI, ensure your system has the necessary tools for downloading and extracting files:

```console
sudo apt update && sudo apt install -y curl tar gzip coreutils gpg git
```
## Download and extract the CircleCI CLI

Next, download the CircleCI CLI binary for Linux arm64 and extract it:

```console
curl -fLSs https://github.com/CircleCI-Public/circleci-cli/releases/download/v0.1.33494/circleci-cli_0.1.33494_linux_arm64.tar.gz | tar xz
sudo mv circleci-cli_0.1.33494_linux_arm64/circleci /usr/local/bin/
```
- The `curl` command fetches the official CircleCI CLI archive from GitHub.  
- The `| tar xz` command extracts the compressed binary in a single step.  
- After extraction, a new folder named `circleci-cli_0.1.33494_linux_arm64` appears in your current directory.

## Verify the installation

To ensure that the CLI is installed successfully, check its version:

```console
circleci version
```
The first time this runs, an interactive shell might open. For now, press `Ctrl+C` to abort. You should now see an output similar to:

```output
0.1.33494+7cc6570 (release)
```

If this version number appears, the CircleCI CLI installation on your AWS Graviton instance was successful!
