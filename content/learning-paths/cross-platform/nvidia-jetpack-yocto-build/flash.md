---
title: Flashing the Yocto image onto Nvidia Jetson
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, we'll prepare a local linux host, running Ubuntu 22.04 or greater, download the completed yocto build artifact file, and use the Nvidia supplied instructions for flashing our Nvidia Jetson device with the newly created yocto image. 

### Prepare a local ubuntu host

Ubuntu will be used locally to connect to and flash the Nvidia Jetson device. Ubuntu 22.04 or later is recommended. The following pre-requisites should also be installed:

```bash
sudo apt update
sudo apt upgrade
sudo apt install -y dtc build-essential gdisk gptfdisk udisks2 bmap-tools libxml2-utils
sudo apt-get install -y zstd tar usbutils
```

### Install the Google Cloud SDK

Please following the instructions here: https://docs.cloud.google.com/sdk/docs/install-sdk to install the google cloud SDK on your local Ubuntu host. 

Once installed, you must first login in with the SDK CLI:

```bash
gcloud auth login
```

From your localh ubuntu host, you can confirm that SSH works by logging into your C4A cloud instance:

From your Google cloud console, please note down:

        - your C4A instance name
        - your Google Cloud project name
        - the zone your C4A instance is currently executing in

Once these are acquired, you can log into your C4A instance via SSH in the google cloud SDK CLI:

```bash
gcloud compute ssh C4A_INSTANCE_NAME --project GOOGLE_CLOUD_PROJECT_NAME --ssh-flag="-o ServerAliveInterval=60 -o ServerAliveCountMax=9999" --zone=C4A_CURRENT_ZONE
```

### Download the completed Yocto build artifacts

Once confirmed that SSH works above, with the SSH session above, note the location of your bundled artifact file... it should be in $HOME/jetpack-yocto-builder within the C4A instance.  

In the SSH shell to your C4A host:

```bash
cd $HOME/jetpack-yocto-builder
ls -al *.tar.gz
pwd
```

Back on your local Ubuntu host, type:

```bash
mkdir $HOME/flashing
cd $HOME/flashing
gcloud compute scp C4A_INSTANCE_NAME:~/jetpack-yocto-builder/demo*tar.gz ./yocto_image.tar.gz --project GOOGLE_CLOUD_PROJECT_NAME --zone=C4A_CURRENT_ZONE
```

You should now see a 3-4GB file on your local Ubuntu host:

```bash
cd $HOME/flashing
ls -al yocto_image.tar.gz
```

Next, extract the contents of this file to acquire the "zst" file (which will be used for flashing):

```bash
cd $HOME/flashing
tar xzpf yocto_image.tar.gz
mkdir $HOME/flashing/image
cd $HOME/flashing/image
tar xzpf ../*.zst
```

You should now have an "initrd_flash" executable in your current directory:

```bash
ls -al ./initrd_flash
```

You are now ready to flash.  Please keep this shell (on your local Ubuntu host where ./initrd_flash is located) active as you'll use it in the next section. 

### Peforming the flash to the Nvidia Jetson device. 

At this point, the instructions for flashing a Nvidia Jetson device varies slightly by device. 

Please follow the Nvidia instructions located here: https://oe4t.github.io/master/Flashing.html starting with **Step 2**. Your open shell on youir Ubuntu host (where ./initrd_flash is located) effectively completes your **Step 1** in the Nvidia instructions.  

The Nvidia instructions will outline:

        - Placing your specific Nvidia Jetson device into "recovery mode"
        - Connecting the appropriate USB port from your Nvidia Jetson device to your local Ubuntu host
        - Initiating the flashing process by executing "./initrd_flash" on your local Ubuntu host

After completing the above Nvidia flashing instructions on your Ubuntu host, your Nvidia Jetson device is now ready to run your custom Yocto image!  

You will need to now connect your Nvidia Jetson device to a monitor and keyboard and optional wired ethernet connection and power it up. 

## What we've learned and what's next

In this section we downloaded and flashed our custom Yocto image for our Nvidia Jetson device. Then we followed the specific Nvidia Jetson device instructions to place our device into "recovery mode" followed by fully flashing the device with our custom Yocto image. 

In the next section, we'll look at what our Nvidia Jetson device looks and feels like running our custom Yocto image!