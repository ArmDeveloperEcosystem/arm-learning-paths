---
title: Allow access to the Alluxio Web UI on Azure
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure external traffic for Alluxio Web UI

To allow external traffic on port **19999** for Alluxio on an Azure virtual machine, open the port in the Network Security Group (NSG). The NSG can be attached to the virtual machine's network interface or subnet.

{{% notice Note %}}For more information about Azure setup, see [Getting started with Microsoft Azure Platform](/learning-paths/servers-and-cloud-computing/csp/azure/).{{% /notice %}}

### Add an inbound firewall rule in Azure

To expose the TCP port **19999**, create a firewall rule.

1. Navigate to the [Azure portal](https://portal.azure.com), go to **Virtual Machines**, and select your virtual machine.

![Azure Portal Virtual Machines page with the target VM selected. Check that you are opening the correct virtual machine before configuring its network access.#center](images/virtual_machine.png "Virtual Machines")

2. In the left menu, select **Networking**, then select **Network settings**.

![Azure Portal Networking page showing the network settings linked to the virtual machine. Use this entry to reach the Network Security Group settings for the inbound rule.#center](images/networking.png "Network settings")

3. Navigate to **Create port rule**, and select **Inbound port rule**.

![Azure Portal Create port rule menu with Inbound port rule selected. Choose this option to open port 19999 for the Alluxio Web UI.#center](images/port_rule.png "Create rule")

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

You can now access the Alluxio Web UI over port **19999**.

## What you've learned and what's next

You've now configured the Azure Network Security Group to allow incoming traffic on port 19999. This firewall rule enables external access to the Alluxio Web UI for monitoring cluster status and storage usage.

Next, you'll integrate Alluxio with Apache Spark and begin analyzing cached data performance.
