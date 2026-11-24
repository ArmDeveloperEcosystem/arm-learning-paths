---
title: "Register and provision the Greengrass core device"
description: Create an AWS IoT thing and device certificate for PocketBeagle 2, install them with a Greengrass nucleus lite configuration, and confirm the board appears as a healthy core device.
weight: 5
layout: "learningpathall"
---

## Create the device identity in AWS

Use the same AWS account and Region for every step. The steps follow the connection kit workflow for Greengrass nucleus lite in the [pinned upstream provisioning guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md). It provisions one unique identity per board and doesn't use a fleet provisioning claim certificate.

This setup can incur AWS charges. AWS IoT Greengrass bills each core device that connects to AWS in a given month, and AWS IoT Core bills for connectivity and messaging. The AWS Free Tier covers a small test like this for a limited time. For rates and eligibility, see [AWS IoT Greengrass pricing](https://aws.amazon.com/greengrass/pricing/) and [AWS IoT Core pricing](https://aws.amazon.com/iot-core/pricing/). The Greengrass pricing page also explains how to stop billing for a device when you finish.

In the AWS IoT console:

1. Open **Greengrass devices**, then **Core devices**, and choose **Set up core device**.
2. Choose the option to set up one core device. Name it `MyPocketBeagle2` and select **Nucleus Lite**.
3. Create a dedicated thing group named `PocketBeagleDevices`, or add the device to that group if you created it separately. Do not use a group containing production devices.
4. Choose **Create thing**, then **Download connection kit**. Save it privately on the host computer that connects to the board over USB, for example in `~/Downloads`. The file name is based on the thing name, so it is `MyPocketBeagle2-connectionKit.zip` if you used the name above.

This workflow creates the IoT thing, a device certificate, an IoT policy, a token-exchange AWS Identity and Access Management (IAM) role, and an IoT role alias. If the console offers installation commands, don't run them, because the Yocto image already includes the Greengrass runtime.

If the console returns an error when you choose **Create thing**, for example because your AWS account restricts it, use the [manual alternative](#manual-alternative-create-the-credentials-without-a-connection-kit) instead of the connection kit.

## Set variables on the host computer

On the host computer, set variables used throughout the remaining pages. Replace the sample Region if needed, and use an authenticated AWS CLI v2 profile:

```bash
export AWS_REGION=us-east-1
export THING_NAME=MyPocketBeagle2
export THING_GROUP=PocketBeagleDevices
aws sts get-caller-identity
aws iot list-thing-groups-for-thing --thing-name "$THING_NAME"
```

The `aws sts get-caller-identity` command confirms that the AWS CLI uses the account you expect. The last command confirms that the thing exists and lists its thing groups.

## Prepare a credentials directory on the board

From the host computer, create a directory for the credentials on the board. The single quotes make the board, not the host computer, expand `$HOME`:

```bash
ssh root@192.168.7.2 'mkdir -p "$HOME/gg-provision"'
```

This directory temporarily holds the connection kit until you install it.

## Upload the connection kit to the board

From the host computer, change to the folder that holds the connection kit and copy it to the board with `scp`:

```bash
cd ~/Downloads
scp MyPocketBeagle2-connectionKit.zip root@192.168.7.2:./gg-provision
```

## Edit the connection kit configuration

From the host computer, open an SSH session to the board:

```bash
ssh root@192.168.7.2
```

Unzip the connection kit:

```bash
cd $HOME
cd ./gg-provision
unzip ./MyPocketBeagle2-connectionKit.zip
```

Display the `config.yaml` file:

```bash
cat ./config.yaml
```

The file looks like this. The Region, endpoints, and role alias are your own values. The `{{config_dir}}` and `{{nucleus_component}}` placeholders are the parts to change:

```yaml
---
system:
  certificateFilePath: "{{config_dir}}/device.pem.crt"
  privateKeyPath: "{{config_dir}}/private.pem.key"
  rootCaPath: "{{config_dir}}/AmazonRootCA1.pem"
  thingName: "MyPocketBeagle2"
services:
  {{nucleus_component}}:
    componentType: "NUCLEUS"
    configuration:
      awsRegion: "us-east-1"
      iotRoleAlias: "GreengrassV2TokenExchangeCoreDeviceRoleAlias"
      iotDataEndpoint: "YOUR_IOT_DATA_ENDPOINT-ats.iot.us-east-1.amazonaws.com"
      iotCredEndpoint: "YOUR_IOT_CRED_ENDPOINT.credentials.iot.us-east-1.amazonaws.com"
```

Replace `{{config_dir}}` with `/etc/greengrass`, the directory that holds the credentials on the board. Replace `{{nucleus_component}}` with `aws.greengrass.NucleusLite`, the name of the Greengrass nucleus lite service. This command makes both changes in place:

```bash
sed -i -e 's|{{config_dir}}|/etc/greengrass|g' \
  -e 's|{{nucleus_component}}|aws.greengrass.NucleusLite|g' config.yaml
grep '{{' config.yaml
```

The `grep` command prints nothing when no placeholders remain.

### Check the identity in AWS

Before you continue, check the device's identity in the AWS IoT console. Note the thing name, Region, data endpoint, credential provider endpoint, and role alias in `config.yaml`. In the console, find the role alias under **Security > Role aliases** and record its IAM role name, which helps if token exchange fails later. The inline Hello World component doesn't need an S3 permissions policy.

Then confirm that the device certificate is **ACTIVE**, is attached to this thing, and has the generated IoT policy attached. The policy must allow the device's IoT and Greengrass communication, and `iot:AssumeRoleWithCertificate` on the role alias Amazon Resource Name (ARN). The IAM role must trust `credentials.iot.amazonaws.com`. To troubleshoot each association, see the [pinned upstream provisioning guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md).

## Finalize the Greengrass configuration

In the same SSH session, copy the files from the updated connection kit to the Greengrass configuration directory on the board:

```bash
cd "$HOME/gg-provision"
cp config.yaml device.pem.crt private.pem.key AmazonRootCA1.pem /etc/greengrass/
cd /etc/greengrass
chmod 640 device.pem.crt private.pem.key AmazonRootCA1.pem
chown ggcore:ggcore device.pem.crt private.pem.key AmazonRootCA1.pem
ls -al
```

The command copies only the four credential and configuration files, not the connection kit zip. The output is similar to:

```output
total 28
drwxr-xr-x  3 root   root   4096 Oct 22 19:32 .
drwxr-xr-x 48 root   root   4096 Oct 22 19:34 ..
-rw-r-----  1 ggcore ggcore 1188 Oct 22 19:35 AmazonRootCA1.pem
drwxr-xr-x  2 root   root   4096 Mar  9  2018 config.d
-rw-r--r--  1 root   root    540 Oct 22 19:35 config.yaml
-rw-r-----  1 ggcore ggcore 1220 Oct 22 19:35 device.pem.crt
-rw-r-----  1 ggcore ggcore 1675 Oct 22 19:35 private.pem.key
```

The Greengrass configuration is complete. Restart the Greengrass services on the board:

```bash
systemctl restart greengrass-lite.target
systemctl status --with-dependencies greengrass-lite.target
```

The Greengrass services should now be running.

## Verify the Greengrass core device

On the board, inspect service health and connection logs:

```bash
systemctl status --with-dependencies greengrass-lite.target
systemctl --failed
journalctl -u ggl.core.iotcored.service -u ggl.core.ggdeploymentd.service -b --no-pager
```

The core services should be running without repeated certificate, authorization, or endpoint errors. On the host computer, query the registered core device:

```bash
aws greengrassv2 get-core-device --core-device-thing-name "$THING_NAME"
```

The output is similar to the following. Its format depends on your AWS CLI output setting:

```output
{
    "coreDeviceThingName": "MyPocketBeagle2",
    "coreVersion": "2.6.0",
    "platform": "linux",
    "architecture": "aarch64",
    "status": "HEALTHY",
    "lastStatusUpdateTimestamp": 1792697816.549,
    "tags": {}
}
```

In the AWS IoT console, the device appears under **Greengrass devices > Core devices** with a healthy status. An IoT thing alone doesn't prove that the Greengrass runtime connected. If the device doesn't appear or isn't healthy, check these items:

- Clock synchronization on the board
- Outbound connectivity from the board
- Certificate activation
- IoT policy attachment
- The same Region in the console, the AWS CLI, and `config.yaml`

When the core device reports healthy, delete the temporary directory on the board. It holds a copy of the private key, which the board no longer needs there:

```bash
rm -r "$HOME/gg-provision"
```

## Manual alternative: create the credentials without a connection kit

Use these steps only if you can't download a connection kit from the console. You create the same resources yourself, then rejoin the main steps.

### Create the resources

Follow [Manual Provisioning by Creating a Thing](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md#manual-provisioning-by-creating-a-thing) in the pinned upstream provisioning guide. It creates an IAM role, an IoT role alias, an IoT policy, and a thing with a certificate. When you finish, you have:

- A device certificate and private key
- The Amazon Root certificate authority (CA) certificate
- The thing name, Region, and role alias name

### Use a pre-approved role (optional)

Most readers use the role that the connection kit creates and don't need a permissions boundary. If your administrator requires a pre-approved role, use that role instead of creating one, and keep its boundary.

To point a device-specific alias at the approved role, replace both placeholders in this command:

```bash
aws iot update-role-alias --role-alias YOUR_ROLE_ALIAS --role-arn YOUR_APPROVED_ROLE_ARN
```

If the alias doesn't exist, run `create-role-alias` with the same arguments. Your administrator must confirm the role's trust and certificate-policy permissions. In `config.yaml`, set `iotRoleAlias` to the alias name, not its Amazon Resource Name (ARN).

### Copy the credentials to the board

On the host computer, keep the credentials in a private directory outside any source checkout. Identify the device certificate, the private key, and the Amazon Root CA certificate. Save copies with these file names: `device.pem.crt`, `private.pem.key`, and `AmazonRootCA1.pem`. Don't confuse the device certificate with the CA certificate or the public key.

Restrict the private key's permissions, then copy the three files to the board. Run these commands from the directory that holds the files:

```bash
chmod 600 private.pem.key
scp device.pem.crt private.pem.key AmazonRootCA1.pem \
    root@192.168.7.2:./gg-provision/
```

AWS CLI credentials stay on the host computer. The board authenticates with its device private key and certificate.

### Add the thing to the thing group

If the thing group doesn't exist, create it:

```bash
aws iot create-thing-group --thing-group-name "$THING_GROUP"
```

If the thing isn't a member of `PocketBeagleDevices`, add it. The command produces no output on success:

```bash
aws iot add-thing-to-thing-group --thing-name "$THING_NAME" \
    --thing-group-name "$THING_GROUP"
```

Confirm membership before you continue:

```bash
aws iot list-thing-groups-for-thing --thing-name "$THING_NAME"
```

### Get the endpoints

Get the AWS IoT data endpoint and credential provider endpoint for your account. On the host computer, run:

```bash
aws iot describe-endpoint --endpoint-type iot:Data-ATS
aws iot describe-endpoint --endpoint-type iot:CredentialProvider
```

Record the full `endpointAddress` value from each command.

### Create the configuration file

Create a file named `config.yaml` with the following contents. Replace `YOUR_IOT_DATA_ENDPOINT` and `YOUR_IOT_CRED_ENDPOINT` with the full endpoint addresses from the previous step. Set `iotRoleAlias` to your role alias name, and set `awsRegion` to your Region:

```yaml
---
system:
  certificateFilePath: "/etc/greengrass/device.pem.crt"
  privateKeyPath: "/etc/greengrass/private.pem.key"
  rootCaPath: "/etc/greengrass/AmazonRootCA1.pem"
  thingName: "MyPocketBeagle2"
services:
  aws.greengrass.NucleusLite:
    componentType: "NUCLEUS"
    configuration:
      awsRegion: "us-east-1"
      iotRoleAlias: "YOUR_ROLE_ALIAS"
      iotDataEndpoint: "YOUR_IOT_DATA_ENDPOINT"
      iotCredEndpoint: "YOUR_IOT_CRED_ENDPOINT"
```

Copy the file to the board with the other credential files:

```bash
scp config.yaml root@192.168.7.2:/root/gg-provision/
```

On the board, in an SSH session, confirm that the directory contains the four files:

```bash
cd ~/gg-provision
ls -al
```

The output is similar to:

```output
-rw-r--r-- 1 root root 1188 Oct 21 15:36 AmazonRootCA1.pem
-rw-r--r-- 1 root root  528 Oct 21 15:36 config.yaml
-rw-r--r-- 1 root root 1220 Oct 21 15:36 device.pem.crt
-rw-r--r-- 1 root root 1675 Oct 21 15:36 private.pem.key
```

Continue with [Check the identity in AWS](#check-the-identity-in-aws). The `config.yaml` file already has its final paths, so skip the placeholder replacement.

## What you have accomplished

The board has a unique AWS identity and connects as a Greengrass core device. Next, publish an inline Hello World component for the device to run.
