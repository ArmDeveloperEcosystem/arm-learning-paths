---
# User change
title: "Set up the ExecuTorch build environment"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## For macOS: build ExecuTorch in a Docker container

On macOS, it’s easiest to build ExecuTorch in an Ubuntu container. This keeps your toolchain consistent with the rest of the Learning Path and avoids gaps in macOS-native cross-compilers (for example, the Arm GNU Toolchain doesn’t provide an “AArch64 GNU/Linux target” for macOS).

This container isn’t part of the runtime deployment. It’s a build environment that produces the artifacts you later move onto the FRDM i.MX 93:

- Prebuilt ExecuTorch libraries you link into Cortex-M33 firmware
- `.pte` model files compiled for Ethos-U65

Keeping this step reproducible helps you focus on the actual bring-up milestone: booting custom firmware on Cortex-M33 and using Ethos-U65 for inference.

Start by installing and launching [Docker Desktop](https://www.docker.com/).

Next, create a working directory for your container build:

   ```bash
   mkdir ubuntu-24-container
   ```

Now create a `Dockerfile` and switch into the directory:

   ```bash
   cd ubuntu-24-container
   touch Dockerfile
   ```

Add the following content to your `Dockerfile` to install a few basic tools in the image:

   ```dockerfile
   FROM ubuntu:24.04

   ENV DEBIAN_FRONTEND=noninteractive

   RUN apt update -y && \
       apt install -y \
       software-properties-common \
       curl vim git
   ```

   The `ubuntu:24.04` container image includes Python 3.12, which you use later in this Learning Path.

   Build the container image:

   ```bash
   docker build -t ubuntu-24-container .
   ```

Run the container and open an interactive shell:

   ```bash { output_lines = "2-3" }
   docker run -it ubuntu-24-container /bin/bash
   # Output will be the Docker container prompt
   root@<CONTAINER ID>:/#
   ```

If you already created a container before, reuse it instead of creating a new one.

First, list your containers to find the container ID:

```bash { output_lines = "2-4" }
docker ps -a
# Output
CONTAINER ID  IMAGE                    COMMAND      CREATED        STATUS                       PORTS  NAMES
0123456789ab  ubuntu-24-container  "/bin/bash"  27 hours ago   Exited (255) 59 minutes ago.        container_name
```

Then start the container and attach a shell:

```bash
docker start 0123456789ab
docker exec -it 0123456789ab /bin/bash
```

Once you’re inside the container, move to your home directory:

```bash
cd /root
```

## Install dependencies

Install the packages ExecuTorch needs to build. If you’re not running as root, prefix the commands with `sudo`.

   ```bash
   apt update
   apt install -y \
     python-is-python3 python3.12-dev python3.12-venv python3-pip \
     gcc g++ \
     make cmake \
     build-essential \
     ninja-build \
     libboost-all-dev
   ```

## Create a Python virtual environment

Create and activate a virtual environment so your Python packages stay scoped to this project:
   ```bash { output_lines = "3" }
   python3 -m venv .venv
   source .venv/bin/activate
   ```

## Get the ExecuTorch source code

Clone ExecuTorch and initialize its submodules:

   ```bash
   git clone https://github.com/pytorch/executorch.git
   cd executorch
   git fetch --tags
   git checkout c70a742344e30158dc370d7d35d60ed07660fee0
   git submodule sync
   git submodule update --init --recursive
   ```

{{% notice EthosUCompileSpec parameters %}}
The `EthosUCompileSpec` parameters used in this guide:

| Parameter         | Value                 | Description                                    |
| ----------------- | --------------------- | ---------------------------------------------- |
| `target`          | `ethos-u65-256`       | Targets the Ethos-U65 with 256 MAC units       |
| `system_config`   | `Ethos_U65_High_End`  | High-end system configuration for optimal performance |
| `memory_mode`     | `Shared_Sram`         | Uses shared SRAM memory mode                   |
{{% /notice %}}

## What you've learned and what's next

In this section you've:

- Set up an Ubuntu 24.04 Docker container for building ExecuTorch (macOS users)
- Installed required dependencies and created a Python virtual environment
- Cloned the ExecuTorch repository and checked out the correct version

With your build environment configured and the ExecuTorch source checked out, the next step is building and installing the ExecuTorch package.
