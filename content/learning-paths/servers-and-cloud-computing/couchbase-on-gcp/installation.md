---
title: Install Couchbase
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Couchbase on GCP VM
This section explains how to install and configure **Couchbase Server** on a GCP Linux VM (SUSE or RHEL-based). 
Follow the steps below carefully to ensure a successful setup.

### System Preparation
Before installing Couchbase, update the system and install the required tools.

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl wget net-tools lsb-release
```
### Download Couchbase Server
Download the Couchbase Server package for ARM64 architecture.

```console
cd ~
wget -O couchbase-server-8.0.0-linux.aarch64.rpm \
https://packages.couchbase.com/releases/8.0.0/couchbase-server-community-8.0.0-linux.aarch64.rpm
```
**Verify the downloaded file:**
After downloading, verify that the file exists and check its size.

```console
ls -lh couchbase-server-8.0.0-linux.aarch64.rpm
```
This helps confirm the file was downloaded correctly and not truncated or corrupted.

### Install Couchbase Server
Install the downloaded Couchbase RPM package.

```console
sudo rpm -ivh couchbase-server-8.0.0-linux.aarch64.rpm
```
- **rpm -ivh** → Installs the RPM package, displaying verbose output and progress (v for verbose, h for hash marks).
- This command installs Couchbase and sets up the necessary directories, binaries, and services.

**Confirm that Couchbase has been installed successfully:**

```console
rpm -qa | grep couchbase
```
You should see an output similar to:
```output
couchbase-server-community-8.0.0-3777.aarch64
```
### Start Couchbase Service
Start and enable the Couchbase service so that it runs automatically on startup.

```console
sudo systemctl start couchbase-server
sudo systemctl enable couchbase-server
```

**Verify service status:**
```console
sudo systemctl status couchbase-server
```

You should see the following snippet as part of your output:
```output
Active: active(running) since YYY XXXX-XX-XX
```

### Check Required Ports
This command checks if those ports are open and active. If you see “LISTEN” next to these ports, it means Couchbase is ready to accept connections.

Couchbase uses the following ports for basic operation:

- Web Console: `8091`  
- Query Service: `8093` (optional for N1QL queries)  
- Data Service: `11210`  

Check if the ports are listening:

```console
sudo ss -tuln | grep -E '8091|11210'
```

```output
tcp   LISTEN 0      128          0.0.0.0:8091       0.0.0.0:*
tcp   LISTEN 0      1024         0.0.0.0:11210      0.0.0.0:*
tcp   LISTEN 0      1024            [::]:11210         [::]:*
```

Once the **installation and setup are complete**, you can now proceed to the **baseline testing** phase.
