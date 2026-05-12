---
title: Use SSH to connect to WSL

weight: 5
layout: learningpathall
---


## Run SSH on WSL 

SSH can be used to connect to WSL and to copy files from Windows.

If you only want to copy files between Windows and WSL on the current machine, SSH is not needed. 

WSL automatically mounts the Windows `C:\` drive on `/mnt/c`

For example, if you download a file while using a browser in the Windows `Downloads` directory and you want to bring it into Linux use the `cp` command.

Substitute your username and the filename to be copied.

```bash
cp /mnt/c/Users/<username>/Downloads/<filename> .
```

If SSH is needed to access WSL from a different machine continue with the instructions below.

## Install SSH server

Install the SSH server inside the Linux distribution. 

```bash
sudo apt install openssh-server -y
```

Start the SSH server:

```bash
sudo /etc/init.d/ssh start
```

The SSH server can also be started automatically using systemd. Refer to the [systemd](/learning-paths/laptops-and-desktops/wsl2/systemd/) information.

Once the SSH server is started, it's possible to ssh from the Windows Command Prompt to WSL. 

Make sure to add the Linux username to the `ssh` command if the Windows username is different from the Linux username.

```cmd
ssh.exe user@localhost
```

## Change the SSH server port

You can use a higher port number for the SSH server. Do this if you are not able to connect from another machine. 

Modify the SSH config file to change the port number for the SSH server. 

Use port 2022 for SSH instead of the default port 22.

Use a text editor to modify the file `/etc/ssh/sshd_config` and uncomment the `#Port 22` to be just `Port 2022`

To edit from the command line:
```
sudo sed -i -E 's,^#?Port.*$,Port 2022,' /etc/ssh/sshd_config
```

Restart the SSH server for the new port to be used:

```bash
sudo /etc/init.d/ssh stop
sudo /etc/init.d/ssh start
```

Use `ssh` with `-p` to specify the new port. 

```cmd
ssh user@localhost -p 2022
```

There are two options to SSH from another machine on the local network:
 - Bridged networking
 - Port forwarding

# Bridged networking

WSL uses NAT by default. This means the Linux distribution running in WSL will get an IP address starting with 172.X.X.X and not an IP address on the local network. NAT makes it impossible to SSH to WSL.

One way to get an IP on the local network is to use a bridged network. 

For more information refer to the [short WSL bridging and networking reference](https://github.com/luxzg/WSL2-fixes/blob/master/networkingMode%3Dbridged%20-%20quick%20setup.md)

# Port forwarding

Another way to connect to WSL via SSH is to forward or proxy the Windows port for SSH, such as 2022, to the WSL instance. 

Before starting, find the IP address of the WSL instance.

```cmd
wsl hostname -I
```

Save the IP address. 

Run `New-NetFirewallRule` from a PowerShell prompt with Administrator privilege to allow port 2022 from outside Windows:

```cmd
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd) for WSL' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 2022
```

Run `netsh` from a Windows Command Prompt with Administrator privilege. Substitute the IP address with the one found using the `wsl hostname` command above for the `connectaddress`. This forwards port 2022 to the WSL IP address.

```console
netsh interface portproxy add v4tov4 listenport=2022 listenaddress=0.0.0.0 connectport=2022 connectaddress=172.18.164.187
```

Try to ssh from another machine on the local network. 

Get the IP address of Windows:

```cmd
ipconfig
```

From another local machine SSH to the Windows IP on port 2022 and it should forward to WSL running on that Windows computer. 




