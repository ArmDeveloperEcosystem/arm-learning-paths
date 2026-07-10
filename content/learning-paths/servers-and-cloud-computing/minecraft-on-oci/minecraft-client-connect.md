---
title: Connect the Minecraft client
description: Configure security lists and OS-level firewalls to open port 25565, and connect to the Minecraft server.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect the Minecraft client to the server

### Opening the port for the Minecraft server

Before you connect to the Minecraft server, change the network policy to allow clients to connect to the Minecraft server over TCP port number 25565. To do this, you need to modify the networking settings for your instance in the OCI dashboard.

1. On the OCI Instances page, choose your Minecraft server instance.
2. In the **Networking** tab, click on the subnet name:
   ![OCI Networking panel displaying instance subnet configurations#center](oci_instance_networking.webp "Open the networking panel in OCI")
3. On the **Security** tab of the subnet page, choose the security list which is active for the instance
   (by default, this is called "Default Security List for vcn-xxxxxxxx")
   ![OCI Subnet Details page highlighting the Default Security List#center](subnet_security_list.webp "Select the Default Security List on the Subnet Details page")
4. Under **Security rules**, add a new Ingress rule (this means the rule applies to incoming traffic
   from outside the instance). Set **Source CIDR** to the public IP address (or range) of the
   players who will connect to your server. For example, if your home IP address is `203.0.113.45`,
   set the Source CIDR to `203.0.113.45/32` to allow only that address. You can add multiple
   ingress rules if players connect from different networks.

   {{% notice Warning %}}
   Avoid using `0.0.0.0/0` as the Source CIDR. This opens the port to the entire internet and
   exposes your server to unauthorized access attempts. Always restrict access to only the IP
   addresses that need to connect.
   {{% /notice %}}

   Set the **Destination Port Range** field to 25565.
   ![OCI Ingress Rules dialog with source CIDR and destination port #center](open_minecraft_port.webp "Configure an Ingress rule to open port 25565")

   You can find your current public IP address by searching "what is my IP address" in a web browser
   from the network you will use to connect.

You will also need to update the instance's local firewall to allow connections to port 25565 on your instance. Run the following commands:

```console
sudo firewall-cmd --permanent --add-port=25565/tcp
sudo firewall-cmd --reload
```

You should now be able to run your Minecraft server on the OCI instance, then start your client on your laptop or desktop. You will first be asked to log in with your Microsoft or Mojang account.

Use the credentials you created for your Microsoft account.

### Connecting to the server from the Minecraft client

1. Before connecting to the server with the client for the first time, you will need to
[register for a Microsoft account](https://signup.live.com/).
2. Start your Minecraft client and log in with your Microsoft account credentials.
3. Start the "Minecraft Java edition" client from the launcher.
   ![Minecraft launcher screen](minecraft_launcher.webp)
4. Choose **Multiplayer** mode - read and click through the warning that third party servers are not operated by Mojang.
5. To add your server to the menu of available servers, choose **Add server**, name your server
something meaningful ("My OCI server" for example) and put the IP address of your instance into the
**Server Address** field:
   ![Minecraft multiplayer server dialog showing Server Name and Server Address fields filled in#center](configuring_new_minecraft_server.webp "Add your OCI instance public IP address to the Server Address field")

You can now join the server and start building!

![Minecraft game client showing successful connection to the custom multiplayer server#center](connecting_to_server.webp "Connect to the custom Minecraft server")

### What you've accomplished

In this guide, you successfully:

- Provisioned an Arm-based VM instance on Oracle Cloud Infrastructure.
- Installed Java and deployed the Minecraft server software.
- Configured OCI security ingress rules and server-side firewalls to expose the port.
- Added and connected to the server using the Minecraft client application.

### Next steps

Now that your server is running, you can share the IP address with friends for multiplayer play. You can also explore automated startup scripts to ensure the server automatically recovers from reboots.