---
# User change
title: "Run the Arm CCA stack using a pre-built docker container"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

You will need at least 30 GB of free disk space on your machine to run the docker container with the Arm CCA reference software stack.

## Overview

The Arm Confidential Compute Architecture (CCA) enables the construction of protected execution
environments called Realms. Realms allow lower-privileged software, such as an application or a virtual machine, to
protect its content and execution from attacks by higher-privileged software, such as an OS or a hypervisor. Realms provide an environment for confidential computing, without requiring the Realm owner to trust the software components that manage the resources used by the Realm.

The Arm Realm Management Extension (RME) is an Arm v9-A architecture extension. It defines the set of hardware features and properties that are required to comply with the Arm CCA architecture. RME introduces a new security state "Realm world", in addition to the traditional Secure and Non-secure states.

In this learning path, you will learn how to run the reference integration software stack for Arm CCA in a pre-built docker container. Shown below is a graphical depiction of the software stack you will run on your development machine:

![img #center](cca-stack-overview.png)

Within the pre-built docker container, you will learn how to create a Realm that runs a guest Linux kernel and run a simple application within the Realm. This learning path focuses on the common pattern of using a Realm to protect an entire virtual machine.

## Download the docker image

Start by downloading the docker container image. This docker image contains the pre-built binaries for the Arm CCA reference software stack and the Armv-A Base Architecture Envelop Model (AEM) FVP with support for RME extensions. 

Install [docker engine](/install-guides/docker/docker-engine) on your machine.

Pull the docker image from DockerHub:

```console
docker pull armswdev/aemfvp-cca-image
```
Confirm that the docker container image was downloaded successfully:

```console
docker image list
```

The output should be similar to:

```output
REPOSITORY        				TAG       IMAGE ID       CREATED       SIZE
armswdev/aemfvp-cca-image   	arm64     cf2cfc5c6391   3 days ago     26.2GB
```
Run the docker container:

```console
docker run -it armswdev/aemfvp-cca-image /bin/bash
```
You are now inside the `/tmp/cca-stack` directory of the running `armswdev/aemfvp-cca-image` container.

```output
ubuntu@84eb170a69b9:/tmp/cca-stack$
```

## Run the software stack

The pre-built binaries for the Arm CCA reference software stack are present in the `output/aemfvp-a-rme` directory. 

```console
ls output/aemfvp-a-rme/
```
This includes the Trusted Firmware binaries, the host root filesystem and the host Linux kernel image:

```output
bl1.bin  fip.bin  fip-std-tests.bin  host-fs.ext4  Image
```

These binaries can run on an Armv-A Base Architecture Envelop Model (AEM) FVP with support for RME extensions. AEM FVPs are fixed configuration virtual platforms of Armv8-A and Armv9-A architectures with comprehensive system IP. The FVP is also contained within this docker container.

Launch the `run-cca-fvp.sh` script to run the Arm CCA pre-built binaries on the FVP:

```console
./run-cca-fvp.sh
```

{{% notice Note %}}
A number of `Info` and `Warning` messages will be emitted by the FVP. These can safely be ignored.
{{% /notice %}}

The `run-cca-fvp.sh` script uses the `screen` command to connect to the different UARTs in the FVP.  

You should see the host Linux kernel boot on your terminal:

```output
udhcpc: started, v1.31.1
udhcpc: sending discover
udhcpc: sending select for 172.20.51.1
udhcpc: lease of 172.20.51.1 obtained, lease time 86400
deleting routers
adding dns 172.20.51.254
FAIL
Starting dropbear sshd: OK

Welcome to Buildroot
buildroot login:
```

You will be prompted to log in to buildroot. Enter `root` as both the username and password.

You have successfully booted four worlds (Root, Secure, Non-secure and Realm) on the FVP at this point. Trusted Firmware-A is running in root, Realm Management Monitor (RMM) in Realm, host Linux in Non-secure and Hafnium in Secure. 

## Create a virtual guest in a Realm

Guest VMs can be launched in a Realm using `kvmtool` from your host Linux prompt. The kernel `Image` and filesystem `realm-fs.ext4` for the Realm are packaged into the buildroot host file system.

Use `kvmtool` to launch guest Linux in a Realm:

```console
lkvm run --realm -c 2 -m 256 -k /realm/Image -d /realm/realm-fs.ext4 -p earlycon
```
You should see the guest Linux kernel starting to boot in a Realm. This step can take several minutes.

After boot up, you will be prompted to log in at the guest Linux buildroot prompt. Use `root` again as both the username and password.

```output
Starting network: udhcpc: started, v1.31.1
udhcpc: sending discover
udhcpc: sending select for 192.168.33.15
udhcpc: lease of 192.168.33.15 obtained, lease time 14400
deleting routers
adding dns 172.20.51.254
OK
Starting dropbear sshd: OK

Welcome to Buildroot
buildroot login:
```
You have successfully created a virtual guest in a Realm using the Arm CCA reference software stack.

To shutdown the guest, use the `poweroff` command.

You should see the following output from the guest:

```output
Stopping dropbear sshd: OK
Stopping network: OK
Saving random seed: OK
Stopping klogd: OK
Stopping syslogd: OK
umount: devtmpfs busy - remounted read-only
[   42.595975] EXT4-fs (vda): re-mounted 9e9fa588-c41f-404a-a627-6616bb8491b1 ro. Quota mode: none.
The system is going down NOW!
Sent SIGTERM to all processes
logout
Sent SIGKILL to all processes
Requesting system poweroff
[   44.697156] reboot: Power down
  Info: KVM session ended normally.
```
The guest has shut down and you are back at the host Linux kernel prompt.

To exit the simulation, use `Ctrl-a + d`. You will be placed back into the running docker container. 

To exit the docker container, run `exit`.

In the next section, you will learn how to run a simple application inside the Realm.
