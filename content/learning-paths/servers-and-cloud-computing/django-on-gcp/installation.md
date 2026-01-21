---
title: Install Django on your Arm-based VM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Django and dependencies

After connecting to your SUSE Linux Enterprise Server (SLES) VM using SSH, you'll install the Google Cloud CLI, update your system, install Python 3.11, and set up a virtual environment for your Django project.

## Install Google Cloud CLI (gcloud)

The Google Cloud CLI is required to authenticate with GCP and allow your Django application VM to interact with Google Cloud services such as GKE, Cloud SQL, Artifact Registry, Memorystore, and to build, deploy, and operate the Django platform.

### Download gcloud SDK (Arm64)

```console
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-arm.tar.gz
```

### Extract and install gcloud

```console
tar -xzf google-cloud-cli-linux-arm.tar.gz
cd google-cloud-sdk
./install.sh
```

Accept the default options during installation.

### Initialize gcloud

```console
source ~/.bashrc
gcloud init
```

During initialization:

- Select the correct project (for example: imperial-time-xxxxxx)
- Choose the default region (for example: us-central1)

### Verify authentication

```console
gcloud auth list
```

You should see an output similar to:
```output
Credentialed Accounts
ACTIVE  ACCOUNT
*       <PROJECT_NUMBER>-compute@developer.gserviceaccount.com
```

## Update your system

Begin by refreshing your package list and upgrading installed software to ensure you have the latest versions and security patches:

```console
sudo zypper refresh
sudo zypper update -y
```

## Install Python 3.11 and development tools

Django requires Python 3.10 or later. You'll install Python 3.11 along with pip (Python's package manager) and essential build tools needed for compiling Python packages:

```console
sudo zypper install -y python311 python311-pip python311-devel git gcc make
```

Verify that Python and pip are installed correctly:

```bash
python3.11 --version
pip3.11 --version
```

The output is similar to:

```output
Python 3.11.10
pip 22.3.1 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

## Create a project directory and virtual environment

Create a dedicated directory for your Django project and set up a Python virtual environment to isolate your project's dependencies:

```console
mkdir ~/myproject && cd ~/myproject
python3.11 -m venv venv
source venv/bin/activate
```

The `python3.11 -m venv venv` command creates an isolated Python environment named `venv` inside your project folder. Running `source venv/bin/activate` activates this environment.

Once activated, your command prompt displays `(venv)` at the beginning, indicating you're working inside an isolated Python environment where all packages are isolated from your system Python installation.

## Upgrade pip and install Django

With your virtual environment active, upgrade pip to the latest version:

```console
python3 -m pip install --upgrade pip
```

Now install Django and additional useful packages for web development:

```bash
python3 -m pip install django gunicorn
```

This installs:
- **Django** — the web framework for building your application
- **Gunicorn** — a production-ready WSGI (Web Server Gateway Interface) server for running Django applications

Verify that Django is installed correctly:

```bash
django-admin --version
```

The output is similar to:

```output
5.2.8
```

## Summary and what's next

You have successfully installed the Google Cloud CLI, Python 3.11, Django, and Gunicorn on your Arm-based VM. Your environment is now fully prepared to build, containerize, and deploy a Django REST API on GKE with Cloud SQL and Memorystore.
