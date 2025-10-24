---
title: Install Buildkite on a Google Axion C4A Arm VM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get started with installing the Buildkite agent
This section walks you through installing the Buildkite agent on a Google Axion C4A Arm VM, enabling it to connect to your Buildkite account and run the CI/CD pipelines.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt update
sudo apt install unzip -y
  {{< /tab >}}
  {{< tab header="SUSE Linux" language="bash">}}
sudo zypper refresh
sudo zypper install -y curl unzip
  {{< /tab >}}
{{< /tabpane >}}

## Download and install the Buildkite agent

Use this one-line command to download and run the Buildkite installer:

```console
sudo bash -c "$(curl -sL https://raw.githubusercontent.com/buildkite/agent/main/install.sh)" 
```
The installer performs the following steps:

- Downloads the latest version of the agent, for example `v3.109.1`  
- Installs the Buildkite agent into the home directory of the root user at `/root/.buildkite-agent`  
- Creates a default config file (`buildkite-agent.cfg`) where you’ll later add your agent token 

You should see this output:

```output
 
  _           _ _     _ _    _ _                                _
 | |         (_) |   | | |  (_) |                              | |
 | |__  _   _ _| | __| | | ___| |_ ___    __ _  __ _  ___ _ __ | |_
 | '_ \| | | | | |/ _` | |/ / | __/ _ \  / _` |/ _` |/ _ \ '_ \| __|
 | |_) | |_| | | | (_| |   <| | ||  __/ | (_| | (_| |  __/ | | | |_
 |_.__/ \__,_|_|_|\__,_|_|\_\_|\__\___|  \__,_|\__, |\___|_| |_|\__|
                                                __/ |
                                               |___/
Finding latest release...
Installing Version: v3.109.1
Destination: /root/.buildkite-agent
Downloading https://github.com/buildkite/agent/releases/download/v3.109.1/buildkite-agent-linux-arm64-3.109.1.tar.gz

A default buildkite-agent.cfg has been created for you in /root/.buildkite-agent

Don't forget to update the config with your agent token! You can find it token on your "Agents" page in Buildkite

Successfully installed to /root/.buildkite-agent

You can now start the agent!

  /root/.buildkite-agent/bin/buildkite-agent start

For docs, help and support:

  https://buildkite.com/docs/agent/v3

Happy building! <3
```

## Verify installation

Now verify the installation by checking the Buildkite agent version. This confirms that the agent is installed and ready to use:

```console
sudo /root/.buildkite-agent/bin/buildkite-agent --version
```

The expected output is similar to:

```output
buildkite-agent version 3.109.1+10971.5c28e309805a3d748068a3ff7f5c531f51f6f495
```

{{% notice Note %}}
The Buildkite Agent version 3.43.0 introduces Linux/Arm64 Docker image for the Buildkite Agent, making deployment and installation easier for Linux users on Arm. You can view the [Buildkite agent GitHub release note](https://github.com/buildkite/agent/releases/tag/v3.43.0).

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Buildkite Agent version v3.43.0 or later for Arm platforms.
{{% /notice %}}
### Install Docker

Buildkite uses Docker to build and push images.

This step ensures Docker is always available for your CI/CD pipelines.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt update
sudo apt install python-is-python3 python3-pip -y
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
  {{< /tab >}}
  {{< tab header="SUSE Linux" language="bash">}}
sudo zypper install -y git python3 python3-pip docker
sudo usermod -aG docker $USER ; newgrp docker
  {{< /tab >}}
{{< /tabpane >}}

Verify the Docker installation by checking the version and running a test container:

```console
docker run hello-world
```

You will see the Docker message:

```output
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

##  Install Docker Buildx

Docker Buildx is a plugin that allows the building of multi-architecture images, for example `arm64` and `amd64`. 
If you're using SUSE Linux, you need to install Docker Buildx manually. On Ubuntu, Docker Buildx is included by default, so you can skip this step.

## Download Docker Buildx

Download the Docker Buildx binary and move it to the Docker CLI plugin directory. This enables advanced multi-architecture builds on your Arm VM.

```console
wget https://github.com/docker/buildx/releases/download/v0.26.1/buildx-v0.26.1.linux-arm64
chmod +x buildx-v0.26.1.linux-arm64
sudo mkdir -p /usr/libexec/docker/cli-plugins
sudo mv buildx-v0.26.1.linux-arm64 /usr/libexec/docker/cli-plugins/docker-buildx
```

After installing, verify that Docker Buildx is available:

```console
docker buildx version
```

The expected output is similar to:

```output
github.com/docker/buildx v0.26.1
```

If you see the version information, Docker Buildx is installed correctly and ready for use.

{{% notice Note %}}
If you encounter a "permission denied" error, ensure your user is in the `docker` group and that the plugin file is executable.
{{% /notice %}}

You can now use Docker Buildx to build and push multi-architecture images, which is especially useful for Arm-based CI/CD pipelines.

## What you've accomplished

Great job! You’ve installed Docker, Docker Buildx, and the Buildkite agent on your Arm VM. Next, you’ll set up and connect your Buildkite agent to your account.
