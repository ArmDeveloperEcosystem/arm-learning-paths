---
# User change
title: "Build and run the Arm CCA stack on an Arm FVP with RME extensions"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin

You need atleast 30 GB of free disk space on your machine to build the software stack.

Install `git` and other packages required to run the FVP:

```console
sudo apt update && sudo apt install git telnet xterm net-tools
```

Install [docker engine](/install-tools/docker/docker-engine) on your machine. You will build the software stack in a docker container which contains all the build dependencies for the software stack.

```

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

Create a directory to store the software source files. Then run the container and mount this directory on the host inside the container:

```console
mkdir ~/cca-stack
./container.sh -v ~/cca-stack run
```

You are now inside the root directory of the `aemfvp-builder` container and ready to build the software stack.

## Build the reference CCA software stack

Inside the running container, change directory into the mounted directory. 



