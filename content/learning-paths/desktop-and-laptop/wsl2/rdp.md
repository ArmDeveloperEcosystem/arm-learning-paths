---
title: Connect to WSL using RDP and VNC

weight: 6
layout: learningpathall
---

## Install desktop software and remote desktop protocol (RDP)

RDP provides a remote desktop from Windows to WSL. The RDP client is run on Windows and displays the Linux desktop running in WSL.

Install the RDP server and the XFCE4 desktop.

```bash
sudo apt install -y xfce4 xrdp
```

Set XFCE4 as the default desktop.

```bash
echo xfce4-session >~/.xsession
```

If systemd is running the xrdp server will start automatically on install, but it needs a restart after modifying .xsession.

```bash
sudo service xrdp restart
```

Check if xrdp is running.

```bash
systemctl status xrdp
```

If xrdp is not running, start it.

```bash
sudo service xrdp start
```

Get the IP address of WSL. Make a note if the IP address.

```bash
ifconfig
```

If if config is not installed, install it.

```bash
sudo apt install net-tools -y
```

On Windows, start the remote desktop viewer, mstsc. It is also called "Remote Desktop Connection" on the Windows application menu.

Enter the IP address of WSL in the box.

Click Yes that you really want to connect.

Enter the Linux username and password for the WSL distribution.

## Install desktop software and use VNC for a remote desktop

VNC can also be used for a virtual desktop. 

Refer to [VNC](/install-tools/vnc/) for details. The instructions work exactly as presented for WSL2.

