---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: VNC on Arm Linux

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- desktop
- linux

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author: Jason Andrews


### Link to official documentation
official_docs: https://tigervnc.org/

test_images:
- ubuntu:latest
test_maintenance: true

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Virtual Network Computing (VNC) is one of the common tools used to connect to a remote Linux desktop. During development, it can be useful to quickly create a remote desktop on an Arm server.

This guide provides information about how to set up VNC on a remote Arm Linux machine.

This installation only works on newer versions of Ubuntu and Debian. It was successfully tested on Ubuntu 22.04 and Ubuntu 24.04.

## What is VNC?

VNC is a client-server application. A VNC server runs on a remote machine. A VNC client runs on the local machine and connects to the remote server.

### How do I install the VNC server and xfce4 desktop?

To use VNC, you need to install a VNC server. There are multiple VNC servers you can use. This guide uses [TigerVNC](https://tigervnc.org/).

You also need desktop software. There are many options for this, but using [xfce4](https://www.xfce.org/) provides a minimal install with good performance.

Install the desktop software:

```bash
sudo apt-get install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils xfce4-terminal -y
```

Install the VNC server:

```bash
sudo apt-get install tigervnc-standalone-server tigervnc-common -y
```

### How do I set a VNC password?

Run the `vncpasswd` command to set a password for VNC. This is not the password for your user account, but for the VNC client to connect to the VNC server.

```console
vncpasswd
```

Remember this password for later when you connect the client.

### How do I configure the desktop startup for VNC?

Create a file at `$HOME/.vnc/xstartup` with the following contents:

```console
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4
```
Make sure the `xstartup` file has executable permissions:

```console
chmod +x $HOME/.vnc/xstartup
```

### How do I set up a systemd service to manage VNC?

To create a systemd service to start the VNC server, create the file `/etc/systemd/system/vncserver@.service`.

Use `sudo` or root privileges because this file is in a system directory.

If your username is not `ubuntu` change the `User` value to match your username after you create the new file. 

```ini
 [Unit]
 Description=Remote desktop service (VNC)
 After=syslog.target network.target

 [Service]
 Type=simple
 User=ubuntu
 PAMName=login
 PIDFile=/home/%u/.vnc/%H%i.pid
 ExecStartPre=/bin/sh -c '/usr/bin/vncserver -kill :%i > /dev/null 2>&1 || : '
 ExecStart=/usr/bin/vncserver :%i -localhost no -geometry 1440x900 -alwaysshared -fg
 ExecStop=/usr/bin/vncserver -kill :%i

 [Install]
 WantedBy=multi-user.target
```

The following commands are for any Linux distribution that uses `systemd`.

To start the VNC service:

```console
sudo systemctl start vncserver@1.service
```

To stop the VNC service:

```console
sudo systemctl stop vncserver@1.service
```

To restart the VNC service:

```console
sudo systemctl restart vncserver@1.service
```

### How do I use port forwarding via SSH to connect to VNC?

The default port for the first instance of VNC is `5901`. SSH port forwarding is the recommended solution for accessing the Linux desktop on a cloud machine. This way, no additional ports need to be opened in the security group.

SSH to your remote Linux machine. See [SSH](/install-guides/ssh/) for additional details.

Substitute your private key file and the public IP address of the remote machine in the following command:

```console
ssh -i <private_key> -L 5901:localhost:5901 ubuntu@<public_ip_address>
```

Once connected via SSH, use a VNC client to connect. [Download](https://sourceforge.net/projects/tigervnc/files/stable/1.12.0/) and install a TigerVNC client for your computer.

Open the VNC client and enter the following for the VNC server:

```console
localhost:5901
```
You will be prompted for the password you created earlier with `vncpasswd`.

A remote Linux desktop should appear on your local computer. When you are finished, close the VNC client first and then exit the SSH connection.

![Linux desktop #center](/install-guides/_images/xfce4.png)
