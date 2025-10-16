---
title: Install Buildkite
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Buildkite on a Google Axion C4A Arm VM
This section guides you through installing the Buildkite agent on a Google Axion C4A Arm VM, enabling it to connect to your Buildkite account and run CI/CD pipelines.

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

### Download and Install Buildkite Agent

```console
sudo bash -c "$(curl -sL https://raw.githubusercontent.com/buildkite/agent/main/install.sh)" 
```

This one-line command downloads and runs the Buildkite installer.  

The installer performs the following steps:

- Download the latest version of the agent, for example `v3.109.1`  
- Install it into the home directory of the root user at `/root/.buildkite-agent`  
- Create a default config file (`buildkite-agent.cfg`) where you’ll later add your agent token 

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

### Verify installation
This command checks the version of the Buildkite agent and confirms it is installed successfully.

```console
sudo /root/.buildkite-agent/bin/buildkite-agent --version
```
You should see output similar to:

```output
buildkite-agent version 3.109.1+10971.5c28e309805a3d748068a3ff7f5c531f51f6f495
```

{{% notice Note %}}
The Buildkite Agent version 3.43.0 introduces Linux/Arm64 Docker image for the Buildkite Agent, making deployment and installation easier for Linux users on Arm. You can view the [release note](https://github.com/buildkite/agent/releases/tag/v3.43.0).

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Buildkite Agent version v3.43.0 as the minimum recommended on the Arm platforms.
{{% /notice %}}

### Install Docker and Docker Buildx

Buildkite will use Docker to build and push images. 

First, refresh the package repositories and install the required packages including git, Python3-pip, and Docker:

Next, enable and start the Docker service to ensure it runs automatically when your VM starts:

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


SUSE Linux requires some extra steps to start Docker, you can skip this for Ubuntu:

```console
sudo systemctl enable docker
sudo systemctl start docker
```

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

Docker Buildx is a plugin that allows building multi-architecture images, for example `arm64` and `amd64`. 

For SUSE Linux, you need to install Docker Buildx. This is not necessary on Ubuntu.

Download the binary and move it to the Docker CLI plugin directory:

```console
wget https://github.com/docker/buildx/releases/download/v0.26.1/buildx-v0.26.1.linux-arm64
chmod +x buildx-v0.26.1.linux-arm64
sudo mkdir -p /usr/libexec/docker/cli-plugins
sudo mv buildx-v0.26.1.linux-arm64 /usr/libexec/docker/cli-plugins/docker-buildx
```

Now that the Buildkite installation is complete, you can set up the Buildkite agent.
