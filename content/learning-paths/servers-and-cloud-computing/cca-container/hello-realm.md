---
# User change
title: "Run a simple application inside a Realm using a ready-made docker container"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin

Make sure you running and inside the `armswdev/aemfvp-cca-image` docker container.

```console
docker run -it armswdev/aemfvp-cca-image /bin/bash
```

## Create a simple initramfs to boot the guest linux kernel image

Linux kernels contain a gzipped cpio format archive. When the kernel boots up, this archive is extracted into the root filesystem. The kernel then checks whether the root filesystem contains a file named "init" and tries to run it. At this point the kernel is done booting, and the "init" application executes the system the rest of the way. 

In this learning path, you will package a simple hello world application into the initramfs for the guest linux kernel. 

## Create a simple initramfs

Using a file editor of your choice, create a file named `hello.c`. Copy the contents below into the file:

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
`test.cpio.gz` is the compressed archive you will use the initramfs for the guest linux kernel.


Copy this initramfs into a directory that you will mount inside the host linux kernel running on the FVP after you boot the reference CCA stack binaries.

``console
mkdir -p ~/FM-share
cp -r test.cpio-gz ~/FM-share
```
## Run 

```console
./run-cca-fvp.sh
```

Mount a 9p drive on your host linux kernel using /etc/fstab
```console
vi /etc/fstab
```
With the /etc/fstab file open now add the following line to it:

```console
FM	/mnt	9p	trans=virtio,version=9p2000.L,aname=/mnt	0 	0"
```
Save and close the file. Now run the mount command:

```console
mount -a
```





