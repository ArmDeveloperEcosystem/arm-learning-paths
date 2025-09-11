---
title: Deploy Envoy on Google Axion C4A Arm virtual machines
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Install Envoy Proxy v1.30.0 on a Google Axion C4A Arm VM
In this section you'll install Envoy Proxy v1.30.0 on a Google Cloud Axion C4A virtual machine running RHEL 9. You'll install the dependencies, download the official static Arm64 Envoy binary, and verify the installation. 

## Install Dependencies

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

## Install Envoy (static Arm64 binary)

Download the Envoy binary. `-L` follows redirects:

```console
sudo curl -L \
  -o /usr/local/bin/envoy \
  https://github.com/envoyproxy/envoy/releases/download/v1.30.0/envoy-1.30.0-linux-aarch_64
```
Change the permissions on the downloaded binary to make it an executable:

```console
sudo chmod +x /usr/local/bin/envoy
```
Verify the installation by checking its version:

```console
envoy --version
```
This confirms the binary is correctly placed and executable.

Expected output:

```output
envoy  version: 50ea83e602d5da162df89fd5798301e22f5540cf/1.30.0/Clean/RELEASE/BoringSSL
```
Envoy is now installed. Continue to baseline testing in the next section.
