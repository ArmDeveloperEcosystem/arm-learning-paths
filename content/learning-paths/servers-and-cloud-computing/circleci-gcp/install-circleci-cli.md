---
title: Install CircleCI CLI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install CircleCI CLI on GCP VM
This section explains how to install the CircleCI Command Line Interface (CLI) on a SUSE Linux (Arm64) virtual machine running on Google Cloud C4A (Axion). The CLI allows you to interact with CircleCI directly from your terminal, to validate configuration files, run jobs locally, or manage runners.

### Install Required Packages

Before installing the CLI, make sure your SUSE environment has the necessary repositories and development tools. Add the openSUSE Leap repository:

```bash
sudo zypper addrepo https://download.opensuse.org/distribution/leap/15.5/repo/oss/ openSUSE-Leap-15.5-OSS
```

Refresh package repositories:
```bash
sudo zypper refresh
```
This updates the local metadata so that zypper recognizes the latest available packages and dependencies.

# Install git
Before installing the CircleCI CLI, make sure your system has the basic tools required for downloading and extracting files.

```console
sudo zypper install -y curl tar gzip coreutils gpg git-core
```
Once Git and the required tools are installed, you’re ready to download and configure the CircleCI CLI binary for Arm64.

## Download and Extract the CircleCI CLI
Download the CircleCI CLI binary for Linux Arm64 and extract it.

```console
curl -fLSs https://github.com/CircleCI-Public/circleci-cli/releases/download/v0.1.33494/circleci-cli_0.1.33494_linux_arm64.tar.gz | tar xz
sudo mv circleci-cli_0.1.33494_linux_arm64/circleci /usr/local/bin/
```
Explanation of the commands:

- The `curl` command downloads the `.tar.gz` archive from the official CircleCI GitHub release page.
- The `| tar xz` part extracts the downloaded file directly without saving it separately.

After extraction, you’ll see a new folder named `circleci-cli_0.1.33494_linux_arm64` in your current directory.

### Verify the Installation
Check that the CircleCI CLI is installed and executable:

```console
circleci version
```
You should see output similar to:
```output
0.1.33494+7cc6570 (release)
```
The CircleCI CLI is now installed and running natively on your SUSE Arm64 VM (Google Cloud C4A).
