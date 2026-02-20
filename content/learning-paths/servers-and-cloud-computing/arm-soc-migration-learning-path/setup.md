---
title: Install ARM SoC Migration Power
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install and configure Kiro's ARM SoC Migration Power

In this section, you will install Kiro IDE, enable the Kiro ARM SoC Migration Power, and prepare the required development environment.

Kiro runs locally on your development machine. The Migration Power uses the Arm MCP server deployed as a containerized backend (via Docker) to provide Arm-specific guidance. You will also provision an AWS Graviton3 instance to act as the source platform for the migration example.

### Install Kiro IDE

Kiro IDE provides AI-powered development assistance and hosts the ARM SoC Migration Power that will guide you through the migration process.

Download and install Kiro IDE for your platform:

**macOS:**
```bash
brew install --cask kiro
```

**Windows and Linux:**
Download the installer from [https://kiro.dev](https://kiro.dev)

Launch Kiro IDE after installation completes.

### Install the Power in Kiro

The ARM SoC Migration Power extends Kiro with specialized knowledge and tools for migrating applications between Arm platforms.

1. Open Kiro IDE
2. Navigate to Powers panel. Press Cmd + Shift + P (Mac) or Ctrl + Shift + P (Windows)
3. Click on the ARM SoC Migration Power in the Recommended section
4. Click Install

### Verify Installation
After installation, test the Power by entering: "I just installed the arm-soc-migration power and want to use it."

The Power should respond and guide you through any additional setup steps.

It supports migrations across a wide range of Arm-based platforms, including:
  * AWS Graviton (Neoverse-based servers)
  * Raspberry Pi (Cortex-A)
  * NVIDIA Jetson
  * NXP i.MX
  * Other Linux-based Arm SoCs
### Install Prerequisites

The ARM SoC Migration Power uses the Arm MCP (Model Context Protocol) server to provide specialized Arm migration capabilities. The Arm MCP server runs via Docker.

Install Docker on your local development machine (required for ARM MCP server):

**macOS:**
```bash
brew install --cask docker
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y docker.io

# Or use Docker's official installation script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

**Windows:**
Download Docker Desktop from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

Verify installation:
```bash
docker --version
```

{{% notice Note %}}
Ensure Docker is running before using the ARM SoC Migration Power. The power will automatically pull and run the ARM MCP server container when needed.
{{% /notice %}}

### Launch AWS Graviton Instance (Source Platform)

You will use an AWS Graviton instance as the source platform in this migration scenario.

{{% notice Note %}}
Before proceeding, ensure you are authenticated with AWS CLI. You must have valid AWS credentials configured to create and manage EC2 instances.

Verify your AWS CLI authentication:
```bash
aws sts get-caller-identity
```
If you see an error or need to configure AWS CLI, follow the [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to set up your credentials.
{{% /notice %}}

Create an SSH key, security group, and launch a `c7g.medium` Graviton3 instance:

```bash
aws ec2 create-key-pair --key-name graviton-migration-key --query 'KeyMaterial' --output text > graviton-migration-key.pem && chmod 400 graviton-migration-key.pem && SG_ID=$(aws ec2 create-security-group --group-name graviton-migration-sg --description "Security group for ARM SoC migration" --query 'GroupId' --output text) && aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 0.0.0.0/0 && aws ec2 run-instances --image-id $(aws ec2 describe-images --owners amazon --filters "Name=name,Values=al2023-ami-2023*-arm64" "Name=state,Values=available" --query 'reverse(sort_by(Images, &CreationDate))[0].ImageId' --output text) --instance-type c7g.medium --key-name graviton-migration-key --security-group-ids $SG_ID --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=graviton-migration-source}]' --query 'Instances[0].InstanceId' --output text
```
Wait approximately 30 seconds for the instance to enter the running state. Retrieve the SSH command:

```bash
echo "ssh -i graviton-migration-key.pem ec2-user@$(aws ec2 describe-instances --filters "Name=tag:Name,Values=graviton-migration-source" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)"
```

Copy and execute the output command to connect to your instance.

### Install Development Tools on Graviton Instance

The Graviton instance needs some development tools (gcc, make) to compile the sensor-monitor example application. You will also install wget and tar for downloading and extracting files.

Once connected to your Graviton instance, install the required tools:

```bash
sudo dnf install -y gcc make wget tar
```

## Expected Outcome

After completing this section, you should have:
- Kiro IDE installed locally
- ARM SoC Migration Power installed and verified
- AWS Graviton c7g.medium instance running Amazon Linux 2023 (arm64)
- Build tools installed on the source platform
- SSH key saved locally for secure access

You are now ready to build and test the application on the source platform before migrating it to the target edge device (Raspberry Pi 5).

