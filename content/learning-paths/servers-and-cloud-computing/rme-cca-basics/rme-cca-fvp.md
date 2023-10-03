---
# User change
title: "Build and run the Arm CCA stack on an Arm FVP"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin

You need atleast 30 GB of free disk space on your machine to build the software stack.

Install the necessary packages:

```console
sudo apt update && sudo apt install git telnet xterm net-tools
```

## Overview

The Arm Confidential Compute Architecture (Arm CCA) enables the construction of protected execution
environments called Realms. Realms allow lower-privileged software, such as application or a virtual machine to
protect its content and execution from attacks by higher-privileged software, such as an OS or a hypervisor. Realms provide an environment for confidential computing, without requiring the Realm owner to trust the software components that manage the resources used by the Realm.

The Arm Realm Management Extension (RME) architecture defines the set of hardware features and properties that are required to comply with the Arm CCA architecture. RME introduces a new security state "Realm world", in addition to the traditional Secure and Non-Secure states.

In this learning path, you will learn how to build and run the reference integration software stack for Arm CCA which demonstrates support for Arm's Realm Management Extension (RME) architecture feature. You will also learn how to create a realm that runs a guest linux kernel. 

## Build the docker container

You will build the Arm CCA reference software stack in a docker container which contains all the build dependencies. 
Install [docker engine](/install-guides/docker/docker-engine) on your machine.

Clone the repository that contains the docker container file and utility scripts:

```console
git clone --branch AEMFVP-A-RME-2023.09.29 https://git.gitlab.arm.com/arm-reference-solutions/docker.git
```
Build the docker container:

```console
cd docker
./container.sh build
```
The script `container.sh` defines the docker file and image name used to create the container.

Confirm that the docker container image was built successfully:

```
docker image list
```

The expected output is:

```output
REPOSITORY        TAG       IMAGE ID       CREATED       SIZE
aemfvp-builder    latest    2fa7ce18f57a   7 mins ago    1.83GB
```

Create a directory on your host machine to store the software source files. Then run the container and mount this directory inside the container:

```console
mkdir ~/cca-stack
./container.sh -v ~/cca-stack run
```

You are now inside the root directory of the `aemfvp-builder` container and ready to build the software stack.

## Build the reference CCA software stack

You can build the Arm CCA software stack in your running container using a manifest file. The manifest file is a collection of all component repositories needed to build this reference stack. 

Inside the running container, change directory into the mounted directory.
Use the repo tool and the manifest file to download the software stack:

```console
cd ~/cca-stack
repo init -u https://git.gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-manifest.git -m pinned-aemfvp-a-rme.xml -b refs/tags/AEMFVP-A-RME-2023.09.29
repo sync -c -j $(nproc) --fetch-submodules --force-sync --no-clone-bundle
```

Build the stack:

```console
./build-scripts/aemfvp-a-rme/build-test-buildroot.sh -p aemfvp-a-rme all
```

The binary executables are built in the `~/cca-stack/output/aemfvp-a-rme` directory.
You can now exit the docker container.

```console
exit
```

## Run the software stack

The binary executables built in the previous step can run on an Armv-A Base Architecture Envelop Model (AEM) FVP with support for RME extensions. AEM FVPs are fixed configuration virtual platforms of Armv8-A and  Armv9-A architectures with comprehensive system IP.  

On your host machine, download and extract this FVP:

```console
cd ~/cca-stack
https://developer.arm.com/-/media/Files/downloads/ecosystem-models/FVP_Base_RevC-2xAEMvA_11.23_9_Linux64_armv8l.tgz
tar -xvzf FVP_Base_RevC-2xAEMvA_11.23_9_Linux64_armv8l.tgz
```

Create an environment variable `MODEL` and set it to point to the FVP executable. Launch the `boot.sh` script to run the binaries on the FVP:

```console
export MODEL=~/cca-stack/Base_RevC_AEMvA_pkg/models/Linux64_armv8l_GCC-9.3/FVP_Base_RevC-2xAEMvA
./model-scripts/aemfvp-a-rme/boot.sh -p aemfvp-a-rme shell
```

{{% notice Note %}}
A number of `Info` and `Warning` messages will be emitted by the FVP. These can safely be ignored.

If you see an error of the form `xterm: Xt error: Can't open display:`, ensure that your terminal application (e.g. `PuTTY`) has `X11 forwarding` enabled.
{{% /notice %}}

The FVP boots up with four terminal windows. 

You should see the host linux kernel boot on terminal_0. You will then be prompted to login to buildroot. Enter `root` as both the username and password.

[img_1]


`terminal_3` is connected to the Realm Management Monitor
## Create a virtual guest in a realm

You can now run `kvmtool` from your host linux prompt to launch a realm which runs guest linux. The kernel and filesystem for the realm are packaged into the buildroot host file system.

You should see the guest linux kernel boot up in a realm and you will be presented with a buildroot prompt. To log into the realm, use `root` again as boot the username and password.

[img_2]

You have successfully created a virtual guest in a realm using the Arm CCA reference software stack.
