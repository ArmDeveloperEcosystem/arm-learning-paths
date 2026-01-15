---
title: Create a Firewall Rule on Azure
weight: 4


### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
In this section, you will create a firewall rule in the Microsoft Azure Console to allow inbound TCP traffic on port 8080.

To allow external traffic on port **8080** for your application running on an Azure Virtual Machine, you must open the port in the **Network Security Group (NSG)** attached to the VM's network interface or subnet.

{{% notice Note %}}
For support on Azure setup, see the Learning Path [Getting started with Microsoft Azure Platform](/learning-paths/servers-and-cloud-computing/csp/azure/).
{{% /notice %}}


### Create a Firewall Rule in Azure

To expose the TCP port 8080, create a firewall rule.

Navigate to the [Azure Portal]([https://console.cloud.google.com/](https://portal.azure.com)), go to ****Virtual Machines**, and select **your VM**.

![Create a firewall rule alt-text#center](images/virtual_machine.png "Virtual Machines")

Next, in the left menu, click **Networking** and in the **Networking** select **Network settings** that is associated with the VM's network interface.

![Create a firewall rule alt-text#center](images/networking.png "Network settings")

Now, navigate to **Create port rule**, select **Inbound port rule**.

![Create a firewall rule alt-text#center](images/port_rule.png "Create rule")

Next, configure it using the following details. After filling in the details, click **Add** to save the rule.

![Create a firewall rule alt-text#center](images/inbound_rule.png "Network settings")

The network firewall rule has now been created
