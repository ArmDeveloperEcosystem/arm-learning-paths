---
title: Create a firewall rule on GCP
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section you'll learn how to create a firewall rule in Google Cloud Console to allow traffic on TCP port 8091. This step is required for the Learning Path to ensure your Couchbase deployment is accessible.

{{% notice Note %}}
If you need help setting up Google Cloud Platform (GCP), see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Create a firewall rule in GCP
To expose TCP port 8091 for Couchbase, start by creating a new firewall rule in Google Cloud Console:

- Open the [Google Cloud Console](https://console.cloud.google.com/).
- In the navigation menu, select **VPC network** > **Firewall**.
- Select **Create firewall rule**.

You'll use this rule to allow incoming traffic on TCP port 8091, which is required for Couchbase access on your Arm-based VM.

![Google Cloud Console showing the Create firewall rule page with fields for Name set to allow-tcp-8091, Network dropdown, Direction set to Ingress, Action set to Allow, Targets set to Specified target tags with allow-tcp-8091 entered, and Source IPv4 ranges set to 0.0.0.0/0. The interface is clean and organized, focusing on configuring firewall settings for a virtual machine. The overall tone is neutral and instructional. alt-text#center](images/firewall-rule.png "Create a firewall rule")

- Set **Name** to `allow-tcp-8091`.
- Select the network you want to use for your VM. The default is `autoscaling-net`, but your organization might use a different network.
- Set **Direction of traffic** to **Ingress**.
- Set **Action on match** to **Allow**.
- For **Targets**, select **Specified target tags** and enter `allow-tcp-8091` in the **Target tags** field.
- In **Source IPv4 ranges**, enter `0.0.0.0/0`.

This configuration allows incoming TCP traffic on port 8091 from any IPv4 address.

![Google Cloud Console interface displaying the Create firewall rule page. The main section shows fields for Name set to allow-tcp-8091, Network dropdown, Direction set to Ingress, Action set to Allow, Targets set to Specified target tags with allow-tcp-8091 entered, and Source IPv4 ranges set to 0.0.0.0/0. The environment is a clean, organized web dashboard focused on configuring firewall settings for a virtual machine. The tone is neutral and instructional. All visible text is transcribed in the description. alt-text #center](images/network-rule.png "Creating the TCP/8091 firewall rule")

## Specify protocols and ports

Next, configure the protocols and ports for your firewall rule:

- Under **Protocols and ports**, select **Specified protocols and ports**.
- Check the **TCP** box.
- In the **Ports** field, enter `8091`.
- Select **Create** to finish adding the firewall rule.

This step ensures that only TCP traffic on port 8091 is allowed through the firewall.

![Google Cloud Console showing the Protocols and ports section of the Create firewall rule page. The TCP checkbox is selected and the Ports field contains 8091. The interface is part of a clean, organized web dashboard for configuring firewall settings. Visible text includes Protocols and ports, Specified protocols and ports, TCP, and Ports 8091. The tone is neutral and instructional. alt-text#center](images/network-port.png "Specifying the TCP port to expose")

Your network firewall rule has now been created. You're ready to continue with VM creation.