---
title: Open inbound ports in the Network Security Group
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Allow external traffic to TCP ports 22 (SSH) and 8080

Every new virtual machine created through the Azure wizard is associated with a **Network Security Group (NSG)**. An NSG acts as a stateful firewall – if no rule explicitly allows traffic, Azure blocks it by default.

In this step, you'll open port 22 for SSH and port 8080 so that a web application running on the VM is reachable from your IP for testing. Substitute a different port if required by your workload, or a different IP range if you'd like broader accessibility.

1. In the Azure Portal, open the newly-created VM resource and select **Networking → Network settings** from the left-hand menu.
2. Select the **Network security group**.
3. Select **Create Port Rule**, then choose **Inbound port rule** from the drop-down menu.

4. Fill in the form with **My IP address** as the source and 22 as the destination port:

   ![Add inbound security rule with source of my IP and destination port 22#center](images/create-nsg-rule.png)

5. Select **Add**.
To open port 8080, repeat steps 3-5 and enter 8080 as the destination port.

You have now opened ports 22 and 8080 to your IP. In the next step, you will verify connectivity from your local machine.
