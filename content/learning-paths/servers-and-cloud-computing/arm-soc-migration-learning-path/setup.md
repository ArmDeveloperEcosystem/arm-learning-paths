---
title: Install Arm SoC Migration Power
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install and configure Kiro's Arm SoC Migration Power

In this section, you will install Kiro IDE, enable Kiro Arm SoC Migration Power, and prepare the development environment.

Kiro runs locally on your development machine. The Migration Power uses the Arm MCP server deployed as a containerized backend (using Docker) to provide Arm-specific guidance. You will also provision an AWS Graviton3 instance to act as the source platform for the migration example.

### Install Kiro IDE

Kiro IDE provides AI-powered development assistance and hosts the Arm SoC Migration Power that will guide you through the migration process.

Download and install Kiro IDE for your platform:

**macOS:**
```bash
brew install --cask kiro
```

**Windows and Linux:**
Visit [https://kiro.dev](https://kiro.dev) to download the installer for your platform.

After installation completes, launch Kiro IDE to proceed.



### Install the Power in Kiro

The Arm SoC Migration Power extends Kiro with specialized knowledge and tools for migrating applications between Arm platforms.

- Open Kiro IDE
- Navigate to the **Powers** panel. Press Cmd + Shift + P (Mac) or Ctrl + Shift + P (Windows)
- Select the Arm SoC Migration Power in the **Recommended** section
- Select **Install**

### Verify installation

After installation, test the Power by entering: "I just installed the arm-soc-migration power and want to use it."

The Power should respond and guide you through any additional setup steps.

It supports migrations across a wide range of Arm-based platforms, including:

- AWS Graviton (Neoverse-based servers)
- Raspberry Pi (Cortex-A)
- NVIDIA Jetson
- NXP i.MX
- Other Linux-based Arm SoCs

### Install prerequisites

The Arm SoC Migration Power uses the Arm MCP (Model Context Protocol) server to provide specialized Arm migration capabilities. The Arm MCP server runs via Docker.

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
Ensure Docker is running before using the Arm SoC Migration Power. The Power will automatically pull and run the Arm MCP server container when needed.
{{% /notice %}}

### Launch AWS Graviton instance (source platform)

You will use an AWS Graviton instance as the source platform in this migration scenario.

{{% notice Note %}}
Before proceeding, ensure you are authenticated with the AWS CLI. Follow the [AWS CLI install guide](/install-guides/aws-cli/) if you haven't configured credentials yet.

Verify your AWS CLI authentication:
```bash
aws sts get-caller-identity
```
If you see an error or need to configure AWS CLI, follow the [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to set up your credentials.
{{% /notice %}}

Create an SSH key and security group, then launch a `c7g.medium` Graviton3 instance. Run each command separately to make it easier to identify any errors.

Create the SSH key:

```bash
aws ec2 create-key-pair --key-name graviton-migration-key \
  --query 'KeyMaterial' --output text > graviton-migration-key.pem
chmod 400 graviton-migration-key.pem
```

Create the security group and allow SSH access:

```bash
SG_ID=$(aws ec2 create-security-group \
  --group-name graviton-migration-sg \
  --description "Security group for Arm SoC migration" \
  --query 'GroupId' --output text)
aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID --protocol tcp --port 22 --cidr 0.0.0.0/0
```

Find the latest Amazon Linux 2023 arm64 AMI and launch the instance:

```bash
AMI_ID=$(aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=al2023-ami-2023*-arm64" "Name=state,Values=available" \
  --query 'reverse(sort_by(Images, &CreationDate))[0].ImageId' \
  --output text)
aws ec2 run-instances \
  --image-id $AMI_ID \
  --instance-type c7g.medium \
  --key-name graviton-migration-key \
  --security-group-ids $SG_ID \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=graviton-migration-source}]' \
  --query 'Instances[0].InstanceId' --output text
```
Wait until the instance state is `running`. Retrieve the SSH command:

```bash
echo "ssh -i graviton-migration-key.pem ec2-user@$(aws ec2 describe-instances --filters "Name=tag:Name,Values=graviton-migration-source" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)"
```

Copy and execute the output command to connect to your instance.

### Install development tools on the Graviton instance

The Graviton instance needs development tools to compile the sensor-monitor example application.

Once connected to your Graviton instance, install the required tools:

```bash
sudo dnf install -y gcc make wget tar
```

## What you've accomplished and what's next

In this section:

- You installed Kiro IDE and the Arm SoC Migration Power
- You launched an AWS Graviton3 instance as your source platform
- You installed the build tools needed for the migration example

In the next section, you'll build and test the sensor-monitor application on the Graviton instance to establish a validated baseline before migration.

