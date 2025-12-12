---
title: Create a Firewall Rule on GCP
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will learn how to create a Firewall Rule within Google Cloud Console.  For this learning path, we need to expose TCP port 15672.

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Create a Firewall Rule in GCP

For this learning path, we need to expose TCP port 15672.  To accomplish this, we first need to create a firewall rule.
- Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
- Go to **VPC Network > Firewall** and press **Create firewall rule**.

![Create a firewall rule](images/firewall-rule.png "Create a firewall rule")

- Next, we create the firewall rule that will expose TCP port 15672 for our learning path.
- Set the "Name" of the new rule to "allow-tcp-15672"
- Select your network that you intend to bind to your VM (default is "autoscaling-net" but your organization might have others that you need to use)
- Direction of traffic should be set to "Ingress"
- Allow on match should be set to "Allow" and the "Targets" should be set to "Specified target tags".
- Enter "allow-tcp-15672" to the "Target tags" text field
- Set the "Source IPv4 ranges" text value to "0.0.0.0/0"

![Create a firewall rule](images/network-rule.png "Creating the TCP/15672 firewall rule")

- Lastly, we select "Specified protocols and ports" under the "Protocols and ports" section
- Select the "TCP" checkbox
- Enter "15672" in the "Ports" text field
- Press "Create"

![Specifying the TCP port to expose](images/network-port.png "Specifying the TCP port to expose")

Our network firewall rule is now created so we can continue with the VM creation!