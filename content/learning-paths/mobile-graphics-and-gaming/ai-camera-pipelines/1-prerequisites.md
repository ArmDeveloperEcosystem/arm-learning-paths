---
title: Prerequisites
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Host machine requirements

This Learning Path demonstrates how to improve the performance of camera pipelines using SME2 on Arm. You’ll need an Arm64 machine with SME2 support, preferably running an Ubuntu-based distribution. The instructions have been tested on Ubuntu 24.04.

## Install required software

Make sure the following tools are installed:
- **Git** – version control, for cloning the AI camera pipelines codebase
- **Git LFS** – extension to Git for managing large files using lightweight pointers
- **Docker** – an open-source container platform for running applications in isolated environments
- **OpenMP runtime (`libomp`)** – LLVM’s OpenMP runtime library, required for enabling parallel execution during application performance optimization

### Git and Git LFS

Install with the commands for your OS:

{{< tabpane code=true >}}
  {{< tab header="Linux/Ubuntu" language="bash">}}
sudo apt update
sudo apt install -y git git-lfs
# one-time LFS setup on this machine:
git lfs install
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install git git-lfs
# one-time LFS setup on this machine:
git lfs install
  {{< /tab >}}
{{< /tabpane >}}

### Docker

Check that Docker is installed:

```bash { output_lines="2" }
docker --version
Docker version 27.3.1, build ce12230
```

If you see "`docker: command not found`," follow the [Docker Install Guide](https://learn.arm.com/install-guides/docker/).

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