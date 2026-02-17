---
title: Build and scan multi-architecture container images with Trivy
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this module, you will build a multi-architecture container image and perform vulnerability scanning using Trivy on an Azure Cobalt 100 Arm64 Ubuntu VM.

You will:

- Install Docker on Arm64
- Build and push multi-arch container images
- Install Trivy on Arm64
- Scan container images locally
- Generate vulnerability reports

## Prerequisites

Ensure:

- Azure Cobalt 100 Arm64 Ubuntu VM
- [Docker Hub account](https://hub.docker.com) (create one if you don't have it)
- [GitHub account](https://github.com) (create one if you don't have it)
- Internet connectivity

Verify architecture:

```bash
uname -m
```

## Install Docker on Arm64 VM

Update your system and install required tools for Docker installation.

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release
```

**Add Docker GPG key:**

Adds Docker’s official signing key so packages are trusted.

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

**Add repository:**

Register Docker’s package source for Arm64 Ubuntu.

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**Install Docker:**

Install Docker Engine and Buildx for multi-architecture builds.

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin
```

**Enable Docker without sudo:**

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Adds the user to the docker group and applies the new group permissions immediately, enabling non-root access to Docker.

**Verify:**

Confirm Docker is running natively on Arm64.

```bash
docker info | grep Architecture
```

You should see a result similar to:

```output
Architecture: aarch64
```

## Configure Docker Buildx for Multi-Architecture Builds

**Create builder:**

Create a special Docker builder capable of building images for multiple CPU architectures.

```bash
docker buildx create --name multiarch-builder --use
```

**Initialize:**

Prepare the builder to support multi-platform builds.

```bash
docker buildx inspect --bootstrap
```

## Create Demo Application

Creates a workspace for the demo container application.

```bash
mkdir $HOME/trivy-multiarch-demo
cd $HOME/trivy-multiarch-demo
```

## Create Dockerfile

Create a file called **Dockerfile** with the following content:

```bash
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
```

## Create HTML file

Create a HTML file named **index.html** with the following content:

```bash
<h1>Multi-Architecture NGINX on Azure Cobalt Arm64</h1>
```

## Login to Docker Hub

**Run the login command:**

```bash
docker login
```

Docker displays a one-time device code and a login URL:

```text
https://login.docker.com/activate
```

**Steps to complete login:**

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

## Build and Push Multi-Architecture Image

Build and push your multi-architecture image replacing <DOCKER_USERNAME> with your username you saved from the last step:

```bash
cd $HOME/trivy-multiarch-demo
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t <DOCKER_USERNAME>/trivy-multiarch-nginx:latest \
  --push .
```

- Builds the container for both amd64 and arm64
- Pushes the multi-arch image to Docker Hub

This allows the same image to run on different CPU architectures.

In a browser, go to [Docker Hub](https://hub.docker.com). Press "login" and supply your Docker username and password. Select "Repositories" -> "trivy-multiarch-nginx". You should see your container image details there:

![Trivy scanning multi-architecture container image#center](images/trivy-multiarch.png "Trivy Multi-Arch Image Scan")

## Install Trivy on Arm64

**Download:**

Download the Arm64-compatible Trivy scanner.

```bash
cd $HOME
wget https://github.com/aquasecurity/trivy/releases/download/v0.68.1/trivy_0.68.1_Linux-ARM64.deb
```

{{% notice Note %}}
The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Trivy 0.29.0 or later for Arm platforms.
{{% /notice %}}

**Install:**

Install Trivy on your system.

```bash
sudo dpkg -i trivy_0.68.1_Linux-ARM64.deb
```

**Verify:**

```bash
trivy version
```

The following output should resemble:

```output
Version: 0.68.1
```

## Scan Image Locally

Run a scan with trivy replacing <DOCKER_USERNAME> with the username you saved previously:

```bash
trivy image <DOCKER_USERNAME>/trivy-multiarch-nginx:latest
```

Trivy analyzes the container image and lists security vulnerabilities.

## Generate JSON report

Generate a JSON report using trivy for your scan:

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

## Outcome

You have:

- Installed Docker on Arm64
- Built multi-architecture container images
- Pushed images to Docker Hub
- Installed Trivy on Azure Cobalt 100
- Scanned images for vulnerabilities
- Generated security reports

## What you've accomplished and what's next

You've successfully:

- Set up Docker on your Azure Cobalt 100 Arm64 virtual machine
- Created and pushed a multi-architecture container image that runs on both amd64 and arm64
- Installed Trivy and performed local vulnerability scanning
- Generated JSON reports for security analysis

Next, you'll integrate Trivy into a CI/CD pipeline using self-hosted GitHub Actions runners to automate security scanning.
