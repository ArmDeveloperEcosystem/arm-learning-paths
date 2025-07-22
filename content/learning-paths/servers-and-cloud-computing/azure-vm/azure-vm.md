---
title: Create custom Azure Linux 3.0 Arm image for the VM
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Roadmap to the Azure Linux 3.0 Arm VM image

In this learning path, we will start by [downloading the Aarch64 ISO of Azure Linux 3.0](https://github.com/microsoft/azurelinux#iso). Using qemu-img, we’ll create a raw disk image and boot a virtual machine with the ISO to install the OS onto the disk. Once the installation is complete, we will convert the raw disk to a fixed-size VHD, upload it to Azure Blob Storage, and then use the Azure CLI to create a custom Arm image. This custom image will enable us to launch Azure Linux 3.0 virtual machines on Arm-based infrastructure, even though the Azure Marketplace currently provides this image only for x64 systems.

Next, switch to a Linux-based environment and proceed with the following steps.

#### 1. Install the Dependencies
```bash
$ sudo apt update && sudo apt install qemu-system-arm qemu-system-aarch64 qemu-efi-aarch64 qemu-utils ovmf -y
```
#### 2. Download the Azure Linux 3.0 ISO
```bash
$ wget https://aka.ms/azurelinux-3.0-aarch64.iso
```
#### 3. Use qemu-img to create a 32 GB raw disk image
```bash
$ qemu-img create -f raw azurelinux-arm64.raw 34359738368
```
This step creates a 32 GB empty raw disk image to install the OS.

#### 4. Boot the ISO and install the OS to the raw image
```bash
$ qemu-system-aarch64 \ 
  -machine virt \ 
  -cpu cortex-a72 \ 
  -m 4096 \ 
  -nographic \ 
  -bios /usr/share/qemu-efi-aarch64/QEMU_EFI.fd \ 
  -drive if=none,file=azurelinux-arm64.raw,format=raw,id=hd0 \ 
  -device virtio-blk-device,drive=hd0 \ 
  -cdrom azurelinux-3.0-aarch64.iso \ 
  -netdev user,id=net0 \ 
  -device virtio-net-device,netdev=net0
```

This step boots the Azure Linux 3.0 ISO on an emulated Arm VM and installs the OS onto the raw disk.

Once the OS boots successfully, install Azure Linux Agent required for VM provisioning, and poweroff the VM, as below:

```bash
$ sudo dnf install WALinuxAgent -y 
$ sudo systemctl enable waagent 
$ sudo systemctl start waagent 
$ sudo poweroff
```
#### 5. Convert Raw Disk to VHD Format
Now that the raw disk image is all set to be used, convert the image to fixed-size VHD, campatible to Azure.

```bash
$ qemu-img convert -f raw -o subformat=fixed,force_size -O vpc azurelinux-arm64.raw azurelinux-arm64.vhd
```

{{% notice Note %}}
VHD files have 512 bytes of footer attached at the end. The “force_size” flag ensures that the exact virtual size specified is used for the final VHD file (in our case, 32 GiB). Without this, qemu-img may round the size or adjust for footer overhead (especially when converting from raw to VHD). “force_size” forces the final image to match the original size. This flag helps make the final VHD size a clean, whole number in MB or GiB, which Azure requires.
{{% /notice %}}

#### 6. Set environment variables
Below uploading the VHD file to Azure Blob storage, set the Environment Variables for the Azure CLI.

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
You can modify the values of these environment variables—such as RESOURCE_GROUP, VM_NAME, LOCATION, and others—based on your naming preferences, region, and resource requirements.
{{% /notice %}}

#### 7. Create a Resource Group on Azure
After [installing the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest), create a new resource group.

```bash
$ az group create --name "$RESOURCE_GROUP" --location "$LOCATION"
```

#### 8. Create Azure Blob Storage on Azure

```bash
$ az storage account create \ 
  --name "$STORAGE_ACCOUNT" \ 
  --resource-group "$RESOURCE_GROUP" \ 
  --location "$LOCATION" \ 
  --sku Standard_LRS \ 
  --kind StorageV2
```

#### 9. Create Blob Container in the Blob Storage Account

```bash
  $ az storage container create \ 
  --name "$CONTAINER_NAME" \ 
  --account-name "$STORAGE_ACCOUNT"
```

#### 10. Upload VHD to the Blob container created in step 9

```bash
$ az storage blob upload \ 
  --account-name "$STORAGE_ACCOUNT" \ 
  --container-name "$CONTAINER_NAME" \ 
  --name "$VHD_NAME" \ 
  --file ./azurelinux-arm64.vhd
```

This successfully uploads the VHD to the Azure Blob Storage account. Confirm the same after visiting the blob storage of your Azure account.

Now, let’s create a custom VM image from this VHD, using Azure Shared Image Gallery.

#### 11. Create Azure Shared Image Gallery
```bash
$ az sig create \ 
  --resource-group "$RESOURCE_GROUP" \ 
  --gallery-name "$GALLERY_NAME" \ 
  --location "$LOCATION"
```
 
#### 12. Create the Image Definition
```bash
$ az sig image-definition create  
 --resource-group "$RESOURCE_GROUP"  
 --gallery-name "$GALLERY_NAME"  
 --gallery-image-definition "$IMAGE_DEF_NAME"  
 --publisher "$PUBLISHER"  
 --offer "$OFFER"  
 --sku "$SKU"  
 --os-type "$OS_TYPE"  
 --architecture "$ARCHITECTURE"  
 --hyper-v-generation "$HYPERV_GEN"
```

#### 13. Create Image Version
```bash
$ az sig image-version create  
 --resource-group "$RESOURCE_GROUP"  
 --gallery-name "$GALLERY_NAME"  
 --gallery-image-definition "$IMAGE_DEF_NAME"  
 --gallery-image-version "$IMAGE_VERSION"  
 --location "$LOCATION"  
 --os-vhd-uri "[https://${STORAGE_ACCOUNT}.blob.core.windows.net/${CONTAINER_NAME}/${VHD_NAME](https://${storage_account}.blob.core.windows.net/$%7BCONTAINER_NAME%7D/$%7BVHD_NAME)}"  
 --os-vhd-storage-account "$STORAGE_ACCOUNT"  
 --storage-account-type "$STORAGE_ACCOUNT_TYPE" 
```

This registers the VHD as a version of your custom image.

#### 14. Retrieve the Image ID
Once the image has been versioned, retrieve the unique ID for use in VM creation.

```bash
$ IMAGE_ID=$(az sig image-version show  
 --resource-group "$RESOURCE_GROUP"  
 --gallery-name "$GALLERY_NAME"  
 --gallery-image-definition "$IMAGE_DEF_NAME"  
 --gallery-image-version "$IMAGE_VERSION"  
 --query "id" -o tsv)
```

#### 15. Create the VM Using the Custom Image
Finally, create the VM with this custom image.

```bash
$ az vm create \ 
  --resource-group "$RESOURCE_GROUP" \ 
  --name "$VM_NAME" \ 
  --image "$IMAGE_ID" \ 
  --size "$VM_SIZE" \ 
  --admin-username "$ADMIN_USER" \ 
  --generate-ssh-keys \ 
  --public-ip-sku Standard
```

This deploys Azure Linux 3.0 Arm64 VM from the custom image. Confirm the same after visiting your Azure account “Virtual Machines” section.

After the VM is successfully created, fetch the Public IP of the VM.

```bash
$ az vm show \ 
  --resource-group "$RESOURCE_GROUP" \ 
  --name "$VM_NAME" \ 
  --show-details \ 
  --query "publicIps" \ 
  -o tsv
```
With the Public IP retrieved, SSH into the VM.

```bash
$ ssh azureuser@<public-ip-address>
```

Replace **public-ip-address** with the IP returned in the previous command.

You can now log into your custom Azure Linux 3.0 Arm64 VM and start using it!

