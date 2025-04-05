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

weight: 4                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## How do I install Docker Desktop for Arm Linux?

Docker Desktop is available for Arm Linux, but not yet documented.

Make sure you are on an Arm Linux computer by running:

```console
uname -m
```

The output should be:

```output
aarch64
```

Before installing Docker Desktop install Docker Engine using:

```console
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
```

You can download and install Docker Desktop on Ubuntu and Debian distributions. 

The path to the download depends on the version. The easiest way is to copy the link for the Debian download of Docker Desktop from the latest [Docker Desktop release notes](https://docs.docker.com/desktop/release-notes/) and replace the instances of `amd64` with `arm64`. This will provide the URL to download.

For example:

```console
wget https://desktop.docker.com/linux/main/arm64/187762/docker-desktop-arm64.deb
```

Install Docker Desktop using:

```console
sudo apt install ./docker-desktop-arm64.deb
```

The Docker icon is now available to start Docker Desktop.

![img1 #center](/install-guides/_images/docker-icon.png)

To print the Docker Desktop version use:

```console
docker version
```

The output may be different depending on your version:

```output
Server: Docker Desktop 4.40.0 (187762)
 Engine:
  Version:          28.0.4
  API version:      1.48 (minimum version 1.24)
  Go version:       go1.23.7
  Git commit:       6430e49
  Built:            Tue Mar 25 15:07:18 2025
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.7.26
  GitCommit:        753481ec61c7c8955a23d6ff7bc8e4daed455734
 runc:
  Version:          1.2.5
  GitCommit:        v1.2.5-0-g59923ef
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

You can now use Docker Desktop on Arm Linux. The image below shows Docker Desktop running on a System76 Thelio Astra with Ubuntu 24.04 desktop.

![img1 #center](/install-guides/_images/docker-desktop.png)

Docker Desktop is now ready to use. You can explore [Docker related Learning Paths](/tag/docker/).

You may want to create an account on [Docker Hub](https://hub.docker.com) to share images and automate workflows.
