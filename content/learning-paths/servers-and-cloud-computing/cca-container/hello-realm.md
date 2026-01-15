---
# User change
title: "Run an application in a Realm"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

Download the [`armswdev/cca-learning-path:cca-simulation-v3`](https://hub.docker.com/r/armswdev/cca-learning-path:cca-simulation-v3) docker container.

## Running an application in a Realm

In the previous section, you were able to boot a guest virtual machine as the Realm. In this section, you will learn how to run your own application within that Realm. The application inherits the confidential protection of the guest virtual machine it is running in.

A convenient way to run an application inside a Realm, within the context of this example, is to *inject* the application into the guest filesystem. In this section, you will inject a simple **hello world** program into the guest filesystem.

## Inject a simple application in the guest filesystem

### Compile the application

Create a directory in which you will build the simple **hello world** application:

```console
mkdir ~/CCA-docker-share
cd ~/CCA-docker-share
```

Using a file editor of your choice, create a file named `hello.c` in this directory. Copy the contents below into the file:

```console
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  printf("\n******* Hello from the Realm ! *******\n\n");

  return EXIT_SUCCESS;
}
```

Now start the container:

```console
docker run -v ~/CCA-docker-share:/home/cca/CCA-docker-share --rm --privileged -it armswdev/cca-learning-path:cca-simulation-v3
```

{{% notice Note %}}
The docker session is started with the `--rm` option, which means the container will be destroyed when it is exited, allowing you to experiment with the images without fear: at the next session, you will get working pristine images ! If you intend your changes to persist across docker sessions, omit the `--rm` option to docker.

The `--privileged` option is needed to be able to mount the host and guest filesystems inside the container.

The `~/CCA-docker-share` directory on your development machine is available within the container at `/home/cca/CCA-docker-share` thanks to the `-v ~/CCA-docker-share:/home/cca/CCA-docker-share` command line option to `docker run`.
{{% /notice %}}

Inside the running container, compile the **hello world** application, the source code file `hello.c` should be present in the shared directory `/home/cca/CCA-docker-share` :

```console { output_lines="2" }
ls CCA-docker-share/
hello.c
aarch64-linux-gnu-gcc -O1 -static -o hello CCA-docker-share/hello.c
```

You now have a `hello` statically linked binary for the **hello world** application inside `/home/cca/`:

```console { output_lines="2" }
ls
CCA-docker-share  FastRAM.cfg  cca-3world  hello  run-cca-fvp.sh
```

### Inject the application into the guest filesystem.

While still in the docker container, mount the host filesystem, then the guest filesystem (which lives inside the host filesystem), then copy the `hello` binary file to the guest filesystem and then unmount the guest and host filesystems:

```console
sudo mkdir -p /mnt/host-fs /mnt/guest-fs
sudo mount -t auto -w -o loop cca-3world/host-rootfs.ext2 /mnt/host-fs
fs_start=$(fdisk -l /mnt/host-fs/cca/guest-disk.img |grep "Linux filesystem"| tr -s ' ' | cut -f2 -d" ")
sudo mount -t auto -w -o loop,offset=$(($fs_start*512)) /mnt/host-fs/cca/guest-disk.img /mnt/guest-fs
sudo cp hello /mnt/guest-fs/cca/
sudo umount /mnt/guest-fs
sudo umount /mnt/host-fs
```

### Execute **hello world** in the realm

Now, as previously, start the CCA host in the FVP:

```console
./run-cca-fvp.sh
```

```console
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 172.20.51.1, server 172.20.51.254
udhcpc: lease of 172.20.51.1 obtained from 172.20.51.254, lease time 86400
deleting routers
adding dns 172.20.51.254
OK
Starting chrony: OK
Starting crond: OK
Setting up macvtap... [   16.681271] smc91x 1a000000.ethernet eth0: entered promiscuous mode
OK

Welcome to the CCA host
host login:
```

Log into the CCA host, using `root` as the username (no password required), then start a realm with:

```console
cd /cca
./lkvm run --realm --disable-sve --irqchip=gicv3-its --firmware KVMTOOL_EFI.fd -c 1 -m 512 --no-pvtime --force-pci --disk guest-disk.img --measurement-algo=sha256 --restricted_mem
```

```console
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 192.168.33.15, server 192.168.33.1
udhcpc: lease of 192.168.33.15 obtained from 192.168.33.1, lease time 14400
deleting routers
adding dns 172.20.51.254
FAIL
Starting chrony: OK
Starting crond: OK
Setting up macvtap... OK

Welcome to the CCA realm
realm login:
```

Log into the CCA realm, using `root` as the username (no password required).

Now change directory to `/cca`: the **hello world** application should be there as the binary file `hello`, just run it:

```console { output_lines="3" }
cd /cca
ls
arc         hello       kbs-client
./hello

******* Hello from the Realm ! *******

```

You have successfully run your own application inside the Realm !

As before, with `poweroff` you can now exit the realm, then the host.
