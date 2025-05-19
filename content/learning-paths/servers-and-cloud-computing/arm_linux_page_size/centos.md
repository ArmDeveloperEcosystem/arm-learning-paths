---
layout: learning-path
title: Increasing Linux Kernel Page Size on Arm (CentOS)
author: Geremy Cohen
minutes_to_complete: 30
skill_level: Intermediate
os: CentOS
categories:
  - Performance and Architecture
tools:
  - Bash
  - yum, grubby
weight: 4
---

## 1. Common Setup
- Verify you’re on 4 KB pagesize:
  ```bash
  getconf PAGESIZE   # should print 4096
  ```
- Backup `/boot` and `/etc`, or snapshot your VM

## 2. Install & Reboot
```bash
sudo yum install kernel-64k
sudo grubby --set-default /boot/vmlinuz-*-64k
sudo reboot
```

## 3. Verify 64 KB is Active
```bash
getconf PAGESIZE   # should now print 65536
uname -r           # confirm “-64k” suffix
```

## 4. Revert to 4 KB Pagesize
```bash
sudo yum remove kernel-64k
sudo grubby --remove-kernel /boot/vmlinuz-*-64k
sudo reboot
```