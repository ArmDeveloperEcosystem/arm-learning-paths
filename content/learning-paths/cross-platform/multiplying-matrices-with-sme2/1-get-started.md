---
title: Set up your SME2 development environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose your SME2 setup: native or emulated

To build or run SME2-accelerated code, first set up your development environment.
This section walks you through the required tools and two supported setup options:

* [**Native SME2 hardware**](#set-up-a-system-with-native-SME2-support) - build and run directly on a system with SME2 support. For supported devices, see [Devices with SME2 support](#devices-with-sme2-support). 

* [**Docker-based emulation**](#set-up-a-system-using-sme2-emulation-with-docker) - use a container to emulate SME2 in bare metal mode (without an OS).

## Download and explore the code examples

To get started, begin by [downloading the code examples](https://gitlab.arm.com/learning-cde-examples/code-examples/-/archive/main/code-examples-main.tar.gz?path=learning-paths/cross-platform/multiplying-matrices-with-sme2).

Now extract the archive, and change directory to:
``code-examples/learning-paths/cross-platform/multiplying-matrices-with-sme2.``

```BASH
tar xfz code-examples-main-learning-paths-cross-platform-multiplying-matrices-with-sme2.tar.gz -s /code-examples-main-learning-paths-cross-platform-multiplying-matrices-with-sme2/code-examples/
cd code-examples/learning-paths/cross-platform/multiplying-matrices-with-sme2
```

The directory structure should look like this:

```TXT
code-examples/learning-paths/cross-platform/multiplying-matrices-with-sme2/
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

Amongst other files, it includes:
- Code examples.
- A `Makefile` to build the code.
- `run-fvp.sh` to run the FVP model.
- A `docker` directory containing:
  - `assets.source_me` to provide toolchain paths.
  - `build-my-container.sh`, a script that automates building the Docker image from the `sme2-environment.docker` file. It runs the Docker build command with the correct arguments so you don’t have to remember them. 
  - `sme2-environment.docker`, a custom Docker file that defines the steps to build the SME2 container image. It installs all the necessary dependencies, including the SME2-compatible compiler and Arm FVP emulator.
  - `build-all-containers.sh`, a script to build multi-architecture images.
- `.devcontainer/devcontainer.json` for VS Code container support.

{{% notice Note %}}
From this point, all instructions assume that your current directory is
``code-examples/learning-paths/cross-platform/multiplying-matrices-with-sme2``, so ensure that you are in the correct directory before proceeding.
{{% /notice %}}

## Set up a system with native SME2 support

To run SME2 code natively, ensure your system includes SME2 hardware and uses a compiler version that supports SME2.

For the compiler, you can use [Clang](https://www.llvm.org/) version 18 or later, or [GCC](https://gcc.gnu.org/) version 14 or later. This Learning Path uses ``clang``.

{{% notice Note %}}
At the time of writing, macOS ships with `clang` version 17.0.0, which doesn't support SME2. Use a newer version, such as 20.1.7, available through Homebrew.{{% /notice%}}

You can check your compiler version using the command:``clang --version``

### Install Clang

Install Clang using the instructions below, selecting either macOS or Linux/Ubuntu, depending on your setup:

{{< tabpane code=true >}}

  {{< tab header="Linux/Ubuntu" language="bash">}}
  sudo apt install clang
  {{< /tab >}}

  {{< tab header="macOS" language="bash">}}
  brew install clang
  {{< /tab >}}

{{< /tabpane >}}

You are now all set to start hacking with SME2.

## Set up a system using SME2 emulation with Docker

If your machine doesn't support SME2, or you want to emulate it, you can use the Docker-based environment that this Learning Path models.

The Docker container includes both a compiler and [Arm's Fixed Virtual Platform (FVP)
model](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms)
for emulating code that uses SME2 instructions. You can either run the prebuilt container image provided in this Learning Path or build it yourself using the Docker file that is included. 

If building manually, follow the instructions in the ``sme2-environment.docker`` file to install the required tools on your machine.

### Install and verify Docker

{{% notice Note %}}
Docker is optional, but if you don’t use it, you must manually install the compiler and FVP, and ensure they’re in your `PATH`.
{{% /notice %}}

To begin, start by checking that Docker is installed on your machine:

```BASH { output_lines="2" }
docker --version
Docker version 27.3.1, build ce12230
```

If the above command fails with an error message similar to "``docker: command not found``", then follow the steps from the [Docker Install Guide](https://learn.arm.com/install-guides/docker/) to install Docker.

{{% notice Note %}}
You might need to log out and back in again or restart your machine for the changes to take
effect.
{{% /notice %}}

Once you have confirmed that Docker is installed on your machine, you can check
that it is working with the following:

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

You can use Docker in the following ways:
- [Directly from the command line](#run-commands-from-a-terminal-using-docker) - for example, when you are working from a terminal on your local machine.

- [Within a containerized environment](#use-an-interactive-docker-shell) - by configuring VS Code to execute all the commands inside a Docker container, allowing you to work seamlessly within the
Docker environment.

### Run commands from a terminal using Docker

When a command is executed in the Docker container environment, you must prepend
it with instructions on the command line so that your shell executes it within
the container.

For example, to execute ``COMMAND ARGUMENTS`` in the SME2 Docker container, the
command line looks like this:

```BASH
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v2 COMMAND ARGUMENTS
```

This invokes Docker, using the
``armswdev/sme2-learning-path:sme2-environment-v2`` container image, and mounts
the current working directory (the
``code-examples/learning-paths/cross-platform/multiplying-matrices-with-sme2``)
inside the container to ``/work``, then sets ``/work`` as the working directory
and runs ``COMMAND ARGUMENTS`` in this environment.

For example, to run ``make``, you need to enter:

```BASH
docker run --rm -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v2 make
```

### Use an interactive Docker shell

The standard `docker run` commands can be long and repetitive. To streamline your workflow, you can start an interactive Docker session that allows you to run commands directly - without having to prepend docker run each time.

To launch an interactive shell inside the container, use the `-it` flag:

```BASH
docker run --rm -it -v "$PWD:/work" -w /work armswdev/sme2-learning-path:sme2-environment-v2
```

You are now in the Docker container, and you can execute all commands directly. For
example, the ``make`` command can now be simply invoked with:

```BASH
make
```

To exit the container, simply hit CTRL+D. Note that the container is not persistent (it was invoked with ``--rm``), so each invocation will use a container freshly built from the image. All the files reside outside the container, so changes you make to them will be persistent.

###  Develop with Docker in Visual Studio Code

If you are using Visual Studio Code as your IDE, the container setup is already configured with `devcontainer/devcontainer.json`.

Make sure you have the [Microsoft Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed.

Then select the **Reopen in Container** menu entry as shown below.

It automatically finds and uses ``.devcontainer/devcontainer.json``:

![VSCode Docker alt-text#center](VSCode.png "Figure 1: Setting up the Docker container.")

All your commands now run within the container, so there is no need to prepend
them with a Docker invocation, as VS Code handles all this seamlessly for you.

{{% notice Note %}}
For the rest of this Learning Path, shell commands include the full Docker
invocation so that if you are not using VS Code you can copy the complete command line.
However, if you are using VS Code, you only need to use the `COMMAND ARGUMENTS`
part.
{{% /notice %}}

### Devices with native SME2 support

These Apple devices support SME2 natively.

- iPad

  - iPad Pro 11"

  - iPad Pro 13"

- iPhone

  - iPhone 16

  - iPhone 16 Plus

  - iPhone 16e

  - iPhone 16 Pro

  - iPhone 16 Pro Max

- iMac

- MacBook Air

  - MacBook Air 13"

  - MacBook Air 15"

- Mac mini



- MacBook Pro

  - MacBook Pro 14"

  - MacBook Pro 16"

- Mac Studio



