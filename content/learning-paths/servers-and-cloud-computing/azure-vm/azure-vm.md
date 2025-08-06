---
title: Create an Azure Linux image for Arm 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can view the Azure Linux 3.0 project on [GitHub](https://github.com/microsoft/azurelinux). The project README includes links to ISO downloads.

Using [QEMU](https://www.qemu.org/), you can create a raw disk image, boot a virtual machine with the ISO, and install the operating system. After installation is complete, you'll convert the image to a fixed-size VHD, upload it to Azure Blob Storage, and use the Azure CLI to create a custom Arm image. 

## Download and create a virtual disk file

Use `wget` to download the Azure Linux ISO image file:

```bash
wget https://aka.ms/azurelinux-3.0-aarch64.iso
```

Create a 32 GB empty raw disk image to install the OS:

```bash
qemu-img create -f raw azurelinux-arm64.raw 34359738368
```

{{% notice Note %}}
You can change the disk size by adjusting the value passed to `qemu-img`. Ensure it meets the minimum disk size requirements for Azure (typically at least 30 GB). 
{{% /notice %}}


## Boot the VM and install Azure Linux

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

Follow the installer prompts to enter the hostname, username, and password. Use `azureuser` as the username to ensure compatibility with later steps.

{{% notice Note %}}The installation process takes several minutes.{{% /notice %}}

At the end of installation, confirm the reboot prompt. After rebooting into the newly-installed OS, install and enable the Azure Linux Agent: 

```bash
sudo dnf install WALinuxAgent -y
sudo systemctl enable waagent
sudo systemctl start waagent
sudo poweroff
```

{{% notice Note %}} It can take a few minutes to install the agent and power off the VM.{{% /notice %}}

## Convert the raw disk to VHD format

Now that the raw disk image is ready for you to use, convert it to fixed-size VHD, which makes it compatible with Azure.

```bash
qemu-img convert -f raw -o subformat=fixed,force_size -O vpc azurelinux-arm64.raw azurelinux-arm64.vhd
```

{{% notice Note %}}
VHD files include a 512-byte footer at the end. The `force_size` flag ensures the final image size matches the requested virtual size. Without this, QEMU might round the size or adjust for footer overhead (especially when converting from raw to VHD). The `force_size` flag forces the final image to match the original size. This is required for Azure compatibility, as it avoids rounding errors and ensures the VHD ends at a whole MB or GB boundary.
{{% /notice %}}

In the next step, you'll upload the VHD image to Azure and register it as a custom image for use with Arm-based virtual machines.
