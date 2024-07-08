---
# User change
title: "Before you start"

weight: 2 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
You can use a variety of open source tools and Linaro Forge to learn how to debug and optimize parallel applications.

## Before you begin

You will need an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or any Arm server or laptop running Linux.

The instructions are tested on Ubuntu 20.04. Other Linux distributions are possible with some modifications.

### Install the required software

1. Install Linaro Forge 

Follow the instructions in the [Linaro Forge install guide](/install-guides/forge/).

You can confirm Forge is installed by running:

```bash
ddt --version
```

2. Install the required Linux software

Use the Linux package manager to install the required tools:

```bash
sudo apt update
sudo apt install -y make mpich \
  python-is-python3 python3-dev python3-numpy python3-scipy python3-mpi4py \
  lsb-release \
  bc \
  build-essential \
  gfortran \
  git \
  openmpi-bin \
  linux-tools-common linux-tools-generic linux-tools-`uname -r` \
  dos2unix \
  libblas-dev \
  libx11-xcb1 libice6 libsm6 libopenmpi-dev \
  libc6 libglapi-mesa libxdamage1 libxfixes3 libxcb-glx0 libxcb-dri2-0 \
  libxcb-dri3-0 libxcb-present0 libxcb-sync1 libxshmfence1 libxxf86vm1

sudo ln -s /usr/bin/f2py3 /usr/bin/f2py
```

3. Enable profiling

Your Linux distribution may not allow some types of user profiling.

Allow profiling with `perf` by running:

```bash
sudo sysctl -w kernel.perf_event_paranoid=1
```

4. Download the example code

The example code is contained in a package you can download. 

Use `wget` to download the example code:

```bash
wget https://developer.arm.com/-/media/Files/downloads/hpc/aas-forge-trials-package/arm_hpc_tools_trial.tar.gz
tar xf arm_hpc_tools_trial.tar.gz
cd arm_hpc_tools_trial
```

5. Change the format of the example files

The example code files are formatted with DOS line endings and need to be converted to Linux format.

Use a text editor to create a new file named `d2u.sh` and copy the contents below into the file:

```bash
#!/bin/bash

dos2unix ./src/C/mmult.c
dos2unix ./src/F90/mmult.F90
dos2unix ./src/make.def
dos2unix ./src/Py/F90/mmult.F90
dos2unix ./src/Py/C/mmult.c
```

6. Run the script to convert the files to unix format:

```bash
bash ./d2u.sh
```

You are now ready to start learning about parallel application development.
