---
title: CMake

additional_search_terms:
- linux
- ide
- ci/cd


minutes_to_complete: 10

author_primary: Jason Andrews

official_docs: https://cmake.org/documentation/

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

It is available for a variety of operating systems and there are multiple ways to install it. 

## What should I do before installing CMake for Arm Linux distributions or CMake for Windows on Arm?

This article provides quick instructions to install CMake for Arm Linux distributions and for Windows on Arm.

### How do I download and install CMake for Windows on Arm?

Confirm you are using a Windows on Arm device such as Windows Dev Kit 2023 or a laptop such as Lenovo ThinkPad X13s or Surface Pro 9 with 5G.

### How do I download and install CMake for Arm Linux distributions?

Confirm you are using an Arm computer with 64-bit Linux by running:

```bash { target="ubuntu:latest" }
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## How do I download and install on Windows on Arm?

Native CMake support for Windows on Arm is available starting with version 3.24. Installers are available now from the [CMake download](https://cmake.org/download/) page. Emulated CMake can be used but is no longer needed unless an older version of CMake must be used.

Download the [Windows ARM64 Installer](https://github.com/Kitware/CMake/releases/download/v3.28.1/cmake-3.28.1-windows-arm64.msi) and run it. 

The welcome screen will appear:

![Install #center](/install-guides/_images/cmake-welcome.png)

Accept the End-User License Agreement. 

Check `Add CMake to the system PATH for the current user` if you want to easily invoke cmake from any directory.

![Install #center](/install-guides/_images/cmake-path.png)

Follow the prompts to complete the installation. 

Wait for the installer to complete and click `Finish`:

![Install #center](/install-guides/_images/cmake-finish.png)

## How do I download and install on Linux?

There are multiple ways to install CMake on Linux. 

### Use the package manager

Use `apt` on Ubuntu and Debian to install:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install cmake -y
```

Use `dnf` to install on Fedora and Amazon Linux 2023:

```console
sudo dnf install cmake -y
```

Depending on your Linux distribution you may have a version of `cmake` which is too old or too new for your project. 

### Use Snap

Installing with `snap` provides the latest version of `cmake`:

```console
sudo snap install cmake --classic
```

With `snap` the `cmake` executable is installed in `/snap/bin` which should already be in your search path.

### Use a specific release from GitHub

If you need a specific version look for it in the [GitHub releases area](https://github.com/Kitware/CMake/releases)

Substitute the release number you want to install in the commands below.. 

1. Download a release from GitHub:

```console
cd $HOME
wget -N https://github.com/Kitware/CMake/releases/download/v3.28.1/cmake-3.28.1-Linux-aarch64.sh
```

2. Run the install script and set the search path using:

```console
mkdir cmake
bash /home/$USER/cmake-3.28.1-Linux-aarch64.sh --skip-license --exclude-subdir --prefix=$HOME/cmake
export PATH=$PATH:$HOME/cmake/bin
```

### How do I verify that CMake is installed?

1. Confirm CMake is installed on Linux or Windows. 

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

2. Print the CMake version

To print the version run:

```console
cmake --version
```

The output is similar to:

```output
cmake version 3.28.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

You are ready to use CMake.
