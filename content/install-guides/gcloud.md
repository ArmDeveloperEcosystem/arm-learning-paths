---
additional_search_terms: 
- cloud
- google cloud
- google
- gcloud


layout: installtoolsall
minutes_to_complete: 5
author_primary: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://cloud.google.com/sdk/docs/install-sdk
test_images:
- ubuntu:latest
test_maintenance: false
title: Google Cloud Platform (GCP) CLI 
tool_install: true
weight: 1
---

The Google Cloud CLI, `gcloud`, allows you to run commands in your Google Cloud account.

`gcloud` is available for Windows, macOS, Linux and supports the Arm architecture. 

## What should I consider before installing gcloud?

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

## How do I download and install for Ubuntu on Arm?

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

## How do I acquire user access credentials for Google Cloud? {#acquire-user-credentials}

You can use `gcloud` to obtain user access credentials for Google Cloud using a web flow. You will put the credentials in a well-known location for Application Default Credentials (`ADC`).

Run the following command to obtain user access credentials:

```console
gcloud auth application-default login
```

The command outputs a uniquely generated URL and a prompt to enter an authorization code, as shown below:

![gcloud1 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/1f6fbbe1-eb08-49b6-bfd5-2b6e54462dc3)

Open the URL in your browser and copy the unique authentication code.

![gcloud2 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/71065844-9d98-40be-a746-c0bb498ae913)

Now, paste the authentication code as shown below. The following output indicates a successful log in:

```output
Enter authorization code: 4/0AfgeXvsdW0jpvy3dBg5SH03DryspZyV5nz0j3lIDg4LwjL1AgikjjJYHgWlcap3Xtb0ioA

Credentials saved to file: [/home/ubuntu/.config/gcloud/application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).
```

After a successful log in, you will be able to use the `Google Cloud CLI` and automation tools like [Terraform](../terraform) from the terminal.
