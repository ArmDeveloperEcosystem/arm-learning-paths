---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Docker Desktop

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- containers
- virtual machines

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://docs.docker.com/desktop/

weight: 3                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
## How do I install and test Docker Desktop?

All of the download files are available on the 
[Docker Desktop product page](https://www.docker.com/products/docker-desktop/).

| Installation instructions |
|-------|
| [Windows](https://docs.docker.com/desktop/install/windows-install/) |
| [Linux](https://docs.docker.com/desktop/install/linux-install/) |
| [macOS](https://docs.docker.com/desktop/install/mac-install) |

All of the Docker Desktop products use the `x86_64` / `amd64` architecture except macOS on Apple Silicon.

On any platform, confirm the Docker Desktop installation is successful with:
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
Apple Silicon is reported as `arm64`.

Docker Engine is now ready to use. You can explore [Docker related Learning Paths](/tag/docker/).

You may want to create an account on [Docker Hub](https://hub.docker.com) to share images and automate workflows.
