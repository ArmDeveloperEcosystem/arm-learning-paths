---
title: Install Django
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Django on GCP VM
This guide walks you through installing Django on a **Google Cloud Platform (GCP) SUSE Linux Arm64 VM**, including all dependencies, Python setup, and environment preparation.

### Update Your System
Before installing Django, it’s good practice to update your package list and upgrade installed software to ensure you have the latest versions and security patches.

```console
sudo zypper refresh
sudo zypper update -y
```

### Install Python and Tools
**Django** requires **Python 3.10+**. We will use Python 3.11, which is compatible with Django 5.
You will also install `pip` for package management, and basic developer tools (`git`, `gcc`, and `make`) to build Python packages and work with Django projects.
```console
sudo zypper install -y python311 python311-pip python311-devel 
sudo zypper install -y git gcc make
```

**Use Python 3.11 as the Default (optional):**

If multiple Python versions exist on your system, you can set Python 3.11 as your default Python 3 interpreter using **update-alternatives**.

```console
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
sudo update-alternatives --config python3
```

**Ensure that both Python and pip are installed correctly:**

```console
python3 --version
pip3 --version
```

You should see an output similar to:
```output
Python 3.11.13
pip 22.3.1 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

### Create a Project Folder and Virtual Environment
It’s recommended to create a dedicated project directory and use a **virtual environment** to isolate project dependencies.

```console
mkdir ~/myproject && cd ~/myproject
python3 -m venv venv
source venv/bin/activate
```
- `python3 -m venv venv` — creates a virtual environment named venv inside your project folder.
- `source venv/bin/activate` — activates the virtual environment.
Once activated, your command prompt will show (venv) at the beginning, indicating that you’re working inside an isolated Python environment.

### Upgrade Pip and Install Django
With your virtual environment active, upgrade pip and install Django using the following commands:

```console
pip3 install --upgrade pip
pip3 install django
```

**Confirm that Django is installed correctly by checking its version:**

```console
django-admin --version
```

You should see an output similar to:
```output
5.2.7
```
Django is installed successfully and ready for project setup.
