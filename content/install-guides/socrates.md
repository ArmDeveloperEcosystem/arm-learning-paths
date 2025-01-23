---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Socrates

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- architecture
- soc
- ip
- coresight
- corelink
- success kits
- hsk

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

author_primary: Ronan Synnott

### Link to official documentation
official_docs: https://developer.arm.com/documentation/101400

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Arm Socrates](https://developer.arm.com/Tools%20and%20Software/Socrates) is a tool used to select, configure and create Arm IP for easy and error free integration into a System on Chip(SoC).

## Download installer packages

Socrates is a component of [Arm Hardware Success Kits](https://www.arm.com/products/development-tools/success-kits).

It is available to download via the [Arm Product Download Hub](https://developer.arm.com/downloads/).

You can download Socrates as an individual component, or you can download the complete success kits.

For more information on the Download Hub, refer to the [Arm Product Download Hub install guide](/install-guides/pdh/).

## Installation

Arm Socrates requires a Linux machine running Red Hat Enterprise Linux. 

Full specifications are given in the [Installation Guide](https://developer.arm.com/documentation/101400/latest/Setting-up-your-environment/Installation-requirements).

Extract the downloaded software and run the installer. For example:

```command
tar -xf socrates.tar.gz
./ARM-Socrates-1.8.0.1-Linux-x86-64-Install --S --i-agree-to-the-contained-eula
```

Full installation instructions are provided in the [Arm Socrates Installation Guide](https://developer.arm.com/documentation/101400).

See also the output of:
```command
./ARM-Socrates-1.8.0.1-Linux-x86-64-Install --help
```

## Set up the product license

Arm Socrates is license managed. License setup instructions are available in the [Arm License install guide](/install-guides/license/).

Configuration of some Arm IP products require a corresponding license for that IP.

Full details are provided in the [Installation Guide](https://developer.arm.com/documentation/101400/latest/Setting-up-licensing), as well as the Release Notes provided within the downloaded tarball.


## Update IP Catalog

You will need to update the `IP Catalog` within the IDE for the first usage.

A short-cut should pop-up, else navigate the menu to `Window` > `Preferences` > `IP Catalog` > `Updates`, and click `Check for updates`.

Click `Install IP Catalog Updates` if needed.

Click `Apply and Close` when complete.


## Get started

To check Socrates has installed correctly, use the `socrates.sh` command or double‑click the Socrates icon.

You can run `socrates.sh` directly from the installation location, through an alias to the installation location, or you can add the installation location to your path variable.

There is an `Installation Health Check` script provided that runs the first time that you start the software, or the first time that you run a new version. The script checks that all required dependencies are installed and identifies any common installation problems.

Arm has produced a series of videos to help new users get started and learn how to use the tool.\
They are available on the [Arm YouTube channel](https://www.youtube.com/c/arm):

 * [Getting Started](https://youtube.com/playlist?list=PLgyFKd2HIZlY_y7b5OTtyrso45q-eCM_s)
 * [NIC-400 Configuration](https://youtube.com/playlist?list=PLgyFKd2HIZlaQBfd8YEMwSQX_cWIxODgG)
 * [NI-700 Configuration](https://youtube.com/playlist?list=PLgyFKd2HIZlahIsHSSw7ViwiFxeBYc36b)

