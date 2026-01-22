---
title: Install Jenkins on Azure Ubuntu Arm64 virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Jenkins on Azure Ubuntu Arm64

To install Jenkins on an Azure Ubuntu 24.04 LTS Arm64 virtual machine, follow these steps.

At the end of the installation, Jenkins is:

* Installed and running as a system service
* Accessible on port 8080
* Verified on Arm64 (aarch64) with Java 17

## Update the system and install basic tools

Update the OS and install basic tools to securely download and manage Jenkins packages.

```console
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget gnupg ca-certificates
```

## Install Java 17

Jenkins LTS officially supports Java 17. Install the Java runtime:

```console
sudo apt install -y openjdk-17-jdk
```

Verify Java installation:

```console
java -version
```

The output is similar to:
```output
openjdk version "17.0.17" 2025-10-21
OpenJDK Runtime Environment (build 17.0.17+10-Ubuntu-124.04)
OpenJDK 64-Bit Server VM (build 17.0.17+10-Ubuntu-124.04, mixed mode, sharing)
```

## Add the Jenkins repository

Add the official Jenkins signing key to ensure package authenticity:

```console
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | \
sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
```

Add the Jenkins stable repository:

```console
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/ | \
sudo tee /etc/apt/sources.list.d/jenkins.list
```

## Install Jenkins

Install the latest stable Jenkins LTS release:

```console
sudo apt update
sudo apt install -y jenkins
```

## Start and enable the Jenkins service

Start Jenkins immediately and enable it to launch automatically after system reboot:

```console
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

Verify the service is running:

```console
sudo systemctl status jenkins
```

The output is similar to:
```output
Active: active (running)
```

## Verify the Jenkins version

Check the installed Jenkins version:

```console
jenkins --version
```

The output is similar to:
```output
2.528.3
```

## What you've accomplished and what's next

You've successfully installed Jenkins LTS on your Azure Ubuntu Arm64 virtual machine. Your installation includes:

- Jenkins service running and enabled for automatic startup
- Java 17 runtime properly configured
- Jenkins accessible on port 8080
- Arm64-native deployment ready for CI/CD workloads

Next, you'll configure firewall rules to allow external access to Jenkins.
