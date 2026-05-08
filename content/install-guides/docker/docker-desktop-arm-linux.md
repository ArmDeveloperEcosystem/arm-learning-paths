---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Docker Desktop for Arm Linux

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

Docker Desktop is available for Arm Linux, but not yet documented.

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

{{% notice Note %}}
The following command uses Docker Desktop version 4.70.0 for Debian. The same command works with other versions. Replace the download link used in this step with the link for your version of choice. To find the latest version, see [Docker Desktop release notes](https://docs.docker.com/desktop/release-notes/). Replace the instances of `amd64` in the download URL with `arm64`.
{{% /notice %}}

For example:

```console
wget https://desktop.docker.com/linux/main/arm64/224270/docker-desktop-arm64.deb
```

Install Docker Desktop using:

```console
sudo apt install ./docker-desktop-arm64.deb
```

The Docker icon is now available to start Docker Desktop.

![A screenshot of applications on a Linux desktop with an icon for Docker Desktop #center](/install-guides/_images/docker-icon.png)

To print the Docker Desktop version, run:

```console
docker version
```

The output depends on your version and is similar to:

```output
Server: Docker Desktop 4.70.0 (224270)
 Engine:
  Version:          29.4.0
  API version:      1.54 (minimum version 1.40)
  Go version:       go1.26.1
  Git commit:       daa0cb7
  Built:            Tue Apr  7 08:36:25 2026
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          v2.2.1
  GitCommit:        dea7da592f5d1d2b7755e3a161be07f43fad8f75
 runc:
  Version:          1.3.4
  GitCommit:        v1.3.4-0-gd6d73eb8
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

You can now use Docker Desktop on Arm Linux. The following image shows Docker Desktop running on a System76 Thelio Astra desktop with Ubuntu 24.04.

![A screenshot showing a list of local container images on the Docker Desktop application. The application is running on a System76 Thelio Astra desktop with Ubuntu 24.04. #center](/install-guides/_images/docker-desktop.png)

You're now ready to use Docker Desktop. You can explore [Docker related Learning Paths](/tag/docker/).

You can also create an account on [Docker Hub](https://hub.docker.com) to share images and automate workflows.
