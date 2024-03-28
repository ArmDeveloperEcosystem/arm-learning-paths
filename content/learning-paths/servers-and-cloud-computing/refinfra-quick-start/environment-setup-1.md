---
title: Environment Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
Arm has developed a suite of [Neoverse Reference Designs](https://developer.arm.com/Tools%20and%20Software/Neoverse%20Reference%20Design) compute sub-systems.

They are supported by free-of-charge [Arm Ecosystem FVPs](https://developer.arm.com/downloads/-/arm-ecosystem-fvps), and complete [software stacks](https://gitlab.arm.com/infra-solutions) to illustrate how these systems boot to Linux.

This learning path is based on the `Neoverse N2` Reference Design (`RD-N2`).

## Environment Setup

Full instructions to setup the environment is given in [Setup the Neoverse Reference Design software stack workspace](https://neoverse-reference-design.docs.arm.com/en/latest/platforms/common/setup-workspace.html).

### Host platform

The host machine can be AArch64 or x86-64 with Ubuntu Linux 22.04.

64GB of free disk space and 32GB of RAM is minimum requirement to sync and build the platform software stack. 48GB of RAM is recommended.

### Install repo

We will start by obtaining the repo tool to simplify the checkout of source code that spans multiple repositories.

Additional instructions are available [here](https://source.android.com/docs/setup/download#installing-repo).

```bash
sudo apt-get update
sudo apt-get install -y repo
```
Verify installation with:
```bash
repo version
```

### Fetch source code

Create a new directory into which you will download the source code and build the stack.

```bash
mkdir rd-infra
cd rd-infra
```

To obtain the manifest, choose a tag of the platform reference firmware.

[RD-INFRA-2023.09.29](https://neoverse-reference-design.docs.arm.com/en/latest/releases/RD-INFRA-2023.09.29/release_note.html) is used here. See the [release notes](https://neoverse-reference-design.docs.arm.com/en/latest/releases/index.html) for more information.

Specify the platform you want the manifest for. In the [manifest repo](https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests) there are a number of available platforms. As per these [instructions](https://neoverse-reference-design.docs.arm.com/en/latest/platforms/common/setup-workspace.html#platform-manifest-names) select `pinned-rdn2.xml`

```bash
repo init -u https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests.git -m pinned-rdn2.xml -b refs/tags/RD-INFRA-2023.12.22
```
The manifest defines repositories of firmware sources, build and model scripts, and linux along with some tooling.

Fetch the sources with the `repo sync` command. This will take a few minutes to complete.
```bash
repo sync -c -j $(nproc) --fetch-submodules --force-sync --no-clone-bundle
```

### Docker setup

Use a `docker` container for the build to improve reliability and reduce dependency on the host OS setup. The reference firmware build system can function in host OS without a container, but this way we don't have to worry about host OS incompatibility in this workbook.

Install docker:
```bash
sudo apt-get install docker.io
```

You must add your username to the docker group and re-login to be able to talk to the docker daemon. Instructions [here](https://docs.docker.com/engine/install/linux-postinstall/).

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
logout
```

You may need to restart the docker service as well:
```bash
sudo service docker restart
```

### Container Setup

Set up a container to perform the build in. A container execution script is provided. See the help for more information.

```bash
cd container-scripts
./container.sh -h
```

Build the default configuration:

```bash
./container.sh build
```
Verify the container was built:

```bash
docker image list
```
Will output similar to:
```output
REPOSITORY        TAG              IMAGE ID       CREATED         SIZE
rdinfra-builder   latest           8729adb0b96c   8 minutes ago   3.07GB
ubuntu            jammy-20230624   5a81c4b8502e   6 months ago    77.8MB
```

Mount the source checkout into the container:
```bash
./container.sh -v /home/ubuntu/rd-infra/ run
```

{{% notice Host based builds %}}
If you do choose to build this on the host, you need to get all the pre-requisites that would otherwise be installed in the container during its creation.

The build system provides a script for this that you must run as `root`:
```bash
sudo ./build-scripts/rdinfra/install_prerequisites.sh
```
{{% /notice %}}
