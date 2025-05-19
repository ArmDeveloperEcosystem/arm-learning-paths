---
layout: learning-path
title: Increasing Linux Kernel Page Size on Arm (Ubuntu)
author: Geremy Cohen
minutes_to_complete: 30
skill_level: Intermediate
os: Ubuntu
categories:
  - Performance and Architecture
tools:
  - Bash
  - apt, dpkg
weight: 2
---

## 1. Common Setup
- Verify you’re on 4 KB pagesize:
  ```bash
  getconf PAGESIZE   # should print 4096
  ```
- Backup `/boot` and `/etc`, or snapshot your VM

## 2. Download / Install / Compile & Reboot
```bash
sudo apt update
sudo apt install linux-image-6.1.0-64k linux-headers-6.1.0-64k
sudo update-grub
sudo reboot
```

## 3. Verify 64 KB is Active
```bash
getconf PAGESIZE   # should now print 65536
uname -r           # confirm “-64k” suffix
```

## 4. Revert to 4 KB Pagesize
```bash
sudo apt remove linux-image-*-64k
sudo update-grub
sudo reboot
```