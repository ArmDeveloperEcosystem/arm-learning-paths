---
title: Check the Zena CSS Linux guest
description: Check the Zena CSS Linux guest's architecture, tools, and storage before building a CPU workload.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the Zena CSS Linux guest

Start from the Linux console or SSH shell prepared in the Zena CSS onboarding Learning Path. Check this guest before downloading source code or a model. The required tools and free space depend on the actual EWAOL image and chamber configuration.

## Record the environment

Run these commands in the **Primary Compute Linux guest**:

```bash
cat /etc/os-release; uname -m; uname -r; cat /sys/devices/system/cpu/online; grep -E '^(MemTotal|MemAvailable):' /proc/meminfo; df -h /
```

The guest reports an Arm64 architecture, commonly `aarch64`, and shows its own CPU, memory, and root-filesystem values. The tested setup used ANA 2026.02 on a g4 chamber without changing the supplied Zena VP's CPU or memory settings. ANA Lab Manager showed **Simulation CPUs: 4**; the Linux output below shows **16 online CPUs** (`0-15`) and the EWAOL image's approximately 8 GB of usable guest memory. Use the Linux output when describing guest-visible CPUs; do not read the ANA simulation setting as a Linux core count.

```
ID=ewaol
NAME="Edge Workload Abstraction and Orchestration Layer"
VERSION="v2.1.0 (styhead)"
VERSION_ID=v2.1.0
VERSION_CODENAME="styhead"
PRETTY_NAME="Edge Workload Abstraction and Orchestration Layer v2.1.0 (styhead)"
CPE_NAME="cpe:/o:openembedded:ewaol:v2.1.0"
aarch64
6.6.54-yocto-standard
0-15
MemTotal:        8120232 kB
MemAvailable:    7856280 kB
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        28G  1.3G   25G   5% /
```

## Check build and transfer tools

See which tools are available in this guest:

```bash
for tool in git cmake make gcc g++ wget sha256sum tar; do
    command -v "$tool" || printf 'Missing: %s\n' "$tool"
done
```

The later pages need a C/C++ compiler, Make, CMake, Git, a model transfer method, and a SHA-256 utility. If a tool is missing, record it before proceeding. Do not install a package from an unrelated Linux distribution into the EWAOL image.

```
/usr/bin/git
Missing: cmake
/usr/bin/make
/usr/bin/gcc
/usr/bin/g++
/usr/bin/wget
/usr/bin/sha256sum
/usr/bin/tar
```

## Set the work directory

The Zena guest shown above has 25 GB available on its root filesystem. Use one directory under `/root` for the source, build, model, and results:

```bash
LP2_WORK_DIR=/root/zena-llamacpp
mkdir -p "$LP2_WORK_DIR"
```

The tested run used this directory for the source, build, model, and result archive. The root filesystem had 25 GB available before these files were created.

If your guest has less available space, choose a directory on a filesystem with enough capacity before running the next page. Keep this shell open so `LP2_WORK_DIR` remains set.

ANA's **Auto Shutdown** duration is configurable. Check the selected duration in Lab Manager before starting the build, and plan to save your work before the VP stops.

## What you have learned

You have identified the Linux guest and set a work directory for the workload. The next page builds llama.cpp using the tools available in this image.
