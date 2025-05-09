---
title: Prerequisites
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Host machine requirements

This Learning Path demonstrates how to improve the performance of camera pipelines using KleidiAI and KleidiCV in applications running on Arm. You will need an Arm64 machine, preferably running an Ubuntu-based distribution. The instructions have been tested on Ubuntu 24.04.

## Install required software

Make sure the following tools are installed:
- `git` - a version control system, for cloning the Voice Assistant codebase.
- `git lfs` - an extension to `git` for managing large files by storing lightweight references instead of the files themselves.
- `docker` - an open-source containerization platform for running applications in isolated environments.
- `libomp` - LLVM's OpenMP runtime library, required for enabling parallel execution during application performance optimization.

### git and git lfs

These tools can be installed by running the following command, depending on your OS:

{{< tabpane code=true >}}
  {{< tab header="Linux/Ubuntu" language="bash">}}
sudo apt install git git-lfs -y
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install git git-lfs
  {{< /tab >}}
{{< /tabpane >}}

### Docker

Start by checking that `docker` is installed on your machine by typing the following command line in a terminal:

```bash { output_lines="2" }
docker --version
Docker version 27.3.1, build ce12230
```

If you see an error like "`docker: command not found`," then follow the steps from the [Docker Install Guide](https://learn.arm.com/install-guides/docker/).

{{% notice Note %}}
You might need to log in again or restart your machine for the changes to take effect.
{{% /notice %}}

Once you have confirmed that Docker is installed on your machine, you can check that it is operating normally with the following:

```bash { output_lines="2-27" }
docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c9c5fd25a1bd: Pull complete 
Digest: sha256:c41088499908a59aae84b0a49c70e86f4731e588a737f1637e73c8c09d995654
Status: Downloaded newer image for hello-world:latest

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

### OpenMP library

`libomp` is the OpenMP library developed by the LLVM project. It provides the necessary support for executing OpenMP parallel programs.

`libomp` can be installed by running the following command, depending on your OS:

{{< tabpane code=true >}}
  {{< tab header="Linux/Ubuntu" language="bash">}}
sudo apt install libomp-19-dev -y
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install libomp
  {{< /tab >}}
{{< /tabpane >}}