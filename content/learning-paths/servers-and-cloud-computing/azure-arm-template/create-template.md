---
title: Create the Resource Manager template
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Azure Resource Manager template structure

An Azure Resource Manager template consists of several key sections:

- **$schema**: Defines the template language version
- **contentVersion**: Your template's version number
- **parameters**: Input values that customize the deployment
- **variables**: Computed values used throughout the template
- **resources**: Azure resources to create
- **outputs**: Values returned after deployment

## Create the template file

Create a new file named `cobalt-vm-template.json` on your local machine. This template deploys a Cobalt 100 VM with all necessary networking components.

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "projectName": {
      "type": "string",
      "metadata": {
        "description": "Prefix for resource names"
      }
    },
    "location": {
      "type": "string",
      "defaultValue": "[resourceGroup().location]",
      "metadata": {
        "description": "Azure region for resources"
      }
    },
    "adminUsername": {
      "type": "string",
      "metadata": {
        "description": "Admin username for the VM"
      }
    },
    "adminPublicKey": {
      "type": "string",
      "metadata": {
        "description": "SSH public key for authentication"
      }
    },
    "vmSize": {
      "type": "string",
      "defaultValue": "Standard_D4ps_v6",
      "metadata": {
        "description": "Cobalt 100 VM size (Dpsv6 series)"
      }
    }
  },
  "variables": {
    "vNetName": "[concat(parameters('projectName'), '-vnet')]",
    "vNetAddressPrefixes": "10.0.0.0/16",
    "vNetSubnetName": "default",
    "vNetSubnetAddressPrefix": "10.0.0.0/24",
    "vmName": "[concat(parameters('projectName'), '-vm')]",
    "publicIPAddressName": "[concat(parameters('projectName'), '-ip')]",
    "networkInterfaceName": "[concat(parameters('projectName'), '-nic')]",
    "networkSecurityGroupName": "[concat(parameters('projectName'), '-nsg')]",
    "networkSecurityGroupName2": "[concat(variables('vNetSubnetName'), '-nsg')]"
  },
  "resources": [
    {
      "type": "Microsoft.Network/networkSecurityGroups",
      "apiVersion": "2023-04-01",
      "name": "[variables('networkSecurityGroupName')]",
      "location": "[parameters('location')]",
      "properties": {
        "securityRules": [
          {
            "name": "ssh_rule",
            "properties": {
              "description": "Allow SSH access",
              "protocol": "Tcp",
              "sourcePortRange": "*",
              "destinationPortRange": "22",
              "sourceAddressPrefix": "*",
              "destinationAddressPrefix": "*",
              "access": "Allow",
              "priority": 100,
              "direction": "Inbound"
            }
          }
        ]
      }
    },
    {
      "type": "Microsoft.Network/publicIPAddresses",
      "apiVersion": "2023-04-01",
      "name": "[variables('publicIPAddressName')]",
      "location": "[parameters('location')]",
      "properties": {
        "publicIPAllocationMethod": "Dynamic"
      },
      "sku": {
        "name": "Basic"
      }
    },
    {
      "type": "Microsoft.Network/networkSecurityGroups",
      "apiVersion": "2023-04-01",
      "name": "[variables('networkSecurityGroupName2')]",
      "location": "[parameters('location')]",
      "properties": {
        "securityRules": [
          {
            "name": "default-allow-ssh",
            "properties": {
              "priority": 100,
              "access": "Allow",
              "direction": "Inbound",
              "destinationPortRange": "22",
              "protocol": "Tcp",
              "sourceAddressPrefix": "*",
              "sourcePortRange": "*",
              "destinationAddressPrefix": "*"
            }
          }
        ]
      }
    },
    {
      "type": "Microsoft.Network/virtualNetworks",
      "apiVersion": "2023-04-01",
      "name": "[variables('vNetName')]",
      "location": "[parameters('location')]",
      "dependsOn": [
        "[resourceId('Microsoft.Network/networkSecurityGroups', variables('networkSecurityGroupName2'))]"
      ],
      "properties": {
        "addressSpace": {
          "addressPrefixes": [
            "[variables('vNetAddressPrefixes')]"
          ]
        },
        "subnets": [
          {
            "name": "[variables('vNetSubnetName')]",
            "properties": {
              "addressPrefix": "[variables('vNetSubnetAddressPrefix')]",
              "networkSecurityGroup": {
                "id": "[resourceId('Microsoft.Network/networkSecurityGroups', variables('networkSecurityGroupName2'))]"
              }
            }
          }
        ]
      }
    },
    {
      "type": "Microsoft.Network/networkInterfaces",
      "apiVersion": "2023-04-01",
      "name": "[variables('networkInterfaceName')]",
      "location": "[parameters('location')]",
      "dependsOn": [
        "[resourceId('Microsoft.Network/publicIPAddresses', variables('publicIPAddressName'))]",
        "[resourceId('Microsoft.Network/virtualNetworks', variables('vNetName'))]",
        "[resourceId('Microsoft.Network/networkSecurityGroups', variables('networkSecurityGroupName'))]"
      ],
      "properties": {
        "ipConfigurations": [
          {
            "name": "ipconfig1",
            "properties": {
              "privateIPAllocationMethod": "Dynamic",
              "publicIPAddress": {
                "id": "[resourceId('Microsoft.Network/publicIPAddresses', variables('publicIPAddressName'))]"
              },
              "subnet": {
                "id": "[resourceId('Microsoft.Network/virtualNetworks/subnets', variables('vNetName'), variables('vNetSubnetName'))]"
              }
            }
          }
        ],
        "networkSecurityGroup": {
          "id": "[resourceId('Microsoft.Network/networkSecurityGroups', variables('networkSecurityGroupName'))]"
        }
      }
    },
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2023-03-01",
      "name": "[variables('vmName')]",
      "location": "[parameters('location')]",
      "dependsOn": [
        "[resourceId('Microsoft.Network/networkInterfaces', variables('networkInterfaceName'))]"
      ],
      "properties": {
        "hardwareProfile": {
          "vmSize": "[parameters('vmSize')]"
        },
        "osProfile": {
          "computerName": "[variables('vmName')]",
          "adminUsername": "[parameters('adminUsername')]",
          "linuxConfiguration": {
            "disablePasswordAuthentication": true,
            "ssh": {
              "publicKeys": [
                {
                  "path": "[concat('/home/', parameters('adminUsername'), '/.ssh/authorized_keys')]",
                  "keyData": "[parameters('adminPublicKey')]"
                }
              ]
            }
          }
        },
        "storageProfile": {
          "imageReference": {
            "publisher": "Canonical",
            "offer": "ubuntu-24_04-lts",
            "sku": "server-arm64",
            "version": "latest"
          },
          "osDisk": {
            "createOption": "FromImage",
            "managedDisk": {
              "storageAccountType": "Premium_LRS"
            }
          }
        },
        "networkProfile": {
          "networkInterfaces": [
            {
              "id": "[resourceId('Microsoft.Network/networkInterfaces', variables('networkInterfaceName'))]"
            }
          ]
        }
      }
    }
  ],
  "outputs": {
    "vmName": {
      "type": "string",
      "value": "[variables('vmName')]"
    },
    "resourceGroup": {
      "type": "string",
      "value": "[resourceGroup().name]"
    }
  }
}
```

## Key template elements for Cobalt 100

The template includes several Arm-specific configurations.

**VM size**: The `vmSize` parameter defaults to `Standard_D4ps_v6`, part of the Dpsv6 series powered by Cobalt 100 processors. The D4ps_v6 size provides four vCPUs with general-purpose compute capabilities on Arm64 architecture.

Other available Cobalt 100 VM sizes include `Standard_D2ps_v6` (two vCPUs), `Standard_D8ps_v6` (8 vCPUs), and `Standard_D16ps_v6` (16 vCPUs).

**Image reference**: The `storageProfile` section specifies the operating system image with Arm64 architecture. The template uses Ubuntu 24.04 LTS:

```json
"imageReference": {
  "publisher": "Canonical",
  "offer": "ubuntu-24_04-lts",
  "sku": "server-arm64",
  "version": "latest"
}
```

You can change the Arm64 image used in the `imageReference` section. For Ubuntu 22.04 LTS:
```json
"imageReference": {
  "publisher": "Canonical",
  "offer": "0001-com-ubuntu-server-jammy",
  "sku": "22_04-lts-arm64",
  "version": "latest"
}
```

To find available Arm64 images for other Linux distributions, use:
```bash
az vm image list --all --architecture Arm64 --output table
```

**SSH authentication**: The template configures SSH key authentication and disables password authentication for enhanced security:

```json
"linuxConfiguration": {
  "disablePasswordAuthentication": true,
  "ssh": {
    "publicKeys": [
      {
        "path": "[concat('/home/', parameters('adminUsername'), '/.ssh/authorized_keys')]",
        "keyData": "[parameters('adminPublicKey')]"
      }
    ]
  }
}
```

## What you've accomplished and what's next

You've created a complete Resource Manager template that defines network infrastructure, a Cobalt 100 VM with Ubuntu 24.04 LTS, and SSH key authentication. The template uses parameters for flexibility, allowing you to customize deployments without modifying the template structure.

Next, you'll deploy this template to Azure and connect to your new Cobalt 100 VM.