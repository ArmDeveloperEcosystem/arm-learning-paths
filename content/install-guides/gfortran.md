---
additional_search_terms:
- compiler
- fortran
- hpc
- forge
- linux
- cloud

layout: installtoolsall
minutes_to_complete: 15
author: Florent Lebeau
multi_install: false
multitool_install_part: false
official_docs: https://gcc.gnu.org/onlinedocs/gfortran/
test_images:
- ubuntu:latest
- fedora:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: GFortran
tool_install: true
weight: 1
---

[GNU Fortran](https://gcc.gnu.org/fortran/) is the Fortran compiler front end and run-time libraries for GCC, the GNU Compiler Collection.

GFortran is available on all Linux distributions and can be installed using the package manager.

## Before you begin

Follow the instructions below to install and use `gfortran` on an Arm Linux distribution.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download 

The Linux package manager downloads the required files so there are no special instructions.

## Installation {#install}

### Installing on Debian based distributions such as Ubuntu

Use the `apt` command to install software packages on any Debian based Linux distribution, including Ubuntu.

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install gfortran -y
```

### Installing on Red Hat / Fedora / Amazon Linux

These Linux distributions use `yum` as the package manager. 

To install the most common development tools use the commands below. If the machine has `sudo` you can use it.

```bash { target="fedora:latest" }
sudo yum update -y
sudo yum install gcc-gfortran -y
```

If `sudo` is not available become _root_ and omit the `sudo`.

```console
sudo yum update -y
sudo yum install gcc-gfortran -y
```


## Setting up product license {#license}

Arm GNU Toolchain is open source and freely available for use. No licenses need to be set up for use.

## Get started {#start}

To confirm the installation is complete run:

```bash
gfortran --version
```

To compile an example program, create a text file named `hello.f90` with the contents below.

```fortran { file_name="hello.f90" }
program hello
  ! This is a comment line; it is ignored by the compiler
  print *, 'Hello, Arm world!'
end program hello
```

To compile the program use:

```bash
gfortran hello.f90 -o hello
```

To run the application use:

```bash { command_line="user@localhost" }
./hello
```

The program will print the string specified in the print statement.
