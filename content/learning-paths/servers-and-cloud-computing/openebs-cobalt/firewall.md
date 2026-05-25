---
title: Allow access to the OpenEBS application on Azure
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure external traffic for the OpenEBS application

To allow external traffic to the Kubernetes application running with OpenEBS persistent storage on an Azure virtual machine, open the Kubernetes NodePort in the Network Security Group (NSG).

The NSG can be attached to the virtual machine's network interface or subnet.

{{% notice Note %}}For more information about Azure setup, see [Getting started with Microsoft Azure Platform](/learning-paths/servers-and-cloud-computing/csp/azure/).{{% /notice %}}

## Verify the Kubernetes service

Check the Kubernetes service to identify the exposed NodePort:

```bash
kubectl get svc
```

The output is similar to:

```output
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)
nginx-openebs   NodePort    10.x.x.x        <none>        80:31635/TCP
```

In this example, the NodePort exposed externally is  `31635`.

### Add an inbound firewall rule in Azure

To expose the Kubernetes NodePort externally, create a firewall rule.

1. Navigate to the [Azure portal](https://portal.azure.com), go to **Virtual Machines**, and select your virtual machine.

![Azure Portal Virtual Machines page with the target VM selected. Check that you are opening the correct virtual machine before configuring its network access.#center](images/virtual_machine.png "Virtual Machines")

2. In the left menu, select **Networking**, then select **Network settings**.

![Azure Portal Networking page showing the network settings linked to the virtual machine. Use this entry to reach the Network Security Group settings for the inbound rule.#center](images/networking.png "Network settings")

3. Navigate to **Create port rule**, and select **Inbound port rule**.

![Azure Portal Create port rule menu with Inbound port rule selected. Choose this option to open port 31635 to expose the Kubernetes Node Port Externally.#center](images/port_rule.png "Create rule")

4. Configure the inbound security rule with the following settings:

- **Source:** My IP address  
- **Source IP addresses:** *(auto-populated with your current public IP)*  
- **Source port ranges:** *  
- **Destination:** Any  
- **Destination port ranges:** **31635**  
- **Protocol:** TCP  
- **Action:** Allow  
- **Name:** allow-openebs-port

{{% notice Note %}}Setting Source to My IP address restricts access to the Kubernetes application to your current machine only. Source port ranges remains * because this refers to the client's ephemeral outbound port, which is dynamically assigned. If your IP address changes or you need to access the application from another machine, update the source IP in this rule.{{% /notice %}}

5. After filling in the details, select **Add** to save the rule.

You can now access the Kubernetes application externally using the NodePort.

## What you've learned and what's next

You've now configured the Azure Network Security Group to allow external access to the Kubernetes application running with OpenEBS LocalPV persistent storage.

This firewall rule enables external browser access to the application deployed on your single-node Kubernetes cluster running on Azure Cobalt 100 Arm64.

Next, you'll install OpenEBS LocalPV on Kubernetes and configure persistent storage provisioning for stateful workloads.
