---
title: Deploy the template
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a resource group

Azure Resource Manager templates deploy resources into a resource group. Create a new resource group to contain your Cobalt 100 VM and its associated resources:

```bash
az group create --name cobalt-rg --location eastus
```

Replace `eastus` with your preferred Azure region. To see available regions that support Cobalt 100 VMs, query Azure for VM SKUs and filter for the Dpsv6 series:

```bash
az vm list-skus --location eastus --size Standard_D --all --output table | grep "ps_v6"
```

The output is similar to:
```output
virtualMachines  eastus       Standard_D16ps_v6       2,3      None
virtualMachines  eastus       Standard_D2ps_v6        2,3      None
virtualMachines  eastus       Standard_D32ps_v6       2,3      None
virtualMachines  eastus       Standard_D48ps_v6       2,3      None
virtualMachines  eastus       Standard_D4ps_v6        2,3      None
virtualMachines  eastus       Standard_D64ps_v6       2,3      None
virtualMachines  eastus       Standard_D8ps_v6        2,3      None
virtualMachines  eastus       Standard_D96ps_v6       2,3      None
```

## Prepare template parameters

The template requires several parameters for deployment. You can provide these values interactively or use a parameters file.

First, read your SSH public key:

```bash
cat ~/.ssh/azure_cobalt_key.pub
```

Copy the output, which you'll use as the `adminPublicKey` parameter.

## Deploy with Azure CLI (interactive)

Deploy the template using the Azure CLI. The command prompts you to enter parameter values:

```bash
az deployment group create \
  --resource-group cobalt-rg \
  --template-file cobalt-vm-template.json \
  --parameters projectName=cobaltdemo \
               adminUsername=azureuser \
               adminPublicKey="<your-ssh-public-key>"
```

Replace `<your-ssh-public-key>` with the output from the `cat` command above.

The deployment takes approximately two to three minutes. Azure CLI displays progress and shows you when the deployment completes.

## Deploy with a parameters file (optional)

For repeated deployments or automation, create a parameters file named `cobalt-vm-parameters.json`:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "projectName": {
      "value": "cobaltdemo"
    },
    "adminUsername": {
      "value": "azureuser"
    },
    "adminPublicKey": {
      "value": "ssh-rsa AAAAB3NzaC1yc2EAAAA... your-email@example.com"
    },
    "vmSize": {
      "value": "Standard_D4ps_v6"
    }
  }
}
```

Replace the `adminPublicKey` value with your actual SSH public key.

Deploy using the parameters file:

```bash
az deployment group create \
  --resource-group cobalt-rg \
  --template-file cobalt-vm-template.json \
  --parameters @cobalt-vm-parameters.json
```

## Verify the deployment

Check the deployment status:

```bash
az deployment group show \
  --resource-group cobalt-rg \
  --name cobalt-vm-template \
  --query properties.provisioningState
```

The output displays `"Succeeded"` when the deployment completes.

List the resources created in the resource group:

```bash
az resource list --resource-group cobalt-rg --output table
```

The output is similar to:

```output
Name                                                     ResourceGroup    Location    Type                                     Status
-------------------------------------------------------  ---------------  ----------  ---------------------------------------  ---------
cobaltdemo-ip                                            cobalt-rg        eastus      Microsoft.Network/publicIPAddresses      Succeeded
default-nsg                                              cobalt-rg        eastus      Microsoft.Network/networkSecurityGroups  Succeeded
cobaltdemo-nsg                                           cobalt-rg        eastus      Microsoft.Network/networkSecurityGroups  Succeeded
cobaltdemo-vnet                                          cobalt-rg        eastus      Microsoft.Network/virtualNetworks        Succeeded
cobaltdemo-nic                                           cobalt-rg        eastus      Microsoft.Network/networkInterfaces      Succeeded
cobaltdemo-vm                                            cobalt-rg        eastus      Microsoft.Compute/virtualMachines        Succeeded
cobaltdemo-vm_OsDisk_1_a3e13c940d07463cace48cfd1458a151  COBALT-RG        eastus      Microsoft.Compute/disks                  Succeeded
```

The output shows the resources created: virtual machine, network interface, public IP address resource, virtual network, network security groups, and OS disk.

## Retrieve the VM's public IP address

Get the public IP address to connect to your VM:

```bash
az vm show \
  --resource-group cobalt-rg \
  --name cobaltdemo-vm \
  --show-details \
  --query publicIps \
  --output tsv
```

Save this IP address, because you'll use it to connect via SSH.

{{% notice Note %}}
The public IP address is dynamically allocated and won't be available until the VM is fully running. If the command returns empty, wait a minute and try again.
{{% /notice %}}

## What you've accomplished and what's next

You've deployed an Arm-based Cobalt 100 VM using an Azure Resource Manager template. The deployment includes network infrastructure with security groups, a public IP address, and a VM running Ubuntu 24.04 LTS.

Next, you'll connect to your VM and verify the Arm64 architecture.
