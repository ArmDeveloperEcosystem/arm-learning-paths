---
# User change
title: "Run the Arm CCA stack on an Arm FVP using a ready-made docker container"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin

You will need at least 30 GB of free disk space on your machine to run the docker container with the Arm CCA reference software stack.

## Overview

The Arm Confidential Compute Architecture (CCA) enables the construction of protected execution
environments called Realms. Realms allow lower-privileged software, such as an application or a virtual machine to
protect its content and execution from attacks by higher-privileged software, such as an OS or a hypervisor. Realms provide an environment for confidential computing, without requiring the Realm owner to trust the software components that manage the resources used by the Realm.

The Arm Realm Management Extension (RME) is an Arm v9-A architecture extension and defines the set of hardware features and properties that are required to comply with the Arm CCA architecture. RME introduces a new security state "Realm world", in addition to the traditional Secure and Non-Secure states.

In this learning path, you will learn how to run the reference integration software stack for Arm CCA in a ready-made docker container. Within this container, you will learn how to create a Realm that runs a guest Linux kernel and run a simple application within the Realm. 

## Download the docker image

For your convenience, the pre-built Arm CCA reference software stack and the Armv-A Base Architecture Envelop Model (AEM) FVP with support for RME extensions are made available in a docker container. 

Install [docker engine](/install-guides/docker/docker-engine) on your machine.

Pull the docker image from DockerHub:

```console
docker pull armswdev/aemfvp-cca-image
```
Confirm that the docker container image was dowloaded successfully:

```
docker image list
```

The expected output is:

```output
REPOSITORY        TAG       IMAGE ID       CREATED       SIZE
aemfvp-builder    latest    2fa7ce18f57a   7 mins ago    1.83GB
```
You can now run the docker container:

```console
docker run -it armswdev/aemfvp-cca-image /bin/bash
```

You should see the following output:

```output
Running docker image: aemfvp-builder ...
ubuntu@ip-172-16-0-235:/$
```

You are now inside the `/tmp/cca-stack` directory of the `armswdev/aemfvp-cca-image` container.

## Inspect the docker container

The binary executables are built in the `~/cca-stack/output/aemfvp-a-rme` directory.


## Run the software stack

The pre-built binary executables can run on an Armv-A Base Architecture Envelop Model (AEM) FVP with support for RME extensions. AEM FVPs are fixed configuration virtual platforms of Armv8-A and  Armv9-A architectures with comprehensive system IP. The FVP is also contained within this docker container.

Launch the `run-cca-fvp.sh` script to run the binaries on the FVP:

```console
./run-cca-fvp.sh
```

{{% notice Note %}}
A number of `Info` and `Warning` messages will be emitted by the FVP. These can safely be ignored.
{{% /notice %}}

The FVP boots up with the binaries. The `run-cca-fvp-.sh` script uses the `screen` command to connect to the different UARTs in the FVP.  

You should see the host Linux kernel boot on your terminal. You will be prompted to login to buildroot. Enter `root` as both the username and password.

![img_1 #center](./cca-img1.png)


You have successfully booted four worlds (Root, Secure, Non-secure and Realm) on the FVP at this point. Trusted Firmware-A is running in root, RMM in Realm, host Linux in non-secure and Hafnium in secure. 

## Create a virtual guest in a Realm

Guest VMs can be launched in a Realm using `kvmtool` from your host Linux prompt. The kernel `Image` and filesystem `realm-fs.ext4` for the Realm are packaged into the buildroot host file system.

```console
lkvm run --realm -c 2 -m 256 -k /realm/Image -d /realm/realm-fs.ext4 -p earlycon
```

You should see the guest Linux kernel starting to boot in a Realm. This step can take several minutes.

After boot up, you will be prompted to login at the guest Linux buildroot prompt. Use `root` again as both the username and password.

![img_3 #center](./cca-img3.png)


You have successfully created a virtual guest in a Realm using the Arm CCA reference software stack.

In the next section you will learn how to run a simple hello world application in the virtual guest running in a Realm.
