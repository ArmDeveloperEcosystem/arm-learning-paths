---
# User change
title: "How do I install Arch Linux?"

weight: 2

layout: "learningpathall"
---

You can install Arch Linux on the [Pinebook Pro laptop](https://www.pine64.org/pinebook-pro/) and use it for Linux development on Arm. 

## What should I consider before installing Arch Linux?

You will need a Pinebook Pro laptop and a microSD card of at least 8GB and class 10 or faster. 

You will also need a second computer to write the software image to the microSD card. The instructions for writing the microSD card are written for Linux. 

You can use macOS as the second computer, but the steps required to partition the microSD card are different. There are no macOS instructions here, but you are free to try. You can also ask for help on GitHub. 

Basic command line knowledge is helpful, but most of the commands you need are included in the instructions.

Some vim knowledge is required. If you need to a crash course or a want to do a refresher, on a computer with vim installed run the following command: 

```console
vimtutor
```
It takes about 15-30 minutes to complete to complete the tutorial. 

## How do I Install Arch Linux ARM on a microSD card?

Install Arch Linux using the instructions on GitHub. 

1. Follow the instructions titled [Installation on microSD card or eMMC module](https://github.com/SvenKiljan/archlinuxarm-pbp/blob/main/INSTALL.md)

The instructions explain how to create the microSD card and boot Arch Linux. 

{{% notice Note %}}
If the `wifi-menu` isn't working on the first try, check the Wi-Fi privacy kill switch. 

Press the Pine64 logo key + F11. If the num lock light blinks twice Wi-Fi has just been enabled. If it blinks three times Wi-Fi has just been disabled. 

Enable it, then shutdown, wait a few seconds, the power back on.
{{% /notice %}}

2. (optional) Run the operating system from the internal eMMC instead of the SD card

To install the OS to eMMC follow the steps under "Installation of eMMC module without a USB adapter". Using eMMC provides faster performance and you won't need to have the microSD card in the slot during future use. 

After completing the installation you should be at a root command prompt with no window manager and the Wi-Fi is connected. 

Refer to the [Frequently asked questions](https://github.com/SvenKiljan/archlinuxarm-pbp/blob/main/FAQ.md) for more information. 

Continue with the steps below to create a new user and update the Arch Linux software. 

## How do I configure Arch Linux correctly? 

1. Create a user, replace `username` with your desired user name

```console
useradd -m username
```

2. Create a password for the `username`

```console
passwd username
```

3. Update the system and packages

Because Arch is a rolling release, the following command should be ran often. At least once a week, or before installing new software.

```console
pacman -Syu
```

4. Install `sudo`

```console
pacman -Sy sudo
```

5. Add the new user to the sudoers group

You are already root so you can directly edit the sudoers file.

```console
visudo
```
    
Navigate to the bottom of the file. About 10 lines from the bottom look for this line:

```output
root ALL=(ALL:ALL) ALL 
```

Add a new line which is the same, but with your `username`:

```console
username ALL=ALL(ALL:ALL) ALL
```

Save the file and exit. 

6. Automatically connect Wi-Fi on start-up

The `wifi-menu` doesn't reconnect after restarting. 

You can enable automatic connection by running the command below.

Note that `wlan0` should be the wireless adapter for the Pinebook Pro, but if for some reason it's not you can verify by going to `/etc/netctl` and looking inside the file that is named with your Wi-Fi device name. 

```console
sudo systemctl enable netctl-auto@wlan0.service
```

Arch Linux is now installed and configured.
