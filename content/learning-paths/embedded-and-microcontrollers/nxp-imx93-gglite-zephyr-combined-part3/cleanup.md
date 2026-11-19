---
title: "NXP FRDM i.MX93: Remove the apps and verify cleanup" 
description: "Revise desired state and prove repeatable application-MCU cleanup."
weight: 8
layout: "learningpathall"
---

## Shutting down both applications via revised deployment

Retrieve the latest deployment ID again, since another change may have occurred. On the Ubuntu host:

```bash
aws greengrassv2 list-deployments --target-arn "$GROUP_ARN" --history-filter LATEST_ONLY
```

Set CURRENT_DEPLOYMENT_ID to the latest deployment ID found above:

```bash
export CURRENT_DEPLOYMENT_ID=YOUR_LATEST_GROUP_DEPLOYMENT_ID
```

Now, lets revise the deployment with an update effectively de-selecting both custom components:

```bash
aws greengrassv2 get-deployment --deployment-id "$CURRENT_DEPLOYMENT_ID" > current-deployment.json
python3 - <<'PYTHON'
import json,os
from pathlib import Path
current=json.loads(Path('current-deployment.json').read_text())
assert current['targetArn']==os.environ['GROUP_ARN']
components=current.get('components',{}).copy()
components.pop('com.arm.NXPIMX93.ZephyrExternalTemperature',None)
components.pop('com.arm.NXPIMX93.ExternalTemperatureBridge',None)
Path('remove-deployment.json').write_text(json.dumps({'targetArn':os.environ['GROUP_ARN'],'deploymentName':'Remove NXP FRDM i.MX 93 temperature apps','components':components},indent=2)+'\n')
PYTHON
export REMOVE_ID=$(aws greengrassv2 create-deployment   --cli-input-json file://remove-deployment.json --query deploymentId --output text)
aws greengrassv2 list-effective-deployments --core-device-thing-name "$THING_NAME"
aws greengrassv2 list-installed-components --core-device-thing-name "$THING_NAME"
```

Wait for this removal revision to succeed. 

## Confirming that the board has been cleaned up

Using the recorded run-unit names and work paths:

```bash
export FW_UNIT=`systemctl list-unit-files --type=service | grep NXPIMX93 | awk '{print $1}' | grep Zephyr`
export BRIDGE_UNIT=`systemctl list-unit-files --type=service | grep NXPIMX93 | awk '{print $1}' | grep Bridge`
journalctl -u "$FW_UNIT" -u "$BRIDGE_UNIT" -b --no-pager -n 100
nxp-mcore status
systemctl is-active "$FW_UNIT" "$BRIDGE_UNIT"
```

You should see that the application Cortex-M33 is now **offline**, prior firmware filename restored, normal quiescence/stop messages, inactive or removed component units, and no new IoTCore JSON messages being published in the MQTT test console.  

## Additional detail: To re-enable, invoke a redeployment adding the components back into the deployment itself

Reapply the saved `deployment.json` to re-enable both components to be listed as part of the revised deployment. Once successfully deployed, you should again see JSON temperature messages published into AWS IoTCore via the MQTT test client. 

## Additional detail: Optionally retire cloud resources

After removal from every target, delete the two recorded private component version ARNs with `aws greengrassv2 delete-component --arn VERSION_ARN`. Remove only their versioned S3 prefixes and delete the bucket only if dedicated and empty.

If no device still needs this path's supplemental policy and role permission:

```bash
aws iot detach-policy --policy-name NXPIMX93ExternalTemperaturePublish --target "$CERT_ARN"
aws iot delete-policy --policy-name NXPIMX93ExternalTemperaturePublish
aws iam delete-role-policy --role-name "$ROLE_NAME"   --policy-name NXPIMX93ExternalTemperatureArtifacts
```

## What you have learned

You can successfully enable and disable these two components via updated deployments. This feature provides an `on/off` management capability for the components and their associated apps (artifacts). In generalized lifecycle management of edge devices, this technique, along with updating S3 artifacts, revising component versions, and revising deployment references to component versions, are all used to manage the overall application and its lifecycle within the edge device.
