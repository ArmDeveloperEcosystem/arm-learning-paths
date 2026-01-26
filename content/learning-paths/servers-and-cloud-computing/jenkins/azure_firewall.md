---
title: Create a firewall rule on Azure
weight: 4


### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure Azure firewall for Jenkins

To allow external traffic on port 8080 for your application running on an Azure virtual machine, open the port in the Network Security Group (NSG) attached to the virtual machine's network interface or subnet.

{{% notice Note %}} For more information about Azure setup, see [Getting started with Microsoft Azure Platform](/learning-paths/servers-and-cloud-computing/csp/azure/).{{% /notice %}}


## Create a firewall rule in Azure

To expose the TCP port 8080, create a firewall rule.

Navigate to the [Azure Portal](https://portal.azure.com), go to **Virtual Machines**, and select your virtual machine.

![Azure portal Virtual Machines page showing list of running VMs with details like status, location, and size alt-txt#center](images/virtual_machine.png "Virtual Machines")

In the left menu, select **Networking** and in the **Networking** select **Network settings** that is associated with the virtual machine's network interface.

![Azure portal Network settings page showing network interface and security group configuration alt-txt#center](images/networking.png "Network settings")

Navigate to **Create port rule**, and select **Inbound port rule**.

![Azure portal showing Create port rule dropdown with Inbound port rule option highlighted alt-txt#center](images/port_rule.png "Create rule")

Configure it using the following details. After filling in the details, select **Add** to save the rule.

![Azure portal inbound security rule configuration form showing port 8080, TCP protocol, and Allow action alt-txt#center](images/inbound_rule.png "Network settings")

The network firewall rule is now created.
