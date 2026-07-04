---
title: Create a firewall rule for Grafana/TimescaleDB
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Create a firewall rule in Google Cloud Console to expose TCP port 3000 for the TimescaleDB (Grafana) management interface.

{{% notice Note %}}
For help with GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Configure the firewall rule

Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Google Cloud Console VPC Network Firewall page showing the Create firewall rule button in the top menu bar alt-txt#center](images/firewall-rule.png "Create a firewall rule in Google Cloud Console")

Next, create the firewall rule that exposes TCP port 3000.
Set the **Name** of the new rule to "allow-tcp-3000". Select your network that you intend to bind to your VM (default is "autoscaling-net" but your organization might have others).

Set **Direction of traffic** to "Ingress". Set **Allow on match** to "Allow" and **Targets** to "Specified target tags". Enter "allow-tcp-3000" in the **Target tags** text field. Set **Source IPv4 ranges** to "0.0.0.0/0".

![Google Cloud Console Create firewall rule form with Name set to allow-tcp-3000, Direction of traffic set to Ingress, and Target tags field showing allow-tcp-3000 alt-txt#center](images/network-rule.png "Configuring the allow-tcp-3000 firewall rule")

Finally, select **Specified protocols and ports** under the **Protocols and ports** section. Select the **TCP** checkbox, enter "3000" in the **Ports** text field, and select **Create**.

![Google Cloud Console Protocols and ports section with the TCP checkbox selected and port 3000 entered in the Ports text field alt-txt#center](images/network-port.png "Setting TCP port 3000 in the firewall rule")

## What you've accomplished and what's next

In this section, you:

- Created a firewall rule to expose TCP port 3000 for Grafana web interface access
- Configured network ingress rules to allow remote connections from any source IP

Next, you'll provision a Google Axion C4A Arm virtual machine and apply this firewall rule to enable external access to Grafana.
