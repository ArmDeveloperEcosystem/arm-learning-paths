---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: VNC

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

### Link to official documentation
official_docs: 

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Virtual Network Computing (VNC) is one of the common tools used to connect to a remote Linux desktop. During development it may be useful to quickly create a remote desktop on an Arm server.

This section provides info about how to setup VNC on a remote Arm Linux machine.

Feel free to seek out additional VNC tutorials or add more information to this page. 

This installation only works on newer versions of Ubuntu and Debian. It was sucessfully tested on **Ubuntu 22.04** and is known to fail on **Ubuntu 20.04**.

## VNC 

VNC is a client server application. A VNC server runs on a remote machine. A VNC client runs on the local machine and connects to the remote server.

### Install VNC server and xfce4 desktop

To use VNC, a VNC server needs to be installed. There are multiple VNC servers which can be used. This receipe uses [TigerVNC](https://tigervnc.org/)

Desktop software is also needed. There are many options for this, but using xfce4 makes for a minimal install with good performance. 

Install the desktop software.

```bash
sudo apt-get install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils xfce4-terminal -y
```

Install the VNC server.

```bash
sudo apt-get install tigervnc-standalone-server tigervnc-common -y
```

### Set a VNC password

Run the password command to set a password for VNC. This is not the password for the user account, just for the VNC client to connect to the VNC server.

```bash
vncpasswd
```

Remember the password for later when the client is conneted. 

### Configure the desktop startup

Create a file at $HOME/.vnc/xstartup with the contents:

```console
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4
```

Make sure he xstartup file has executable permission.

```bash
chmod +x $HOME/.vnc/xstartup
```

### Setup a systemd service to start and stop VNC

To create a systemd service to start the VNC server create the file /etc/systemd/system/vncserver@.service

Use sudo or root as it is located in a read-only area.


```console
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

The commands below are for any Linux distrbution using systemd. 

To start the SSH daemon:

```console
sudo systemctl start vncserver@1.service
```

To stop the SSH daemon:

```console
sudo systemctl stop vncserver@1.service
```

To restart the VNC service:

```console
sudo systemctl restart vncserver@1.service 
```

### Use port forwarding via SSH to connect

The default port for the first instance of VNC is 5901. SSH port forwarding is the best solution for accessing the Linux desktop on a cloud machine. This way no additional ports need to be opened in the security group. 

SSH to your remote Linux machine. Refer to [SSH](/install-tools/ssh/) for additional details. 

Substitute your private key file and public IP address of the remote machine.

```console
ssh -i <private_key> -L 5901:localhost:5901 ubuntu@<public_ip_address>
```

Once connected via SSH, use a VNC client to connect. [Download](https://sourceforge.net/projects/tigervnc/files/stable/1.12.0/) an install a TigerVNC client for your computer.

Open the VNC client and enter localhost:5901 for the VNC server. 

You will be prompted for the password created earlier with vncpasswd.

A remote Linux Desktop should appear on your local computer. Make sure to close the VNC client first and then exit the SSH connection. 

![Linux desktop](/install-tools/_images/xfce4.png)

