---
title: Install CircleCI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This section walks you through how to install the CircleCI Command Line Interface (CLI) on a SUSE Linux (Arm64) virtual machine running on Google Cloud C4A (Axion). The CLI allows you to interact with CircleCI directly from your terminal, to validate configuration files, run jobs locally, or manage runners.

## Install dependencies

Before installing the CLI, make sure your SUSE environment has the right repositories and development tools.

First, add the openSUSE Leap repository. This step ensures you can access the latest packages for your system:

```console
sudo zypper addrepo https://download.opensuse.org/distribution/leap/15.5/repo/oss/ openSUSE-Leap-15.5-OSS
```

Next, refresh your package list so zypper recognizes the newest packages and dependencies:

```console
sudo zypper refresh
```

You may be prompted to trust or reject a key... if so please press "t" to accept/trust the key. 

Now your system is ready to install the required tools for the CircleCI CLI.

## Install Git and required tools

To prepare your SUSE Linux (Arm64) VM for the CircleCI CLI, install Git and essential utilities for downloading and extracting files:

```console
sudo zypper install -y curl tar gzip coreutils gpg git-core
```

After installing these tools, your environment is ready to download and set up the CircleCI CLI binary for Arm64.

## Download and extract the CircleCI CLI

Download the CircleCI CLI binary for Linux Arm64, then extract and move it to your system path.

First, run the following command to download and extract the CLI in one step:

```console
curl -fLSs https://github.com/CircleCI-Public/circleci-cli/releases/download/v0.1.33494/circleci-cli_0.1.33494_linux_arm64.tar.gz | tar xz
```

This command downloads the official CircleCI CLI archive and extracts its contents into your current directory.

Next, move the CLI binary to a directory in your system path so you can run it from anywhere:

```console
sudo mv circleci-cli_0.1.33494_linux_arm64/circleci /usr/local/bin/
```

After running these commands, you’ll see a new folder called `circleci-cli_0.1.33494_linux_arm64` in your directory. The CLI is now ready to use.

## Verify the Installation
Check that the CircleCI CLI is installed and executable:

```console
circleci version
```
You should see output similar to:
```output
0.1.33494+7cc6570 (release)
```
The CircleCI CLI is now installed and running natively on your SUSE Arm64 VM (Google Cloud C4A).
