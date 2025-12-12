---
# User change
title: "Run the Arm CCA stack using a pre-built docker container"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Download the docker image

Start by downloading the docker container image.

This docker image contains the pre-built binaries for the Arm CCA reference software stack and the Armv-A Base Architecture Envelope Model (AEM) FVP with support for RME extensions.

Install [docker engine](/install-guides/docker/docker-engine) on your machine.

Pull the docker image from DockerHub:

```console
docker pull armswdev/cca-learning-path:cca-simulation-v3
```
Confirm that the docker container image was downloaded successfully:

```console
docker image list
```

The output should be similar to:

```output
IMAGE                                                                          ID             DISK USAGE   CONTENT SIZE   EXTRA

...
armswdev/cca-learning-path:cca-simulation-v3                                   21500198bb93       1.18GB             0B
...
```
Run the docker container:

```console
docker run --rm -it armswdev/cca-learning-path:cca-simulation-v3
```
You are now inside the home directory (`/home/cca`) of user `cca` in the running `armswdev/cca-learning-path:cca-simulation-v3` container.

```output
cca@a9866f863546:~$
```

## Run the software stack

The pre-built binaries for the Arm CCA reference software stack are present in the `cca-3world/` directory.

```console
ls cca-3world/
```
This includes the Realm Management Monitor (`rmm.img`), the host root filesystem (`host-rootfs.ext2`) and the host Linux kernel image (`Image`) and the trusted firmware binaries:

```output
FVP_AARCH64_EFI.fd  Image  bl1.bin  bl2.bin  bl31.bin  dt_bootargs.dtb  fip.bin  host-rootfs.ext2  kselftests.tgz  modules.tgz  rmm.img
```

These binaries can run on an Armv-A Base Architecture Envelope Model (AEM) FVP with support for RME extensions. AEM FVPs are fixed configuration virtual platforms of Armv8-A and Armv9-A architectures with comprehensive system IP. The FVP is also contained within this docker container.

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

You will be prompted to log in to the CCA host. Enter `root` as the username (no password is required).

You have successfully booted 3 worlds (Root, Non-secure and Realm) on the FVP at this point:

* Trusted Firmware-A is running in Root.
* Realm Management Monitor (RMM) in Realm.
* Host Linux in Non-secure.

## Create a virtual guest in a Realm

Guest VMs can be launched in a Realm using `kvmtool` from your host Linux prompt. The realm disk image `guest-disk.img` is included into the host file system.

Use `kvmtool` to launch guest Linux in a Realm:

```console
cd /cca
./lkvm run --realm --disable-sve --irqchip=gicv3-its --firmware KVMTOOL_EFI.fd -c 1 -m 512 --no-pvtime --force-pci --disk guest-disk.img --measurement-algo=sha256 --restricted_mem
```

You should see the guest Linux kernel starting to boot in a Realm. This step can take several minutes.

After boot up, you will be prompted to log in at the guest Linux prompt, use the `root` username (no password required):

