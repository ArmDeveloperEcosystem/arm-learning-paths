---
title: Make your Gerrit deployment accessible on Google Cloud Platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a firewall rule on Google Cloud Platform

Create a firewall rule in Google Cloud console to allow incoming TCP traffic on port 8080 and make your Gerrit deployment accessible.

{{% notice Note %}}
If you need help setting up Google Cloud Platform (GCP), see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

### Use the Google Cloud console to create a firewall rule

To expose TCP port 8080 for Gerrit, start by creating a new firewall rule in Google Cloud console:

1. Open the [Google Cloud console](https://console.cloud.google.com/).
2. In the navigation menu, select **VPC network** > **Firewall**.
3. Select **Create firewall rule**.

![Google Cloud Console showing the Create firewall rule page with Name set to allow-tcp-8080, Direction set to Ingress, Action set to Allow, Targets set to Specified target tags with allow-tcp-8080, and Source IPv4 ranges set to 0.0.0.0/0. These settings configure the firewall to allow incoming TCP traffic on port 8080 from any IPv4 address.#center](images/firewall-rule.png "Create a firewall rule")

4. Set **Name** to `allow-tcp-8080`.
5. Select the network you want to use for your VM. The default is `autoscaling-net`, but your organization might use a different network.
6. Set **Direction of traffic** to **Ingress**.
7. Set **Action on match** to **Allow**.
8. For **Targets**, select **Specified target tags** and enter `allow-tcp-8080` in the **Target tags** field.
9. In **Source IPv4 ranges**, enter `0.0.0.0/0`.

This configuration allows incoming TCP traffic on port 8080 from any IPv4 address.

![Google Cloud Console showing the firewall rule configuration form with allow-tcp-8080 in the Name field, Ingress direction, Allow action, Specified target tags field with allow-tcp-8080, and Source IPv4 ranges set to 0.0.0.0/0. This configuration enables TCP port 8080 traffic for Gerrit access.#center](images/network-rule.png "Creating the TCP/8080 firewall rule")

10. Next, configure the protocols and ports for your firewall rule:

    - Under **Protocols and ports**, select **Specified protocols and ports**.
    - Check the **TCP** box.
    - In the **Ports** field, enter `8080`.
    - Select **Create** to finish adding the firewall rule.

This step ensures that only TCP traffic on port 8080 is allowed through the firewall.

![Google Cloud Console showing the Protocols and ports section with TCP checkbox selected and Ports field containing 8080. This ensures only TCP traffic on port 8080 is allowed through the firewall for Gerrit.#center](images/network-port.png "Specifying the TCP port to expose")

## What you've accomplished and what's next

You've now created a network firewall rule to allow access to your Gerrit deployment. 

Next, you'll create a Google Axion C4A virtual machine that you'll use to deploy Gerrit.