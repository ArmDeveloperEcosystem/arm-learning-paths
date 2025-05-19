---
layout: learning-path
title: Increasing Linux Kernel Page Size on Arm (Debian)
author: Geremy Cohen
minutes_to_complete: 30
skill_level: Intermediate
os: Debian
categories:
  - Performance and Architecture
tools:
  - Bash
  - apt, dpkg, make
weight: 3
---

## 1. Common Setup
- Verify you’re on 4 KB pagesize:
  ```bash
  getconf PAGESIZE   # should print 4096
  ```
- Backup `/boot` and `/etc`, or snapshot your VM

## 2. Build & Install Kernel & Reboot
```bash
sudo apt-get update
apt-get source linux-image-$(uname -r)
cd linux-*/debian
# Edit debian/rules: set DEB_PAGESIZE=65536
DEB_PAGESIZE=65536 dpkg-buildpackage -b -us -uc
sudo dpkg -i ../linux-image-*.deb ../linux-headers-*.deb
sudo update-grub
sudo reboot
```

## 3. Verify 64 KB is Active
```bash
getconf PAGESIZE   # should now print 65536
uname -r           # confirm custom build
```

## 4. Revert to 4 KB Pagesize
```bash
sudo apt-get remove --purge linux-image-*
sudo apt-get install --reinstall linux-image-$(uname -r | sed 's/-[^-]*$//')
sudo update-grub
sudo reboot
```