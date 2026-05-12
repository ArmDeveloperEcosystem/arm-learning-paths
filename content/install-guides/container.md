---
title: Container CLI for macOS
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
tool_install: true
weight: 1
---

Container CLI is an open-source command-line tool from Apple for building and running Arm Linux containers directly on macOS. With Container CLI, you can run containers using lightweight virtual machines without Docker Desktop or full Linux VMs.

The CLI supports the full Open Container Initiative (OCI) workflow: building, running, tagging, and pushing container images.

In this guide, you'll learn how to install and use the Container CLI to run Arm Linux containers natively on Apple silicon Macs.

## Before you begin

First, confirm you are using an Apple silicon Mac by running:

```bash
uname -m
```

The output should be:

```output
arm64
```
{{% notice Note %}}
Container CLI supports only Apple silicon Macs (M1, M2, M3, and M4).
{{% /notice %}}

Check your macOS version:

```bash
sw_vers -productVersion
```

Example output:

```output
15.6.1
```

You must run macOS 15.0 or later to use the Container CLI.

## Install Container CLI

To install Container CLI, go to the [GitHub Releases page](https://github.com/apple/container/releases) and download the latest signed `.pkg` installer.  

For example, the following commands use version `0.11.0`. Replace `0.11.0` with the latest version:

```bash
wget https://github.com/apple/container/releases/download/0.11.0/container-0.11.0-installer-signed.pkg
```

Install the package:

```bash
sudo installer -pkg container-0.11.0-installer-signed.pkg -target /
```

This installs the Container binary at `/usr/local/bin/container`.

Start the container system service:

```bash
container system start
```

You must start the service to use commands like `build`, `run`, or `push`. It may need to be restarted after rebooting.

The background server process is now running. 

Verify the CLI version:

```bash
container --version
```

The output is similar to:

```output
container CLI version 0.11.0 (build: release, commit: d9b8a8d)
```

## Verify installation by building and running a container


In a working directory, create a file named `Dockerfile`:

```dockerfile
FROM ubuntu:latest
CMD echo -n "Architecture is " && uname -m
```

This image prints the system architecture when executed.

### Build the image

Run the following to build and tag the container image as `uname`:

```bash
container build -t uname .
```

Example output:

```output
Successfully built uname:latest
```

### Run the container

Run the container to verify it prints the system architecture.

```bash
container run --rm uname
```

Expected output:

```output
Architecture is aarch64
```

The `--rm` flag cleans up the container after it exits.

## Tag and push the image

After the image is built and tested locally, you can push it to a container registry such as Docker Hub. This allows the image to be reused across machines or shared with others.

{{% notice Note %}}
The following commands are for Docker Hub. The same commands work with any other OCI-compliant registry such as GitHub Container Registry (ghcr.io) or any OCI-compliant registry. Replace `docker.io` with the appropriate registry hostname.
{{% /notice %}}

Tag the image with a registry-compatible name:

```bash
container images tag uname docker.io/<your-username>/uname:latest
```

Replace `<your-username>` with your Docker Hub username.

Log in to Docker Hub:

```bash
container registry login docker.io
```

Enter your Docker Hub username and password.

Next, upload the tagged image to Docker Hub:

```bash
container images push docker.io/<your-username>/uname:latest
```

## List images and containers

To view images:

```bash
container images ls
```

To view running or stopped containers:

```bash
container ls
```

## Uninstall the Container CLI

The CLI includes an uninstall script. You can choose whether to keep or delete your container data.

 To uninstall and retain user data (images and containers):

```bash
uninstall-container.sh -k
```
The command is useful if you plan to reinstall Container CLI later and want to keep your local container data.

Otherwise, to uninstall and delete all user data:

```bash
uninstall-container.sh -d
```

This will remove the CLI and all related images, logs, and metadata.

You’ve now ready to use Container CLI.  
