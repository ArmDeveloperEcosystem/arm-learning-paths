---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Compiler for Embedded

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- armclang
- compiler

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://developer.arm.com/documentation/100748

### TEST SETTINGS
test_images:
- ubuntu:latest
- fedora:latest
test_link: null
test_maintenance: true
test_status:
- passed
- passed

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) is a mature toolchain tailored to the development of bare-metal software, firmware, and Real-Time Operating System (RTOS) applications for Arm.

A safety qualified branch of Arm Compiler for Embedded, known as [Arm Compiler for Embedded FuSa](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded%20FuSa), is available for safety critical applications.


## Use as supplied with Arm Development Studio or Keil MDK

The easiest way to access the Arm Compiler for Embedded is to use the version provided with [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio). A given Development Studio version will contain the latest compiler version available at the time of release, and is generally up to date.

Cortex-M users can also use the compiler as provided with [Keil MDK](https://www2.keil.com/mdk5).

Alternative versions can be [downloaded separately](#download).

Arm Compiler for Embedded FuSa must also be [downloaded separately](#download).

## Standalone compiler packages {#download}

Individual compiler packages for all supported host platforms can be downloaded from the [Arm Product Download Hub](../pdh).

- [Arm Compiler for Embedded](https://developer.arm.com/downloads/view/ACOMPE)
- [Arm Compiler for Embedded FuSa](https://developer.arm.com/downloads/view/ACOMP616)

These can either be used standalone or [integrated](#armds) into your Arm Development Studio installation.

To install on Windows, unzip the downloaded package, launch the installer, and follow on-screen prompts.
```console
win-x86_64\setup.exe
```
To install on Linux hosts, untar, then run the install script (note the exact filenames are version and host dependent). For example:

{{< tabpane code=true >}}
  {{< tab header="x86_64" >}}
mkdir tmp
mv ARMCompiler6.19_standalone_linux-x86_64.tar.gz tmp
cd tmp
tar xvfz ARMCompiler6.19_standalone_linux-x86_64.tar.gz
./install_x86_64.sh --i-agree-to-the-contained-eula --no-interactive -d /home/$USER/ArmCompilerforEmbedded6.19
{{< /tab >}}
{{< tab header="aarch64" >}}
mkdir tmp
mv ARMCompiler6.19_standalone_linux-aarch64.tar.gz tmp
cd tmp
tar xvfz ARMCompiler6.19_standalone_linux-aarch64.tar.gz
./install_aarch64.sh --i-agree-to-the-contained-eula --no-interactive -d /home/$USER/ArmCompilerforEmbedded6.19
{{< /tab >}}
{{< /tabpane >}}

Remove the install data when complete.

```console
cd ..
rm -r tmp
```
Add the `bin` directory of the installation to the `PATH` and confirm `armclang` can be invoked.

{{< tabpane code=true >}}
  {{< tab header="bash" >}}
export PATH=/home/$USER/ArmCompilerforEmbedded6.19/bin:$PATH
{{< /tab >}}
  {{< tab header="csh/tcsh" >}}
set path=(/home/$USER/ArmCompilerforEmbedded6.19/bin $path)
{{< /tab >}}
{{< /tabpane >}}

See also: [What should I do if I want to download a legacy release of Arm Compiler?](https://developer.arm.com/documentation/ka005184)

## Integrate with Arm Development Studio {#armds}

To integrate this compiler with Arm Development Studio, [register](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain) the installation before then [configuring](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain/Configure-a-compiler-toolchain-for-the-Arm-DS-command-prompt) the environment to use that version.

Full installation instructions are given in the [documentation](https://developer.arm.com/documentation/100748/latest/Getting-Started/Installing-Arm-Compiler-for-Embedded).

## Setting up product license

Arm Compiler for Embedded and Arm Compiler for Embedded FuSa are license managed. License setup instructions are available [here](../license/).

## Verify installation

Check that the correct compiler version is being used:
```console
armclang --version
```
To verify everything is working, build a simple `Hello World` example as described [here](https://developer.arm.com/documentation/100748/latest/Getting-Started/Compiling-a-Hello-World-example).
```C
// hello.c
#include <stdio.h>
int main() {
  printf("Hello World\n");
  return 0;
}
```
```console
armclang --target=aarch64-arm-none-eabi hello.c
```
