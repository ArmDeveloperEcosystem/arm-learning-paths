---
title: Set up environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Set up the development environment

This learning path has been validated on Ubuntu 22.04 LTS and macOS.

{{% notice %}}
If you are running Windows on your host machine, you can use Ubuntu through Windows subsystem for Linux 2 (WSL2). Check out [this learning path](https://learn.arm.com/learning-paths/laptops-and-desktops/wsl2/setup/) to get started.
{{% /notice %}}

## Install Python, pip and git

You will use Python to build the firmware image and pip to install some dependencies. Verify Python is installed by running
```bash
python3 --version
```

You should see an output like the following.
```output
Python 3.12.7
```

Install `pip` and `venv` with the following commands.

```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

check the output to verify `pip` is installed correctly.
```
pip3 --version
```

```output
pip 24.2 from /<path-to>/pip (python 3.12)
```

It is considered good practice to manage `pip` packages through a virtual environment. Create one with the steps below.

```bash
python3 -m venv $HOME/yolo-venv
source $HOME/yolo-venv/bin/activate
```

Your terminal displays `(yolo-venv)` in the prompt indicating the virtual environment is active.

You will need to have the git version control system installed. Run the command below to verify that git is installed on your system.

```bash
git --version
```

You should see output similar to that below.

```output
git version 2.39.3
```

## Install make

Install the make build tool, which is used to build the firmware in the next section.

{{< tabpane code=true >}}
  {{< tab header="Linux" language="shell">}}
sudo apt update
sudo apt install make -y
  {{< /tab >}}
  {{< tab header="MacOS" language="shell">}}
brew install make
  {{< /tab >}}
{{< /tabpane >}}

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
{{% notice Note %}}
To run this learning path on macOS, you need to verify that your installation is for the GNU Make - not the BSD version.
{{% /notice %}}
## Install Arm GNU toolchain

The toolchain is used to compile code from the host to the embedded device architecture.

{{< tabpane code=true >}}
  {{< tab header="Linux" language="shell">}}
cd $HOME
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.2.rel1/binrel/arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
tar -xvf arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
export PATH="$HOME/arm-gnu-toolchain-13.2.Rel1-x86_64-arm-none-eabi/bin/:$PATH"
  {{< /tab >}}
  {{< tab header="MacOS" language="shell">}}
cd $HOME
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-darwin-arm64-arm-none-eabi.tar.xz
tar -xvf arm-gnu-toolchain-13.3.rel1-darwin-arm64-arm-none-eabi.tar.xz
export PATH="$HOME/arm-gnu-toolchain-13.3.rel1-darwin-arm64-arm-none-eabi/bin/:$PATH"
  {{< /tab >}}
{{< /tabpane >}}

{{% notice %}}
You can add the `export` command to the `.bashrc` file. This was, the Arm GNU toolchain is configured from new terminal sessions as well.
{{% /notice %}}


Now that your development environment is set up, move on to the next section where you will generate the firmware image.