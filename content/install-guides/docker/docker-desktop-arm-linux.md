---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Docker Desktop for Arm Linux
description: Install Docker Desktop on arm64 Arm Linux and verify the setup so you can run container workflows with the Docker Desktop graphical environment.

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- containers
- virtual machines

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author: Jason Andrews

### Link to official documentation
official_docs: https://docs.docker.com/desktop/
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=docker

weight: 4                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## Install Docker Desktop for Arm Linux

Docker Desktop provides a graphical interface for managing containers, images, and volumes. It bundles Docker Engine, Docker CLI, Docker Compose, and Kubernetes into a single install. On Arm Linux, Docker Desktop runs a lightweight VM using KVM, giving you the same container development experience available on macOS and Windows.

To make sure you are on an Arm Linux computer, run:

```console
uname -m
```

The output should be:

```output
aarch64
```

Before installing Docker Desktop, install Docker Engine. For installation steps, see [Docker Engine](/install-guides/docker/docker-engine/).

<!-- ```console
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
``` -->

After installing Docker Engine, you can download and install Docker Desktop on Ubuntu and Debian distributions. 

Download Docker Desktop:

```console
wget https://desktop.docker.com/linux/main/arm64/docker-desktop-arm64.deb
```

Install Docker Desktop using:

```console
sudo apt install ./docker-desktop-arm64.deb
```

The Docker icon is now available to start Docker Desktop.

![A screenshot of applications on a Linux desktop with an icon for Docker Desktop #center](/install-guides/_images/docker-icon.png)

## Verify Docker Desktop is installed

To print the Docker Desktop version, run:

```console
docker version
```

The output depends on your version and is similar to:

```output
Server: Docker Desktop 4.85.0 (235549)
 Engine:
  Version:          29.7.1
  API version:      1.55 (minimum version 1.40)
  Go version:       go1.26.5
  Git commit:       c5b8ce9
  Built:            Fri Jul 31 17:07:22 2026
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          v2.2.6
  GitCommit:        11ce9d5f3c68c941867e82890e93e815c1304f1b
 runc:
  Version:          1.3.6
  GitCommit:        v1.3.6-0-g491b69ba
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

You can now use Docker Desktop on Arm Linux. The following image shows Docker Desktop running on a System76 Thelio Astra desktop with Ubuntu 24.04.

![A screenshot showing a list of local container images on the Docker Desktop application. The application is running on a System76 Thelio Astra desktop with Ubuntu 24.04. #center](/install-guides/_images/docker-desktop.png)

You're now ready to use Docker Desktop. You can explore [Docker related Learning Paths](/tag/docker/).

You can also create an account on [Docker Hub](https://hub.docker.com) to share images and automate workflows.
