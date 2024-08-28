---
title: AWS IoT Greengrass
author_primary: Michael Hall
additional_search_terms:
- iot
- AWS
- Greengrass

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

[AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) is an open source Internet of Things (IoT) edge runtime and cloud service that helps you build, deploy, and manage IoT applications on your devices.

## Before you begin

Follow the instructions below to install AWS IoT Greengrass on your device and register the device with the AWS IoT Greengrass service.

The instructions provide the fastest and simplest configuration for deploying AWS IoT Greengrass into a development environment, and they may not be suitable for production deployments.

## Prepare your AWS Role

Before installing AWS IoT Greengrass on your device you first need to create an AWS IAM role with sufficient permissions to create Greengrass Things, Groups, and Roles.

You will also create and save an access key and secret access key for AWS CLI access. 

### Before you begin

Log in to the AWS console, set the AWS region you want to use in upper right corner, and navigate to the Identify and Access Management (IAM) dashboard.


### Create an IAM role and access credentials

1. Create a new IAM user named `gguser`

2. Create new group named `ggusergroup`

3. Click the `Create policy` button (this will open in a new tab)

4. Switch to the `JSON` tab and paste in the following:

```json {line_numbers=true}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateTokenExchangeRole",
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:CreatePolicy",
                "iam:CreateRole",
                "iam:GetPolicy",
                "iam:GetRole",
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::account-id:role/GreengrassV2TokenExchangeRole",
                "arn:aws:iam::account-id:policy/GreengrassV2TokenExchangeRoleAccess"
            ]
        },
        {
            "Sid": "CreateIoTResources",
            "Effect": "Allow",
            "Action": [
                "iot:AddThingToThingGroup",
                "iot:AttachPolicy",
                "iot:AttachThingPrincipal",
                "iot:CreateKeysAndCertificate",
                "iot:CreatePolicy",
                "iot:CreateRoleAlias",
                "iot:CreateThing",
                "iot:CreateThingGroup",
                "iot:DescribeEndpoint",
                "iot:DescribeRoleAlias",
                "iot:DescribeThingGroup",
                "iot:GetPolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DeployDevTools",
            "Effect": "Allow",
            "Action": [
                "greengrass:CreateDeployment",
                "iot:CancelJob",
                "iot:CreateJob",
                "iot:DeleteThingShadow",
                "iot:DescribeJob",
                "iot:DescribeThing",
                "iot:DescribeThingGroup",
                "iot:GetThingShadow",
                "iot:UpdateJob",
                "iot:UpdateThingShadow"
            ],
            "Resource": "*"
        }
    ]
}
```

5. Replace  `account-id` on lines 16 and 17 with your AWS account ID

You can find your account ID by clicking on your user name in the top-right corner of the AWS console. 

![Role Permissions Editor #center](/install-guides/_images/gg-role-permissions.png)

6. Name the new policy `GGDeploymentAccess`

7. Back on the group creation page, click the refresh button then search for and select `GGDeploymentAccess` 

![Group Policy Selection #center](/install-guides/_images/gg-group-policy.png)

8. Click `Create user group`

9. Review and create user

10. Click on `gguser` and navigate to the `Security credentials` tab

11. Click `Create access keys`

12. Select `Command Line Interface (CLI)` for your key type, ignoring the warnings for now (you should delete they keys when you're done testing).

13. Copy your `Access key` and `Secret access key`. 

![Access Keys #center](/install-guides/_images/gg-access-keys.png)

You will use the credentials in the next section. 

## Download and install AWS IoT Greengrass

Before starting, install `unzip` and `default-jdk`:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install unzip default-jdk -y
```

Set the environment variables to allow AWS IoT Greengrass to connect with your AWS account. Replace the access key and secret access key with the values you saved in the [previous section](#prepare-your-aws-role).

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

This will install the AWS IoT Greengrass v2 software on your device, and and register the device with the Greengrass service.

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

Confirm the AWS IoT Greengrass system service was installed and is running:

```bash { target="ubuntu:latest" command_line="user@localhost | 2-11"}
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

## View your device in the AWS console

In your browser, go to the AWS console and navigate to the IoT Greengrass console. 

You will see the new device listed in the Greengrass core devices.

Click on the device name to see more device details. 

![Greengrass Devices #center](/install-guides/_images/greengrass-devices.png)

You are now ready to use AWS IoT Greengrass v2 on your device. 