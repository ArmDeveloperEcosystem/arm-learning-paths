---
title: Import filesystems into WSL

weight: 8
layout: learningpathall
---

## Import file systems into WSL

In addition to installing Linux distributions using the Windows Store and the online list, file systems can be directly imported into WSL.

### Install Alpine Linux

Check the [Alpine Downloads](https://alpinelinux.org/downloads/)

Look for the mini root filesystem for `aarch64` and download it.

In the commands below use your Windows user name instead of `<username>`.

At a Windows Command Prompt import the downloaded filesystem into WSL as a Linux distribution:

```cmd
wsl --import alpine1 c:\Users\<username>\alpine alpine-minirootfs-3.16.2-aarch64.tar.gz
```

The name of the distribution will be alpine1.

The storage will be in `c:\Users\<username>\alpine`

When the import is complete, list the installed distributions:

```cmd
wsl --list
```

The new alpine1 distribution will be on the list.

Start alpine:

```cmd
wsl -d alpine1
```

Alpine Linux is now running in WSL.

### Install Raspberry Pi OS

Check the [Raspberry Pi OS Downloads](http://downloads.raspberrypi.org/)

Navigate to [raspios_lite_arm64](http://downloads.raspberrypi.org/raspios_lite_arm64/)

Download the root filesystem named `root.tar.xz`

At a Windows Command Prompt import the downloaded filesystem into WSL as a Linux distribution:

```cmd
wsl --import rpios c:\Users\<username>\rpios root.tar.xz
```

The name of the distribution will be `rpios`

The storage will be in `c:\Users\<username>\rpios`

When the import is complete, list the installed distributions:

```cmd
wsl --list
```

The new `rpios` distribution will be on the list.

Start Raspberry Pi OS.

```cmd
wsl -d rpios
```

Raspberry Pi OS on aarch64 is now running in WSL.

