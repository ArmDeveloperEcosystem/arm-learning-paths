---
title: Set Up Environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the development environment

### Step 1.1. Install Ubuntu

If you are running Windows on your host machine, we recommend using Ubuntu through Windows subsystem for Linux 2 (WSL2). Please see [this learning path](https://learn.arm.com/learning-paths/laptops-and-desktops/wsl2/setup/) for assistance  

This learning path has been validated on Ubuntu 22.04 LTS. However, we expect other linux distributions to work. To verify the Linux distribution you are using you can run the `cat /etc/*release*` command. 

```bash
cat /etc/*release*
```
The top lines from the terminal output will show the distribution version. 

```output
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.5 LTS"
...
```

### Step 1.2. (Optional) Install Microsoft VS Code

This is only optional. You can use any text editor you are comfortable with to view or edit code. By typing “wsl” in VS Code terminal, you can switch to Linux environment.

### Step 1.3. Install python 3

Go to website python.org to download and install.
Verify python is installed by
python3 --version
You should see an output like the following.
```output
Python 3.12.7
```
### Step 1.4. Install python-pip

```bash
sudo apt update
sudo apt install python3-pip -y
pip3 --version
```

If `pip3` is correctly installed you should see an output similar to tht following.

```output
pip 24.2 from <path to pip3>/pip (python 3.12)
```

### Step 1.5. Install make

You will need to install the make build tool in order to build the firmware in the following section.

```bash
sudo apt update
sudo apt install make -y
```

Successful installation of make will show the following when the `make --version` command is run.

```output
$ make --version
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

### Step 1.6. Install ARM GNU toolchain

```bash
cd ~
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.2.rel1/binrel/arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
tar -xvf arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
export PATH="$HOME/arm-gnu-toolchain-13.2.Rel1-x86_64-arm-none-eabi/bin/:$PATH"
```

Please note: you may want to add the command to your `bashrc` file. This enables the Arm GNU toolchain to be easily accessed from any new terminal session. 

