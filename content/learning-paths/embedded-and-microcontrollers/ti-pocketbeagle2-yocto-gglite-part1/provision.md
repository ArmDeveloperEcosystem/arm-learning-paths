---
title: "Register and provision the Greengrass core device"
description: Provision a unique AWS IoT identity on PocketBeagle 2 with the supplied helper and verify the Greengrass Lite cloud connection.
weight: 5
layout: "learningpathall"
---

## Create the device identity in AWS

Use the same AWS account and Region throughout this Learning Path. This page uses the Nucleus Lite connection-kit workflow documented in the [pinned upstream provisioning guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md). It provisions one unique identity per board; it does not use a fleet provisioning claim certificate.

In the AWS IoT console:

1. Open **Greengrass devices**, then **Core devices**, and choose **Set up core device**.
2. Choose the option to set up one core device. Name it `MyPocketBeagle2` and select **Nucleus Lite**.
3. Create a dedicated thing group named `PocketBeagleDevices`, or add the device to that group if you created it separately. Do not use a group containing production devices.
4. Choose **Create thing**, then **Download connection kit**. Save it privately on your Ubuntu host that has the USB connection to the pocketbeagle2.

The above workflow creates the IoT thing, device certificate, IoT policy, token-exchange IAM role, and IoT role alias. If the console offers software installation commands, use the runtime already in the Yocto image and the bundled provisioning helper instead of installing another runtime.

## Prepare a credentials temp directory on pocketbeagle2

In an SSH shell on your pocketbeagle2, type:

```bash
cd $HOME
mkdir ./gg-provision
```

We will use this directory to temporarily store the credential kit prior to installation.

{{% notice Important Note %}}
Please delete this temporary directory after the configuration/provisioning of greengrass is complete. It will no longer be needed.
{{% /notice %}}

On the Ubuntu host, configure variables used throughout the remaining pages. Replace the sample Region if needed, and use an authenticated AWS CLI v2 profile:

```bash
export AWS_REGION=us-east-1
export THING_NAME=MyPocketBeagle2
export THING_GROUP=PocketBeagleDevices
aws sts get-caller-identity
aws iot list-thing-groups-for-thing --thing-name "$THING_NAME"
```

## Upload the connection kit to the pocketbeagle2

From the Ubuntu host connected to your pocketbeagle2, invoke a scp session to copy the connection kit to the pocketbeagle2:

```bash
scp MyPocketBeagle2-connectionKit.zip root@192.168.7.2:./gg-provision
```

{{% notice Important Note %}}

If your AWS account is restricted such that you get an error when pressing the **Create thing** button above, you may need to manually create your entire connection kit manually via the AWS CLI.  If this is the case then

## Optional - only if your organization requires a pre-approved role or permissions boundary

