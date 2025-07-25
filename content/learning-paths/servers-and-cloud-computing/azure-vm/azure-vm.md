---
title: Create an Azure Linux image for Arm 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can view the Azure Linux 3.0 project on [GitHub](https://github.com/microsoft/azurelinux). There are links to the ISO downloads in the project README.

Using QEMU, you can create a raw disk image and boot a virtual machine with the ISO to install the OS onto the disk. 

Once the installation is complete, you can convert the raw disk to a fixed-size VHD, upload it to Azure Blob Storage, and then use the Azure CLI to create a custom Arm image. 

## Download and create a virtual disk file

Use `wget` to download the Azure Linux ISO image file.

```bash
wget https://aka.ms/azurelinux-3.0-aarch64.iso
```

Use `qemu-img` to create a 32 GB raw disk image.

This step creates a 32 GB empty raw disk image to install the OS. You can increase the disk size by modifying the value passed to `qemu-img`. 

```bash
qemu-img create -f raw azurelinux-arm64.raw 34359738368
```

## Boot and install the OS

Use QEMU to boot the operating system in an emulated Arm VM.

```bash
qemu-system-aarch64 \ 
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

Once the OS boots successfully, install the Azure Linux Agent for VM provisioning, and power off the VM.

```bash
sudo dnf install WALinuxAgent -y 
sudo systemctl enable waagent 
sudo systemctl start waagent 
sudo poweroff
```

## Convert the raw disk to VHD Format

Now that the raw disk image is ready to be used, convert the image to fixed-size VHD, making it compatible with Azure.

```bash
qemu-img convert -f raw -o subformat=fixed,force_size -O vpc azurelinux-arm64.raw azurelinux-arm64.vhd
```

{{% notice Note %}}
VHD files have 512 bytes of footer attached at the end. The `force_size` flag ensures that the exact virtual size specified is used for the final VHD file. Without this, QEMU may round the size or adjust for footer overhead (especially when converting from raw to VHD). The `force_size` flag forces the final image to match the original size. This flag helps make the final VHD size a clean, whole number in MB or GiB, which is required for Azure.
{{% /notice %}}

Next, you can save the image in your Azure account. 
