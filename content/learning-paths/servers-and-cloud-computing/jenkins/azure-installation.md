---
title: Install Jenkins on Azure Ubuntu Arm64 VM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Install Jenkins on Azure Cobalt 100
This guide explains how to install **Jenkins** on an **Azure Ubuntu 24.04 LTS Arm64 VM**.

At the end of this guide, Jenkins will be:

* Installed and running as a system service
* Accessible on **port 8080**
* Verified on **Arm64 (aarch64)** with **Java 17**

### System Preparation
Updates the OS and installs basic tools required to securely download and manage Jenkins packages.

```console
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget gnupg ca-certificates
```

These tools are required to securely download Jenkins packages.

### Install Java 17 (Required)
Install the supported Java runtime required for running Jenkins LTS reliably.
Jenkins LTS officially supports **Java 17**.

```console
sudo apt install -y openjdk-17-jdk
```

### Verify Java Installation
Confirms that Java 17 is installed correctly and available in the system PATH.

```console
java -version
```

You should see an output similar to:
```output
openjdk version "17.0.17" 2025-10-21
OpenJDK Runtime Environment (build 17.0.17+10-Ubuntu-124.04)
OpenJDK 64-Bit Server VM (build 17.0.17+10-Ubuntu-124.04, mixed mode, sharing)
```

### Add Jenkins Official Repository (Stable LTS)
Add the official Jenkins signing key to ensure package authenticity and security.

```console
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | \
sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
```

This key ensures Jenkins packages are trusted.

### Add Jenkins Stable Repository
Configure the system to download Jenkins LTS packages from the official Jenkins repository.

```console
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/ | \
sudo tee /etc/apt/sources.list.d/jenkins.list
```

### Install Jenkins (Latest Stable LTS)
Install the latest stable Jenkins Long-Term Support release on the Arm64 VM.

```console
sudo apt update
sudo apt install -y jenkins
```

This installs the **latest Jenkins LTS available** at install time.

### Start and Enable Jenkins Service
Starts Jenkins immediately and enables it to launch automatically after system reboot.

```console
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

### Verify Service Status
Confirms that the Jenkins service is running successfully without errors.

```console
sudo systemctl status jenkins
```

You should see an output similar to:
```output
Active: active (running)
```

### Verify Jenkins Version
Validates the installed Jenkins LTS version to ensure correct deployment on Arm64.

```console
jenkins --version
```

You should see an output similar to:
```output
2.528.3
```
This confirm the installed Jenkins LTS version.

This installation confirm Jenkins LTS is successfully deployed on an Azure Ubuntu Arm64 VM.
