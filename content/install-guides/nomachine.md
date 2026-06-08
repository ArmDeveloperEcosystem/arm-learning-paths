---
additional_search_terms:
- cloud
- desktop
- linux

layout: installtoolsall
minutes_to_complete: 30
author: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://www.nomachine.com/all-documents
test_images:
- ubuntu:latest
test_link: null
test_maintenance: false
title: NoMachine
tool_install: true
weight: 1
---

[NoMachine](https://www.nomachine.com/) is a client-server application that you can use to connect to a remote Linux desktop, including Arm servers and cloud instances. The NoMachine server runs on the remote machine. The client runs on the local machine and connects to the remote server.

During development, it might be useful to quickly create a remote desktop on an Arm server.

In this guide, you'll learn how to set up NoMachine on a remote Arm Linux machine running Ubuntu.

### Install the xfce4 desktop

To connect to a remote desktop, you need to install desktop software. You can use [xfce4](https://www.xfce.org/) for a minimal install with good performance. 

Install the desktop software:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt-get install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils xfce4-terminal -y
```

### Install NoMachine on a remote server

Create two files on the server in the home directory `$HOME`. Use a text editor to copy and paste this script into a file on the remote machine at `$HOME/nx-key.sh`. The contents of the files are as follows:

```file { file_name="nx-key.sh" }
#!/bin/bash

if [ -f $HOME/.ssh/authorized_keys ]; then
    [ -d $HOME/.nx/config ] || mkdir -p $HOME/.nx/config
    cp $HOME/.ssh/authorized_keys $HOME/.nx/config/authorized.crt
else
    echo "No .ssh/authorized_keys file found"
fi
```

Use a text editor to copy and paste this script into a file on the remote machine at `$HOME/install-nomachine.sh`:

{{% notice Note %}}
The following commands use NoMachine version 9.5.7. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To download the latest version, see [NoMachine downloads](https://downloads.nomachine.com/).
{{% /notice %}}

```file { file_name="install-nomachine.sh" }
#!/bin/bash

# install NoMachine for remote desktop
wget https://download.nomachine.com/download/9.5/Arm/nomachine_9.5.7_2_arm64.deb
sudo dpkg -i nomachine_9.5.7_2_arm64.deb
if [ $? != 0 ]; then
  exit 1
fi

# user of the AMI must run the nx-key.sh to copy their key for NX
echo "$HOME/nx-key.sh" >> /home/$USER/.bashrc
sudo systemctl set-default multi-user

exit 0
```

Give both scripts executable permission:

```bash
chmod +x nx-key.sh install-nomachine.sh
```

On the remote machine, run the install script:

```bash { ret_code="0" }
./install-nomachine.sh
```

### Set a user password for a NoMachine connection

For NoMachine to work, it's best to have a user account on the remote machine with a password. Many cloud instances have accounts without passwords and use only ssh keys to connect. 

If the user account already has a password, you can skip this step. 

To enable passwords, edit the file `/etc/sshd_config` and set `PasswordAuthentication to yes`.

To enable it in a script or from the command line, run:

```console
sudo sed -i '/PasswordAuthentication no/c\PasswordAuthentication yes' /etc/ssh/sshd_config
```

Restart the SSH daemon:

```console
sudo systemctl restart ssh
```

Set a password for the user account. The example shows ubuntu. Change the username as needed.

```console
sudo passwd ubuntu
```

Enter a new password. 

Remember the password for later when the client is connected. 


### Open the NoMachine port

The default port for NoMachine is `4000`. If needed, open this port in the security group. Make sure to open ports only from your IP address, not from anywhere. 

### Install the NoMachine client

[Download](https://downloads.nomachine.com/) and install NoMachine on the client you want to connect from. There are options for most operating systems including Android and iOS. 

Start NoMachine on the client computer by following these steps: 

1. Enter a name for the connection and the (public) IP of the remote machine. The default port is `4000`.

![NoMachine client connection screen showing the Host field and NX port 4000. Use this screen to create a connection profile for your Arm server.#center](/install-guides/_images/nx-connect.png "NoMachine connection profile")

2. The next screen is the login screen. Enter the username and password for the account on the remote machine.

![NoMachine login screen with username and password fields. Enter the Linux account credentials from your Arm server to start the session.#center](/install-guides/_images/nx-login.png "NoMachine login")

3. If a question about creating a new display is presented, answer Yes. 

![NoMachine prompt asking whether to create a new display. Select Yes to start the remote desktop session.#center](/install-guides/_images/nx-confirm.png "Create a new display")
4. NoMachine will resize the remote desktop to fit in the client window. Change the remote display resolution to match the client window size. 

![NoMachine display settings screen showing resolution options. Choose a resolution that matches your client window for clear desktop rendering.#center](/install-guides/_images/nx-resize.png "Set display resolution")

5. Finally, the desktop will appear and is ready to use. 

![Linux xfce4 remote desktop rendered in the NoMachine client window, confirming the remote desktop session is active and ready to use#center](/install-guides/_images/nx-desktop.png "NoMachine remote desktop session")

You're now ready to use NoMachine.