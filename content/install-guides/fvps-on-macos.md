---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: AVH FVPs on macOS

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- AVH
- Keil
- FVP
- Mac

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author_primary: Christopher Seidl

### Link to official documentation
official_docs: https://github.com/Arm-Examples/FVPs-on-Mac/blob/main/README.md


### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
This guide is intended to get you up and running with the [Arm Virtual Hardware (AVH) Fixed Virtual Platforms (FVPs)](https://www.arm.com/products/development-tools/simulation/virtual-hardware) on macOS. For a thorough review of all options, refer to the official documentation.

## Prerequisites

[Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/).

If this is for commercial use, you might require a paid subscription.

## Clone the repo

Open a terminal and set the working directory to the location in which you would like to store the Fast Model. Then run:

```sh
git clone https://github.com/Arm-Examples/FVPs-on-Mac.git
```

This creates the subdirectory `FVPs-on-Mac` in the current working directory.

## Build the Docker wrapper

Run the build script to create the Docker image and populate the `bin` folder with model wrappers:

```sh
./build.sh
```


When this completes, inspect the created `bin` folder containing symlinks to `fvp.sh`.
These wrappers can be used exactly like any native model executable:

```sh
./bin/FVP_MPS2_Cortex-M3 --version
```

## Expose models to local environment

Add `$(pwd)/FVPs-on-Mac/bin` to `PATH` environment:

```sh
export PATH=$PATH:$(pwd)/FVPs-on-Mac/bin
```

Put this to your `~/.zshrc` to make it permanent.

For further information, refer to the [repository's README.md file](https://github.com/Arm-Examples/FVPs-on-Mac).
