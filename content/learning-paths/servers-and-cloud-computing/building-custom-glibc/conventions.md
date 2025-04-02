---
title: Naming Conventions
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You may need root access on your host system to do minimal setup and install packages that are described in the following sections.

## Naming conventions

In the following sections we use host system to checkout sources and build various
tools and we also make configuration changes to the guest system that will run on
the Arm [Fixed Virtual Platform (FVP)][1] model.


The GCC cross toolchain directory should include all necessary tools. For example, the `gcc` tool path would be `/path/to/cross/gcc/bin/aarch64-none-linux-gnu-gcc`. 

**Please Note**: The cross compiler available from your distribution through a package manager is not suitable to explore architectural features and user needs to build your own custom GNU cross compiler. Please read [this resource ](https://wiki.osdev.org/GCC_Cross-Compiler#Using_the_new_Compiler) for further explanation. 


Tools must be installed in the specified paths for clarity and best practices. 


Table 1. Directory layout

| Path                                 | Description                                |
|--------------------------------------|--------------------------------------------|
| `/path/to/cross/gcc`                 | GCC cross toolchain installation directory |
| `/home/user`                         | Home directory of your host non-root user  |
| `/home/user/shrinkwrap`              | Directory of shrinkwrap installation       |
| `/home/user/workspace`               | Workspace directory                        |
| `/home/user/workspace/linux`         | Folder with the Linux kernel sources       |
| `/home/user/workspace/linux-headers` | Directory for installing kernel headers    |
| `/home/user/workspace/linux-build`   | Folder for the Linux kernel build output   |
| `/home/user/workspace/glibc`         | Folder for the Glibc sources               |
| `/home/user/workspace/glibc-build`   | Directory for the Glibc build output       |





In the next steps we create a Python virtual environment. It doesn't matter where
it is located, but to avoid ambiguity let's presume it is in `~/workspace/venv`.

[1]: https://developer.arm.com/downloads/-/arm-ecosystem-fvps