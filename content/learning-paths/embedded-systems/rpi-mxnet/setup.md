 ---
# User change
title: "Install a Raspberry Pi OS file system"

weight: 2

layout: "learningpathall"

---

## Before you begin

An Arm Linux server or an Arm cloud instance running Ubuntu is required. The instructions were tested on Ubuntu 22.04.

Setup the machine and verify you can use SSH to connect.

A Raspberry Pi 3 or Raspberry Pi 4 is needed to test the compiled application. This step is optional and can be skipped if a board is not available. 

## Before you begin 

For large embedded software projects you can reduce compile time using an Arm server and transfer the compiled applications to embedded Linux hardware. A Raspberry Pi running Raspberry Pi OS is used as an example embedded system. MXNet, a flexible and efficient library for deep learning, is used as an example software application. This strategy can be applied to other applications and other Arm hardware. 

C++ projects for embedded Linux can take a long time to build. This makes it difficult to customize, build, and deploy applications on Arm single board computers such as the Raspberry Pi. MXNet is a good example of a large C++ project which takes time to build. 

Cross-compiling, instruction translation with qemu, and native compiling on the target board are possible ways to build C++ applications. Learn how you can use an Arm server to shorten compile time without the difficulties associated with cross-compiling and instruction translation. 

## Download a Raspberry Pi OS file system 

Connect to an Arm server using SSH.

1. Confirm you are using an Arm machine

Run the command:

```bash
uname -m
```

The output should be:

```output
aarch64
```

2. Download a 64-bit Raspberry Pi OS image 

This is the version of the Raspberry Pi OS that you want to deploy on a Raspberry Pi board with an application installed. 

```console
wget http://downloads.raspberrypi.org/raspios_lite_arm64/images/raspios_lite_arm64-2023-02-22/2023-02-21-raspios-bullseye-arm64-lite.img.xz
```

3. Uncompress the downloaded file system image

Uncompress the file using `unxz`:

```console
unxz 2023-02-21-raspios-bullseye-arm64-lite.img.xz
```

## Increase the image size and mount the file system

The downloaded image will not have enough free space to compile a large project. The image size can be increased to make room to add additional software. 

1. Select an unused loop device 

Use any loop device which is not already being used. Device number 10 is shown in the commands below. 

Use the `ls` command to see the existing loop devices: 

```console
ls /dev/loop*
```

Substitute a higher number if `/dev/loop10` already exists. 

2. Increase the image size 

Increase the image size to 8 Gb. Larger sizes can be used if more space is needed, but the new size should not be larger than the size of your Raspberry Pi SD card.

```console
sudo losetup -P /dev/loop10 2023-02-21-raspios-bullseye-arm64-lite.img
sudo fallocate -l 8000M 2023-02-21-raspios-bullseye-arm64-lite.img
sudo losetup -c /dev/loop10
```

3. Resize the image partition 

The partition manipulation program, `parted` is an interactive program to increase the size of disk partitions. Run `parted` with the created loop device. 

```console
sudo parted /dev/loop10
```

Once `parted` starts, there are three commands to run. 

Enter `print free` to print the current partition table. Locate the end of the free space, in this case it is 8389MB. 

Enter `resizepart 2` to change the size of partition 2. Enter the end of the free space from the first command (8389MB). 

Enter `q` to quit.

The output from a `parted` session is shown below for reference.

```output
GNU Parted 3.3
Using /dev/loop10
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print free                                                       
Model: Loopback device (loopback)
Disk /dev/loop10: 8389MB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  Flags
        16.4kB  4194kB  4178kB           Free Space
 1      4194kB  273MB   268MB   primary  fat32        lba
 2      273MB   2001MB  1728MB  primary  ext4
        2001MB  8389MB  6388MB           Free Space

(parted) resizepart 2                                                     
End?  [2001MB]? 8389MB                                                    
(parted) q                                                                
Information: You may need to update /etc/fstab.
```

4. Resize the file system 

Resize the file system to use the newly created space.

```console
sudo e2fsck -f /dev/loop10p2
sudo resize2fs  /dev/loop10p2
```

5. Mount the file systems

Mount the file systems on `/mnt`

```console
sudo mount /dev/loop10p2 /mnt
sudo mount /dev/loop10p1 /mnt/boot
cd /mnt
sudo mount -t proc /proc proc/
sudo mount --rbind /sys sys/
sudo mount --rbind /dev dev/
```

The directory `/mnt` now contains the Raspberry Pi root file system. 

## Use change root to enter the file system 

Use the `chroot` command to enter the Raspberry Pi OS file system. This places the Raspberry Pi file system at `/` 

```console
sudo chroot /mnt /bin/bash
```

The bash shell is now inside the Raspberry Pi file system. It runs as if this is a Raspberry Pi and the file system is the same as if it was being done on a Raspberry Pi board. 

Continue to the next section to build MXNet, an example C++ application. 

