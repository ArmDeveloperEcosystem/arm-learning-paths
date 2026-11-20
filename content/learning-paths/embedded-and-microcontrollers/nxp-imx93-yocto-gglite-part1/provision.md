---
title: "NXP FRDM i.MX 93 Dev Board : Provision Greengrass Lite" 
description: "Initialize this board with a unique certificate and its existing NXP runtime."
weight: 5
layout: "learningpathall"
---

## Create our board's AWS IoTCore/Greengrass identity

On the Ubuntu host via web browser, log into the AWS console and use the one account and Region throughout this board's series. In **AWS IoT Core → Greengrass devices → Core devices → Set up core device**, select **Nucleus Lite**, create `MyNXPIMX93`, and use the dedicated thing group `NXPIMX93Devices`. Select `Set up a device with your own custom build` and press `Create thing` to create the new device in AWS IoTCore. Next, download the connection kit to your Ubuntu host. Our board and its Yocto image already has the Greengrass Lite package installed and ready to provision.


```bash
export AWS_REGION=us-east-1
export THING_NAME=MyNXPIMX93
export THING_GROUP=NXPIMX93Devices
aws sts get-caller-identity
aws iot list-thing-groups-for-thing --thing-name "$THING_NAME"
```

## Upload the connection kit to the iMX93 dev board

From the Ubuntu host connected to your iMX93 dev board, invoke a scp session to copy the connection kit to the iMX93 dev board:

```bash
scp MyNXPIMX93-connectionKit.zip root@OUR_BOARD_IP_ADDRESS:./gg-provision
```

{{% notice Important Note %}}

If your AWS account is restricted such that you get an error when pressing the **Create thing** button above, you may need to manually create your entire connection kit manually via the AWS CLI.  If this is the case then

## Optional - only if your organization requires a pre-approved role or uses permissions boundary

Most users can use the role created by the connection kit and do not need to configure a permissions boundary. If your administrator requires a pre-approved role, keep its boundary and follow the [manual provisioning guide](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.3.0/docs/Provisioning.md#manual-provisioning-by-creating-a-thing), reusing that role instead of creating one.

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
    root@OUR_BOARD_IP_ADDRESS:./gg-provision/
```

AWS CLI credentials stay on the administrative workstation. The board authenticates with its device private key and certificate.

The endpoints must match your recorded device settings. If you provisioned manually and the thing group does not exist, create it:

```bash
aws iot create-thing-group --thing-group-name "$THING_GROUP"
```

The group list must contain `NXPIMX93Devices`. If the thing is not a member, add it:

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
  thingName: "MyNXPIMX93"
services:
  {{nucleus_component}}:
    componentType: "NUCLEUS"
    configuration:
      awsRegion: "us-east-1"
      iotRoleAlias: "GreengrassV2TokenExchangeCoreDeviceRoleAlias"
      iotDataEndpoint: "YOUR_IOT_DATA_ENDPOINT-ats.iot.us-east-1.amazonaws.com"
      iotCredEndpoint: "YOUR_IOT_CRED_ENDPOINT.credentials.iot.us-east-1.amazonaws.com"
```

Save and copy this file up with our other created key files to your imx93 dev board from your Ubuntu host:

```bash
scp config.yaml root@OUR_BOARD_IP_ADDRESS:/root/gg-provision/
```

On your imx93 dev board via a SSH shell confirm that you have the following files created:

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

Please continue with the next section editing the `config.yaml` in this directory on your imx93 dev board file per instructions below by skipping to the `Prepare the credentials config file` step below.
{{% /notice %}}

## Prepare the credentials config file

From the Ubuntu host connected to your imx93 dev board, open a SSH session:

```bash
ssh root@OUR_BOARD_IP_ADDRESS
```

Unzip the contents of the connection kit (zipped and not already placed there manually):

```bash
cd $HOME
cd ./gg-provision
unzip ./MyNXPIMX93-connectionKit.zip
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
  thingName: "MyNXPIMX93"
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
  thingName: "MyNXPIMX93"
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

Continuing with the SSH session into the imx93 dev board, copy all contents from our updated connection kit to the greengrass config directory already setup on your imx93 dev board:


```bash
cd $HOME/gg-provision
cp * /etc/greengrass
rm /etc/greengrass/*.zip
chmod 640 /etc/greengrass/*key
chmod 640 /etc/greengrass/*pem
chmod 640 /etc/greengrass/*crt
chown -R ggcore:ggcore /etc/greengrass
ls -al /etc/greengrass
```

The expected contents of `/etc/greengrass` should be:

```output
root@imx93 dev board:~/gg-provision# ls -al /etc/greengrass
total 28
drwxr-xr-x  3 ggcore ggcore 4096 Oct 22 19:32 .
drwxr-xr-x 48 root   root   4096 Oct 22 19:34 ..
-rw-r-----  1 ggcore ggcore 1188 Oct 22 19:35 AmazonRootCA1.pem
drwxr-xr-x  2 ggcore ggcore 4096 Mar  9  2018 config.d
-rw-r--r--  1 ggcore ggcore  540 Oct 22 19:35 config.yaml
-rw-r-----  1 ggcore ggcore 1220 Oct 22 19:35 device.pem.crt
-rw-r-----  1 ggcore ggcore 1675 Oct 22 19:35 private.pem.key
root@imx93 dev board:~/gg-provision# 
```

Your imx8plus dev board's AWS IoT Greengrass configuration is now complete!  Restart the greengrass services on the imx8plus dev board:

```bash
python3 /usr/libexec/nxp-lp/check-greengrass.py
gg_units="$(python3 /usr/libexec/nxp-lp/check-greengrass.py --units)" &&
    systemctl add-wants greengrass-lite.target $gg_units &&
    systemctl enable greengrass-lite.target &&
    systemctl restart greengrass-lite.target
systemctl status --with-dependencies greengrass-lite.target
```

Your iMX93 dev board's greengrass service should now be operational. 

## Additional details: The Greengrass services

The pinned image uses Greengrass Lite **2.3.0**. Token exchange service is
`ggl.core.tesd.service` (`tesd`), and fleet status service is
`ggl.core.gg-fleet-statusd.service` (`gg-fleet-statusd`).

The image deliberately leaves services disabled until credentials exist. The
commands above validate all 12 executables and 19 core units, attach every core
service/socket to the target, then start it. Restarting an empty target alone
does not activate its disabled members. The provisioning helper performs the
same complete-runtime check and activation when used instead of manual setup.

## Verify the imx8plus dev board greengrass operational status

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
    "coreDeviceThingName": "MyNXPIMX93",
    "coreVersion": "2.3.0",
    "platform": "linux",
    "architecture": "aarch64",
    "status": "HEALTHY",
    "lastStatusUpdateTimestamp": 1792697816.549,
    "tags": {}
}
```

Wait for the device to appear under **Greengrass devices > Core devices** and report healthy connectivity. If it does not, check clock synchronization, outbound connectivity, certificate activation, IoT policy attachment, and Region consistency. An IoT thing's existence alone does not prove the Greengrass runtime connected.

## What you have accomplished

The board has a unique AWS IoTCore identity and connects as a Greengrass core device. Next, we will publish a simple Hello World Greengrass custom component for the device to run.