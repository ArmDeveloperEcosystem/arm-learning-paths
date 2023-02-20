---
layout: learningpathall
title: Installing the Remote.It Device Package
weight: 3
---

This section explains how to setup Remote.It when you have access to the target device. You may be sitting near the target device now or can connect using SSH, but want to access it from somewhere else in the future. For example, you may at home with a Raspberry Pi 3 or 4 device and you want to connect to it later using SSH when you are not at home.

## Install Remote.It device package on a target device and connect using SSH

Use a local console or SSH to access the target device. Refer to [SSH](/install-tools/ssh/) for help installing and configuring SSH.

Follow the steps below to install the target device package software and connect using SSH.

1 Create an account and log in to your Remote.It Dashboard by using the Web Portal [https://app.remote.it](https://app.remote.it) with a browser or the [Remote.It Desktop Application](https://link.remote.it/download/desktop)

2 Click the + icon in the Dashboard and your device type or cloud instance type to add a new target device

3 Copy the generated command, paste it in the target device terminal or SSH terminal, and press return to execute the command to install.

Watch the Remote.It Dashboard until the new device appears. Click the Connect button under the SSH server to make the networking connection between the target device and you.

4 Click the Launch icon on the right in the blue box. Add the SSH username when the prompted and click save. It should launch your default terminal application. If you would rather create the connection directly in the SSH client of your choice, you can use the other icons to copy the portions of the url you need for your client. For example, the host or the port.

For example, if the username on the target device is 'ubuntu' run:

```console
ssh ssh://ubuntu@proxy50.rt3.io:37348
```

The command can also be formatted with the port number using the `-p` option.

```console
ssh ubuntu@proxy50.rt3.io -p 37348
```

If you use a key pair for security and not a password, you can modify your ssh command as needed to pass in the PemKey path location on your computer.

## Install Remote.It during creation of a new AWS EC2 instance

For a new virtual machines from cloud service providers, the previous instructions would require you to open port 22 for SSH, setup Remote.It, and then close port 22. Although this works, there is a way to automatically install Remote.It during virtual machine initialization. This example covers AWS.

In AWS, customizing a new virtual machine is done using **user data**. Other cloud service providers have similar ways to run commands during the initial machine setup.

Follow the steps below to install the target device software on a new AWS EC2 instance. This will enable an SSH connection without every opening port 22.

1 Create an account and log in to your Remote.It Dashboard by using the Web Portal [https://app.remote.it](https://app.remote.it) with a browser or the [Remote.It Desktop Application](https://link.remote.it/download/desktop)

2 Click the + icon in the Dashboard and select AWS to add a new target device

3 Copy the generated command

4 Log into your AWS account console and go to the EC2 Dashboard

5 Select Launch Instance and setup your configurations for the instance
NOTE: You do not need to allow SSH traffic, you can select a Security Group with no inbound public rules. The security group for the EC2 instance does not need to open port 22 for SSH. This increases security for the EC2 instance.

Open Advanced details to the **user data** input box which is near the bottom.

Before pasting the generated command from Remote.It, add the following to the first line of the **user data** entry box

```console
#!/bin/sh
```

Paste the generated command on the second line.

The results should look similar to the two lines below, but with your actual registration code. Do not use this example.

```console
#!/bin/sh
R3_REGISTRATION_CODE="XXXXX-ABCD-1432-5555-123456789ABC" sh -c "$(curl -L https://downloads.remote.it/remoteit/install_agent.sh)"
```

Watch the Remote.It Dashboard until the new device appears. Click the Connect button under the SSH server to make the networking connection between the target device and you.

4 You can use the icons in the blue connection box to copy the portions of the url you need for your client. For example, the host or the port or the command. Click on the icon that looks like a chain link to copy the ssh command.

AWS EC2 instances use a key pair for SSH. The key pair is configured during EC2 setup in the AWS console. Replace `keyfile.pem` with the path and name of your SSH private key file.

For example, if the username of the account on the EC2 instance (target device) is `ubuntu` run:

For example:

```console
ssh -i /pemkeys/keyfile.pem ssh://ubuntu@proxy50.rt3.io:37348
```

You are now connected to the target device.

The startup time may be slightly longer for a new EC2 instance due to the target device software installation time, but with the benefit of increased security.

## Add additional services

You can use Remote.It to connect to additional services that are running on your device and listening on a port such as a web server, VNC, or MQTT. You can also add a [jump target](https://link.remote.it/support/jumpbox) to a service in the VPC such as a database which will allow you to connect directly through your target device.

From your Remote.It Dashboard target device page, click the + (Add Device) link. Select the type of service, leave the service host/url blank and verify the details for port. If your service type is not found, you can select either TCP or UDP and provide the port information.

If you need to create a connection to a port that is not running directly on your target devicem and your target device can access it via internal IP address or internal DNS, add a service in the same way above, but add the details of the IP or interal DNS name in the service host/url field.

Start your connection and use the connection information in the client application that will use the connection. For example, if it is a web address, you will use a browser Or if it is a VNC connection, you will use your VNC client.
