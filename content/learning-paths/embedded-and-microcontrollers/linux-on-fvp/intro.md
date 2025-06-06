---
title: Introduction to Arm Fixed Virtual Platforms (FVPs)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Arm Fixed Virtual Platforms (FVPs) are simulation models that let you run and test full software stacks on Arm systems before physical hardware is available. They replicate the behavior of Arm CPUs, memory, and peripherals using fast binary translation.

### Why Use FVPs?
FVPs are useful for developers who want to:
- Prototype software before silicon availability
- Debug firmware and kernel issues
- Simulate multicore systems

FVPs provide a programmer's view of the hardware, making them ideal for system bring-up, kernel porting, and low-level debugging.

### Freely Available Arm Ecosystem FVPs
Several pre-built Armv8-A FVPs can be downloaded for free from the [Arm Ecosystem Models](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms#Downloads) page. Categories include:
- Architecture
- Automotive
- Infrastructure
- IoT

A popular model is the **AEMv8-A Base Platform RevC**, which supports Armv8.7 and Armv9-A. The [Arm reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst) is designed for this model. In this Learning Path, you will use the Armv-A Base Platform RevC FVP to get started.

### CPU-Specific Arm Base FVPs
Other FVPs target specific CPU types and come pre-configured with a fixed number of cores. These are often called **CPU FVPs**.

Here are some examples:
- FVP_Base_Cortex-A55x4
- FVP_Base_Cortex-A72x4
- FVP_Base_Cortex-A78x4
- FVP_Base_Cortex-A510x4+Cortex-A710x4

To use these, request access via [support@arm.com](mailto:support@arm.com).

### Setting Up Your Environment
This Learning Path uses the [Arm reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst).

Create a workspace directory to use as a base for this Learning Path.

```
mkdir linux-on-fvp-workspace && cd linux-on-fvp-workspace
export WORKSPACE=$PWD
```

Follow the software user guide to download the stack, up until the point of enabling the network. You can use the workspace directory you just created, instead of creating an additional one. This includes downloading the FVP, installing some dependencies and using a pre-built docker image to set up the packages needed. Install some additional dependencies, and add the FVP binary to your `PATH` environment variable.

```
sudo apt update
sudo apt install bridge-utils net-tools mtools
export PATH=$WORKSPACE/Base_RevC_AEMvA_pkg/models/Linux64_armv8l_GCC-9.3
:$PATH
```

To verify the process, you should be able to run the `build-test-busybox.sh` script.

```
cd $WORKSPACE
docker_run ./build-scripts/aemfvp-a/build-test-busybox.sh -p aemfvp-a all
```

The build will take a few minutes.

{{% notice Note %}}
If you're running into compatibility issues with OpenSSL, you have to install a separate version:

```bash
cd $WORKSPACE
wget https://www.openssl.org/source/openssl-1.1.1.tar.gz
tar -xvzf openssl-1.1.1.tar.gz
cd openssl-1.1.1/
./Configure linux-aarch64 --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib
make -j$(($(nproc)+1))
sudo make install
export LD_LIBRARY_PATH=/usr/local/ssl/lib:${LD_LIBRARY_PATH}
```
{{% /notice %}}

Once configured, you’ll be ready to run and debug Linux on your selected Arm FVP model. Move on to the next section.
