---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: CMSIS-Build

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cbuild

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://open-cmsis-pack.github.io/devtools/buildmgr/latest/index.html


### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[CMSIS-Build](https://open-cmsis-pack.github.io/devtools/buildmgr/latest/index.html) is a set of tools to enable IDEs and command-line tools to share the same projects. 

Historically, IDEs have maintained project information in files which are unique to the IDE. Command line users often use tools such as make and cmake to capture project build information. 

CMSIS-Build unifies project information, making it easy to share between IDEs and command line tools. Keil MDK projects can be can be used from the Linux command line.

The instructions below cover how to install, configure, and use CMSIS-Build from the Linux command line. This is useful for developers who prefer Linux and for automated testing driven by scripts on Linux.

## Introduction

CMSIS-Build is developed on [GitHub](https://github.com/Open-CMSIS-Pack/devtools) and is part of the [Open-CMSIS-Pack project](https://www.open-cmsis-pack.org/).

Follow the instructions below to install CMSIS-Build on a Linux machine.

## Prerequisites

The instructions are the same for an Arm or x86_64 Linux machine, and Ubuntu or a Debian based Linux distribution is assumed.

CMSIS-Build has the following prerequisites: 
- cmake
- ninja
- compiler such as GCC or Arm Compiler for Embedded

Install the prerequisites.

```bash
sudo apt install cmake ninja-build -y
```

The minimum cmake version is 3.18

If the cmake version from the Linux package manager is too old it can be updated to a newer version using snap.

```bash
sudo apt remove cmake -y
sudo snap install cmake --classic
```

## Download 

Download the latest install file from GitHub. Downloads are provided in the [Releases area](https://github.com/Open-CMSIS-Pack/devtools/releases)

The current version is 1.3.0. 

```console
wget https://github.com/Open-CMSIS-Pack/devtools/releases/download/tools%2Fbuildmgr%2F1.3.0/cbuild_install.sh
```

## Installation

To install, run the downloaded `cbuild_install.sh` script.

To interactively answer the questions from the installer run the script and respond to the prompts.

```console
bash ./cbuild_install.sh
```

The default installation directory is `./cbuild` Change the installation directory as needed.

The default location for storing CMSIS-Packs is `$HOME/.cache/arm/packs`

All of the compilers are not necessary, just accept the defaults for compilers which are not needed. 

At the end of the installer a message is displayed to source the setup file.

The path will be different based on your selections.

```bash
source /home/ubuntu/cbuild/etc/setup
```

The command to source the setup file can be added to .bashrc or .profile 

To change any settings after installation, modify the `etc/setup` file. 

To adjust compiler settings after installation, modify the `.cmake` files in `etc`. These files contain paths and other settings for each compiler. 

## Automated Installation

To automate installation a text file with answers can be passed to `cbuild_install.sh`

The inputs are:
- Installation path
- Directory for storing CMSIS PACKS
- Path to Arm Compiler for Embedded
- Path to Arm Compiler 5
- Path to GNU Arm Embedded compiler
- Path to IAR C/C++ Compiler

The input file can be created manually with an editor. Each line in the file represents an input to an interactive prompt. Leave a blank line to accept the default for a prompt.

If the input file creation also needs to be automated use the command below and enter the input for each prompt or leave a blank line to accept the default.

```bash
cat <<EOF >>cmsis.input
./ctools
$HOME/packs
$HOME/ArmCompilerforEmbedded6.19



EOF
```

Run the installer with the input file. Make sure the directory for the CMSIS Packs exists before running the install.

```bash
bash ./cbuild_install.sh < cmsis.input
```

## Setting up product license {#license}

CMSIS-Build is open source and freely available for use. No licenses need to be set up for use. Compilers, such as Arm Compiler for Embedded, invoked by CMSIS-Build may require a license.

## Get started {#start}

Test CMSIS-Build by building a simple example.

The executables included in CMSIS-Build are [cbuild.sh](https://open-cmsis-pack.github.io/devtools/buildmgr/latest/cbuild.html), [cbuildgen](https://open-cmsis-pack.github.io/devtools/buildmgr/latest/cbuildgen.html) and [cpackget](https://open-cmsis-pack.github.io/devtools/buildmgr/latest/cpackget.html). Refer to the documentation for more details.

Confirm CMSIS-Build is installed correctly by building a Blinky example.

Get the Blinky example for the NXP LPCXpresso55S69 board.

```bash
git clone https://github.com/Arm-Examples/Blinky_LPCXpresso55S69_RTX.git
cd Blinky_LPCXpresso55S69_RTX
```

Build it using `cbuild.sh` to confirm CMSIS-Build and the compiler are installed and working.

The necessary CMSIS Packs will be installed and 

```bash
cbuild.sh Blinky.cprj  --packs
```

If all goes well `Objects/image.axf` will be produced and no errors will occur.
