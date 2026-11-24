---
title: "Deploy to the thing group and verify Hello World"
description: Deploy the Hello World component to PocketBeagle 2 through an AWS IoT thing group and verify execution in the device journal.
weight: 7
layout: "learningpathall"
---

## Deploy to the group

After creating the Hello World component, deploy it to the thing group. 

On the host computer, confirm that the board belongs to the thing group. Get the Amazon Resource Name (ARN) of the group:

```bash
aws iot list-things-in-thing-group --thing-group-name "$THING_GROUP"
export GROUP_ARN=$(aws iot describe-thing-group \
  --thing-group-name "$THING_GROUP" --query thingGroupArn --output text)
aws greengrassv2 list-deployments --target-arn "$GROUP_ARN"
```

Ensure that the member list includes `MyPocketBeagle2`. Use a dedicated group with no previous deployment. If a deployment already exists, inspect it before continuing. 

{{% notice Note %}}
A new deployment to the same target replaces the previous component selection of that target. Keep any components that you still need. For more information, see [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) in the AWS documentation.
{{% /notice %}}

Create a deployment document targeting the group ARN, rather than the individual thing ARN. You can use either the AWS CLI or the console

To create a deployment using the CLI, run:

```bash
python3 - <<'PYTHON'
import json
import os
from pathlib import Path

request = {
    "targetArn": os.environ["GROUP_ARN"],
    "deploymentName": "PocketBeagle 2 Hello World group deployment",
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

Keep the deployment ID for use in subsequent commands. The deployment contains only the Hello World component, because the Greengrass nucleus lite runtime is already installed in the image.

To create a deployment in the console:

1. Select **Greengrass devices**, then select **Deployments** and **Create**.
2. Select **Thing group**.
3. Select `PocketBeagleDevices`.
4. Add version `1.0.1` of `com.arm.HelloGreengrassLiteWorld`. 
5. Review the target and component version, then select **Deploy**. 


## Check delivery to the board

On the host computer, check the deployment and its effective status on the board:

```bash
aws greengrassv2 get-deployment --deployment-id "$DEPLOYMENT_ID"
aws greengrassv2 list-effective-deployments \
  --core-device-thing-name "$THING_NAME"
aws greengrassv2 list-installed-components \
  --core-device-thing-name "$THING_NAME"
```

The group deployment can remain `ACTIVE`, because it keeps serving group members. That status alone doesn't prove installation on a particular board.

In the `list-effective-deployments` output, find the entry whose `deploymentId` matches `$DEPLOYMENT_ID`. Its `coreDeviceExecutionStatus` is `SUCCEEDED` when the board applied the deployment. In the `list-installed-components` output, `com.arm.HelloGreengrassLiteWorld` version `1.0.1` has a `lifecycleState` of `RUNNING`. Cloud status updates can lag behind the board, so repeat the commands after a minute if needed.

## Observe the application on the board

From the host computer, open an SSH session to the board:

```bash
ssh root@192.168.7.2
```

On the board, inspect the deployment logs and find the systemd service of the component:

```bash
journalctl -u ggl.core.ggdeploymentd.service -b --no-pager -n 100
systemctl list-units --all --type=service | grep -F HelloGreengrassLiteWorld
```

The first column of the `systemctl` output is the unit name. Save it in a variable. If the command lists more than one unit, set the variable to the unit that runs the component:

```bash
export COMPONENT_UNIT=$(systemctl list-units --all --type=service | grep -F HelloGreengrassLiteWorld | awk '{print $1}')
systemctl status "$COMPONENT_UNIT"
```

The service is `active (running)`. 

Follow its journal:

```bash
journalctl -u "$COMPONENT_UNIT" -b -f
```

The command keeps running and follows the log. 

The output is similar to:

```output
Hello from Greengrass nucleus lite on PocketBeagle 2!
Hello from Greengrass nucleus lite on PocketBeagle 2!
```

There's a new message every 60 seconds.

The journal adds timestamps and service prefixes. Wait for at least two messages about 60 seconds apart, then press **Ctrl+C** to stop following the journal. The component continues running.

To ensure that the component ran successfully, confirm the following details:

- The thing belongs to the target group
- This deployment succeeds on the device
- The repeated message of the application appears in the device journal

This proves that a cloud group deployment reached the runtime and ran the inline lifecycle command.

## Troubleshoot a failed deployment

If the deployment fails, check the following information to troubleshoot it:

| Symptom | What to check |
| --- | --- |
| No effective deployment | Same account and Region, correct group ARN, thing membership, and IoT connectivity |
| Authorization or token-exchange failure | Active certificate, attached IoT policy, role alias, and IAM role trust |
| No matching manifest | `uname -m` is `aarch64`, Linux is running, and the manifest selects `aws_nucleus_lite` |
| Component exits immediately | Component unit journal and the inline `run` lifecycle command |
| Edited YAML has no effect | Existing configuration database takes precedence, so use supported configuration updates rather than resetting an established device |

For service-level faults, inspect `systemctl --failed`, as well as the `ggl.core.iotcored.service` and `ggl.core.ggdeploymentd.service` journals. Correct the reported cause before retrying. Don't create another identity to work around an authorization error.

## (Optional) Remove the test application

To stop the application through the same group target, revise the group deployment to omit the component:

```bash
python3 - <<'PYTHON'
import json
import os
from pathlib import Path

Path("update-deployment.json").write_text(json.dumps({
    "targetArn": os.environ["GROUP_ARN"],
    "deploymentName": "Remove PocketBeagle 2 Hello World test",
    "components": {}
}, indent=2) + "\n")
PYTHON
export DEPLOYMENT_ID=$(aws greengrassv2 create-deployment \
  --cli-input-json file://update-deployment.json --query deploymentId --output text)
printf '%s\n' "$DEPLOYMENT_ID"
```

Wait for this revision to report `SUCCEEDED`, then confirm that the application stops. If you added other components to the group deployment, keep them in the component selection. Canceling a deployment doesn't uninstall a component.

## What you've accomplished

You deployed the component and verified that it ran successfully.

To extend the Learning Path, you can replace the message loop with a sensor application. Publish a new component version, and revise the group deployment to select it.
