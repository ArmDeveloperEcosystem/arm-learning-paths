---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: SSH

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

### Link to official documentation
official_docs: 

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Secure Shell (SSH) is the primary tool used to connect to remote Linux servers. It provides a secure shell on a remote machine, and is used frequently in cloud and server development. 

This section provides answers to the most frequently asked SSH setup questions related to server and cloud development.

Feel free to seek out additional SSH tutorials or add more information to this page. 

## SSH 

SSH is a client server application. An SSH server, also called the SSH deamon, runs on a remote machine.  An SSH client runs on the local machine (the one you are typing on) and connects to the remote daemon. 

### Decide if the SSH daemon is already running

For SSH to work, the SSH deamon must be running on the remote machine. Many Linux distributions install and run the SSH daemon automatically.

To find out if the SSH daemon is already running running use the `ps` command.

```console
ps -ef | grep ssh
```

If the result includes a line with `sshd` the daemon is running.


```console
root      1113     1  0 18:48 ?        00:00:00 /usr/sbin/sshd -D
```

Another way to check if the SSH daemon is running is to query the SSH service.

```console
sudo systemctl status sshd
```

If the output displays "running", then the SSH daemon is already running.

```console
Active: active (running) since Tue 2022-09-27 01:04:44 UTC; 17h ago
```

### Install SSH server

If the SSH daemon is not running on the remote Linux machine, install it using the package manager.

For Ubuntu/Debian distributions:
```bash
sudo apt-get install openssh-server 
```

For Red Hat and Amazon Linux distributions.

```bash
sudo yum install openssh-server 
```

### Start and Stop the SSH daemon

The commands below are for any Linux distrbution using systemd. This includes Debian, Ubuntu, and Amazon Linux. 

To start the SSH daemon:

```console
sudo systemctl start ssh 
```

To stop the SSH daemon:

```console
sudo systemctl stop ssh 
```

To restart the SSH daemon:

```console
sudo systemctl restart ssh 
```

### Use a password with SSH

For security reasons, cloud instances don’t enable password logins and there is no password set for the user accounts (such as ubuntu or ec2-user).

Password access is useful to connect when the private key is not available. 

To enable passwords edit the file `/etc/sshd_config` and set `PasswordAuthentication` to yes

To enable it from the command line, run this command:

```console
sudo sed -i '/PasswordAuthentication no/c\PasswordAuthentication yes' /etc/ssh/sshd_config
```

Restart the SSH daemon using the commands above. 

To use a password for SSH a password must be created. 

To create a password for the user ubuntu:

```console
sudo passwd ubuntu
```

For improved security, set the security group of the cloud instance to allow port 22 traffic (SSH) from a minimal set of IP addresses, not anywhere on the internet. Use password access with caution. 

### SSH keys

SSH uses a private and a public key. The public key is placed on the remote machine (server) and the private key is kept on the local machine (client). The keys allow the client to connect to the server.

If a new key pair is needed use the ssh-keygen command to generate a key pair. 

```console
ssh-keygen
```

Answer the questions. Pressing enter to accept all defaults works fine. 

By default, the keys are created in `~/.ssh/id_rsa.pub` (public key) and `~/.ssh/id_rsa` (private key)

Cloud service providers have different ways to manage key pairs. They may also provide ways to generate keys and download them from the web console.

AWS creates a key pair and provides a `.pem` file which is downloaded to the local machine to access AWS EC2 instances. The `.pem` file is the private key.

Accessing an AWS EC2 instance running Ubuntu using:

```console
ssh -i <private_key> ubuntu@<public_ip_address>
```

To use SSH without specifying `-i <private_key>` every time create an SSH configuration for the remote machine. 

Edit the file `~/.ssh/config` on the local machine. 

Pick a name for the remote machine, such as myserver, add the public IP address or DNS name as the Hostname.

User is the username on the remote machine and IdentityFile is the path to the private key on the local machine. 

```console
Host myserver
         Hostname      150.136.142.90
         User          ubuntu
         IdentityFile  ~/mykeyfile.pem
```

With a config file SSH can be used with only the Hostname and no arguments.

```console
ssh myserver
```

### Add a new key pair

If you want to give access to somebody else without enabling password access or sharing your private key, you can add another key pair to the remote machine. You may also want to change the key pair used when the remote machine was created. 

To add or change the key pair edit the file `~/.ssh/authorized_keys` on the remote machine. 

Add a new public key to `authorized_keys`. You can also delete the current public key and just use the new one. 

If you ran `ssh-keygen` on your local machine, the public key is at `~/.ssh/id_rsa.pub` 

Use the new private key on the local machine to connect. If you have `~/.ssh/id_rsa` on your local machine it will be used automatically and you can SSH to the remote machine.
