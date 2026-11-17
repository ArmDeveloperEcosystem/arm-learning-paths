---
title: "Deploy to the thing group and verify Hello World"
description: Deploy the Hello World component to PocketBeagle 2 through an AWS IoT thing group and verify execution in the device journal.
weight: 7
layout: "learningpathall"
---

## Deploy to the group

On the Ubuntu host, confirm group membership and retrieve the group's ARN:

```bash
aws iot list-things-in-thing-group --thing-group-name "$THING_GROUP"
export GROUP_ARN=$(aws iot describe-thing-group \
  --thing-group-name "$THING_GROUP" --query thingGroupArn --output text)
aws greengrassv2 list-deployments --target-arn "$GROUP_ARN"
```

The member list must include `MyPocketBeagle2`. This tutorial expects a dedicated group with no previous deployment. If a deployment already exists, inspect it before continuing. A new deployment to the same target replaces that target's previous component selection, so retain any components that you still need. See [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html).

Create a deployment document targeting the group ARN, rather than the individual thing ARN:

```bash
python3 - <<'PYTHON'
import json
import os
from pathlib import Path

request = {
    "targetArn": os.environ["GROUP_ARN"],
    "deploymentName": "PocketBeagle2 Hello World group deployment",
    "components": {
        "com.arm.HelloGreengrassLiteWorld": {
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

You can perform the same operation in the console by choosing **Greengrass devices > Deployments > Create**, selecting **Thing group**, choosing `PocketBeagle2HelloWorld`, and adding version `1.0.1` of `com.arm.HelloGreengrassLiteWorld`. Review the target and component version before choosing **Deploy**. Use either the CLI or console workflow once.

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

## Observe the application on PocketBeagle 2

On the pocketbeagle2 board via SSH shell, inspect deployment logs and find the component's systemd service:

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
Hello from Greengrass Lite on PocketBeagle2!
Hello from Greengrass Lite on PocketBeagle2!
```

The journal adds timestamps and service prefixes. Observe at least two messages about 60 seconds apart, then press **Ctrl+C** to stop following the journal. The component continues running.

Successful completion requires all three observations: the thing belongs to the target group, this deployment succeeds on the device, and the application's repeated message appears in the device journal. This proves a cloud group deployment reached the runtime and executed the inline lifecycle command.

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

To stop the application through the same group target, revise the group's deployment to omit the component. This is accomplished on the Ubuntu host:

```bash
python3 - <<'PYTHON'
import json
import os
from pathlib import Path

Path("update-deployment.json").write_text(json.dumps({
    "targetArn": os.environ["GROUP_ARN"],
    "deploymentName": "Remove PocketBeagle2 Hello World test",
    "components": {}
}, indent=2) + "\n")
PYTHON
export DEPLOYMENT_ID=$(aws greengrassv2 create-deployment \
  --cli-input-json file://update-deployment.json --query deploymentId --output text)
printf '%s\n' "$DEPLOYMENT_ID"
```

Wait for this revision to succeed and confirm the application stops. If you added other components to the group deployment, retain them in the component selection. Canceling a deployment is not an uninstall operation.

## What you have accomplished

You built a Yocto image for an Arm board, provisioned its Greengrass identity, published a custom component, and verified execution after a thing group deployment. To extend the exercise, replace the message loop with a sensor application, publish a new component version, and revise the group deployment to select it.

Continue with [Part 2: run Zephyr on the PocketBeagle 2 MCU](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-zephyr-part2/) to add a real-time application alongside Linux.
