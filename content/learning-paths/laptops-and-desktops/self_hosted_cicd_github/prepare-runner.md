---
# User change
title: "Prepare the runner"

weight: 6

layout: "learningpathall"
---

## Prepare the Runner
When using self-hosted runners, you are responsible for patching the operating system and installing all the software required to build the application. In this learning path, you use the .NET SDK and Docker. Therefore, you need to install these components.

For Ubuntu 22.04, the Docker installation process is as follows:

1. Open the Terminal and type the following commands:
```console
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
2. Create the docker group and add your user to it:
```console 
sudo groupadd docker
sudo usermod -aG docker $USER
```
3. Restart the machine, then verify that Docker is working by running the following command in the Terminal:
```console
docker run hello-world
```

To install the .NET SDK:
1. Open the terminal and enter: 
```console
wget https://dot.net/v1/dotnet-install.sh -O dotnet-install.sh
chmod +x ./dotnet-install.sh
./dotnet-install.sh --version latest
```
2. This will generate output similar to the following:
```output
dotnet-install: Attempting to download using aka.ms link https://dotnetcli.azureedge.net/dotnet/Sdk/8.0.203/dotnet-sdk-8.0.203-linux-arm64.tar.gz
dotnet-install: Remote file https://dotnetcli.azureedge.net/dotnet/Sdk/8.0.203/dotnet-sdk-8.0.203-linux-arm64.tar.gz size is 221512731 bytes.
dotnet-install: Extracting zip from https://dotnetcli.azureedge.net/dotnet/Sdk/8.0.203/dotnet-sdk-8.0.203-linux-arm64.tar.gz
dotnet-install: Downloaded file size is 221512731 bytes.
dotnet-install: The remote and local file sizes are equal.
dotnet-install: Installed version is 8.0.203
dotnet-install: Adding to current process PATH: `/home/parallels/.dotnet`. Note: This change will be visible only when sourcing script.
dotnet-install: Note that the script does not resolve dependencies during installation.
dotnet-install: To check the list of dependencies, go to https://learn.microsoft.com/dotnet/core/install, select your operating system and check the "Dependencies" section.
dotnet-install: Installation finished successfully.
```
3. Configure the environment variables for the .NET SDK to ensure the dotnet command is in your PATH:
Configure environment variables:
```console
echo 'export DOTNET_ROOT=$HOME/.dotnet' >> ~/.profile
echo 'export PATH=$PATH:$DOTNET_ROOT:$DOTNET_ROOT/tools' >> ~/.profile
source ~/.profile
```

The VM is ready, and you can associate it with GitHub.
