---
layout: learningpathall
title: Install remote.it on target devices
weight: 3
---

## Before you begin

A second computer running Linux with SSH configured is required for this section. This computer is called the target device.

This section explains how to setup remote.it when you have access to the target device. You may be sitting near the target device now or can connect using SSH, but want to access it from somewhere else in the future. For example, you may at home with a Raspberry Pi 3 or 4 device and you want to connect to it later using SSH when you are not at home.

## Install remote.it on a target device and connect using SSH

Use a local console or SSH to access the target device. Refer to [SSH](/install-tools/ssh/) for help installing and configuring SSH. 

Follow the steps below to install the target device software and connect using SSH.

1 Log in to your remote.it account using a browser to access the dashboard

2 Click the + icon in the dashboard and select Linux to add a new target device

3 Copy the generated command and paste it in the target device terminal 

Watch the dashboard until the new device appears. Click the Connect button under the SSH server to make the networking connection between the target device and the remote.it server.

4 Click the COPY SSH URL icon, which looks like a paper clip. Add the SSH username when the prompted and click save.

5 Return to the initiator device and paste the SSH URL into the terminal. 

For example, if the username on the target device is ubuntu run:

```console
ssh ssh://ubuntu@proxy50.rt3.io:37348
```

The command can also be formatted with the port number using the `-p` option.

```console
ssh ubuntu@proxy50.rt3.io -p 37348
```

You should now connected to the target device using SSH. 

## Install remote.it during creation of a new on AWS EC2 instance

For a new virtual machines from cloud service providers, the previous instructions would require you to open port 22 for SSH, setup remote.it, and then close port 22. Although this works, there is a way to automatically install remote.it during machine initialization. This example covers AWS. 

In AWS, customizing a new virtual machine is done using **user data**. Other cloud service providers have similar ways to run commands during the initial machine setup. 

Follow the steps below to install the target device software on a new AWS EC2 instance. This will enable an SSH connection without every opening port 22.

1 Log in to your remote.it account using a browser to access the dashboard

2 Click the + icon in the dashboard and select Linux to add a new target device

3 Copy the generated command and paste it to the **user data** box in the AWS console

The **user data** input box is near the bottom of the Advanced details in the AWS console.

Before pasting the generated command, add to the first line of the **user data** entry box

```console
#!/bin/sh
```

Paste the generated command on the second line.

The results should look similar to the two lines below, but with your actual registration code.

```console
#!/bin/sh
R3_REGISTRATION_CODE="416ED829-ABCD-1432-5555-123456789ABC" sh -c "$(curl -L https://downloads.remote.it/remoteit/install_agent.sh)"
```

The security group for the EC2 instance does not need to open port 22 for SSH. This increases security for the EC2 instance. 

Watch the dashboard until the new device appears. Click the Connect button under the SSH server to make the networking connection between the target device and the remote.it server.

4 Click the COPY SSH URL icon, which looks like a paper clip. Add the SSH username when the prompted and click save.

5 Return to the initiator device and paste the SSH URL into the terminal. 

AWS EC2 instances use a key pair for SSH. The key pair is configured during EC2 setup in the AWS console. Replace `keyfile.pem` with the name of your SSH private key file.

For example, if the username of the account on the EC2 instance (target device) is `ubuntu` run:

For example:

```console
ssh -i keyfile.pem ssh://ubuntu@proxy50.rt3.io:37348
```

You are now connected to the target device.

The startup time may be slightly longer for a new EC2 instance due to the target device software installation time, but with the benefit of increased security.

This type of connection is called a proxy connection. The target device notifies remote.it about itself and when an initiator device requests a connection remote.it connects the initiator device with the target device. 

