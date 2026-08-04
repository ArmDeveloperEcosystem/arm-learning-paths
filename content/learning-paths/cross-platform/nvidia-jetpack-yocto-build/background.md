---
title: Understand Yocto image builds for NVIDIA Jetson

weight: 2

layout: "learningpathall"
---

## Understand the Yocto build model

The [Yocto Project overview](https://docs.yoctoproject.org/overview-manual/yp-intro.html) describes a framework for creating tailored Linux-based systems. Yocto isn't a Linux distribution. Instead, it provides tools and metadata that let you define the packages, configuration, and image contents for a specific target.

Yocto uses the OpenEmbedded build system and [BitBake](https://docs.yoctoproject.org/bitbake/) to process recipes, configuration files, and layers. Poky provides a reference distribution that you can extend with hardware support, applications, and product-specific configuration.

Unlike a general-purpose Linux distribution with predefined packages and defaults, you can use Yocto to control the complete image through build metadata. You can include only the required software, reproduce the same configuration across builds, and maintain hardware and product changes in separate layers. The tradeoff is greater build complexity and more upfront configuration.

## Use Yocto to build NVIDIA JetPack images

[NVIDIA JetPack](https://docs.nvidia.com/jetson/jetpack/introduction/index.html) provides the Jetson Linux board support package alongside accelerated libraries and developer tools for NVIDIA Jetson platforms.

The [OpenEmbedded for Tegra (OE4T) `meta-tegra` layer](https://github.com/OE4T/meta-tegra) brings NVIDIA Jetson hardware support into the OpenEmbedded and Yocto build environment. `meta-tegra` enables a Yocto image to use the Jetson kernel, boot components, drivers, and deployment artifacts while managing the root file system through Yocto metadata.

You'll use scripts built around `meta-tegra` to complete the following workflow:

1. Provision a Google Axion C4A virtual machine as the Arm build host.
2. Select a supported NVIDIA Jetson target and build its Yocto image.
3. Bundle the deployment artifacts and transfer them to an Ubuntu host.
4. Flash the image to the Jetson platform and confirm that it boots.

Compared with a preconfigured Jetson Linux image, a tailored Yocto image omits unnecessary packages and services. This omission reduces storage use, limits the attack surface, and improves boot time. Layer-based configuration also helps teams reproduce, maintain, and audit product images.

The tradeoff is additional build and maintenance work. Builds can take several hours, and teams must keep JetPack, Jetson Linux, and `meta-tegra` versions aligned while managing layer compatibility, licenses, proprietary components, and device-specific flashing. 

Before changing versions or adding another Jetson platform, see the [`meta-tegra` documentation](https://oe4t.github.io/master/).

## What you've learned and what's next

You’ve learned how Yocto and `meta-tegra` work together to create tailored NVIDIA Jetson images, including the benefits and maintenance tradeoffs.

Next, provision a Google Axion C4A virtual machine to build the image.
