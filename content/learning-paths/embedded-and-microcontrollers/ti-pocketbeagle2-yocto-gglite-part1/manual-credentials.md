---
hide_from_navpane: true
title: "Create Greengrass credentials without a connection kit"
description: Manually create AWS IoT credentials and a Greengrass nucleus lite configuration for PocketBeagle 2 when a connection kit is unavailable.
layout: "learningpathall"
---

## Create Greengrass credentials manually 

Create credentials manually if you can't download a connection kit from the AWS IoT console. After creating the credentials and configuration file, finish setting up the board.

## Prepare the host and board

On the host computer, set the AWS Region, thing name, and thing group name. Use an authenticated AWS CLI v2 profile:

```bash
export AWS_REGION=us-east-1
export THING_NAME=MyPocketBeagle2
export THING_GROUP=PocketBeagleDevices
aws sts get-caller-identity
ssh root@192.168.7.2 'mkdir -p "$HOME/gg-provision"'
```

Check that the AWS CLI uses the account that you expect. The board temporarily stores the credentials in `gg-provision` until you install them.

## Create the AWS IoT resources

To create resources, follow [Manual Provisioning by Creating a Thing](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md#manual-provisioning-by-creating-a-thing) in the Greengrass nucleus lite provisioning guide. You'll create an IAM role, an IoT role alias, an IoT policy, and a thing with a certificate.

When you finish, you have the following resources ready:

- A device certificate and private key
- The Amazon Root certificate authority (CA) certificate
- The thing name, Region, and role alias name

### (Optional) Use a pre-approved role

If your administrator requires a pre-approved role with a permissions boundary, use that role instead of creating one. Keep its boundary.

To point a device-specific alias at the approved role, replace both placeholders in the following command:

```bash
aws iot update-role-alias --role-alias YOUR_ROLE_ALIAS --role-arn YOUR_APPROVED_ROLE_ARN
```

If the alias doesn't exist, run `create-role-alias` with the same arguments. Your administrator needs to confirm the trust and certificate-policy permissions of the role. In `config.yaml`, set `iotRoleAlias` to the alias name, not its Amazon Resource Name (ARN).

## Copy the credentials to the board

On the host computer, keep the credentials in a private directory outside any source checkout. Identify the device certificate, the private key, and the Amazon Root CA certificate. Save copies with these file names: `device.pem.crt`, `private.pem.key`, and `AmazonRootCA1.pem`. Don't confuse the device certificate with the CA certificate or the public key.

Restrict the private key permissions, then copy the three files to the board. Run the commands from the directory that holds the files:

```bash
chmod 600 private.pem.key
scp device.pem.crt private.pem.key AmazonRootCA1.pem \
    root@192.168.7.2:./gg-provision/
```

AWS CLI credentials stay on the host computer. The board authenticates with its device private key and certificate.

## Add the thing to the thing group

If the thing group doesn't exist, create it:

```bash
aws iot create-thing-group --thing-group-name "$THING_GROUP"
```

If the thing isn't a member of `PocketBeagleDevices`, add it to the group:

```bash
aws iot add-thing-to-thing-group --thing-name "$THING_NAME" \
    --thing-group-name "$THING_GROUP"
```
The command produces no output on success.

Confirm membership in the group before you continue:

```bash
aws iot list-thing-groups-for-thing --thing-name "$THING_NAME"
```

## Get the endpoints

On the host computer, get the AWS IoT data endpoint and credential provider endpoint for your account:

```bash
aws iot describe-endpoint --endpoint-type iot:Data-ATS
aws iot describe-endpoint --endpoint-type iot:CredentialProvider
```

Record the full `endpointAddress` value from each command.

## Create the configuration file

Create a file named `config.yaml` with the following contents:

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

Replace `YOUR_IOT_DATA_ENDPOINT` and `YOUR_IOT_CRED_ENDPOINT` with the full endpoint addresses. Set `iotRoleAlias` to your role alias name, and set `awsRegion` to your Region.

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

## What you've accomplished and what's next

You've manually created AWS IoT Greengrass credentials for the PocketBeagle 2.

Next, continue with [Check the identity in AWS](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/provision/#check-the-identity-in-aws). 
