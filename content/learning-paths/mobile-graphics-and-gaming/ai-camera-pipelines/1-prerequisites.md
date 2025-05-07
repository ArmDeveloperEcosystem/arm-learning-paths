---
title: Prerequisites
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Host machine requirements

This learning path demonstrates the benefits of using KleidiCV and KleidiAI in applications running on Arm, so you will need an aarch64 machine, preferably running the Ubuntu distribution. The instructions in this learning path assume an Ubuntu distribution.

## Install software required for this Learning Path

You need to ensure you have the following tools:
- `git`, the version control system, for cloning the Voice Assistant codebase
- `git lfs`, an extension to `git` that helps manage large files by storing references to the files in the repository instead of the actual files themselves
- `docker`, an open-source containerization platform
- `libomp`, LLVM's OpenMP runtime library

### `git` and `git lfs`

These tools can be installed by running the following command (depending on your machine's OS):

{{< tabpane code=true >}}
  {{< tab header="Linux/Ubuntu" language="bash">}}
sudo apt install git git-lfs
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install git git-lfs
  {{< /tab >}}
{{< /tabpane >}}

### `docker`

Start by checking that `docker` is installed on your machine by typing the following command line in a terminal:

```BASH { output_lines="2" }
docker --version
Docker version 27.3.1, build ce12230
```

If the above command fails with a message similar to "`docker: command not found`," then follow the steps from the [Docker Install Guide](https://learn.arm.com/install-guides/docker/).

{{% notice Note %}}
You might need to log in again or restart your machine for the changes to take effect.
{{% /notice %}}

Once you have confirmed that Docker is installed on your machine, you can check that it is operating normally with the following:

```BASH { output_lines="2-27" }
docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
478afc919002: Pull complete
Digest: sha256:305243c734571da2d100c8c8b3c3167a098cab6049c9a5b066b6021a60fcb966
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker followed these steps:

 1. The Docker client contacted the Docker daemon.

 2. The Docker daemon pulled the "hello-world" image from Docker Hub.
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

### `libomp`

`libomp` can be installed by running the following command (depending on your machine's OS):

{{< tabpane code=true >}}
  {{< tab header="Linux/Ubuntu" language="bash">}}
sudo apt install libomp-19-dev
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install libomp
  {{< /tab >}}
{{< /tabpane >}}