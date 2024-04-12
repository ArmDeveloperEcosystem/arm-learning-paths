---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm AMBA Viz
draft: true
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
minutes_to_complete: 15

author_primary: Ronan Synnott

### Link to official documentation
official_docs: https://www.arm.com/products/development-tools/embedded-and-software/amba-viz

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Arm AMBA Viz](https://www.arm.com/products/development-tools/embedded-and-software/amba-viz) is a tool used to visualize AMBA events to accelerate SoC verification.

## Download installer packages

AMBA Viz is a component of [Arm Hardware Success Kits](https://www.arm.com/products/development-tools/success-kits).

It is available to download via the [Arm Product Download Hub](https://developer.arm.com/downloads/view/HWSKT-KS-0002).

You can download AMBA Viz as an individual standalone component, or you can download the complete success kits.

For more information on the Download Hub, refer to the [Arm Product Download Hub install guide](../pdh).

## Installation

AMBA Viz requires a Linux host machine with Java 11 or JavaFX.

Extract the software from the bundle to the desired install location. For example:

```command
tar -xf ambaviz.tar.gz
```

Navigate into the newly created `ambaviz-<version>` folder, and run the following script to set up environment variables.

#### sh/bash
```command
source sourceMe.sh
```
#### csh
```command
sourceMe.csh
```

Full installation instructions are provided in the AMBA Viz Release Notes, located in the extracted directory at:
```command
docs/public/assets/pdfs/ambaviz-release-note.pdf
```

## Set up the product license

AMBA Viz is license managed. License setup instructions are available in the [Arm License install guide](../license/).

## Get started

Typically AMBA Viz is launched with a waveform file:
```command
ambaviz -f <waveform_file>
```

A proprietary `AVDB` waveform format is recommended to improve the performance of AMBA Viz.

To convert `VCD` or `FSDB` files to this format, use the `wave2avdb` script, for example:
```command
wave2avdb -d cmn600 -f waves.vcd -o waves.avdb
```
Full usage instructions are given in the User Guide, located in the extracted directory at:
```command
docs/public/assets/pdfs/ambaviz-user-guide.pdf
```
