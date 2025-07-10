---
title: Container CLI for macOS

draft: true

author: Rani Chowdary Mandepudi

minutes_to_complete: 10

official_docs: https://github.com/apple/container

additional_search_terms:
- container 
- virtualization

layout: installtoolsall
multi_install: false
multitool_install_part: false
test_maintenance: false
weight: 1
---

Container CLI is an open-source command line tool from Apple for building and running Arm Linux containers directly on macOS using lightweight virtual machines, without the need for Docker Desktop or Linux VMs.

It supports the full OCI (Open Container Initiative) workflow: building, running, tagging, and pushing container images.

## What should I do before installing the Container CLI?

This article provides a step-by-step guide to install and use the `container` command-line tool for building and running Arm Linux containers natively on macOS systems with Apple silicon.

Confirm you are using an Apple silicon Mac by running:

```bash
uname -m
```

The output on macOS is:

```output
arm64
```

Container CLI only works on Macs with Apple silicon, including M1, M2, M3, and M4.

Use the following command to verify macOS version:

```bash
sw_vers -productVersion
```

Example output:

```output
15.5
```

Your computer must be running macOS 15.0 or later to use the Container CLI.

## How do I install Container CLI?

To install Container CLI on macOS, follow the steps below:

From the [official GitHub Release page](https://github.com/apple/container/releases), download the latest signed `.pkg` installer. 

For example:

```bash
wget https://github.com/apple/container/releases/download/0.2.0/container-0.2.0-installer-signed.pkg
```

Install the downloaded package using:

```bash
sudo installer -pkg container-0.2.0-installer-signed.pkg -target /
```

This installs the Container binary at `/usr/local/bin/container`

After installation, start the container system service by running the following command:

```bash
container system start
```

{{% notice Note %}}
The system service must be running to use container operations such as build, run, or push. It may also need to be started again after a reboot, depending on system settings.
{{% /notice %}}

The background server process is now running. 

Verify the CLI version:

```bash
container --version
```

Example output:

```output
container CLI version 0.2.0 
```

This confirms that the Container CLI is successfully installed and ready to use.

## How do I build, run, and push a container using the Container CLI?

### Create a Dockerfile

You can define a simple image that prints the system architecture.

Use an editor to create a file named `Dockerfile` with the following contents:

```bash
FROM ubuntu:latest
CMD echo -n "Architecture is " && uname -m
```

### Build the container image

Build the image from the `Dockerfile`. 

This will pull the Ubuntu base image and tag the result as `uname`.

```bash
container build -t uname .
```

The output will be similar to: 

```output
Successfully built uname:latest
```

### Run the container 

Execute the container to verify it runs successfully and prints the system architecture.

```bash 
container run --rm uname
```

The output is: 

```output
Architecture is aarch64
```

The `--rm` flag removes the container after it finishes.

### Tag and push the image

Once the image is built and tested locally, it can be pushed to a container registry such as Docker Hub. This allows the image to be reused across machines or shared with others.

Use the `tag` command to apply a registry-compatible name to the image: 

```bash 
container images tag uname docker.io/<your-username>/uname:latest
```

Replace `<your-username>` with your Docker Hub username.

Before pushing the image, log in to Docker Hub:

```bash 
container registry login docker.io
```

Enter your Docker Hub username and password.

{{% notice Note %}}
The same command works with other registries such as GitHub Container Registry (ghcr.io) or any OCI-compliant registry. Replace `docker.io` with the appropriate registry hostname.
{{% /notice %}}

Next, upload the tagged image to Docker Hub.

```bash 
container images push docker.io/<your-username>/uname:latest
```

Once the push completes successfully, the image will be available in the Docker Hub repository. It can be pulled and run on other systems that support the Arm architecture. 

## How can I list images and containers?

You can view locally built or pulled images using:

```bash 
container images ls
```

To see running or previously executed containers:

```bash
container ls
```

## How do I uninstall the Container CLI?

The Container CLI includes an uninstall script that allows you to remove the tool from your system. You can choose to remove the CLI with or without user data.

Uninstall and keep user data (images, containers):

```bash 
uninstall-container.sh -k
```

Use this if you plan to reinstall later and want to preserve your local container data.

Uninstall and delete all user data:

```bash
uninstall-container.sh -d
```
This will permanently remove the CLI and all container images, logs, and metadata.

You can now build and run Arm Linux containers on macOS. 