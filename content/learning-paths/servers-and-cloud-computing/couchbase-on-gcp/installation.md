---
title: Install Couchbase
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Couchbase on GCP VM
This section walks you through how to install and configure Couchbase Server on a GCP Linux VM (SUSE or RHEL-based). 

To ensure a successful setup, follow each step in order and check the output after each command. This helps you catch issues early and confirms that Couchbase is installed and running correctly.

## Set up your environment
Before installing Couchbase, update the system and install the required tools:

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl wget net-tools lsb-release
```
## Download Couchbase server
Download the Couchbase server package for ARM64 architecture.

```console
cd ~
wget -O couchbase-server-8.0.0-linux.aarch64.rpm \
https://packages.couchbase.com/releases/8.0.0/couchbase-server-community-8.0.0-linux.aarch64.rpm
```
After downloading, verify that the file exists and check its size.

```console
ls -lh couchbase-server-8.0.0-linux.aarch64.rpm
```
This helps confirm the file was downloaded correctly and not truncated or corrupted.

## Install Couchbase server

Now that you've downloaded the Couchbase Server RPM, install it using the following command. This step sets up Couchbase and prepares all required directories, binaries, and services:

```console
sudo rpm -ivh couchbase-server-8.0.0-linux.aarch64.rpm
```

The `rpm -ivh` command installs the package, shows verbose output, and displays progress with hash marks. If the installation completes without errors, Couchbase Server is ready for configuration.

Confirm that Couchbase has been installed successfully:

```console
rpm -qa | grep couchbase
```
You should see an output similar to:
```output
couchbase-server-community-8.0.0-3777.aarch64
```
## Start Couchbase service
Start and enable the Couchbase service so that it runs automatically on startup:

```console
sudo systemctl start couchbase-server
sudo systemctl enable couchbase-server
```

## Verify service status:
```console
sudo systemctl status couchbase-server
```

You should see the following snippet as part of your output:
```output
Active: active(running) since YYY XXXX-XX-XX
```

## Check required ports

To confirm Couchbase is ready to accept connections, check that the required ports are open and listening. If you see "LISTEN" next to these ports, Couchbase is running and network services are available.

Couchbase uses these ports for core functions:

- Web console: `8091`
- Data service: `11210`
- Query service: `8093` (for N1QL queries, optional)

Run the following command to verify the ports are active:

```console
sudo ss -tuln | grep -E '8091|11210|8093'
```

The output is similar to:

```output
tcp   LISTEN 0      128          0.0.0.0:8091       0.0.0.0:*
tcp   LISTEN 0      1024         0.0.0.0:11210      0.0.0.0:*
tcp   LISTEN 0      1024            [::]:11210         [::]:*
```

If you see "LISTEN" for these ports, Couchbase is ready for baseline testing and further configuration. This confirms that the core Couchbase services are running and accessible on your Arm-based GCP VM.

```output
tcp   LISTEN 0      128          0.0.0.0:8091       0.0.0.0:*
tcp   LISTEN 0      1024         0.0.0.0:11210      0.0.0.0:*
tcp   LISTEN 0      1024            [::]:11210         [::]:*
```

Once you've finished installing and setting up Couchbase, you're ready to move on to baseline testing. This next phase checks that your Couchbase Server is running correctly and ready for use.
