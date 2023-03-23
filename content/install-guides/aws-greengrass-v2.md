---
title: AWS IoT Greengrass
author-primary: Michael Hall <michael.hall@arm.com>
additional_search_terms:
- iot
layout: installtoolsall
minutes_to_complete: 15
official_docs: https://docs.aws.amazon.com/greengrass/v2/developerguide/quick-installation.html
prerequisites: AWS Account with IAM use role
test_images:
- ubuntu:latest

tool_install: true
multi_install: false
multitool_install_part: false

weight: 1
---

[AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) is an open source Internet of Things (IoT) edge runtime and cloud service that helps you build, deploy and manage IoT applications on your devices.

## Introduction

This article provides instructions for installing AWS IoT Greengrass on your device, and registering that device with the AWS IoT Greengrass service.

These instructions provide the fastest and simplest configuration for deploying AWS IoT Greengrass into a development environment, they may not be suitable or recommended for production deployments.

## Prepare your AWS Role

Before installing AWS IoT Greengrass on your device you first need to create an AWS IAM role with sufficient permissions to create Greengrass Things, Groups and Roles.

1. Create a new IAM user named `gguser`
1. Create new group named `ggusergroup`
1. Click the `Create policy` button (this will open in a new tab)
1. Switch to the `JSON` tab and paste in this [Minimum Policy for Greengrass Installer](https://docs.aws.amazon.com/greengrass/v2/developerguide/provision-minimal-iam-policy.html)
1. You will need to replace both instances of `account-id` in the JSON with your AWS account ID (located in the user menu in the top-right corner of the AWS console) \
![Role Permissions Editor](../_images/gg-role-permissions.png)
1. Name the new policy `GGDeploymentAccess`
1. Back on the group creation page, click the refresh button then search for and select `GGDeploymentAccess` \
![Group Policy Selection](../_images/gg-group-policy.png)
1. Click `Create user group`
1. Review and create user
1. Click on `gguser` and navigate to the `Security credentials` tab
1. Click `Create access keys`
1. Select `Command Line Interface (CLI)` for your key type, ignoring the warnings for now (you should delete they keys when you're done testing).
1. Copy your `Access key` and `Secret access key`. You will need these in the next section. \
![Access Keys](../_images/gg-access-keys.png)


## Download and install AWS IoT Greengrass

Before starting, install `unzip` and `default-jdk`:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install unzip default-jdk -y
```

You will need to set environment variables to allow AWS IoT Greengrass to connect with your AWS account. These varaibles were obtained in the [previous section](#prepare-your-aws-role).

```bash { target="ubuntu:latest" }
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
```
```bash { target="ubuntu:latest" }
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```
```bash { target="ubuntu:latest" }
export AWS_REGION="us-east-1"
```
{{% notice Note %}}
Replace `us-east-1` with the AWS region you want to use.
{{% /notice %}}

Download the zip file with `curl`, extract the installer, and run it.  

```bash { target="ubuntu:latest" }
curl "https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip" -o "greengrass-nucleus-latest.zip"
unzip greengrass-nucleus-latest.zip -d GreengrassInstaller && rm greengrass-nucleus-latest.zip

sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE \
  -jar ./GreengrassInstaller/lib/Greengrass.jar \
  --aws-region $AWS_REGION \
  --thing-name MyGreengrassCore \
  --thing-group-name MyGreengrassCoreGroup \
  --thing-policy-name GreengrassV2IoTThingPolicy \
  --tes-role-name GreengrassV2TokenExchangeRole \
  --tes-role-alias-name GreengrassCoreTokenExchangeRoleAlias \
  --component-default-user ggc_user:ggc_group \
  --provision true \
  --setup-system-service true

```
{{% notice Note %}}
The `ggc_user` and `ggc_group` names will be used to create a local system user and group, respectively, for running AWS IoT Greengrass components.
{{% /notice %}}

This will install the AWS IoT Greengrass v2 software on your device, and and register that device with the Greengrass service.

Confirm the AWS IoT Greengrass system service was installed and is running:

``` { target="ubuntu:latest" command_line="root@localhost | 2-11"}
systemctl status greengrass
● greengrass.service - Greengrass Core
     Loaded: loaded (/etc/systemd/system/greengrass.service; enabled; vendor pr>
     Active: active (running) since Thu 2023-03-23 02:52:28 UTC; 13h ago
   Main PID: 750 (sh)
      Tasks: 50 (limit: 4467)
     Memory: 525.3M
        CPU: 11.976s
     CGroup: /system.slice/greengrass.service
             ├─750 /bin/sh /greengrass/v2/alts/current/distro/bin/loader
             └─767 java -Dlog.store=FILE -Dlog.store=FILE -Droot=/greengrass/v2>
```
