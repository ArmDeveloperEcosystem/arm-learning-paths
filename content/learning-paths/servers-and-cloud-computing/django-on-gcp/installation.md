---
title: Install Django on your Arm-based VM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Django and dependencies

After connecting to your SUSE Linux Enterprise Server (SLES) VM using SSH, you'll install the Google Cloud CLI, update your system, install Python 3.11, and set up a virtual environment for your Django project.

## Prepare the system

Update the system packages and install dependencies:

```bash
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl git tar gzip
```

### Install Python 3.11

Install Python 3.11:

```bash
sudo zypper install -y python311
which python3.11
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

## Install Google Cloud CLI (gcloud)

The Google Cloud CLI is required to authenticate with GCP and allow your Django application VM to interact with Google Cloud services such as GKE, Cloud SQL, Artifact Registry, Memorystore, and to build, deploy, and operate the Django platform.

### Install Google Cloud SDK (gcloud)

The Google Cloud SDK is required to create and manage GKE clusters.

Download and extract the Google Cloud SDK:

```bash
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-460.0.0-linux-arm.tar.gz
tar -xvf google-cloud-sdk-460.0.0-linux-arm.tar.gz
```

Install gcloud:

```bash
./google-cloud-sdk/install.sh
```

After installation completes, exit and reconnect to apply the PATH changes:

```bash
exit
```

### Initialize gcloud

Authenticate and configure the Google Cloud CLI:

```bash
gcloud init
```

During initialization, select **Login with a new account**. You'll be prompted to authenticate using your browser and receive an auth code to copy back. Select the project you want to use and choose default settings when unsure.

### Verify authentication

```bash
gcloud auth list
```

The output is similar to:
```output
Credentialed Accounts
ACTIVE  ACCOUNT
*       <PROJECT_NUMBER>-compute@developer.gserviceaccount.com
```

## Create a project directory and virtual environment

Create a dedicated directory for your Django project and set up a Python virtual environment to isolate your project's dependencies:

```bash
mkdir ~/myproject && cd ~/myproject
python3.11 -m venv venv
source venv/bin/activate
```

The `python3.11 -m venv venv` command creates an isolated Python environment named `venv` inside your project folder. Running `source venv/bin/activate` activates this environment.

Once activated, your command prompt displays `(venv)` at the beginning, indicating you're working inside an isolated Python environment where all packages are isolated from your system Python installation.

## Upgrade pip and install Django

With your virtual environment active, upgrade pip to the latest version:

```bash
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
5.2.10
```

## Summary and what's next

You have successfully installed the Google Cloud CLI, Python 3.11, Django, and Gunicorn on your Arm-based VM. Your environment is now fully prepared to build, containerize, and deploy a Django REST API on GKE with Cloud SQL and Memorystore.
