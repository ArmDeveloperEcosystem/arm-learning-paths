---
title: Create a Firewall Rule on GCP
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you create a Firewall Rule within Google Cloud Console to expose TCP port 15672.

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Create a Firewall Rule in GCP

To expose TCP port 15672, create a firewall rule.

Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Create a firewall rule](images/firewall-rule.png "Create a firewall rule")

Next, create the firewall rule that exposes TCP port 15672.
Set the **Name** of the new rule to "allow-tcp-15672". Select your network that you intend to bind to your VM (default is "autoscaling-net" but your organization might have others).

Set **Direction of traffic** to "Ingress". Set **Allow on match** to "Allow" and **Targets** to "Specified target tags". Enter "allow-tcp-15672" in the **Target tags** text field. Set **Source IPv4 ranges** to "0.0.0.0/0".

![Create a firewall rule](images/network-rule.png "Creating the TCP/15672 firewall rule")

Finally, select **Specified protocols and ports** under the **Protocols and ports** section. Select the **TCP** checkbox, enter "15672" in the **Ports** text field, and select **Create**.

![Specifying the TCP port to expose](images/network-port.png "Specifying the TCP port to expose")

The network firewall rule is now created and you can continue with the VM creation.
