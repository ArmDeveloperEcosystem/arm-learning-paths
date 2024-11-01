---
title: Set Up Environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the development environment

### Step 2.1. Install Ubuntu 22.04

Himax SDK needs to be compiled in a Linux environment. If you use a Windows computer, it is recommended to install WSL, by searching Ubuntu 22.04.3 LTS in Microsoft store. This learning path has been validated on Ubuntu 22.04 LTS. However, we expect other linux distributions to work. 

### Step 2.2. (Optional) Install Microsoft VS Code

This is only optional. You can use any text editor to view/change code. By typing “wsl” in VS Code terminal, you can switch to Linux environment.

### Step 2.3. Install python 3

Go to website python.org to download and install.
Verify python is installed by
python3 --version
You should see an output like the following.
```bash
Python 3.12.7
```
### Step 2.4. Install python-pip

```bash
sudo apt update
sudo apt install python3-pip
pip3 --version
```

If `pip3` is correctly installed you should see an output similar to tht following.

```output
pip 24.2 from <path to pip3>/pip (python 3.12)
```

### Step 2.5. Install make

You will need to install the make build tool in order to build the firmware in the following section.

```bash
sudo apt update
sudo apt install make -y
```

### Step 2.6. Install ARM GNU toolchain
```bash
cd ~
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.2.rel1/binrel/arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
tar -xvf arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
export PATH="$HOME/arm-gnu-toolchain-13.2.Rel1-x86_64-arm-none-eabi/bin/:$PATH"
```

Please note: you may want to add the command to your `bashrc` file. This enables the Arm GNU toolchain to be easily accessed from any new terminal session. 

