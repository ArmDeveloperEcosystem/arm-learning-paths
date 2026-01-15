---
title: Create a firewall rule on GCP
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To allow inbound TCP traffic on port 8080, create a firewall rule in the Google Cloud Console.

{{% notice Note %}}
For more information about GCP setup, see [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Create a firewall rule in GCP

To expose the TCP port 8080, create a firewall rule.

Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Create a firewall rule alt-text#center](images/firewall-rule1.png "Create a firewall rule")

Next, create the firewall rule that exposes the TCP port 8080.
Set the **Name** of the new rule to "allow-tcp-8080". Select your network that you intend to bind to your VM (default is "autoscaling-net", but your organization might have others).

Set **Direction of traffic** to "Ingress". Set **Allow on match** to "Allow" and **Targets** to "Specified target tags".

![Create a firewall rule alt-text#center](images/network-rule2.png "Creating the TCP/8080 firewall rule")

Next, enter "allow-tcp-8080" in the **Target tags** text field. Set **Source IPv4 ranges** to "0.0.0.0/0".

![Create a firewall rule alt-text#center](images/network-rule3.png "Creating the TCP/8080 firewall rule")

Finally, select **Specified protocols and ports** under the **Protocols and ports** section. Select the **TCP** checkbox, enter "8080" in the **Ports** text field, and select **Create**.

![Specifying the TCP port to expose alt-text#center](images/network-port.png "Specifying the TCP port to expose")

The network firewall rule is now created, and you can continue with the VM creation.
