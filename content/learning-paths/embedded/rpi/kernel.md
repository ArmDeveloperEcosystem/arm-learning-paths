---
# User change
title: "Linux Kernel Compile"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Software development examples to investigate the performance differences between the Raspberry Pi 4 and the Arm cloud server are presented below. Every recent cloud server is faster than a Raspberry Pi 4, but getting an understanding of the relative differences helps software developers understand what to do on a cloud server and what to do on a Raspberry Pi 4. 

The first example is the Linux kernel compile.	
				
## Linux Kernel Compile
					
One of the benefits of the Raspberry Pi compared to other Linux boards used in embedded projects is the ease of building the Linux kernel. The good news is the Linux kernel is very easy to build natively on the Raspberry Pi. The bad news is that it takes a very long time. The instructions even have a warning (with long in bold).	
				
“this step can take a **long** time depending on the Raspberry Pi model in use”		
			
Follow the [Linux kernel information](https://www.raspberrypi.com/documentation/computers/linux_kernel.html) to build a kernel on the Raspberry Pi and then on the cloud server to see how long it takes. 

Follow the instructions for the 64-bit configuration.

The cloud server data shown is for an always free A1 instance on Oracle Cloud with 4 vCPUs and 24 Gb RAM. 

								
| System | Kernel compile time             |
|--------|--------------------------------:|
|Raspberry Pi 4 (8 Gb RAM)   | 81 min 17 sec |
|Oracle A1 instance (24 Gb RAM)    | 20 min 6 sec |

The kernel build command sequence is shown below for reference.

For the Raspberry Pi 4:

```console
sudo apt install git bc bison flex libssl-dev make
git clone --depth=1 https://github.com/raspberrypi/linux
cd linux
KERNEL=kernel8
make bcm2711_defconfig
make -j4 Image.gz modules dtbs
sudo make modules_install
sudo cp arch/arm64/boot/dts/broadcom/*.dtb /boot/
sudo cp arch/arm64/boot/dts/overlays/*.dtb* /boot/overlays/
sudo cp arch/arm64/boot/dts/overlays/README /boot/overlays/
sudo cp arch/arm64/boot/Image.gz /boot/$KERNEL.img
```

For an Arm cloud server running `Ubuntu 22.04`:

```console
sudo apt install git bc bison flex libssl-dev make libc6-dev libncurses5-dev
sudo apt install crossbuild-essential-arm64
git clone --depth=1 https://github.com/raspberrypi/linux
cd linux
KERNEL=kernel8
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- bcm2711_defconfig
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- Image modules dtbs -j6
```

Kernel building is significantly faster on the Arm cloud server and the instructions work perfectly, even though they were intended for cross compiling from another architecture. The drawback is the results must be copied to the Raspberry Pi 4 to use them, extra steps which take time. 
	

