---
title: Install AWS IoT Greengrass
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create AWS access credentials

Before installing AWS IoT Greengrass, you need a set of AWS access credentials. The Greengrass installer uses these credentials to register your edge device with AWS IoT Core and configure the required cloud resources.

{{% notice Note %}}
If you're using an AWS-hosted event account, credentials might be provided to you automatically. If so, copy them for the next step. They should look like this:

```bash
export AWS_ACCESS_KEY_ID=<your-access-key-id>
export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
```

If you already have credentials, skip ahead to [Install Greengrass Nucleus Classic](#install-greengrass-nucleus-classic).
{{% /notice %}}

If you're using a personal AWS account and don't have access credentials yet, follow the steps below to create them.

### Create access credentials for a personal AWS account

Open the AWS Console and search for **IAM**:

![AWS Console search bar with IAM entered as the search term#center](./images/gg_install_iam.png "Search for IAM")

Open the IAM Dashboard:

![IAM Dashboard showing the main overview with users, roles, and policies sections#center](./images/gg_install_iam_dashboard.png "IAM Dashboard")

Select **Users** from the left sidebar:

![IAM Users list showing available user accounts#center](./images/gg_install_iam_2.png "IAM Users list")

Select your user, then select the **Security credentials** tab:

![User details page with the Security credentials tab selected#center](./images/gg_install_iam_3.png "Security credentials tab")

Select **Create access key**:

![Security credentials section with the Create access key button#center](./images/gg_install_iam_4.png "Create access key")

Choose **Other** as the use case and select **Next**:

![Access key use case selection with the Other option highlighted#center](./images/gg_install_iam_5.png "Select use case")

Enter a description for the access key (for example, "Greengrass installer") and select **Create access key**:

![Access key description field with the Create access key button#center](./images/gg_install_iam_6.png "Create access key")

This is the only time you can view the full credentials. Copy them and save them to a temporary file in this format:

```bash
export AWS_ACCESS_KEY_ID=<your-access-key-id>
export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
```

You'll paste these into your SSH session during the Greengrass installation.

## Install Greengrass Nucleus Classic

AWS IoT Greengrass has two versions: **Nucleus Classic**, which is Java-based, and **Nucleus Lite**, which is a native implementation typically used with Yocto-based images. This Learning Path uses Nucleus Classic because it runs on standard Linux distributions that your edge device is already running.

In the AWS Console, navigate to **AWS IoT Core** > **Greengrass** > **Core devices** and select **Set up one core device**.

Select **Linux** as the device type. The console generates download and install commands customized for your account:

![Greengrass core device setup page showing the Linux device type selected and the Nucleus Classic option#center](./images/gg_install_device.png "Set up core device")

Scroll down to see the install steps. The console provides commands tailored to your account. Follow these steps in an SSH session on your edge device:

1. Export your AWS credentials in the terminal:

   ```bash
   export AWS_ACCESS_KEY_ID=<your-access-key-id>
   export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
   ```

2. Copy and run the **Download the installer** command from the console. This downloads the Greengrass Nucleus installer to your device.

3. Copy and run the **Run the installer** command from the console. This installs and starts the Greengrass Nucleus service.

4. Wait for the installer to finish. A successful installation displays a confirmation message.

The screenshot below shows where to find these commands in the console:

![Greengrass setup page showing the Download the installer and Run the installer sections with copy buttons#center](./images/gg_install_device2.png "Installer commands")

## Add permissions to the Greengrass token exchange role

When Greengrass runs a component, it uses a Linux service user called `ggc_user` (on Nucleus Classic installations) to start the process. AWS credentials are passed to the component through its environment at launch time, and the component's AWS SDK uses those credentials to connect to AWS services. The permissions available to the component are controlled by an IAM role called `GreengrassV2TokenExchangeRole`.

By default, this role doesn't include the permissions that the Edge Impulse component needs. You need to add three policies:

- **AWSIoTFullAccess** — allows the component to publish inference results and receive commands through AWS IoT Core MQTT topics.
- **AmazonS3FullAccess** — allows access to S3 buckets where component artifacts are stored.
- **SecretsManagerReadWrite** — allows the component to retrieve the Edge Impulse API key from AWS Secrets Manager.

To add these permissions, navigate to **IAM** > **Roles** in the AWS Console and search for `GreengrassV2TokenExchangeRole`. Then:

1. Select **GreengrassV2TokenExchangeRole** from the search results.
2. Select **Add permissions** > **Attach policies**.
3. Search for **AWSIoTFullAccess**, select it, and select **Add permissions**.
4. Repeat for **AmazonS3FullAccess** and **SecretsManagerReadWrite**.

![GreengrassV2TokenExchangeRole permissions page showing the three newly attached policies#center](./images/iam_ter_update.webp "Updated token exchange role permissions")

After updating, your `GreengrassV2TokenExchangeRole` should show all three policies attached.

## What you've accomplished

In this section, you created AWS access credentials, installed Greengrass Nucleus Classic on your edge device, and configured the token exchange role with the permissions that the Edge Impulse component requires. In the next section, you store your Edge Impulse API key in AWS Secrets Manager.