Most users can use the role created by the connection kit and do not need to configure a permissions boundary. If your administrator requires a pre-approved role, keep its boundary and follow the [manual provisioning guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md#manual-provisioning-by-creating-a-thing), reusing that role instead of creating one.

For a device-specific alias, point it to the approved role with this command, replacing both placeholders:

```bash
aws iot update-role-alias --role-alias YOUR_ROLE_ALIAS --role-arn YOUR_APPROVED_ROLE_ARN
```

Use `create-role-alias` with the same arguments if the alias does not exist. Your administrator must confirm the role's trust and certificate-policy permissions. Pass the alias **name** as `YOUR_ROLE_ALIAS` to the board's provisioning helper. After manual provisioning, continue with [Prepare the credentials](#prepare-the-credentials).

## Prepare the credentials

On your workstation, keep the connection kit or manually downloaded credentials in a private directory outside any source checkout. Extract the kit if you used one, and identify the device certificate, private key, and Amazon Root CA. Save copies with these filenames: `device.pem.crt`, `private.pem.key`, and `AmazonRootCA1.pem`. Do not confuse the device certificate with the CA certificate or public key.

Protect the key and transfer these three files to the board. Run from the directory containing those files:

```bash
chmod 600 private.pem.key
scp device.pem.crt private.pem.key AmazonRootCA1.pem \
    root@192.168.7.2:./gg-provision/
```

AWS CLI credentials stay on the administrative workstation. The board authenticates with its device private key and certificate.

The endpoints must match your recorded device settings. If you provisioned manually and the thing group does not exist, create it:

```bash
aws iot create-thing-group --thing-group-name "$THING_GROUP"
```

The group list must contain `PocketBeagleDevices`. If the thing is not a member, add it:

```bash
aws iot add-thing-to-thing-group --thing-name "$THING_NAME" \
    --thing-group-name "$THING_GROUP"
```

The command produces no output on success. Confirm membership before continuing:

```bash
aws iot list-thing-groups-for-thing --thing-name "$THING_NAME"
```

Lastly, lets get our iot data endpoint and iot credential endpoint values for our specific account. Back on the Ubuntu host type:

```bash
aws iot describe-endpoint --endpoint-type iot:Data-ATS
aws iot describe-endpoint --endpoint-type iot:CredentialProvider
```

Record the full `endpointAddress` from each command. It will be used in the next step. 

## Create the configuration yaml file

Lastly, we need to create the config file for our credentials bundle.  Create a file `config.yaml` with the following contents (replacing YOUR_IOT_DATA_ENDPOINT and YOUR_IOT_CRED_ENDPOINT with your actual endpoint url components from the previous command above). You may also need to update the `awsRegion` to reflect the region you wish to use:

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

Save and copy this file up with our other created key files to your pocketbeagle2 from your Ubuntu host:

```bash
scp config.yaml root@192.168.7.2:/root/gg-provision/
```

On your pocketbeagle2 via a SSH shell confirm that you have the following files created:

```bash
cd ~/gg-provision
ls -al
```

Your output should be:

```output
-rw-r--r-- 1 root root 1188 Oct 21 15:36 AmazonRootCA1.pem
-rw-r--r-- 1 root root  528 Oct 21 15:36 config.yaml
-rw-r--r-- 1 root root 1220 Oct 21 15:36 device.pem.crt
-rw-r--r-- 1 root root 1675 Oct 21 15:36 private.pem.key
```

Please continue with the next section editing the `config.yaml` in this directory on your pocketbeagle2 file per instructions below by skipping to the `Prepare the credentials config file` step below.
{{% /notice %}}

Inspect the downloaded configuration and record the thing name, Region, data endpoint, credential-provider endpoint, and role alias. Find the role alias in **Security > Role aliases** and record its associated IAM role name for troubleshooting token exchange. The inline Hello World component does not need an S3 permissions policy.

Confirm the device certificate is **ACTIVE**, attached to this thing, and has the generated IoT policy attached. That policy must allow the device's IoT/Greengrass communication and `iot:AssumeRoleWithCertificate` on the role alias ARN. The IAM role must trust `credentials.iot.amazonaws.com`. For troubleshooting each association, see the linked Nucleus Lite 2.6.0 provisioning guide.

## Prepare the credentials config file

From the Ubuntu host connected to your pocketbeagle2, open a SSH session:

```bash
ssh root@192.168.7.2
```

Unzip the contents of the connection kit (zipped and not already placed there manually):

```bash
cd $HOME
cd ./gg-provision
unzip ./MyPocketBeagle2-connectionKit.zip
```

Examine the `config.yaml` file:

```bash
cat ./config.yaml
```

The contents of the `config.yaml` file should look like this:

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

Replace `{{config_dir}}` with `/etc/greengrass` and `{{nucleus_component}}` with `aws.greengrass.NucleusLite`:

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
      iotRoleAlias: "GreengrassV2TokenExchangeCoreDeviceRoleAlias"
      iotDataEndpoint: "YOUR_IOT_DATA_ENDPOINT-ats.iot.us-east-1.amazonaws.com"
      iotCredEndpoint: "YOUR_IOT_CRED_ENDPOINT.credentials.iot.us-east-1.amazonaws.com"
```

Save the updated `config.yaml` file. 

## Finailize configuration of AWS IoT Greengrass

Continuing with the SSH session into the pocketbeagle2, copy all contents from our updated connection kit to the greengrass config directory already setup on your pocketbeagle2:

```bash
cd $HOME
cd ./gg-provision
cp * /etc/greengrass
chmod 640 /etc/greengrass/*key
chmod 640 /etc/greengrass/*pem
chmod 640 /etc/greengrass/*crt
chown ggcore:ggcore /etc/greengrass/*key /etc/greengrass/*pem /etc/greengrass/*crt
ls -al /etc/greengrass
```

The expected contents of `/etc/greengrass` should be:

```output
root@pocketbeagle2:~/gg-provision# ls -al /etc/greengrass
total 28
drwxr-xr-x  3 root   root   4096 Oct 22 19:32 .
drwxr-xr-x 48 root   root   4096 Oct 22 19:34 ..
-rw-r-----  1 ggcore ggcore 1188 Oct 22 19:35 AmazonRootCA1.pem
drwxr-xr-x  2 root   root   4096 Mar  9  2018 config.d
-rw-r--r--  1 root   root    540 Oct 22 19:35 config.yaml
-rw-r-----  1 ggcore ggcore 1220 Oct 22 19:35 device.pem.crt
-rw-r-----  1 ggcore ggcore 1675 Oct 22 19:35 private.pem.key
root@pocketbeagle2:~/gg-provision# 
```

Your pocketbeagle2's AWS IoT Greengrass configuration is now complete!  Restart the greengrass services on the pocketbeagle2:

```bash
systemctl restart greengrass-lite.target
systemctl status --with-dependencies greengrass-lite.target
```

Your pocketbeagle2's greengrass service should now be operational. 

## Verify the pocketbeagle2 greengrass operational status

On the board, inspect service health and connection logs:

```bash
systemctl status --with-dependencies greengrass-lite.target
systemctl --failed
journalctl -u ggl.core.iotcored.service -u ggl.core.ggdeploymentd.service -b --no-pager
```

The core services should be running without repeated certificate, authorization, or endpoint errors. On the Ubuntu host, query the registered core device:

```bash
aws greengrassv2 get-core-device --core-device-thing-name "$THING_NAME"
```

Your output should resemble this (may or may not be actual json depending on how you have the aws CLI configured on your Ubuntu host):

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

Wait for the device to appear under **Greengrass devices > Core devices** and report healthy connectivity. If it does not, check clock synchronization, outbound connectivity, certificate activation, IoT policy attachment, and Region consistency. An IoT thing's existence alone does not prove the Greengrass runtime connected.

## What you have accomplished

The board has a unique AWS identity and connects as a Greengrass core device. Next, publish an inline Hello World component for the device to run.
