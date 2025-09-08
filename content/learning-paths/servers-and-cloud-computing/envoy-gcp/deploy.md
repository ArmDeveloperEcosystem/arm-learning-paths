---
title: How to deploy Envoy on Google Axion C4A Arm virtual machines
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## How to deploy Envoy on a Google Axion C4A Arm virtual machine
In this section you will learn how to install Envoy Proxy v1.30.0 on a Google Cloud Axion C4A virtual machine running RHEL 9. You will install the dependencies, download the official static Arm64 Envoy binary and check the installed version. 

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

You will now download and install the Envoy binary on your Arm-based instance.
Download the binary directly to **/usr/local/bin/envoy**. The `-L` flag is crucial as it follows any redirects from the download URL.

```console
sudo curl -L \
  -o /usr/local/bin/envoy \
  https://github.com/envoyproxy/envoy/releases/download/v1.30.0/envoy-1.30.0-linux-aarch_64
```
Change the permissions on the downloaded binary to make it an executable:

```console
sudo chmod +x /usr/local/bin/envoy
```
Verify the installation by checking its version.

```console
envoy --version
```
This confirms the binary is correctly placed and executable.

The output should look like:

```output
envoy  version: 50ea83e602d5da162df89fd5798301e22f5540cf/1.30.0/Clean/RELEASE/BoringSSL
```
This confirms the installation of Envoy.
You can now proceed with the baseline testing in the next section.
