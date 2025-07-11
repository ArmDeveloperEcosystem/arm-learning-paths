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
weight: 1
---

Container CLI is an open-source command-line tool from Apple for building and running Arm Linux containers directly on macOS using lightweight virtual machines without Docker Desktop or full Linux VMs.

It supports the full OCI (Open Container Initiative) workflow: building, running, tagging, and pushing container images.

## What should I do before installing the Container CLI?

This guide shows how to install and use the `container` CLI to run Arm Linux containers natively on Apple silicon Macs.

First, confirm you are using an Apple silicon Mac by running:

```bash
uname -m
```

Expected output:

```output
arm64
```

Container CLI supports only Apple silicon Macs (M1, M2, M3, and M4).

Check your macOS version:

```bash
sw_vers -productVersion
```

Example output:

```output
15.5
```

You must be running **macOS 15.0 or later** to use the Container CLI.

## How do I install Container CLI?

To install Container CLI:

Go to the [GitHub Releases page](https://github.com/apple/container/releases) and download the latest signed `.pkg` installer.

For example:

   ```bash
   wget https://github.com/apple/container/releases/download/0.2.0/container-0.2.0-installer-signed.pkg
   ```

Install the package:

   ```bash
   sudo installer -pkg container-0.2.0-installer-signed.pkg -target /
   ```

This installs the Container binary at `/usr/local/bin/container`.

Start the container system service:

   ```bash
   container system start
   ```

{{% notice Note %}}
The system service must be running to use container operations such as build, run, or push. It may also need to be started again after a reboot, depending on system settings.{{%/notice %}}

The background server process is now running. 

Verify the CLI version:

   ```bash
   container --version
   ```

   Example output:

   ```output
   container CLI version 0.2.0
   ```

## Build and run a container

### Create a Dockerfile

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

Once the image is built and tested locally, it can be pushed to a container registry such as Docker Hub. This allows the image to be reused across machines or shared with others.

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

{{% notice Note %}}
The same command works with other registries such as GitHub Container Registry (ghcr.io) or any OCI-compliant registry. Replace `docker.io` with the appropriate registry hostname.{{% /notice %}}

Next, upload the tagged image to Docker Hub.

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

## How do I uninstall the Container CLI?

The CLI includes an uninstall script. You can choose whether to keep or delete your container data.

To uninstall and **keep** user data (images and containers):

```bash
uninstall-container.sh -k
```

Use this if you plan to reinstall later and want to keep your local container data.

Uninstall and delete all user data:

```bash
uninstall-container.sh -d
```

This will remove the CLI and all related images, logs, and metadata.

---

You’ve now installed Container CLI and built your first Arm Linux container on macOS.
