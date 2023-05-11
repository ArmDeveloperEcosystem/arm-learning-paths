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

## AWS Graviton3

The [AWS C7g EC2](https://aws.amazon.com/ec2/instance-types/c7g/) instances are powered by AWS Graviton3, which uses the [Arm Neoverse V1](https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-v1) processor, and includes Pointer Authentication.

For instructions on how to create an AWS instance, see [this article](/learning-paths/servers-and-cloud-computing/csp/aws).

The instance type should start with `c7g`. This Learning Path assumes `Ubuntu` as the operating system.

{{% notice Note %}}
Earlier Graviton platforms do NOT support Pointer Authentication.
{{% /notice %}}

## Prepare your c7g instance

Install [GCC](/install-guides/gcc/native/) and other build tools to proceed.

```console
sudo apt update
sudo apt install gcc make gdb-multiarch -y
```
