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
docker pull armswdev/aemfvp-cca-v2-image
```
Confirm that the docker container image was downloaded successfully:

```console
docker image list
```

The output should be similar to:

```output
REPOSITORY        				TAG       IMAGE ID       CREATED       SIZE
armswdev/aemfvp-cca-v2-image   	latest    e1c36b91d3d7   5 weeks ago   1.34GB
```
Run the docker container:

```console
docker run -it armswdev/aemfvp-cca-v2-image /bin/bash
```
You are now inside the `/tmp/cca-stack` directory of the running `armswdev/aemfvp-cca-v2-image` container.

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
Image  KVMTOOL_EFI.fd  bl1-uefi.bin  bl1.bin  fip-std-tests.bin  fip-uefi.bin  fip.bin  host-fs.ext4
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

You have successfully booted four worlds (Root, Secure, Non-secure and Realm) on the FVP at this point:

* Trusted Firmware-A is running in Root.
* Realm Management Monitor (RMM) in Realm.
* Host Linux in Non-secure.
* Hafnium in Secure. 

## Create a virtual guest in a Realm

Guest VMs can be launched in a Realm using `kvmtool` from your host Linux prompt. The kernel `Image` and filesystem `realm-fs.ext4` for the Realm are packaged into the buildroot host file system.

Use `kvmtool` to launch guest Linux in a Realm:

```console
lkvm run --realm --restricted_mem -c 2 -m 256 -k /realm/Image -d /realm/realm-fs.ext4 -p earlycon
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

## Obtain a CCA attestation token from the virtual guest in a Realm

Attestation tokens are small reports that are produced by a device upon request. Those tokens are composed of key/value pairs called claims. A CCA attestation token is a collection of claims about the state of a Realm and the CCA platform on which the Realm is running. 

Refer to [section A7.2 of the Realm Management Monitor Specification](https://developer.arm.com/documentation/den0137/latest/) to learn about the details of the CCA attestation token.

To retrieve a CCA attestation token from the running guest, mount the `configfs` filesystem:
```console
mount -t configfs none /sys/kernel/config
```

You can now generate an attestation token by running the following commands:

```console
report=/sys/kernel/config/tsm/report/report0
mkdir $report
dd if=/dev/urandom bs=64 count=1 > $report/inblob
hexdump -C $report/outblob
```

The output should look like:
```output
00000340  00 00 00 00 19 ac cd 58  61 04 76 f9 88 09 1b e5  |.......Xa.v.....|
00000350  85 ed 41 80 1a ec fa b8  58 54 8c 63 05 7e 16 b0  |..A.....XT.c.~..|
00000360  e6 76 12 0b bd 0d 2f 9c  29 e0 56 c5 d4 1a 01 30  |.v..../.).V....0|
00000370  eb 9c 21 51 78 99 dc 23  14 6b 28 e1 b0 62 bd 3e  |..!Qx..#.k(..b.>|
00000380  a4 b3 15 fd 21 9f 1c bb  52 8c b6 e7 4c a4 9b e1  |....!...R...L...|
00000390  67 73 73 4f 61 a1 ca 61  03 1b 2b bf 3d 91 8f 2f  |gssOa..a..+.=../|
000003a0  94 ff c4 22 8e 50 91 95  44 ae 19 ac cc 67 73 68  |...".P..D....gsh|
000003b0  61 2d 32 35 36 19 ac d0  67 73 68 61 2d 32 35 36  |a-256...gsha-256|
000003c0  19 ac ce 58 20 d7 6c b0  e0 f4 d1 00 4d 51 5f e6  |...X .l.....MQ_.|
000003d0  c9 20 a8 e4 72 9d 26 61  0c cd 53 6b 8f 37 a3 65  |. ..r.&a..Sk.7.e|
000003e0  aa 03 b0 a2 2c 19 ac cf  84 58 20 00 00 00 00 00  |....,....X .....|
000003f0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000400  00 00 00 00 00 00 00 00  00 00 00 58 20 00 00 00  |...........X ...|
00000410  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000420  00 00 00 00 00 00 00 00  00 00 00 00 00 58 20 00  |.............X .|
00000430  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000440  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 58  |...............X|
00000450  20 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  | ...............|
00000460  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000470  00 58 60 7c 2e 85 d2 b5  ba d8 ee e1 43 0c 5d f9  |.X`|........C.].|
00000480  38 b8 83 64 a0 75 8d d5  02 a2 43 56 53 ba 2f bc  |8..d.u....CVS./.|
00000490  f1 a9 c7 82 b4 d5 b4 63  15 45 71 5c 50 ea eb a0  |.......c.Eq\P...|
000004a0  21 68 c4 7f 1a e5 00 b6  9a a5 3a 78 38 80 c6 96  |!h........:x8...|
000004b0  c8 f6 eb 92 62 f8 80 43  fe dd 7b e6 af 16 f0 04  |....b..C..{.....|
000004c0  54 95 6e 87 aa 53 4a bc  e2 a4 ab 4d 84 10 b1 c8  |T.n..SJ....M....|
000004d0  84 0e 06                                          |...|
000004d3
```
The output is a CCA attestation token from the guest in the Realm. The CCA attestation token is a Concise Binary Object Representation (CBOR) map, in which the map values are the Realm token and the CCA platform token.

You have successfully generated a CCA attestation token from the guest. In later learning paths, you will learn how to use these tokens as part of the Arm CCA attestation flow. 

You can now shutdown the guest. Use the `poweroff` command.

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
