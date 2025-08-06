---
title: Start an Azure virtual machine with the new image
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I launch a virtual machine using my custom Azure image?

Now that your image is registered, you can launch a new VM using the Azure CLI and the custom image ID. This example creates a Linux VM on Cobalt 100 Arm-based processors using the custom image you created earlier.

## How do I create a virtual machine in Azure using a custom image?

Use the following command to create a virtual machine using your custom image:

```bash
az vm create \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --image "$IMAGE_ID" \
  --size "$VM_SIZE" \
  --admin-username "$ADMIN_USER" \
  --generate-ssh-keys \
  --public-ip-sku Standard
```

After the VM is successfully created, retrieve the public IP address.

```bash
az vm show \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --show-details \
  --query "publicIps" \
  -o tsv
```

Use the public IP address to SSH to the VM. Replace `<public-ip-address>` with the IP returned by the previous command.

```bash
ssh azureuser@<public-ip-address>
```

After connecting, print the machine information:

```bash
uname -a
```

The output is similar to:

```output
Linux MyAzureLinuxARMVM 6.6.92.2-2.azl3 #1 SMP Wed Jul  2 02:43:35 UTC 2025 aarch64 aarch64 aarch64 GNU/Linux
```

You are ready to use your Azure Linux virtual machine.
