---
title: Flash the Yocto image onto the NVIDIA Jetson device
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare a local Ubuntu host

The flashing process requires a physical Ubuntu machine running Ubuntu 22.04 or later, with USB access to the NVIDIA Jetson device.

Install the required packages:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y dtc build-essential gdisk gptfdisk udisks2 bmap-tools libxml2-utils zstd tar usbutils
```

## Install the Google Cloud CLI

You need the Google Cloud CLI to transfer the build artifact from the C4A instance to your local Ubuntu host.

To install the CLI on your host, follow the [Google Cloud CLI installation instructions](https://docs.cloud.google.com/sdk/docs/install-sdk).

After installation, authenticate with your Google Cloud account:

```bash
gcloud auth login
```

## Verify SSH access to the C4A instance

Before transferring files, confirm that you can reach the C4A instance from your Ubuntu host. 

Note the following values from the Google Cloud Console:

- Your C4A instance name
- Your Google Cloud project name
- The zone where the C4A instance is running

Test SSH connectivity, replacing `C4A_INSTANCE_NAME`, `GOOGLE_CLOUD_PROJECT_NAME`, and `C4A_CURRENT_ZONE` with your values:

```bash
gcloud compute ssh C4A_INSTANCE_NAME --project GOOGLE_CLOUD_PROJECT_NAME --ssh-flag="-o ServerAliveInterval=60 -o ServerAliveCountMax=9999" --zone=C4A_CURRENT_ZONE
```

## Transfer the build artifact to your local host

On the C4A instance, confirm the location of the bundled archive:

```bash
cd $HOME/jetpack-yocto-builder
ls -al *.tar.gz
```

The output shows one or more `.tar.gz` files. Note the filename.

On your local Ubuntu host, create a working directory and download the archive:

```bash
mkdir -p $HOME/flashing
cd $HOME/flashing
gcloud compute scp C4A_INSTANCE_NAME:~/jetpack-yocto-builder/demo*tar.gz ./yocto_image.tar.gz --project GOOGLE_CLOUD_PROJECT_NAME --zone=C4A_CURRENT_ZONE
```

Verify that the size of the downloaded file is approximately 3 to 4 GB:

```bash
ls -lh $HOME/flashing/yocto_image.tar.gz
```

## Extract the flashing image

Extract the outer archive and then the inner `.zst` archive to produce the flashing tools:

```bash
cd $HOME/flashing
tar xzpf yocto_image.tar.gz
mkdir -p $HOME/flashing/image
cd $HOME/flashing/image
tar xpf ../*.zst
```

Confirm the `initrd_flash` executable is present:

```bash
ls -l ./initrd_flash
```

The output is similar to:

```output
-rwxr-xr-x 1 user user 12345 Aug  1 12:00 ./initrd_flash
```

Keep this terminal session open for the flashing step.

## Flash the NVIDIA Jetson device

The flashing procedure varies by NVIDIA Jetson model and involves three actions:

1. Place the NVIDIA Jetson device into recovery mode using the hardware button sequence for your model.
2. Connect the device to your Ubuntu host with the appropriate USB cable.
3. Run `./initrd_flash` from the extracted image directory on your Ubuntu host.

Follow the [OE4T flashing instructions](https://oe4t.github.io/master/Flashing.html) starting from **step 2**. The extracted `initrd_flash` directory on your local host satisfies step 1.

After the flash completes, disconnect the USB cable. Connect a monitor, keyboard, and optional wired Ethernet connection to the NVIDIA Jetson device, then power it on.

## What you've accomplished and what's next

You've now transferred the Yocto build artifact to a local Ubuntu host, extracted the flashing tools, and flashed the custom Yocto image onto the NVIDIA Jetson device.

Next, boot the Jetson device and explore the running Yocto image.
