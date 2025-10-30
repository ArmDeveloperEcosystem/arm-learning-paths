---
title: Install CircleCI CLI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install CircleCI CLI on GCP VM
This guide explains how to install the **CircleCI Command Line Interface (CLI)** on a **GCP SUSE Arm64 virtual machine**.  
The CLI allows you to interact with CircleCI directly from your terminal, such as to validate configuration files, run jobs locally, or manage runners.

### Install Required Packages

Add OpenSUSE Leap repository:
```bash
sudo zypper addrepo https://download.opensuse.org/distribution/leap/15.5/repo/oss/ openSUSE-Leap-15.5-OSS
```

Refresh repositories:
```bash
sudo zypper refresh
```
# Install git
Before installing the CircleCI CLI, make sure your system has the basic tools required for downloading and extracting files.

```console
sudo zypper install curl tar gzip coreutils gpg git-core
```

## Download and Extract the CircleCI CLI
Now download the CircleCI CLI binary for Linux Arm64 and extract it.

```console
curl -fLSs https://github.com/CircleCI-Public/circleci-cli/releases/download/v0.1.33494/circleci-cli_0.1.33494_linux_arm64.tar.gz | tar xz
sudo mv circleci-cli_0.1.33494_linux_arm64/circleci /usr/local/bin/
```
- The `curl` command downloads the `.tar.gz` archive from the official CircleCI GitHub release page.
- The `| tar xz` part extracts the downloaded file directly without saving it separately.
- After extraction, you’ll see a new folder named `circleci-cli_0.1.33494_linux_arm64` in your current directory.

### Verify the Installation
Finally, verify that the CLI is installed correctly by checking its version.

```console
circleci version
```
You should see an output similar to:
```output
0.1.33494+7cc6570 (release)
```
If you see similar version output, the installation was successful!
