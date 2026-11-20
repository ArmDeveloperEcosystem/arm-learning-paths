---
title: "NXP FRDM i.MX 8M Plus: Deploy and verify Hello World"
description: "Publish and deploy the NXP FRDM i.MX 8M Plus Hello World component."
weight: 7
layout: "learningpathall"
---

## Deploy the Hello World custom component to our board

On the Ubuntu host, confirm group membership and retrieve the device group's ARN:

```bash
aws iot list-things-in-thing-group --thing-group-name "$THING_GROUP"
export GROUP_ARN=$(aws iot describe-thing-group \
  --thing-group-name "$THING_GROUP" --query thingGroupArn --output text)
aws greengrassv2 list-deployments --target-arn "$GROUP_ARN"
```

With AWS Greengrass `Lite`, we publish components to their associated device group. Only AWS Greengrass `Classic` allows publication of components to individual devices. 

The member list must include `MyNXPIMX8MPlus` - our devices IoTCore name. This tutorial expects a dedicated group with no previous deployment. If a deployment already exists, inspect it before continuing. A new deployment to the same target replaces that target's previous component selection, so retain any components that you still need. See [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html).

Lets create a Greengrass deployment document targeting the group ARN as our device utilizes Greengrass `Lite`:

```bash
python3 - <<'PYTHON'
import json
import os
from pathlib import Path

request = {
    "targetArn": os.environ["GROUP_ARN"],
    "deploymentName": "NXPIMX8MPlus Hello World group deployment",
    "components": {
        "com.arm.NXPIMX8MPlus.HelloGreengrassLiteWorld": {
            "componentVersion": "1.0.1"
        }
    }
}
Path("deployment.json").write_text(json.dumps(request, indent=2) + "\n")
PYTHON
export DEPLOYMENT_ID=$(aws greengrassv2 create-deployment \
  --cli-input-json file://deployment.json --query deploymentId --output text)
printf '%s\n' "$DEPLOYMENT_ID"
```

Keep this deployment ID. The deployment intentionally contains only the custom component; it uses the Lite runtime already installed in the image.

You can perform the same operation in the console by choosing **Greengrass devices > Deployments > Create**, selecting **Thing group**, choosing `NXPIMX8MPlusDevices` - our device group's name, and adding version `1.0.1` of `com.arm.NXPIMX8MPlus.HelloGreengrassLiteWorld`. Review the target and component version before choosing **Deploy**. Use either the CLI or console workflow once.

## Check delivery to this device

Inspect both the deployment and its effective status on the board:

```bash
aws greengrassv2 get-deployment --deployment-id "$DEPLOYMENT_ID"
aws greengrassv2 list-effective-deployments \
  --core-device-thing-name "$THING_NAME"
aws greengrassv2 list-installed-components \
  --core-device-thing-name "$THING_NAME"
```

The group deployment can remain `ACTIVE` to serve group members. That status alone does not prove installation on a particular board. Wait for the matching deployment ID to report `SUCCEEDED` in the effective deployments response, and for component version `1.0.1` to appear as running in the installed-components response. Cloud status updates can lag behind device execution.

## Observe the application on NXP FRDM i.MX 8M Plus

On the board via SSH, inspect deployment logs and find the component's systemd service:

```bash
journalctl -u ggl.core.ggdeploymentd.service -b --no-pager -n 100
systemctl list-units --all --type=service | grep -F HelloGreengrassLiteWorld | awk '{print $1}'
export COMPONENT_UNIT=`systemctl list-units --all --type=service | grep -F HelloGreengrassLiteWorld | awk '{print $1}'`
```

Use the exact unit name reported by `systemctl` to inspect the component. Replace `COMPONENT_UNIT` with that name:

```bash
systemctl status ${COMPONENT_UNIT}
```

You should see that the service is running normally. Next, type:

```bash
journalctl -u ${COMPONENT_UNIT} -b -f
```

For this command (which will be ongoing...) the output should contain this (with additional ones added every 60 seconds):

```output
Hello from Greengrass Lite on NXP FRDM i.MX 8M Plus!
Hello from Greengrass Lite on NXP FRDM i.MX 8M Plus!
```

The journal adds timestamps and service prefixes. Observe at least two messages about 60 seconds apart, then press **Ctrl+C** to stop following the journal. The component continues running.

Successful completion requires all three observations:

      - Our device, as an AWS IoTCore thing, belongs to the targeted AWS Greengrass group: NXPIMX8MPlusDevices
      - This deployment succeeds on the device, and 
      - The application's repeated message appears in the device journal. 
      

This proves our AWS Greengrass group deployment succeeded.

## Troubleshoot a failed deployment

| Symptom | What to check |
| --- | --- |
| No effective deployment | Same account and Region, correct group ARN, thing membership, and IoT connectivity |
| Authorization or token-exchange failure | Active certificate, attached IoT policy, role alias, and IAM role trust |
| No matching manifest | `uname -m` is `aarch64`, Linux is running, and the manifest selects `aws_nucleus_lite` |
| Component exits immediately | Component unit journal and the inline `run` lifecycle command |
| Edited YAML has no effect | Existing configuration database takes precedence; use supported configuration updates rather than resetting an established device |

For service-level faults, inspect `systemctl --failed` and the `ggl.core.iotcored.service` and `ggl.core.ggdeploymentd.service` journals. Correct the reported cause before retrying; do not create another identity to work around an authorization error.

## Optional: remove the test application

If you are continuing to Part 2, keep the board provisioned and Greengrass running. You can keep the Hello World component deployed for the later verification.

To stop the application through the same group target, revise the group's deployment to omit the Hello World component. This is accomplished on the Ubuntu host:

```bash
python3 - <<'PYTHON'
import json
import os
from pathlib import Path

Path("update-deployment.json").write_text(json.dumps({
    "targetArn": os.environ["GROUP_ARN"],
    "deploymentName": "Remove NXPIMX8MPlus Hello World test",
    "components": {}
}, indent=2) + "\n")
PYTHON
export DEPLOYMENT_ID=$(aws greengrassv2 create-deployment \
  --cli-input-json file://update-deployment.json --query deploymentId --output text)
printf '%s\n' "$DEPLOYMENT_ID"
```

Wait for this revision to succeed and confirm the application stops. If you added other components to the group deployment, retain them in the component selection. Canceling a deployment is not an uninstall operation.


Continue with [Part 2: Zephyr on NXP FRDM i.MX 8M Plus](/learning-paths/embedded-and-microcontrollers/nxp-imx8uplus-yocto-zephyr-part2/).

## What you have learned

You can publish AWS Greengrass custom components, like our Hello World component, to the AWS IoT things belonging to a specific AWS Greengrass group. You can inspect both the device and cloud status, as well as remove the test component through revised deployment publication.
