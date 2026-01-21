---
title: Install Jenkins on GCP SUSE Arm64 virtual machine
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To install Jenkins (Stable LTS) on a GCP SUSE Linux Enterprise Server (SLES) Arm64 virtual machine, follow these steps.

## Update the system and install utilities

Update the system and install required utilities:

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl wget ca-certificates gnupg
```

## Install Java 17

Jenkins LTS officially requires Java 17. Install Java:

```console
sudo zypper install -y java-17-openjdk java-17-openjdk-devel
```

Verify Java installation:

```console
java -version
```

The output is similar to:
```text
openjdk version "17.0.13" 2024-10-15
OpenJDK Runtime Environment (build 17.0.13+11-suse-150400.3.48.2-aarch64)
OpenJDK 64-Bit Server VM (build 17.0.13+11-suse-150400.3.48.2-aarch64, mixed mode, sharing)
```

## Add the Jenkins repository

Import the Jenkins repository signing key:

```console
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
```

Add the Jenkins stable repository:

```console
sudo zypper addrepo https://pkg.jenkins.io/redhat-stable/ jenkins
sudo zypper refresh
```

## Install Jenkins

Install the latest stable Jenkins LTS release:

```console
sudo zypper install -y jenkins
```

## Start and enable the Jenkins service

Enable Jenkins to start automatically on boot and start the service:

```console
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

Verify service status:

```console
sudo systemctl status jenkins
```

The output is similar to:
```output
● jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/usr/lib/systemd/system/jenkins.service; enabled; vendor preset: disabled)
     Active: active (running) since Wed 2025-12-17 08:08:22 UTC; 1h 56min ago
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

Jenkins LTS is now successfully installed on your GCP SUSE Arm64 virtual machine.
