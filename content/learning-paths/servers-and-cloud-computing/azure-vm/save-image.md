---
title: Transfer the image to Azure
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can now use the Azure CLI to create a disk image in Azure and copy the local image to Azure. 

## Prepare Azure resources for the image 

Before uploading the VHD file to Azure storage, set the environment variables for the Azure CLI:

```bash
RESOURCE_GROUP="MyCustomARM64Group"  
LOCATION="centralindia"  
STORAGE_ACCOUNT="mycustomarm64storage"  
CONTAINER_NAME="mycustomarm64container"  
VHD_NAME="azurelinux-arm64.vhd"  
GALLERY_NAME="MyCustomARM64Gallery"  
IMAGE_DEF_NAME="MyAzureLinuxARM64Def"  
IMAGE_VERSION="1.0.0"  
PUBLISHER="custom"  
OFFER="custom-offer"  
SKU="custom-sku"  
OS_TYPE="Linux"  
ARCHITECTURE="Arm64"  
HYPERV_GEN="V2"  
STORAGE_ACCOUNT_TYPE="Standard_LRS"  
VM_NAME="MyAzureLinuxARMVM"  
ADMIN_USER="azureuser"  
VM_SIZE="Standard_D4ps_v6"
```

{{% notice Note %}}
You can modify the environment variables such as RESOURCE_GROUP, VM_NAME, and LOCATION based on your naming preferences, region, and resource requirements.
{{% /notice %}}

Logi n to Azure using the CLI:

```bash
az login
```

If a link is printed, open it in a browser and enter the provided code to authenticate. 

Create a new resource group. If you are using an existing resource group for the RESOURCE_GROUP environment variable you can skip this step. 

```bash
az group create --name "$RESOURCE_GROUP" --location "$LOCATION"
```

Create Azure blob storage.

```bash
az storage account create \ 
  --name "$STORAGE_ACCOUNT" \ 
  --resource-group "$RESOURCE_GROUP" \ 
  --location "$LOCATION" \ 
  --sku Standard_LRS \ 
  --kind StorageV2
```

Create a blob container in the blob storage account.

```bash
az storage container create \ 
  --name "$CONTAINER_NAME" \ 
  --account-name "$STORAGE_ACCOUNT"
```

## Upload and save the image in Azure 

Upload the VHD file to Azure.

```bash
az storage blob upload \ 
  --account-name "$STORAGE_ACCOUNT" \ 
  --container-name "$CONTAINER_NAME" \ 
  --name "$VHD_NAME" \ 
  --file ./azurelinux-arm64.vhd
```

You can now use the Azure console to see the image in your Azure account.

Next, create a custom VM image from this VHD, using Azure Shared Image Gallery (SIG).

```bash
az sig create \ 
  --resource-group "$RESOURCE_GROUP" \ 
  --gallery-name "$GALLERY_NAME" \ 
  --location "$LOCATION"
```
 
Create the image definition.

```bash
az sig image-definition create \
 --resource-group "$RESOURCE_GROUP" \
 --gallery-name "$GALLERY_NAME" \
 --gallery-image-definition "$IMAGE_DEF_NAME" \
 --publisher "$PUBLISHER" \
 --offer "$OFFER" \
 --sku "$SKU" \
 --os-type "$OS_TYPE" \
 --architecture "$ARCHITECTURE" \
 --hyper-v-generation "$HYPERV_GEN"
```

Create the image version to register the VHD as a version of the custom image.

```bash
az sig image-version create \
 --resource-group "$RESOURCE_GROUP" \
 --gallery-name "$GALLERY_NAME" \
 --gallery-image-definition "$IMAGE_DEF_NAME" \
 --gallery-image-version "$IMAGE_VERSION" \
 --location "$LOCATION" \
 --os-vhd-uri "https://${STORAGE_ACCOUNT}.blob.core.windows.net/${CONTAINER_NAME}/${VHD_NAME}" \
 --os-vhd-storage-account "$STORAGE_ACCOUNT" \
 --storage-account-type "$STORAGE_ACCOUNT_TYPE" 
```

Once the image has been versioned, you can retrieve the unique image ID for use in VM creation.

```bash
IMAGE_ID=$(az sig image-version show   \
 --resource-group "$RESOURCE_GROUP"   \
 --gallery-name "$GALLERY_NAME"   \
 --gallery-image-definition "$IMAGE_DEF_NAME"  \
 --gallery-image-version "$IMAGE_VERSION" \
 --query "id" -o tsv)
```

Next, you can create a virtual machine with the new image using the image ID.