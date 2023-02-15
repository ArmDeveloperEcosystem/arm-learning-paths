---
# User change
title: "Installing Arch"

weight: 2

layout: "learningpathall"
---

## Prerequisites

You will need a Pinebook Pro and a microSD card of at least 8GB and class 10 or faster. If you are doing the initial microSD card setup on a second computer be aware the instructions are written for Linux. macOS can be used, but the steps required to partition will be different as fdisk on macOS is different and as such will be outside the scope of these instructions.

Basic command line knowledge will be helpful, but the vast majority of commands are written in the instructions.

There is no avoiding it, some basic vi / vim knowledge is required. If you need to a crash course or a refresher, on a computer with vim installed run the following command. It shouldn't take long to complete, only 15 - 30 minutes. 
```cmd
vimtutor
```

## Installing Arch Linux ARM

For reference, the latest release and instructions can be found here: https://github.com/SvenKiljan/archlinuxarm-pbp/releases/latest. The first steps will be taken from there so they are kept up to date alongside the latest Pinebook Pro Arch Linux Arm image.

* Follow the instructions under "Installation on microSD card or eMMC module" https://github.com/SvenKiljan/archlinuxarm-pbp/blob/main/INSTALL.md
    * If wifi-menu isn't working first try: The Pinebook Pro has a WiFi privacy kill switch. Press the Pine64 logo key + F11. If the num lock light blinks twice WiFi has just been enabled. If it blinks three times WiFi has just been disabled. Enable it, then shutdown, wait a few seconds, the power back on.
    * Sometimes after rebooting the wireless device isn't seen and so WiFi doesn't work. The solution I have found so far is confirming the kill switch is off, shutting down, waiting, then starting back up.
* Optional, but it's what I did: if you want to run the OS off the internal eMMC module rather than off the SD card, follow the steps under "Installation of eMMC module without a USB adapter" next.

## Initial Configurations

* Create a user, replace \<username> with desired username
```cmd
useradd -m <username>
```

* Give the user a password
```cmd
passwd <username>
```

* Install sudo
```cmd
pacman -Sy sudo
```

* Add the new user to the sudoers group
```cmd
sudo visudo
```
    
* Navigate to the bottom of the file, and under the line "root ALL=(ALL:ALL) ALL" add a new line with "\<username> ALL=ALL(ALL:ALL) ALL" then save and exit

* Update the system and packages. Because Arch is a rolling release, the following command should be ran often. At least once a week, or before installing new software.
```cmd
pacman -Syu
```

* The wifi-menu doesn't keep you connected after restarting, so to enable automatic connection we will run the following command. Note that wlan0 should be the wireless adapter for the Pinebook Pro, but if for some reason it's not you can verify by going to /etc/netctl/ and looking inside the file that is named after your wifi address.
```cmd
sudo systemctl enable netctl-auto@wlan0.service
```

The barebones Arch should now be installed and configured.
