---
title: "Register and provision the Greengrass core device"
description: Create an AWS IoT thing and device certificate for PocketBeagle 2, install them with a Greengrass nucleus lite configuration, and confirm the board appears as a healthy core device.
weight: 5
layout: "learningpathall"
---

## Create the device identity in AWS

Create a device identity for the PocketBeagle 2 that you booted.

Use the same AWS account and Region for every step. You'll follow the connection kit workflow for Greengrass nucleus lite in the [Greengrass nucleus lite provisioning guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md). The workflow provisions one unique identity per board and doesn't use a fleet provisioning claim certificate.

{{% notice Note %}}
This setup can incur AWS charges. AWS IoT Greengrass bills each core device that connects to AWS in a given month. AWS IoT Core bills for connectivity and messaging.

The AWS Free Tier covers a small test such as this Learning Path for a limited time. For rates, eligibility, and guidance to stop Greengrass billing, see [AWS IoT Greengrass pricing](https://aws.amazon.com/greengrass/pricing/) and [AWS IoT Core pricing](https://aws.amazon.com/iot-core/pricing/).
{{% /notice %}}

In the AWS IoT console:

1. Open **Greengrass devices**, then open **Core devices**.
2. Choose **Set up core device**.
3. Choose the option to set up one core device. Name it `MyPocketBeagle2` and select **Nucleus Lite**.
4. Create a dedicated thing group named `PocketBeagleDevices`, or add the device to that group if you created it separately. Don't use a group containing production devices.
5. Choose **Create thing**, then **Download connection kit**. Save the kit privately on the host computer that connects to the board over USB, for example in `~/Downloads`. The file name is based on the thing name. In this case, it's `MyPocketBeagle2-connectionKit.zip`.

This workflow creates the IoT thing, a device certificate, and an IoT policy. It also creates token-exchange AWS Identity and Access Management (IAM) role, and an IoT role alias.

Don't run any installation commands that the console offers, because the Yocto image already includes the Greengrass runtime.

If the console returns an error when you choose **Create thing**, follow the [manual credentials procedure](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/manual-credentials/) instead of the connection kit. That procedure returns you to this page after creating the configuration file.

## Set variables on the host computer

On the host computer, set variables that you'll use for the rest of the Learning Path. Replace the Region if needed, and use an authenticated AWS CLI v2 profile:

```bash
export AWS_REGION=us-east-1
export THING_NAME=MyPocketBeagle2
export THING_GROUP=PocketBeagleDevices
aws sts get-caller-identity
aws iot list-thing-groups-for-thing --thing-name "$THING_NAME"
```

The `aws sts get-caller-identity` command confirms that the AWS CLI uses the account that you expect. The final command confirms that the thing exists and lists its thing groups.

## Prepare a credentials directory on the board

From the host computer, create a directory for the credentials on the board:

```bash
ssh root@192.168.7.2 'mkdir -p "$HOME/gg-provision"'
```

The single quotes make the board, not the host computer, expand `$HOME`. This directory temporarily holds the connection kit until you install it.

## Upload the connection kit to the board

From the host computer, change to the folder that holds the connection kit. Copy it to the board with `scp`:

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

The file looks similar to:

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
The Region, endpoints, and role alias are your own values. The `{{config_dir}}` and `{{nucleus_component}}` are placeholders that you need to change.

Replace `{{config_dir}}` with `/etc/greengrass`, the directory that holds the credentials on the board. Replace `{{nucleus_component}}` with `aws.greengrass.NucleusLite`, the name of the Greengrass nucleus lite service.

The following command makes both changes in place:

```bash
sed -i -e 's|{{config_dir}}|/etc/greengrass|g' \
  -e 's|{{nucleus_component}}|aws.greengrass.NucleusLite|g' config.yaml
grep '{{' config.yaml
```

The `grep` command prints nothing when no placeholders remain.

### Check the identity in AWS

Before you finalize the Greengrass configuration, check the identity of the device in the AWS IoT console. Note the thing name, Region, data endpoint, credential provider endpoint, and role alias in `config.yaml`. In the console, find the role alias under **Security > Role aliases** and record its IAM role name. This helps if token exchange fails later. The inline Hello World component doesn't need an S3 permissions policy.

Confirm that the device certificate is **ACTIVE**, is attached to this thing, and has the generated IoT policy attached. The policy needs to allow the device IoT and Greengrass communication, and `iot:AssumeRoleWithCertificate` on the role alias Amazon Resource Name (ARN). The IAM role needs to trust `credentials.iot.amazonaws.com`. To troubleshoot each association, see the [Greengrass nucleus lite provisioning guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md).

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

The command copies only the four credential and configuration files. It doesn't copy the connection kit zip.

The output is similar to:

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

The Greengrass configuration is complete.

Restart the Greengrass services on the board:

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

The core services should be running without repeated certificate, authorization, or endpoint errors.

On the host computer, query the registered core device:

```bash
aws greengrassv2 get-core-device --core-device-thing-name "$THING_NAME"
```

The output is similar to:

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

The output format depends on your AWS CLI output setting.

In the AWS IoT console, the device appears under **Greengrass devices > Core devices** with a healthy status. An IoT thing alone doesn't prove that the Greengrass runtime connected.

If the device doesn't appear or isn't healthy, check the following items:

- Clock synchronization on the board
- Outbound connectivity from the board
- Certificate activation
- IoT policy attachment
- The same Region in the console, the AWS CLI, and `config.yaml`

When the core device reports healthy, delete the temporary directory on the board:

```bash
rm -r "$HOME/gg-provision"
```
The directory holds a copy of the private key, which the board no longer needs there.

## What you've accomplished and what's next

You've created a unique AWS identity for the PocketBeagle 2. The board now connects as a Greengrass core device.

Next, you'll publish an inline Hello World component for the device to run.
