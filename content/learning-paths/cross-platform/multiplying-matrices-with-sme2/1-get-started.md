---
title: Set up your Environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing software for this Learning Path

To follow this Learning Path, you will need to set up an environment to develop with SME2.

You will require:

 - A compiler with support for SME2 instructions. You can use [Clang](https://www.llvm.org/)
   version 18 or later, or [GCC](https://gcc.gnu.org/) version 14, or later. This Learning
   Path uses ``Clang``.

 - An emulator to execute code with the SME2 instructions. This Learning
   Path uses [Arm's Fixed Virtual Platform (FVP) model](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms).

You will also require Git and Docker installed on your machine.

### Set up Git

To check if Git is already installed on your machine, use the following command line in a terminal:

```BASH { output_lines=2 }
git --version
git version 2.47.1
```

If the above command line fails with a message similar to "``git: command not found``", then install Git following the steps for your machine's OS.

{{< tabpane code=true >}}
  {{< tab header="Linux/Ubuntu" language="bash">}}
sudo apt install git
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install git
  {{< /tab >}}
{{< /tabpane >}}

### Docker

To enable you to get started easily and with the tools that you need, you can fetch a Docker container with the required compiler and FVP. Alternatively, if you do wish to build the container yourself, the ``Dockerfile`` is also available.


{{% notice Note %}}
This Learning Path works without ``docker``, but the compiler and the FVP must be available in your search path.
{{% /notice %}}

Start by checking that ``docker`` is installed on your machine by typing the following
command line in a terminal:

```BASH { output_lines="2" }
docker --version
Docker version 27.3.1, build ce12230
```

If the above command fails with a message similar to "``docker: command not found``"
then follow the steps from the [Docker Install Guide](https://learn.arm.com/install-guides/docker/).

{{% notice Note %}}
You might need to login again or restart your machine for the changes to take effect.
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

## Environment

Now, [download the code examples](https://gitlab.arm.com/learning-code-examples/code-examples/-/archive/main/code-examples-main.tar.gz?path=learning-paths/cross-platform/sme2)
for this learning path, expand the archive and change your current directory to
``code-examples/learning-paths/cross-platform/sme2`` :

```BASH
tar xfz code-examples-main-learning-paths-cross-platform-sme2.tar.gz -s /code-examples-main-learning-paths-cross-platform-sme2/code-examples/
cd code-examples/learning-paths/cross-platform/sme2
```

This list of content in this directory should look like this :

```TXT
code-examples/learning-paths/cross-platform/sme2/
├── .clang-format
├── .devcontainer/
│   └── devcontainer.json
├── .git/
├── .gitignore
├── Makefile
├── README.rst
├── docker/
│   ├── assets.source_me
│   ├── build-all-containers.sh
│   ├── build-my-container.sh
│   └── sme2-environment.docker
├── hello.c
├── main.c
├── matmul.h
├── matmul_asm.c
├── matmul_asm_impl.S
├── matmul_intr.c
├── matmul_vanilla.c
├── misc.c
├── misc.h
├── preprocess_l_asm.S
├── preprocess_vanilla.c
├── run-fvp.sh
└── sme2_check.c
```

It contains:
- Code examples.
- A ``Makefile`` that builds the code examples.
- A shell script called ``run-fvp.sh`` that runs the FVP.
- A directory called ``docker`` that contains materials related to Docker, which are:
  - A script called ``assets.source_me`` that provides the FVP and compiler toolchain references.
  - A Docker recipe called ``sme2-environment.docker`` to build the container that
  you will use.
  - A shell script called ``build-my-container.sh`` that you can use if you want to build the Docker container. This is not essential however, as ready-made images are made available for you. 
  - A script called ``build-all-containers.sh`` that was used to create the image for you to download to provide multi-architecture support for both x86_64 and AArch64.
- A configuration script for VS Code to be able to use the container from the IDE called ``.devcontainer/devcontainer.json``.

{{% notice Note %}}
From this point in the Learning Path, all instructions assume that your current
directory is ``code-examples/learning-paths/cross-platform/sme2``.{{% /notice %}}


## Using the environment

Docker containers provide you with the functionality to execute commands in an isolated environment, where you have all the necessary tools that you require without having to clutter your machine. The containers runs independently, which means that they do not interfere with other containers on the same machine or server.  

You can use Docker in the following ways:
- Directly from the command line. For example, when you are working from a terminal on your local machine.
- Within a containerized environment. Configure VS Code to execute run all the commands inside a Docker container, allowing you to work seamlessly within the Docker environment.

### Working from a terminal

When a command is executed in the Docker container environment, you must prepend it with instructions on the command line so that your shell executes it within the container. 

For example, to execute ``COMMAND ARGUMENTS`` in the SME2 Docker container, the command line looks like this:

```SH
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v1 COMMAND ARGUMENTS
```

This invokes Docker, using the
``armswdev/sme2-learning-path:sme2-environment-v1``container
image, and mounts the current working directory (the ``code-examples.git/learning-paths/cross-platform/sme2``)
inside the container to ``/work``, then sets ``/work`` as the
working directory and runs ``COMMAND ARGUMENTS`` in this environment.

For example, to run ``make``, you need to enter:

```SH
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v1 make
```

### Working from within the Docker container

Make sure you have the [Microsoft Dev
Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
extension installed. 

Then select the **Reopen in Container** menu entry as Figure 1 shows. 

It automatically finds and uses ``.devcontainer/devcontainer.json``:

![example image alt-text#center](VSCode.png "Figure 1: Setting up the Docker Container.")

All your commands now run within the container, so there is no need to prepend them with a Docker invocation, as VS Code handles all this seamlessly for you.

{{% notice Note %}}
For the rest of this Learning Path, shell commands include the full Docker invocation so that users not using VS Code can copy the complete command line. However, if you are using VS Code, you only need to use the `COMMAND ARGUMENTS` part. 
{{% /notice %}}
