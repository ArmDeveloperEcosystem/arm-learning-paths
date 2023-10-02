---
# User change
title: "Build and run the Arm CCA stack on an Arm FVP"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin

You need atleast 30 GB of free disk space on your machine to build the software stack.

Install `git` and the packages required to run the FVP:

```console
sudo apt update && sudo apt install git telnet xterm net-tools
```

Install [docker engine](/install-guides/docker/docker-engine) on your machine. You will build the software stack in a docker container which contains all the build dependencies for the software stack.


## Build the docker container

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

The binary executables built in the previous step can run on Arm Architecture Envelop Model (AEM) FVP with RME extensions. 

On your host machine, download and extract this FVP:

```console
cd ~/cca-stack
https://developer.arm.com/-/media/Files/downloads/ecosystem-models/FVP_Base_RevC-2xAEMvA_11.23_9_Linux64_armv8l.tgz
tar -xvzf FVP_Base_RevC-2xAEMvA_11.23_9_Linux64_armv8l.tgz
```

Set the `MODEL` variable to point to the FVP executable. Launch the `boot.sh` script to run the binaries on the FVP:

```console
export MODEL=~/cca-stack/Base_RevC_AEMvA_pkg/models/Linux64_armv8l_GCC-9.3/FVP_Base_RevC-2xAEMvA
./model-scripts/aemfvp-a-rme/boot.sh -p aemfvp-a-rme shell
```

You should see four terminal windows pop up. 

You should see the host linux kernel boot up on terminal_0. You will then be prompted to login to buildroot. Enter `root` as both the username and password.

[img_1]

## Create a virtual guest in a realm

You can now run `kvmtool` from your host linux prompt to launch a realm which runs guest linux. The kernel and filesystem for the realm are packaged into the buildroot host file system.

You should see the guest linux kernel boot up in a realm and you will be presented with a buildroot prompt. To log into the realm, use `root` again as boot the username and password.

[img_2]

You have successfully created a virtual guest in a realm using the Arm CCA reference software stack.
