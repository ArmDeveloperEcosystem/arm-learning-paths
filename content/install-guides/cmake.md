---
title: CMake

additional_search_terms:
- linux
- ide
- ci/cd


minutes_to_complete: 10

description: Install CMake on Arm Linux (aarch64) and Windows on Arm to build and manage C and C++ projects using a cross-platform build system.

author: Jason Andrews

official_docs: https://cmake.org/documentation/
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=cmake

test_images:
- ubuntu:latest
test_maintenance: false

layout: installtoolsall
tool_install: true
multi_install: false
multitool_install_part: false
weight: 1
---

[CMake](https://cmake.org/) is an open-source, cross-platform build tool for software development projects, especially C and C++. 

CMake is available on a variety of operating systems and can be installed in different ways. In this guide, you'll learn how to install CMake for Arm Linux distributions and for Windows on Arm. 

## Before you begin

If you're installing CMake for Windows on Arm, ensure you are using a Windows on Arm device such as the Lenovo ThinkPad X13s or Surface Pro 9 with 5G.

If you're installing CMake for Arm Linux, confirm you are using an Arm computer with 64-bit Linux by running:

```bash { target="ubuntu:latest" }
uname -m
```

The output is similar to:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download and install CMake on Windows on Arm

Native CMake support for Windows on Arm is available starting with version 3.24. Emulated CMake can be used but is no longer needed unless you need to use an older version of CMake.

The following steps install CMake version 4.3.1. To find the latest Windows on Arm installer, see [CMake download](https://cmake.org/download/).

To download and install CMake on Windows on Arm, follow these steps: 

1. Download the [Windows ARM64 Installer](https://github.com/Kitware/CMake/releases/download/v4.3.1/cmake-4.3.1-windows-arm64.msi) and run it. The welcome screen will appear.

 ![A screenshot of the Windows CMake Setup Wizard welcome page that asks the user to click the Next button to contunue with installation. #center](/install-guides/_images/cmake-welcome.png)

2. Click **Next** and then accept the End-User License Agreement.

3. Under **Install Options**, to invoke CMake from any directory, select **Add CMake to the system PATH for the current user** and then click **Next**.

4. Follow the prompts to complete the installation. Wait for the installer to complete and then click **Finish**.
![A screenshot of the CMake Windows Setup Wizard that shows that the installation is complete and asks the user to click the Finish button to exit the Wizard. #center](/install-guides/_images/cmake-finish.png) 

<!-- ![Install #center](/install-guides/_images/cmake-path.png) -->

## Download and install CMake on Linux

There are multiple ways to install CMake on Linux. 

### Install CMake using the package manager

On Ubuntu and Debian, use `apt`:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install cmake -y
```

On Fedora and Amazon Linux 2023, use `dnf`:

```console
sudo dnf install cmake -y
```

{{% notice Note %}}
Depending on your Linux distribution, you may have a version of `cmake` which is too old or too new for your project. 
{{% /notice %}}

### Install CMake with Snap

By installing with `snap`, you get the latest version of `cmake`:

```console
sudo snap install cmake --classic
```

With `snap`, the `cmake` executable is installed in `/snap/bin` which should already be in your search path.

### Use a specific CMake release from GitHub

To install a specific version of CMake from GitHub, follow these steps:

{{% notice Note %}}
The following commands use CMake version 4.3.1. The same commands work with other versions. Replace the script used in these steps with the script for your version of choice. To find the latest version, see [CMake releases](https://github.com/Kitware/CMake/releases).
{{% /notice %}} 

1. Download a release from GitHub:

```console
cd $HOME
wget -N https://github.com/Kitware/CMake/releases/download/v4.3.1/cmake-4.3.1-linux-aarch64.sh
```

2. Run the install script and set the search path:

```console
mkdir cmake
bash /home/$USER/cmake-4.3.1-Linux-aarch64.sh --skip-license --exclude-subdir --prefix=$HOME/cmake
export PATH=$PATH:$HOME/cmake/bin
```

### Verify that CMake is installed

After installing CMake, run it to confirm it is installed and can be found: 

```cmd
cmake
```

The output is similar to:

```output
Usage

  cmake [options] <path-to-source>
  cmake [options] <path-to-existing-build>
  cmake [options] -S <path-to-source> -B <path-to-build>

Specify a source directory to (re-)generate a build system for it in the
current working directory.  Specify an existing build directory to
re-generate its build system.

Run 'cmake --help' for more information.
```
After confirming CMake can be found, print the version:

```console
cmake --version
```

The output is similar to:

```output
cmake version 4.3.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

You are now ready to use CMake.
