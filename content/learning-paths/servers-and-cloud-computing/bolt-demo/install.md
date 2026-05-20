---
title: Install BOLT on Linux
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install BOLT on Linux

This guide requires LLVM BOLT 22.1.0 or later for SPE profiling and required options.
Package manager versions might be older, so verify the installed version before continuing.


## Install BOLT from LLVM releases

Install BOLT from a prebuilt [LLVM release](https://github.com/llvm/llvm-project/releases).
This method provides a consistent version across systems. It also lets you use newer releases when available.
The following example uses LLVM 22.1.5, the latest LLVM release available at the time of writing (May 2026).

{{% notice Please Note %}}

If you are using a 1st generation Arm AGI CPU, we recommend installing the latest LLVM release to ensure support for the processor. However due to backwards compatibility, LLVM BOLT 22.1.0 or later can still be used to complete this learning path.

Arm AGI CPU support is expected to be introduced no earlier than LLVM 23. 

{{% /notice %}}


Download and extract LLVM:

```bash
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-22.1.5/LLVM-22.1.5-Linux-ARM64.tar.xz
tar xf LLVM-22.1.5-Linux-ARM64.tar.xz
```

Add LLVM tools to your PATH:

```bash
export PATH="$(pwd)/LLVM-22.1.5-Linux-ARM64/bin:$PATH"
```


## Install BOLT using a package manager

Use a package manager if you prefer a system-managed installation. Package versions depend on your Linux distribution.



{{< tabpane code=true >}}

{{< tab header="Ubuntu/Debian" language="bash">}}
sudo apt update
sudo apt install llvm-bolt
{{< /tab >}}

{{< tab header="Fedora" language="bash">}}
sudo dnf install llvm-bolt
{{< /tab >}}

{{< tab header="openSUSE" language="bash">}}
sudo zypper install llvm-bolt
{{< /tab >}}

{{< /tabpane >}}


BOLT is available on Ubuntu 25.04 and later, Debian 13 and later, Fedora 42 and later, and on openSUSE Tumbleweed.

## Verify the installation

```bash
llvm-bolt --version
```

The command prints the BOLT version. If the command fails, check your PATH.
