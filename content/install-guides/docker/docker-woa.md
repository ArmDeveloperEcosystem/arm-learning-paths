---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Docker for Windows on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- containers
- virtual machines

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://docs.docker.com/engine/

weight: 4                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## Install Docker for Windows on Arm {#docker-woa}

Docker can be run on Windows on Arm machines using the Windows Subsystem for Linux 2 (WSL2).

There is no Docker Desktop for Windows on Arm, [please show your support by asking for it](https://github.com/docker/roadmap/issues/91)

### Before you begin

- Install WSL 2 on the Windows on Arm laptop
- Install a Linux distribution such as Ubuntu 22.04 Linux distribution in WSL 2 from the Microsoft Store

More information is available in the Learning Path [Get started with Windows Subsystem for Linux (WSL) on Arm](/learning-paths/laptops-and-desktops/wsl2/).

### Example Windows on Arm computers

- Lenovo Thinkpad X13s
- Microsoft Surface Pro X
- Samsung Galaxy Book S

### Install and test Docker Engine

You can use the general Linux install instructions to install Docker in WSL 2 for Windows on Arm. 

```console
curl -fsSL test.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
```

The Docker daemon will not automatically start in WSL 2. 

It can be started manually:
```console
sudo /etc/init.d/docker start
```

It can also be started automatically using by editing `/etc/wsl2.conf`

Add the info below to the file:
```console
# Set a command to run when a new WSL instance launches. This example starts the Docker container service.
[boot]
command = service docker start
```

To confirm the installation is successful run:
```console
docker run hello-world
```

The output should be a welcome message such as:

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

Use the `uname` command to identify the architecture:

```console
uname -m
```

The output is `aarch64` (Arm 64-bit).

Docker Engine is now ready to use for Windows on Arm. You can explore [Docker related Learning Paths](/tag/docker/) or learn more about [WSL for Windows on Arm](/learning-paths/laptops-and-desktops/wsl2/).

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

