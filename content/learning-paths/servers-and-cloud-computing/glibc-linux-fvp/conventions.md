---
title: Development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will install packages and review some naming conventions used throughout the learning path.

## Before you begin

Run the following commands to make sure the necessary dependencies are installed on your host machine:

```bash
sudo apt update && sudo apt install -y \
    gcc-aarch64-linux-gnu docker.io git make bash \
    flex bison build-essential libssl-dev bc libelf-dev libncurses-dev \
    python3 python3-pip python-is-python3 python3-venv wget xz-utils coreutils
```

You also need to install the right toolchain for your setup. Go to the downloads page on Developer Hub.

https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads

```bash
sudo systemctl enable --now docker
```

Verify that docker is running. You should see the output below as a result of this command:
```bash
sudo systemctl status docker
```

```output
Active: active (running)
```

## Naming conventions

For a few things you may need root access on your host system to do minimal setup and
install packages that are described in the following sections.

In the following sections we use host system to checkout sources and build various
tools and we also make configuration changes to the guest system that will run on
the Arm [Fixed Virtual Platform (FVP)][1] model.

Before we begin, it's important to describe the specifics of our setup making it easier
to write commands and code examples. Wherever possible we use generic commands and code
examples but in certain places we have to use hardcoded values and absolute paths.

Table 1. Directory layout

| Path                       | Description                                |
|----------------------------|--------------------------------------------|
| `/path/to/cross/gcc`       | GCC cross toolchain installation directory |
| `/home/user` or `$HOME`    | Home directory of your host non-root user  |
| `/home/user/linux`         | Folder with the Linux kernel sources       |
| `/home/user/linux-headers` | Directory for installing kernel headers    |
| `/home/user/linux-build`   | Folder for the Linux kernel build output   |
| `/home/user/glibc`         | Foldr for the Glibc sources                |
| `/home/user/glibc-build`   | Directory foir the Glibc build output      |



We presume that the GCC cross toolchain installation directory contains everything a
cross toolchain would need, for example, the path to the `gcc` tool would be
`/path/to/cross/gcc/bin/aarch64-none-linux-gnu-gcc`.

[1]: https://developer.arm.com/downloads/-/arm-ecosystem-fvps
