---
title: Configure a firewall rule on Azure
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Allow external traffic for Alluxio Web UI

To allow external traffic on port **19999** for Alluxio running on an Azure virtual machine, open the port in the Network Security Group (NSG) attached to the virtual machine's network interface or subnet.

{{% notice Note %}}For more information about Azure setup, see [Getting started with Microsoft Azure Platform](/learning-paths/servers-and-cloud-computing/csp/azure/).{{% /notice %}}

## Create a firewall rule in Azure

To expose the TCP port **19999**, create a firewall rule.

1. Navigate to the [Azure Portal](https://portal.azure.com), go to **Virtual Machines**, and select your virtual machine.

![Azure Portal showing the Virtual Machines list with the target virtual machine selected#center](images/virtual_machine.png "Virtual Machines")

2. In the left menu, select **Networking** and in the **Networking** select **Network settings** that's associated with the virtual machine's network interface.

![Azure Portal showing the Networking section with Network settings and the associated Network Security Group highlighted#center](images/networking.png "Network settings")

3. Navigate to **Create port rule**, and select **Inbound port rule**.

![Azure Portal showing the Create port rule dropdown menu with Inbound port rule selected#center](images/port_rule.png "Create rule")

4. Configure the inbound security rule with the following settings:

- **Source:** My IP address  
- **Source IP addresses:** *(auto-populated with your current public IP)*  
- **Source port ranges:** *  
- **Destination:** Any  
- **Destination port ranges:** **19999**  
- **Protocol:** TCP  
- **Action:** Allow  
- **Name:** allow-alluxio-port

{{% notice Note %}}Setting **Source** to **My IP address** restricts access to port 19999 to your current machine only. Source port ranges remains `*` because this refers to the client's ephemeral outbound port, which is always dynamically assigned. If your IP address changes or you need to access the Alluxio Web UI from a different machine, update the source IP in this rule.{{% /notice %}}

5. After filling in the details, select **Add** to save the rule.

The network firewall rule is now created, allowing Alluxio Web UI to be accessed over port **19999**.

## What you've learned and what's next

You've configured the Azure Network Security Group to allow incoming traffic on port 19999. This firewall rule enables external access to the Alluxio Web UI for monitoring cluster status and storage usage.

Next, you'll integrate Alluxio with Apache Spark and begin analyzing cached data performance.
