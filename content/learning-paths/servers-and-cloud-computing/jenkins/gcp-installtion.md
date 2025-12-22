---
title: Install Jenkins GCP SUSE Arm64 VM
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Jenkins on GCP SUSE Arm64
This section covers the installation of **Jenkins (Stable LTS)** on a **GCP SUSE Linux Enterprise Server (SLES) Arm64 VM**. The goal is to prepare a clean, Arm-native Jenkins environment that will be used later for CI/CD use cases.

### System Preparation
Update the system and install required utilities.

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl wget ca-certificates gnupg
```

### Install Java 17 (Required)
Jenkins LTS officially requires Java 17.

```console
sudo zypper install -y java-17-openjdk java-17-openjdk-devel
```

Verify Java installation:

```console
java -version
```

You should see an output similar to:
```text
openjdk version "17.0.13" 2024-10-15
OpenJDK Runtime Environment (build 17.0.13+11-suse-150400.3.48.2-aarch64)
OpenJDK 64-Bit Server VM (build 17.0.13+11-suse-150400.3.48.2-aarch64, mixed mode, sharing)
```

### Add Jenkins Official Repository (Stable LTS)
Import the Jenkins repository signing key:

```console
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
```

Add the Jenkins stable repository:

```console
sudo zypper addrepo https://pkg.jenkins.io/redhat-stable/ jenkins
sudo zypper refresh
```

### Install Jenkins (Latest Stable LTS)

```console
sudo zypper install -y jenkins
```

This installs the **latest Jenkins LTS** available at install time.

### Start and Enable Jenkins Service
Enable Jenkins to start automatically on boot and start the service.

```console
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

Verify service status:

```console
sudo systemctl status jenkins
```

You should see an output similar to:
```output
● jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/usr/lib/systemd/system/jenkins.service; enabled; vendor preset: disabled)
     Active: active (running) since Wed 2025-12-17 08:08:22 UTC; 1h 56min ago
```

### Verify Jenkins Version

```console
jenkins --version
```

You should see an output similar to:
```output
2.528.3
```

This section completes the installation of Jenkins LTS on a GCP SUSE Arm64 VM using Java 17. Jenkins service health, version validation, network accessibility, and initial UI setup are verified. The system is now ready for Arm-native CI/CD use cases.
