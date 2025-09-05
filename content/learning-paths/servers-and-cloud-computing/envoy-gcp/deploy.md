---
title: How to deploy Envoy on Google Axion C4A Arm virtual machines
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## How to deploy Envoy on a Google Axion C4A Arm virtual machine
This guide shows you how to install Envoy Proxy v1.30.0 on a Google Cloud Axion C4A virtual machine running RHEL 9. You’ll install the basic tools, download the official static Arm64 Envoy binary, give it executable permissions, and check the version. By the end, Envoy will be installed and ready to use on your GCP virtual machine — without needing Docker or building from source.

1. Install Dependencies

```console
sudo dnf install -y \
  autoconf \
  curl \
  libtool \
  patch \
  python3 \
  python3-pip \
  unzip \
  git
pip3 install virtualenv
```

2. Install Envoy (Static Arm64 Binary)

This step downloads and installs the Envoy binary.
Download the binary directly to **/usr/local/bin/envoy**. The `-L` flag is crucial as it follows any redirects from the download URL.

```console
sudo curl -L \
  -o /usr/local/bin/envoy \
  https://github.com/envoyproxy/envoy/releases/download/v1.30.0/envoy-1.30.0-linux-aarch_64
```
Make it executable so the system can run the binary as a command.

```console
sudo chmod +x /usr/local/bin/envoy
```
Verify the installation by checking its version.

```console
envoy --version
```
This confirms the binary is correctly placed and executable.

You should see an output similar to:

```output
envoy  version: 50ea83e602d5da162df89fd5798301e22f5540cf/1.30.0/Clean/RELEASE/BoringSSL
```
This confirms the binary is correctly placed and executable.

Envoy installation is complete. You can now proceed with the baseline testing ahead.
