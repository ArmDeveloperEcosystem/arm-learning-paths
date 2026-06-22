---
title: Create a firewall rule on GCP
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section you'll learn how to create a firewall rule in Google Cloud Console to allow traffic on TCP port 8080. This step is required for the Learning Path to ensure your Gerrit deployment is accessible.

{{% notice Note %}}
If you need help setting up Google Cloud Platform (GCP), see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Create a firewall rule in GCP
To expose TCP port 8080 for Gerrit, start by creating a new firewall rule in Google Cloud Console:

- Open the [Google Cloud Console](https://console.cloud.google.com/).
- In the navigation menu, select **VPC network** > **Firewall**.
- Select **Create firewall rule**.

You'll use this rule to allow incoming traffic on TCP port 8080, which is required for Gerrit access on your Arm-based VM.

![Google Cloud Console showing the Create firewall rule page with Name set to allow-tcp-8080, Direction set to Ingress, Action set to Allow, Targets set to Specified target tags with allow-tcp-8080, and Source IPv4 ranges set to 0.0.0.0/0. These settings configure the firewall to allow incoming TCP traffic on port 8080 from any IPv4 address.#center](images/firewall-rule.png "Create a firewall rule")

- Set **Name** to `allow-tcp-8080`.
- Select the network you want to use for your VM. The default is `autoscaling-net`, but your organization might use a different network.
- Set **Direction of traffic** to **Ingress**.
- Set **Action on match** to **Allow**.
- For **Targets**, select **Specified target tags** and enter `allow-tcp-8080` in the **Target tags** field.
- In **Source IPv4 ranges**, enter `0.0.0.0/0`.

This configuration allows incoming TCP traffic on port 8080 from any IPv4 address.

![Google Cloud Console showing the firewall rule configuration form with allow-tcp-8080 in the Name field, Ingress direction, Allow action, Specified target tags field with allow-tcp-8080, and Source IPv4 ranges set to 0.0.0.0/0. This configuration enables TCP port 8080 traffic for Gerrit access.#center](images/network-rule.png "Creating the TCP/8080 firewall rule")

## Specify protocols and ports

Next, configure the protocols and ports for your firewall rule:

- Under **Protocols and ports**, select **Specified protocols and ports**.
- Check the **TCP** box.
- In the **Ports** field, enter `8080`.
- Select **Create** to finish adding the firewall rule.

This step ensures that only TCP traffic on port 8080 is allowed through the firewall.

![Google Cloud Console showing the Protocols and ports section with TCP checkbox selected and Ports field containing 8080. This ensures only TCP traffic on port 8080 is allowed through the firewall for Gerrit.#center](images/network-port.png "Specifying the TCP port to expose")

Your network firewall rule has now been created. You're ready to continue with VM creation.