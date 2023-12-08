---
# User change
title: Pointer Authentication on Arm

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify
layout: "learningpathall"
---
## Basics of Pointer Authentication

`Return Oriented Programming` (`ROP`) is a software attack where the attacker corrupts the return address stored in the stack to point it to somewhere in the application with a useful sequence of instructions, ending in an indirect branch. These sequences are known as `gadgets`, and are prevalent in most code. By chaining multiple gadgets, the attacker can mislead the program to perform actions that end up in a security compromise. An example of such a security compromise is spawning an interactive shell.

Pointer Authentication is a feature, available for `Armv8.3-A` and `Armv9.0-A` (and later) Arm architectures, to provide some protection against such attacks. A `Pointer Authentication Code` (`PAC`) is generated from the value of a given pointer, and is used to verify pointers before using them.

If attackers attempt to modify such a pointer in memory they will also need to compute the right `PAC` signature for it. Using the ROP example, if the return address stored in the stack is signed and verified before returning to it, the attacker will not be able to control the program flow and an exception is raised.

Generation and use of `PAC` in applications requires compiler support, as function calls and returns will need to be modified. This Learning Path will help you understand the impact of protecting your code in this way..

See [Code reuse attacks: the compiler story](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/code-reuse-attacks-the-compiler-story) for a deeper discussion.

## Arm CPU Pointer Authentication Support Table

Below is a table which lists which Arm processors support Pointer Authentication.

| CPU         | Pointer Auth | Arm ISA version | Notes                               |
|-------------|:------------:|:---------------:|:-----------------------------------:|
| Neoverse V2 | Yes          | Armv9.0-A       |                                     |
| Neoverse N2 | Yes          | Armv9.0-A       |                                     |
| Neoverse E2 | Yes          | Armv9.0-A       |                                     |
| Neoverse V1 | Yes          | Armv8.4-A       | Does not support optional FEAT_EPAC |
| Neoverse N1 | No           | Armv8.2-A       |                                     |
| Neoverse E1 | No           | Armv8.2-A       |                                     |

If you are looking for cloud instances with Pointer Authentication, AWS instances with Graviton3 processors are a good place to start (C7g, M7g, and R7g).

## Preparation for exercise the following sections

Install [GCC](/install-guides/gcc/native/) and other tools. The commands for using the `apt` package manager are below. Similar commands are possible with other package managers (such as `yum`).

```console
sudo apt update
sudo apt install gcc make gdb-multiarch -y
```

## Configure Pointer Authentication in the Linux kernel

{{% notice Note %}}
The information below explains how to disable pointer authentication. This not recommended, but you may want to do it for experimentation purposes.
{{% /notice %}}

Pointer Authentication is a recommended security feature, and is enabled by default in Linux distributions. However, it is possible to turn off Pointer Authentication for debug or performance investigations. It can be disabled with a kernel configuration parameter, or if the the kernel was compiled with Pointer Authentication enabled, it can be disabled with a kernel boot parameter change.

Kernel configuration:
```
CONFIG_ARM64_PTR_AUTH=n
```

Kernel boot parameter:
```
abi.ptrauth_disabled=1
```