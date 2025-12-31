---
title: Create a Firewall Rule on GCP
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will create a firewall rule in the Google Cloud Console to allow inbound TCP traffic on port 8123.

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Create a Firewall Rule in GCP

To expose the TCP port 8123, create a firewall rule.

Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Create a firewall rule alt-text#center](images/firewall-rule1.png "Create a firewall rule")

Set the **Name** of the new rule to "allow-tcp-8123". Select your network that you intend to bind to your VM (default is "autoscaling-net", but your organization might have others).


![Create a firewall rule alt-text#center](images/network-rule2.png "Creating the TCP/8123 firewall rule")

Next, Set **Direction of traffic** to "Ingress". Set **Allow on match** to "Allow" and **Targets** to "Specified target tags". Set **Source IPv4 ranges** to "0.0.0.0/0".

![Create a firewall rule alt-text#center](images/network-rule3.png "Creating the TCP/8123 firewall rule")

Finally, select **Specified protocols and ports** under the **Protocols and ports** section. Select the **TCP** checkbox, enter "8123" in the **Ports** text field, and select **Create**.

![Specifying the TCP port to expose alt-text#center](images/network-port.png "Specifying the TCP port to expose")

The network firewall rule is now created, and you can continue with the VM creation.