```output
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

You have successfully created a virtual guest in a Realm using the Arm CCA reference software stack.

## Obtain a CCA attestation token from the virtual guest in a Realm

Attestation tokens are small reports that are produced by a device upon request. Those tokens are composed of key/value pairs called claims. A CCA attestation token is a collection of claims about the state of a Realm and the CCA platform on which the Realm is running.

Refer to [section A7.2 of the Realm Management Monitor Specification](https://developer.arm.com/documentation/den0137/latest/) to learn about the details of the CCA attestation token.

The retrieval of a CCA attestation token from a running guest is done by reading from `/sys/kernel/config/tsm/report/`. This is available when linux's `configfs` has been mounted, which has been done automatically as part of the guest boot process --- if you are curious, this is the `configfs    /sys/kernel/config      configfs    defaults        0       0` line in `/etc/fstab`.

You can now generate an attestation token by running the following commands:

```console
report=/sys/kernel/config/tsm/report/report0
mkdir $report
dd if=/dev/urandom bs=64 count=1 > $report/inblob
hexdump -C $report/outblob
```

The output should look like:
```output
00000000  d9 01 8f a2 19 ac ca 59  05 ee d2 84 44 a1 01 38  |.......Y....D..8|
00000010  22 a0 59 05 81 a9 19 01  09 78 23 74 61 67 3a 61  |".Y......x#tag:a|
00000020  72 6d 2e 63 6f 6d 2c 32  30 32 33 3a 63 63 61 5f  |rm.com,2023:cca_|
00000030  70 6c 61 74 66 6f 72 6d  23 31 2e 30 2e 30 0a 58  |platform#1.0.0.X|
00000040  20 0d 22 e0 8a 98 46 90  58 48 63 18 28 34 89 bd  | ."...F.XHc.(4..|
00000050  b3 6f 09 db ef eb 18 64  df 43 3f a6 e5 4e a2 d7  |.o.....d.C?..N..|
00000060  11 19 09 5c 58 20 7f 45  4c 46 02 01 01 00 00 00  |...\X .ELF......|
00000070  00 00 00 00 00 00 03 00  3e 00 01 00 00 00 50 58  |........>.....PX|
00000080  00 00 00 00 00 00 19 01  00 58 21 01 07 06 05 04  |.........X!.....|
00000090  03 02 01 00 0f 0e 0d 0c  0b 0a 09 08 17 16 15 14  |................|
000000a0  13 12 11 10 1f 1e 1d 1c  1b 1a 19 18 19 09 61 44  |..............aD|
000000b0  cf cf cf cf 19 09 5b 19  30 03 19 09 62 67 73 68  |......[.0...bgsh|
000000c0  61 2d 32 35 36 19 09 60  78 3a 68 74 74 70 73 3a  |a-256..`x:https:|
000000d0  2f 2f 76 65 72 61 69 73  6f 6e 2e 65 78 61 6d 70  |//veraison.examp|
000000e0  6c 65 2f 2e 77 65 6c 6c  2d 6b 6e 6f 77 6e 2f 76  |le/.well-known/v|
000000f0  65 72 61 69 73 6f 6e 2f  76 65 72 69 66 69 63 61  |eraison/verifica|
00000100  74 69 6f 6e 19 09 5f 8d  a4 01 69 52 53 45 5f 42  |tion.._...iRSE_B|
00000110  4c 31 5f 32 05 58 20 53  78 79 63 07 53 5d f3 ec  |L1_2.X Sxyc.S]..|
00000120  8d 8b 15 a2 e2 dc 56 41  41 9c 3d 30 60 cf e3 22  |......VAA.=0`.."|
00000130  38 c0 fa 97 3f 7a a3 02  58 20 9a 27 1f 2a 91 6b  |8...?z..X .'.*.k|
00000140  0b 6e e6 ce cb 24 26 f0  b3 20 6e f0 74 57 8b e5  |.n...$&.. n.tW..|
00000150  5d 9b c9 4f 6f 3f e3 ab  86 aa 06 67 73 68 61 2d  |]..Oo?.....gsha-|
00000160  32 35 36 a4 01 67 52 53  45 5f 42 4c 32 05 58 20  |256..gRSE_BL2.X |
00000170  53 78 79 63 07 53 5d f3  ec 8d 8b 15 a2 e2 dc 56  |Sxyc.S]........V|
...
00000800  88 cf 5b 66 ce b5 30 59  0a d4 81 79 3d e5 02 dc  |..[f..0Y...y=...|
00000810  ac 70 bc dc b7 05 b2 cc  40 f1 b6 05 a5 52 57 04  |.p......@....RW.|
00000820  26 7a 24 c5 2e 88 6e a7  b6 18 59 2e 9f e8 58 8d  |&z$...n...Y...X.|
00000830  a6 ea 0b 9b 18 90 62 62  07 f0 17 90 b4 27 04 e3  |......bb.....'..|
00000840  ec 89 dd 67 5f 6b 07 47  55 4d a9 7b c1 be d2 03  |...g_k.GUM.{....|
00000850  4f 5d d1 d0 55 d1                                 |O]..U.|
00000856
```

The output is a CCA attestation token from the guest in the Realm. The CCA attestation token is a Concise Binary Object Representation (CBOR) map, in which the map values are the Realm token and the CCA platform token.

You have successfully generated a CCA attestation token from the guest. In later learning paths, you will learn how to use these tokens as part of the Arm CCA attestation flow.

You can now shutdown the guest. Use the `poweroff` command.

You should see the following output from the guest:

```output
(realm) # Destroying macvtap... OK
Stopping crond: stopped /usr/sbin/crond (pid 120) OK
Stopping chrony: OK
Stopping network: ifdown: interface lo not configured OK
Stopping klogd: OK
Stopping syslogd: stopped /sbin/syslogd (pid 66) OK
umount: devtmpfs busy - remounted read-only
[ 1172.990117] EXT4-fs (vda2): re-mounted b984c902-aed2-4217-bbf0-da44ee66446c ro.
The system is going down NOW!
Sent SIGTERM to all processes
Sent SIGKILL to all processes
Requesting system poweroff
[ 1175.167522] reboot: Power down
  Info: KVM session ended normally.
```

The guest has shut down and you are back at the host Linux kernel prompt.

To exit the host session and the simulation, use `poweroff`. You will be placed back into the running docker container.

To exit the docker container, run `exit`.

In the next section, you will learn how to run a simple application inside the Realm.

{{% notice Note %}}
The docker session has been started with the `--rm` option, which means the container will be destroyed when it is exited, allowing you to experiment with the images without fear: at the next session, you will get working pristine images ! If you intend your changes to persist across docker sessions, omit the `--rm` option to docker.
{{% /notice %}}
