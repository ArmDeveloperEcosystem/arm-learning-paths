---
title: Start an Azure virtual machine with the new image
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a virtual machine using the new image

You can now use the newly created Azure Linux image to create a virtual machine in Azure with Cobalt 100 processors. Confirm the VM is created by looking in your Azure account in the “Virtual Machines” section.

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

You are ready to use your Azure Linux virtual machine.
