---
# User change
title: "Run a simple application inside a Realm using a ready-made docker container"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin

Make sure you have downloaded the `armswdev/aemfvp-cca-image` docker container.

```console
docker run -it armswdev/aemfvp-cca-image /bin/bash
```

## Create a simple initramfs to boot the guest linux kernel image

Linux kernels contain a gzipped cpio format archive. When the kernel boots up, this archive is extracted into the root filesystem. The kernel then checks whether the root filesystem contains a file named "init" and tries to run it. At this point the kernel is done booting, and the "init" application executes the system the rest of the way. 

In this learning path, you will package a simple hello world application into the initramfs for the guest linux kernel. 

## Create a simple initramfs

Create a directory in which you will build the simple initramfs:

```console
mkdir ~/FM-share
cd ~/FM-share
```
Using a file editor of your choice, create a file named `hello.c` in this directory. Copy the contents below into the file:

```console
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
  printf("Hello from the Realm!\n");
  sleep(99);
}
```
Now compile the application as the init executable and package it into the initramfs:

```console
aarch64-linux-gnu-gcc -static hello.c -o init
echo init | cpio -o -H newc | gzip > test.cpio.gz
```
`test.cpio.gz` is the compressed archive you will use as the initramfs for the guest linux kernel.


## Run 

Start the docker container with the `FM-share` directory mounted:

```console
docker run -v ~/FM-share:/home/ubuntu/FM-share -it armswdev/aemfvp-cca-image /bin/bash
```
```console
./run-cca-fvp.sh
```
```output
[    3.879183] VFS: Mounted root (ext4 filesystem) readonly on device 254:0.
[    3.879643] devtmpfs: mounted
[    3.897918] Freeing unused kernel memory: 9024K
[    3.901685] Run /sbin/init as init process
[    3.965637] EXT4-fs (vda): re-mounted 34fdcd00-4506-42fc-8af8-a35ca9cf965d r/w. Quota mode: none.
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Saving random seed: OK
Starting network: ip: RTNETLINK answers: File exists
udhcpc: started, v1.31.1
udhcpc: sending discover
udhcpc: sending select for 172.20.51.1
udhcpc: lease of 172.20.51.1 obtained, lease time 86400
deleting routers
adding dns 172.20.51.254
FAIL
Starting dropbear sshd: OK

Welcome to Buildroot
buildroot login: root
Password:
#
```

Mount a 9p drive on the host linux kernel using `/etc/fstab`:

```console
vi /etc/fstab
```
In the `/etc/fstab` file, add the following line to it:

```console
FM	/mnt		9p	trans=virtio,version=9p2000.L,aname=/mnt	0 	0"
```
Save and close the file. Now run the mount command:

```console
mount -a
```
This command mounts the `FM-share` directory in your docker container to the `/mnt` directory of the host linux kernel running in the FVP. Inspect the contents of `/mnt`:

```console
ls /mnt
```

The output should be:
```output
hello.c  init  test.cpio.gz
```
```console
lkvm run --realm --irqchip=gicv3-its -p earlycon --network mode=none -c 1 -m 128 -k /realm/Image -i /mnt/test.cpio.gz
```

```output
[    9.721618] Freeing unused kernel memory: 9024K
[    9.740198] Run /init as init process
Hello world!
```



