---
title: Create the Cobalt 100 virtual machine
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use the Azure Portal to deploy a Cobalt 100 VM

Cobalt 100 is Microsoft’s first Arm-based server processor, built on the Armv9 Neoverse-N2 CPU architecture. It is optimized for the performance and efficiency of scale-out, cloud-based applications.

Azure offers Cobalt 100–powered virtual machines in two series:

- **Dpsv6** and **Dplsv6** (general-purpose)
- **Epsv6** (memory-optimized)


To create a Cobalt 100 VM, follow these steps:

1. Sign in to the [Azure Portal](https://portal.azure.com/).
2. Select **Create a resource → Compute → Virtual machine**.
3. Complete the *Basics* tab:
   ![Azure Portal – Basics tab for the VM wizard#center](images/create-cobalt-vm.png)
   The Dpsv6-series are powered by Cobalt 100. Selecting Standard_D4ps_v6 will give you a Cobalt VM with 4 physical cores. you can change the 4 to another value if you want a different number of cores.
4. Upload your public SSH key or generate a new one in the wizard.
5. Disallow public inbound ports for now.
5. Accept the defaults on the *Disks* tab.
6. On the *Networking* tab ensure that a **Public IP** is selected. You will need it to connect later. Leave the NSG settings as *Basic* for now. 

Click **Review + create** followed by **Create**. Azure now deploys the VM and the automatically-generated Network Security Group (NSG). Provisioning takes ~2 minutes.

Navigate to the **Deployment in progress** pane or open the **Notifications** panel to track progress. When the deployment succeeds proceed to the next step to expose an inbound port.
