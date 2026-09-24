---
title: AWS IoT Greengrass
description: Install AWS IoT Greengrass on an Arm device and register it with AWS so you can build and manage IoT edge applications.
author: Michael Hall
additional_search_terms:
- iot
- AWS
- Greengrass

layout: installtoolsall
minutes_to_complete: 15
official_docs: https://docs.aws.amazon.com/greengrass/v2/developerguide/quick-installation.html
prerequisites: AWS Account with IAM use role
test_maintenance: false
test_images:
- ubuntu:latest
tool_install: true
multi_install: false
multitool_install_part: false

weight: 1
---

[AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) is an open source Internet of Things (IoT) edge runtime and cloud service that helps you build, deploy, and manage IoT applications on your devices.

## Pre-requesite Installation

Before starting, lets install `unzip` and `default-jdk` on our candidate Greengrass device:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install unzip default-jdk -y
```

Follow the instructions below to install AWS IoT Greengrass on your device and register the device with the AWS IoT Greengrass service.

The instructions provide the fastest and simplest configuration for deploying AWS IoT Greengrass into a development environment, and they may not be suitable for production deployments.

{{% notice Note - Administrative access required %}}
You will need to log into the AWS console with administrator access for your AWS account that has the ability to create access keys and assign roles to those keys. Typically, account logins with administrative priviledge can create access keys and assign administrator roles to those keys (but please be careful with those kinds of access keys!).
{{% /notice %}}

While an administrator can easily setup and install devices into your AWS Greengrass environment, the following steps show how to create a Greengrass "installation user" that has just enough permission to also setup and deploy devices into the Greengrass environment. Note that you can always skip down to the access key creation step if you just want to use your main administrator account in AWS.

## Greengrass Installer User Creation

### AWS Role creation

In order to create a Greengrass Installer user, you first need to create an AWS IAM role with sufficient permissions to run the Greengrass installer and setup a Greengrass device.

With this role, you will also create an "installer user" to assume the role. With this user, you will create and save an access key and secret access key for AWS CLI access.

### Greengrass Installer User Creation

Log in to the AWS console, set the AWS region you want to use in upper right corner, and navigate to the Identify and Access Management (IAM) dashboard.

### Creating the AWS Greengrass Installer User Role {#prepare-your-aws-role}

1. Create a new IAM user named `gg_installer_user` by pressing `Create User`

![Create IAM User #center](/install-guides/_images/greengrass-start-create-user.png)

Include access to the AWS Console and provide a custom password for the new user. Press `Next`

![Create IAM User #center](/install-guides/_images/greengrass-create-iam-user.png)

2. Create new group by pressing `Create Group`

![Create IAM User Group #center](/install-guides/_images/greengrass-new-user-next.png)

Name the new group `gg_installer_group`

![Create IAM User Group #center](/install-guides/_images/greengrass-new-group.png)

3. Click the `Create Policy` button (this will open in a new tab) to create a new IAM policy

![Create Policy #center](/install-guides/_images/greengrass-new-policy.png)

4. Switch to the `JSON` tab and paste in the following JSON. This JSON specifies all of the permissions needed by the installer user to install/setup a Greengrass device:

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

5. Replace  `account-id` on lines 16 and 17 with your AWS account ID. Then press `Next`

{{% notice Note %}}
You can find your account ID by clicking on your user name in the top-right corner of the AWS console.
![Role Permissions Editor #center](/install-guides/_images/gg-role-permissions.png)
{{% /notice %}}

6. Name the new policy `GGDeploymentAccess` and press `Create policy`

![Naming the new Role #center](/install-guides/_images/greengrass-name-policy.png)

7. Back on the group creation page, click the refresh button then search for and select `GGDeploymentAccess`. Then press `Create user group`

![Group Policy Selection in Group #center](/install-guides/_images/greengrass-complete-new-group.png)

8. Review and create user

![Create User #center](/install-guides/_images/greengrass-new-user-create-finish.png)

Ensure that your new user belongs to the newly created `gg_installer_group` previously created. Press `Add user to group` to add the new user to the `gg_installer_group` group

![User Group Inclusion #center](/install-guides/_images/greengrass-add-to-group.png)

Your Greengrass installation user is now configured!  Next, lets create some security credentials to be used by the Greengrass Installer

1. Click on `gg_installer_user` and navigate to the `Security credentials` tab

![Creating Security Credential #center](/install-guides/_images/greengrass-create-ak.png)

2. Click `Create access key` to create a new access key

![Creating Security Credential #center](/install-guides/_images/greengrass-config-new-ak.png)

Select `Command Line Interface (CLI)` for your key type, ignoring the warnings for now (you should delete they keys when you're done testing).

3. Set the description/name of the new access key and press `Create access key`

![Creating Security Credential #center](/install-guides/_images/greengrass-new-ak-finish.png)

4. Safe off your `Access key` and `Secret access key`. This will be the only time that you can save both off.

![Access Keys #center](/install-guides/_images/gg-access-keys.png)

You will use the credentials in the next section to install the Greengrass device.

## Prepare the installation environment with access credentials

Set the environment variables to allow AWS IoT Greengrass to connect with your AWS account. Replace the access key and secret access key with the values you saved in the [previous section](#prepare-your-aws-role).

```bash { target="ubuntu:latest" }
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_REGION="us-east-1"
```

{{% notice Note %}}
Replace `us-east-1` with the AWS region you want to use.
{{% /notice %}}

With these credentials created, lets proceed to invoke the Greengrass installer on the selected device. 

## Download the Greengrass Installer

1. From the AWS console, navigate to the `AWS IoTCore` dashboard and select `"Greengrass Devices" --> "Core Devices"` on the left hand navigation tree. Press `"Set up core device" --> "Set up one core device"`:

![Greengrass Dashboard #center](/install-guides/_images/greengrass-dashboard.png)

Next, lets provide a name for your new Greengrass device. Select `"Greengrass nucleus"`. 

{{% notice Note %}}
There are two versions of Greengrass: `"Greengrass nucleus"` (Java-based, heavier-weight) and `"Greengrass nucleus lite"` (native).
There are numerous considerations around which to choose from. For this particular install guide, the Java-based `"Greengras nucleus"` will be selected.
{{% /notice %}}

You can also choose to place the device into a new devices group or an existing devices group. Select `"No group"` if desired or create your own new devices group (either is fine). 

Also, lets select `"Linux"` as the Operating System as well as selecting `"Set up a device by downloading and running an installer locally on device"` to specify the installation type:

![Greengrass Device Install Setup #center](/install-guides/_images/greengrass-setup.png)

2. Navigate down to the "Step 3: Install the Greengrass Core Software"

![Greengrass Device Install Setup #center](/install-guides/_images/greengrass-installer-setup.png)

The dashboard will now provide a curl command to download the installer and run it (within the environment that our AWS access keys/secrets have been setup per above)

3. Set the 3 environment variables in a shell on your target device using your saved off access key and secret. Also specify the AWS region you wish to use:

```bash
export AWS_ACCESS_KEY_ID="My newly created AWS Access Key ID"
export AWS_SECRET_ACCESS_KEY="My newly created AWS Secret Access Key"
export AWS_REGION="My target AWS region"
```

4. Copy and paste the `curl` command to download the installer to your target device. Invoke the `curl` command in the same shell from above

5. Copy and paste the installation command shown in the dashboard. Invoke the command in the same shell from above

{{% notice Note %}}
If your target device is running the newest versions of Ubuntu (25.x, 26.x), then those new distros use a rust-based `sudo` command, by default, that does not obey the `-E` option (export entire environment to the sudo session). If you get an error when running the installer that indicates that the `-E` option is not supported by `sudo`, you can temporarily change back to the non-rust version of `sudo` on your device from the same shell from above:

```bash
sudo update-alternatives --config sudo
```

In this case, select the number representing the version of sudo that is listed simply as `/usr/bin/sudo`. Then re-run the Greengrass installer command. Be sure to switch the version of sudo back once the Greengrass installation has completed.
{{% /notice %}}

6. Press `View Core Devices` to see your newly created Greengrass device in the device list dashboard.

![Greengrass Devices List #center](/install-guides/_images/greengrass-core-device-list.png)

You will see the new device listed in the Greengrass core devices.

Click on the device name to see more device details.

7. On the newly created Greengrass device, confirm the AWS IoT Greengrass system service was installed and is running:

```bash
sudo systemctl status greengrass
```

Output should resemble:

```output
greengrass.service - Greengrass Core
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

{{% notice Note %}}
Greengrass does not run as a `root` user on your device - the `ggc_user` user belonging to the `ggc_group` group will be the service account for running AWS IoT Greengrass components on your device.
{{% /notice %}}


Congrats!!! You are now ready to use AWS IoT Greengrass v2 on your device.