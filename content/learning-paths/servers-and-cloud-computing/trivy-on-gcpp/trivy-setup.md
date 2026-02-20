---
title: Build and scan multi-architecture container images with Trivy
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you'll build a multi-architecture container image and perform vulnerability scanning using Trivy on an Azure Cobalt 100 Arm64 Ubuntu VM.

You will:

- Configure Docker Buildx for multi-architecture builds
- Create a demo container application  
- Push a multi-architecture image to Docker Hub
- Install and verify Trivy on your Arm64 VM
- Perform local vulnerability scanning
- Generate vulnerability reports

## Prerequisites

Before starting, ensure you have:

- An Azure Cobalt 100 Arm64 Ubuntu VM running
- Docker installed and configured on your VM
- A [Docker Hub account](https://hub.docker.com)


To install Docker on your Arm64 VM, follow the [Docker installation guide](/install-guides/docker/).

Once Docker is installed, verify it's running:

```bash
docker --version
uname -m
```

You should see Docker version information and `aarch64` architecture output.

## Install Docker on Arm64 VM

Update your system and install required tools for Docker installation.

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release
```

## Add Docker GPG key

Add Docker’s official signing key so packages are trusted.

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

## Add repository

Register Docker’s package source for Arm64 Ubuntu.

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

## Install Docker

Install Docker Engine and Buildx for multi-architecture builds.

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin
```

## Enable Docker without sudo

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Adds the user to the docker group and applies the new group permissions immediately, enabling non-root access to Docker.

Confirm Docker is running natively on Arm64.

```bash
docker info | grep Architecture
```

You should see a result similar to:

```output
Architecture: aarch64
```

## Configure Docker Buildx for multi-architecture builds

Create builder:

Create a special Docker builder capable of building images for multiple CPU architectures.

```bash
docker buildx create --name multiarch-builder --use
```

## Initialize

Prepare the builder to support multi-platform builds.

```bash
docker buildx inspect --bootstrap
```

The first command creates a builder instance capable of cross-platform builds. The second command initializes it to support multiple platforms.

## Create a demo application

Set up a workspace for your demo container:

```bash
mkdir $HOME/trivy-multiarch-demo
cd $HOME/trivy-multiarch-demo
```

Create a `Dockerfile`:

```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
```

Create an `index.html` file:

```html
<h1>Multi-Architecture NGINX on Azure Cobalt Arm64</h1>
```

## Authenticate with Docker Hub

Run the Docker login command to authenticate:

```bash
docker login
```

Docker displays a one-time device code and a login URL:

```text
https://login.docker.com/activate
```

Steps to complete login:

- Open the displayed URL in your web browser
- Enter the one-time confirmation code shown in the terminal
- Click Confirm / Activate

Once authentication completes, the terminal will show:

```output
WARNING! Your credentials are stored unencrypted in '/home/azureuser/.docker/config.json'.
Configure a credential helper to remove this warning. See
https://docs.docker.com/go/credential-store/

Login Succeeded
```

This confirms your system is now authenticated with Docker Hub and ready to push or pull container images.

Next, run the docker login again:

```bash
docker login
```

Note the "Username" that is presented and save it, as you'll use it in the next step (as DOCKER_USERNAME below).

Finally, create a personal access token in Docker Hub. Log into [Docker Hub](https://hub.docker.com) with your Docker username and password, then select "Account Settings" -> "Personal Access Token" to create a token. Select "Read-Only" privileges and copy and save the token, as it will become your "DOCKER_PASSWORD" in future steps.

## Build and push multi-architecture images

Build your image for both amd64 and arm64 architectures. Replace `<DOCKER_USERNAME>` with your Docker username:

```bash
cd $HOME/trivy-multiarch-demo
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t <DOCKER_USERNAME>/trivy-multiarch-nginx:latest \
  --push .
```

This command builds the container for both architectures and pushes the multi-architecture image directly to Docker Hub. The same image specification can now run on both x86 and Arm systems.

## Install and verify Trivy

Download the Arm64-compatible Trivy scanner:

```bash
cd $HOME
wget https://github.com/aquasecurity/trivy/releases/download/v0.68.1/trivy_0.68.1_Linux-ARM64.deb
```

{{% notice Note %}}
The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Trivy 0.29.0 or later for Arm platforms.
{{% /notice %}}

Install Trivy on your system:

```bash
sudo dpkg -i trivy_0.68.1_Linux-ARM64.deb
```

Verify the installation:

```bash
trivy version
```

You should see version information displayed.

## Perform local vulnerability scanning

Scan your Docker Hub image (replace `<DOCKER_USERNAME>` with your username):

```bash
trivy image <DOCKER_USERNAME>/trivy-multiarch-nginx:latest
```

Trivy analyzes the container layers and reports all detected vulnerabilities with severity levels (LOW, MEDIUM, HIGH, CRITICAL).

## Generate a JSON vulnerability report

Create a machine-readable report for audits and CI pipelines:

```bash
trivy image \
  --format json \
  -o trivy-report.json \
  <DOCKER_USERNAME>/trivy-multiarch-nginx:latest
```

Create a machine-readable vulnerability report for audits and CI pipelines.

```output
2026-01-23T06:42:30Z    INFO    [vuln] Vulnerability scanning is enabled
2026-01-23T06:42:30Z    INFO    [secret] Secret scanning is enabled
2026-01-23T06:42:30Z    INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-01-23T06:42:30Z    INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2026-01-23T06:42:32Z    INFO    Detected OS     family="debian" version="12.5"
2026-01-23T06:42:32Z    INFO    [debian] Detecting vulnerabilities...   os_version="12" pkg_num=149
2026-01-23T06:42:33Z    INFO    Number of language-specific files       num=0
2026-01-23T06:42:33Z    WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.
```

## What you've accomplished and what's next

In this section, you:

- Built and pushed a multi-architecture container image to Docker Hub
- Installed Trivy on your Arm64 VM
- Scanned your container image for vulnerabilities
- Generated a JSON vulnerability report for analysis

You now have a working local security scanning setup. Next, you'll integrate Trivy into a GitHub Actions CI/CD pipeline to automate security scanning on every code push.

