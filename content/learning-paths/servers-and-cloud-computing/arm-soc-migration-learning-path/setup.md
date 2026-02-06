---
title: Install ARM SoC Migration Power
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install and configure Kiro's ARM SoC Migration Power

This section guides you through installing Kiro IDE, the ARM SoC Migration Power, and setting up the required development tools. These steps apply to any ARM SoC migration project.

### Install Kiro IDE

Kiro IDE provides AI-powered development assistance and hosts the ARM SoC Migration Power that will guide you through the migration process.

Download and install Kiro IDE for your platform:

**macOS:**
```bash
brew install --cask kiro
```

**Windows and Linux:**
Download from [https://kiro.dev](https://kiro.dev)

Launch Kiro IDE after installation.

### Install the Power in Kiro

The ARM SoC Migration Power extends Kiro with specialized knowledge and tools for migrating applications between ARM platforms.

1. Open Kiro IDE
2. Navigate to Powers panel. Press Cmd + Shift + P (Mac) or Ctrl + Shift + P (Windows)
3. Click on the ARM SoC Migration Power in the Reocommended section
4. Click Install

### Verify Installation

Test the power by saying: "I just installed the arm-soc-migration power and want to use it."

The power will guide you through any additional setup needed and supports migrations between various ARM SoCs including AWS Graviton, Raspberry Pi, NVIDIA Jetson, NXP i.MX, and more.

### Install Prerequisites

The ARM SoC Migration Power uses an MCP (Model Context Protocol) server to provide specialized ARM migration capabilities. This server requires uv/uvx package manager.

Install uv/uvx package manager (required for ARM MCP server):

**macOS:**
```bash
brew install uv
```

**Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:
```bash
uv --version
uvx --version
```

### Launch AWS Graviton Instance (Source Platform)

{{% notice Note %}}
Before proceeding, ensure you are authenticated with AWS CLI. You must have valid AWS credentials configured to create and manage EC2 instances.

Verify your AWS CLI authentication:
```bash
aws sts get-caller-identity
```

If you see an error or need to configure AWS CLI, follow the [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to set up your credentials.
{{% /notice %}}

We'll use an AWS Graviton instance as our source platform to demonstrate the migration workflow. Graviton provides a cloud-based ARM environment that's easy to set up and tear down.

Create an SSH key, security group, and launch a c7g.medium Graviton instance:

```bash
aws ec2 create-key-pair --key-name graviton-migration-key --query 'KeyMaterial' --output text > graviton-migration-key.pem && chmod 400 graviton-migration-key.pem && SG_ID=$(aws ec2 create-security-group --group-name graviton-migration-sg --description "Security group for ARM SoC migration" --query 'GroupId' --output text) && aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 0.0.0.0/0 && aws ec2 run-instances --image-id $(aws ec2 describe-images --owners amazon --filters "Name=name,Values=al2023-ami-2023*-arm64" "Name=state,Values=available" --query 'reverse(sort_by(Images, &CreationDate))[0].ImageId' --output text) --instance-type c7g.medium --key-name graviton-migration-key --security-group-ids $SG_ID --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=graviton-migration-source}]' --query 'Instances[0].InstanceId' --output text
```

Wait ~30 seconds for the instance to start, then get the SSH command:

```bash
echo "ssh -i graviton-migration-key.pem ec2-user@$(aws ec2 describe-instances --filters "Name=tag:Name,Values=graviton-migration-source" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)"
```

Copy and paste the output to connect to your instance.

### Install Development Tools on Graviton Instance

The Graviton instance needs basic build tools (gcc, make) to compile the sensor-monitor application. We'll also install wget and tar for downloading and extracting files.

Once connected to your Graviton instance, install the required build tools:

```bash
sudo dnf install -y gcc make wget tar
```

## Expected Output

After completing this section, you should have:
- Kiro IDE installed locally with ARM SoC Migration Power active
- AWS Graviton c7g.medium instance running with build tools installed
- SSH key saved locally for secure access
- Ready to develop and test on the source platform

Next, you'll download the sample application locally and deploy it to the Graviton instance for testing.
