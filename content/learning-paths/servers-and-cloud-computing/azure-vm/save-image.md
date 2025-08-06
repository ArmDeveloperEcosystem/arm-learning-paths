---
title: Transfer the image to Azure
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I upload and register a VHD image in Azure?

You're now ready to use the Azure CLI to create and upload a custom disk image to Azure. In this section, you'll configure environment variables, provision the necessary Azure resources, and upload a `.vhd` file. Then, you'll use the Shared Image Gallery to register the image for use with custom virtual machines. 

## How do I set up environment variables for the Azure CLI?

Before uploading your VHD file, set the environment variables for the Azure CLI:

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
Modify the environment variables such as RESOURCE_GROUP, VM_NAME, and LOCATION to suit your naming preferences, region, and resource requirements.
{{% /notice %}}

## How do I log in and create Azure resources?

First, log in to Azure using the CLI:

```bash
az login
```

If prompted, open the browser link and enter the verification code to authenticate.

Then, create a new resource group. If you are using an existing resource group for the RESOURCE_GROUP environment variable, you can skip this step: 

```bash
az group create --name "$RESOURCE_GROUP" --location "$LOCATION"
```

Create a new storage account to store your image:

```bash
az storage account create \
  --name "$STORAGE_ACCOUNT" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --sku Standard_LRS \
  --kind StorageV2
```

Next, create a blob container in the storage account:

```bash
az storage container create \
  --name "$CONTAINER_NAME" \
  --account-name "$STORAGE_ACCOUNT"
```

## How do I upload a VHD image to Azure Blob Storage?

First, retrieve the storage account key:

```bash
STORAGE_KEY=$(az storage account keys list \
  --resource-group "$RESOURCE_GROUP" \
  --account-name "$STORAGE_ACCOUNT" \
  --query '[0].value' --output tsv)
```

Then upload your VHD file to Azure Blob Storage:

```bash
az storage blob upload \
  --account-name "$STORAGE_ACCOUNT" \
  --container-name "$CONTAINER_NAME" \
  --name "$VHD_NAME" \
  --file ./azurelinux-arm64.vhd
```

You can now use the Azure console to view the image in your Azure account.

## How do I register a custom image in the Azure Shared Image Gallery?

Create a custom VM image from the VHD, using the Azure Shared Image Gallery (SIG):

```bash
az sig create \
  --resource-group "$RESOURCE_GROUP" \
  --gallery-name "$GALLERY_NAME" \
  --location "$LOCATION"
```
 
Create the image definition:

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

Create the image version from the uploaded VHD:

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

## How do I retrieve the image ID for VM creation?

Once the image has been versioned, you can retrieve the unique image ID for use in VM creation:

```bash
IMAGE_ID=$(az sig image-version show \
 --resource-group "$RESOURCE_GROUP" \
 --gallery-name "$GALLERY_NAME" \
 --gallery-image-definition "$IMAGE_DEF_NAME" \
 --gallery-image-version "$IMAGE_VERSION" \
 --query "id" -o tsv)
```

You'll use this ID to deploy a new virtual machine based on your custom image.

You've successfully uploaded and registered a custom Arm64 VM image in Azure. In the next section, you'll learn how to create a virtual machine using this image.