---
additional_search_terms: null
layout: installtoolsall
minutes_to_complete: 5
multi_install: false
multitool_install_part: false
official_docs: https://cloud.google.com/sdk/docs/install-sdk
test_images:
- ubuntu:latest
test_maintenance: false
title: Google Cloud CLI (gcloud)
tool_install: true
weight: 1
---

The Google Cloud CLI allows you to run commands in your Google Cloud account.

`gcloud` is available for Windows, macOS, Linux and supports the Arm architecture. 

## Introduction

Use the documentation link to find alternative installation options. 

This article provides a quick solution to install `gcloud` for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash { command_line="user@localhost | 2" }
uname -m
aarch64
```

## Download and Install

The easiest way to install `gcloud` for Ubuntu on Arm is to use the package manager.

Download and install the required software packages.

```bash { target="ubuntu:latest" }
sudo apt-get install -y curl apt-transport-https ca-certificates gnupg
```

Install `gcloud` from the Google repository. 

```bash { target="ubuntu:latest" }
echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install google-cloud-cli -y
```

Confirm the executable is available.

```bash { target="ubuntu:latest" }
gcloud -v
```

The output should be similar to:

```console
Google Cloud SDK 418.0.0
alpha 2023.02.13
beta 2023.02.13
bq 2.0.85
bundled-python3-unix 3.9.16
core 2023.02.13
gcloud-crc32c 1.0.0
gsutil 5.20
```
