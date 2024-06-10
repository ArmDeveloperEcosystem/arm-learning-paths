---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Docker for Windows on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- containers
- virtual machines

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://docs.docker.com/desktop/

weight: 4                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## How do I install Docker for Windows on Arm? 

Docker Desktop on Windows requires WSL 2 or Hyper-V. Both are available for Windows on Arm. 

Docker Desktop for Windows on Arm was [announced at Microsoft Build 2024](https://www.docker.com/blog/announcing-docker-desktop-support-for-windows-on-arm/). The first available version is 4.30. 

### What should I do before installing Docker Desktop for Windows on Arm?

- Install WSL 2 on the Windows on Arm laptop, or turn on Hyper-V and Containers Windows features.

### Which Windows on Arm computers are supported?

Here are three examples of Windows on Arm computers:
- Lenovo Thinkpad X13s.
- Microsoft Surface Pro X.
- Samsung Galaxy Book S.

Additional models of Windows on Arm computers are expected to be available in mid-2024.

### How do I install and test Docker Desktop for Windows on Arm?

The current version is 4.31.0 and you can
download [Docker Desktop for Windows on Arm](https://desktop.docker.com/win/main/arm64/153195/Docker%20Desktop%20Installer.exe) and run the installer.

Check the [Docker Desktop release notes](https://docs.docker.com/desktop/release-notes/) for the latest release information.

Once the installation is complete, you can test it by running `docker` in a Windows Command Prompt or PowerShell Prompt:

```console
docker run hello-world
```

You should see a welcome message similar to the following:

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

Docker Desktop is now ready to use for Windows on Arm. 

You can explore [Docker related Learning Paths](/tag/docker/).

You may want to create an account on [Docker Hub](https://hub.docker.com) to share images and automate workflows.
