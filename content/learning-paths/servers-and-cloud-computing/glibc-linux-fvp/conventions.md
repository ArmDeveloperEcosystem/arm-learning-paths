---
title: Development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will install packages and review the directory structure used throughout the learning path.

## Install dependencies

Run the following commands to make sure the necessary dependencies are installed on your host machine:

```bash
sudo apt update && sudo apt install -y \
    git make bash \
    flex bison build-essential libssl-dev bc libelf-dev libncurses-dev \
    python3 python3-pip python-is-python3 python3-venv wget xz-utils coreutils
```

Install GCC to cross compile Linux applications:
```bash
sudo apt install gcc-aarch64-linux-gnu -y
```

{{% notice Note%}}
The GCC cross toolchain installation directory contains everything a cross toolchain would need, for example, the path to the `gcc` tool would be `/usr/bin/aarch64-linux-gnu-gcc`. 
{{% /notice %}}

Install Docker, refer to the [Docker install guide](/install-guides/docker/).


## Directory Structure

In the following sections you will checkout sources and build various tools on your Linux host machine. Before you begin, lets look at the directory structure of where you will build the different parts of software stack needed to run this learning path.

Table 1. Directory layout

| Path                                 | Description                           |
|--------------------------------------|---------------------------------------|
| `$HOME`                         | Home directory of your host non-root user  |
| `$HOME/workspace`               | Workspace directory                        |
| `$HOME/workspace/linux`         | Folder with the Linux kernel sources       |
| `$HOME/workspace/linux-headers` | Directory for installing kernel headers    |
| `$HOME/workspace/linux-build`   | Folder for the Linux kernel build output   |
| `$HOME/workspace/glibc`         | Folder for the Glibc sources               |
| `$HOME/workspace/glibc-build`   | Directory for the Glibc build output       |

