---
title: Conventions
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

For a few things you may need root access on your host system to do minimal setup and
install packages that are described in the following sections.

## Naming conventions

In the following sections we use host system to checkout sources and build various
tools and we also make configuration changes to the guest system that will run on
the Arm [Fixed Virtual Platform (FVP)][1] model.

Before we begin, it's important to describe the specifics of our setup making it easier
to write commands and code examples. Wherever possible we use generic commands and code
examples but in certain places we have to use hardcoded values and absolute paths.

Table 1. Directory layout

| Path                                 | Description                                |
|--------------------------------------|--------------------------------------------|
| `/path/to/cross/gcc`                 | GCC cross toolchain installation directory |
| `/home/user`                         | Home directory of your host non-root user  |
| `/home/user/workspace`               | Workspace directory                        |
| `/home/user/workspace/linux`         | Folder with the Linux kernel sources       |
| `/home/user/workspace/linux-headers` | Directory for installing kernel headers    |
| `/home/user/workspace/linux-build`   | Folder for the Linux kernel build output   |
| `/home/user/workspace/glibc`         | Folder for the Glibc sources               |
| `/home/user/workspace/glibc-build`   | Directory for the Glibc build output       |



We presume that the GCC cross toolchain installation directory contains everything a
cross toolchain would need, for example, the path to the `gcc` tool would be
`/path/to/cross/gcc/bin/aarch64-none-linux-gnu-gcc`.

In the next steps we create a Python virtual environment. It doesn't matter where
it is located, but to avoid ambiguity let's presume it is in `~/workspace/venv`.

[1]: https://developer.arm.com/downloads/-/arm-ecosystem-fvps
