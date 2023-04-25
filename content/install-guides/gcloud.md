---
additional_search_terms: 
- cloud
layout: installtoolsall
minutes_to_complete: 5
author_primary: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://cloud.google.com/sdk/docs/install-sdk
test_images:
- ubuntu:latest
test_maintenance: false
title: Google Cloud CLI 
tool_install: true
weight: 1
---

The Google Cloud CLI, `gcloud`, allows you to run commands in your Google Cloud account.

`gcloud` is available for Windows, macOS, Linux and supports the Arm architecture. 

## Introduction

Use the documentation link to find alternative installation options. 

This article provides a quick solution to install `gcloud` for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

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

```output
Google Cloud SDK 418.0.0
alpha 2023.02.13
beta 2023.02.13
bq 2.0.85
bundled-python3-unix 3.9.16
core 2023.02.13
gcloud-crc32c 1.0.0
gsutil 5.20
```

## Acquire user credentials

In this section you will learn how to obtain user access credentials for Google Cloud using a web flow. You will put the credentials in a well-known location for Application Default Credentials (`ADC`).

Run the following command to obtain user access credentials:
```console
gcloud auth application-default login
```
A URL is generated as the output of the command:

![image #center](https://user-images.githubusercontent.com/67620689/204504640-c49c0b0d-6a59-4915-ac3a-f03614783d98.PNG)

Open the URL in the browser and copy the authentication code.

![image #center](https://user-images.githubusercontent.com/67620689/204244780-6c0542ab-4240-4be3-8272-fb1e6e38ec08.PNG)

Now paste the authentication code as shown below:

![image #center](https://user-images.githubusercontent.com/67620689/204242841-58e30570-1f88-4755-b3d2-32d7052a9b5d.PNG)

After a successful log in, you will be able to use the `Google Cloud CLI` and automation tools like [Terraform](../terraform) from the terminal.
