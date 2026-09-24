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
prerequisites: AWS account with permissions to create an IAM user
test_maintenance: false
test_images:
- ubuntu:latest
tool_install: true
multi_install: false
multitool_install_part: false

weight: 1
---

[AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) is an open-source Internet of Things (IoT) edge runtime and cloud service that you can use to build, deploy, and manage IoT applications on your devices.

You'll create an AWS Identity and Access Management (IAM) user, then install AWS IoT Greengrass and prepare it for use on your device.

## Before you begin

Before starting, install `unzip` and `default-jdk` on your candidate Greengrass device:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install unzip default-jdk -y
```

## Prepare AWS access

You'll need to use an AWS account that has permissions to create access keys and assign roles to those keys. While you can use an account with administrator access, it's a best practice to use an IAM user with only the necessary permissions.

You'll therefore create a Greengrass installation IAM user with only the permissions needed to set up and deploy devices in the Greengrass environment.

You'll use the installation IAM user to create and save an access key and secret access key for AWS Command Line Interface (AWS CLI) access.

### Create an IAM policy

Before you create the IAM user, create a policy that grants permissions for installing and setting up a Greengrass device. 

To create an IAM policy, complete the following steps:

1. Log in to the AWS console.
2. From the AWS Region dropdown list, select the region that you want to use.
3. Use the search bar to look for AWS IAM, then navigate to the IAM dashboard.
4. Under **Access Management**, select **Policies**.
5. Select **Create policy**.
   ![AWS IAM Create policy page with the JSON editor selected and the Greengrass permissions policy entered. The account ID placeholders on lines 16 and 17 must be replaced before continuing.#center](/install-guides/_images/greengrass-new-policy.png)
6. Switch to the **JSON** tab and paste in the following JSON. The JSON specifies all of the permissions needed by the installer user to install and set up a Greengrass device:

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
   Replace `account-id` on lines 16 and 17 with your AWS account ID.
   ![AWS IAM policy editor showing validation errors because the two resource ARNs contain account-id instead of a valid value. Replace account-id with your 12-digit AWS account ID.#center](/install-guides/_images/gg-role-permissions.png)

   {{% notice Note %}}
   You can find your account ID by selecting your user name in the AWS console navigation bar.
   {{% /notice %}}

7. Select **Next**.
8. For **Policy name**, enter **GGDeploymentAccess**.
   ![AWS IAM Review and create page with GGDeploymentAccess entered as the policy name and the four permitted services listed for review.#center](/install-guides/_images/greengrass-name-policy.png)
9. Select **Create policy**.

### Create an IAM user group

After creating the IAM policy, create an IAM user group and attach the policy to it:

1. Under **Access Management**, select **IAM user groups**.
2. To create a new user group, select **Create group**.
3. For **User group name**, enter **gg_installer_group**.
4. Under **Attach permissions policies**, search for and select the policy **GGDeploymentAccess** that you created earlier. 
   ![AWS IAM Create user group page with gg_installer_group entered as the group name and the GGDeploymentAccess policy selected.#center](/install-guides/_images/greengrass-new-group.png)
5. Select **Create group**.

### Create the AWS Greengrass installer IAM user {#prepare-your-aws-role}

With the IAM user group ready, you can now create the installer IAM user.

To create the IAM user, complete the following steps:

1. Under **Access Management**, select **IAM users**.
2. Select **Create user**.
   ![AWS IAM users page showing the Create user button, which starts creation of the Greengrass installer user.#center](/install-guides/_images/greengrass-start-create-user.png)
3. For **User name**, enter **gg_installer_user**. 
4. To include access to the AWS Console, select the checkbox **Provide user access to the AWS Management Console**.
5. For **Console password**, select **Custom password** and provide a password for the new user.
   ![AWS IAM Specify user details page with gg_installer_user as the user name, console access enabled, and Custom password selected.#center](/install-guides/_images/greengrass-create-iam-user.png)
6. Select **Next**.
7. Under **Permissions options**, select **Add user to group**. 
   ![AWS IAM Set permissions page with Add user to group selected. Choose gg_installer_group from the User groups table before continuing.#center](/install-guides/_images/greengrass-new-user-next.png)
8. Under **User groups**, select the group **gg_installer_group** that you created earlier.
9. Select **Next**, then select **Create user**.

You've now created an IAM user for Greengrass installation. 

### Create access keys 

After creating the IAM user, you can create access keys for AWS CLI access.

To create access keys, complete the following steps:

1. Under **Access Management**, select **IAM users**.
2. Select **gg_installer_user** and navigate to the **Security credentials** tab.

   ![Security credentials tab for the gg_installer_user IAM user, showing the Create access key button in the Access keys section.#center](/install-guides/_images/greengrass-create-ak.png)

3. Under **Access keys**, select **Create access key**.

4. For **Use case**, select **Command Line Interface (CLI)**. 
5. Acknowledge the recommendations by selecting the checkbox, then select **Next**. Delete the keys when you're done testing.

   ![AWS IAM access-key setup page with Command Line Interface selected and the confirmation checkbox enabled so you can proceed.#center](/install-guides/_images/greengrass-config-new-ak.png)

6. Optionally set a description tag for the access key, then select **Create access key**.

   ![AWS IAM Set description tag page with an optional description entered and the Create access key button ready to select.#center](/install-guides/_images/greengrass-new-ak-finish.png)

7. Save your **Access key** and **Secret access key**. This is the only time that you can view the secret access key.

   ![AWS IAM Retrieve access keys page showing the access key, the hidden secret access key, and the Download CSV file option. Save both credentials now because the secret cannot be retrieved later.#center](/install-guides/_images/gg-access-keys.png)

## Register the Greengrass core device and install Greengrass

With the credentials created, you can now invoke the Greengrass installer on the selected device.

To download and install Greengrass on your selected device, complete the following steps:

1. Use the search bar in the AWS console to search for and navigate to **AWS IoT Core**.
2. Under **Manage**, select **Greengrass devices**, then select **Core devices**.
3. Select **Set up one core device**. 
4. For **Core device name**, enter **MyNewGreengrassDevice**.
5. Place the device in a new devices group by selecting **Enter a new group name** and entering **MyNewGreengrassDeviceGroup**.
6. For **Greengrass Core software runtime**, select **Greengrass nucleus**. Greengrass nucleus is Java-based and heavier-weight than the native Greengrass nucleus lite. 

   ![AWS IoT Greengrass core-device setup page with MyNewGreengrassDevice as the device name, MyNewGreengrassDeviceGroup as the new thing group, and Greengrass nucleus selected as the runtime.#center](/install-guides/_images/greengrass-dashboard.png)

7. For **Operating system**, select **Linux**.
8. For **Device setup method**, select **Set up a device by downloading and running an installer locally on device**.

   ![Greengrass device setup options with Linux selected as the operating system and local installer download selected as the setup method.#center](/install-guides/_images/greengrass-setup.png)

9. Set the three environment variables in a shell on your target device using the access key and secret access key that you saved earlier:

   ```bash
   export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
   export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   export AWS_REGION="us-east-1"
   ```
   {{% notice Note %}}
   Replace `us-east-1` with the AWS region that you want to use.
   {{% /notice %}}

10. Copy and paste the `curl` command to download the installer to your target device. Invoke the `curl` command in the same shell that you used to set the environment variables.
11. Copy and paste the installation command shown in the dashboard. Invoke the command in the same shell. 

    ![Greengrass setup page showing commands to export AWS credentials, download the installer, and run it with the selected device and thing-group names.#center](/install-guides/_images/greengrass-installer-setup.png)

{{% notice Note %}}
If your target device is running the newest versions of Ubuntu (25.x, 26.x), the new distributions use a Rust-based `sudo` command by default. This Rust-based command doesn't support the `-E` option to export the entire environment to the `sudo` session.

If you get an error when running the installer that indicates that the `-E` option isn't supported by `sudo`, temporarily change back to the non-Rust version of `sudo` on your device from the same shell:

```bash
sudo update-alternatives --config sudo
```

In this case, select the number representing the version of `sudo` that's listed as `/usr/bin/sudo`. After selecting, re-run the Greengrass installer command. Be sure to switch the version of `sudo` back after you complete the Greengrass installation.
{{% /notice %}}

12. To view your newly created Greengrass device under **Greengrass core devices**, select **View core devices**.

    ![AWS IoT Greengrass core devices page listing MyNewGreengrassDevice with a Healthy status, confirming that installation and provisioning succeeded.#center](/install-guides/_images/greengrass-core-device-list.png)

Select the device name to see more device details.

## Verify Greengrass installation

On the newly created Greengrass device, confirm that the AWS IoT Greengrass system service was installed and is running:

```bash
sudo systemctl status greengrass
```

The output is similar to:

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
Greengrass doesn't run as a `root` user on your device. It runs under the `ggc_user` service account in the `ggc_group` group.
{{% /notice %}}

## Next steps

You're now ready to use AWS IoT Greengrass v2 on your device.

For an introductory Learning Path for using AWS IoT Greengrass on an Arm-based device, see [Deploy IoT applications with AWS IoT Greengrass and Arm Virtual Hardware](/learning-paths/embedded-and-microcontrollers/avh_greengrass/).
