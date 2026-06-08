---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Docker Engine

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- containers
- virtual machines

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author: Jason Andrews

### Link to official documentation
official_docs: https://docs.docker.com/engine/
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=docker-ce

weight: 2                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## Install Docker Engine on Linux

You can run the following commands to install Docker on any Linux machine and on any architecture, from a cloud server to a Raspberry.

The commands can also be used in the Windows Subsystem for Linux 2 (WSL 2) and on a Chromebook.

### Run the installer

Run the installer for Docker on Linux:

```console
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```

### Add your user to the Docker group

Add your user to the docker group:

```console
sudo usermod -aG docker $USER ; newgrp docker
```
The `newgrp` command avoids the need to log out and back in.

### Confirm the installation

To confirm the installation is successful, run:

```console
docker run hello-world
```

The output should be similar to:

```output
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

To identify the architecture, run: 

```console
uname -m
```

The output values can be `aarch64` (Arm 64-bit), `armv7l` (Arm 32-bit) or `x86_64`.

### Available Docker Engine versions

The Stable channel (`get.docker.com`) provides the latest releases for general availability.

The Test channel (`test.docker.com`) installs pre-releases that are for testing before general availability. 

Replace `get.docker.com` with `test.docker.com` in the installation command to use the test version.

### Handle Linux distributions that don't support get.docker.com 

Some Linux distributions are not supported by [get.docker.com](https://get.docker.com).

Generally, the supported list is as follows:
- Ubuntu
- Debian
- SUSE Linux Enterprise Server
- Red Hat Enterprise Linux
- Fedora
- CentOS

An example of a distribution which is not supported and is popular on Arm is [Manjaro](https://manjaro.org).

On Manjaro, install docker using `pacman`:

```console
sudo pacman -Syu 
sudo pacman -S docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER ; newgrp docker
```

To confirm the installation is successful, run the same hello-world example:

```console
docker run hello-world
```

### Start and stop the Docker daemon on Linux distributions with systemd

To start the docker daemon:

```console
sudo systemctl start docker
```

To stop the docker daemon:

```console
sudo systemctl stop docker
```

If the following message is displayed:

```output
Warning: Stopping docker.service, but it can still be activated by:
  docker.socket
```

Stop docker.socket:

```console
sudo systemctl stop docker.socket
```

You can now use Docker Engine and explore [Docker related Learning Paths](/tag/docker/).

You can also create an account on [Docker Hub](https://hub.docker.com) to share images and automate workflows.

