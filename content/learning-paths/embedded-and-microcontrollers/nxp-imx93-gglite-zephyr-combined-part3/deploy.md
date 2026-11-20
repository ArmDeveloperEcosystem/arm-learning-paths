---
title: "NXP FRDM i.MX93: Deploy both components and verify temperature"
description: "Preserve the group selection and observe actual BMP280 JSON in IoT Core."
weight: 7
layout: "learningpathall"
---

## Preserve the latest group deployment

On the Ubuntu host in `$HOME/nxp-imx8uplus-temperature-part3`, retain the variables from the previous section:

```bash
export GROUP_ARN=$(aws iot describe-thing-group --thing-group-name "$THING_GROUP"   --query thingGroupArn --output text)
aws iot list-things-in-thing-group --thing-group-name "$THING_GROUP"
aws greengrassv2 list-deployments --target-arn "$GROUP_ARN" --history-filter LATEST_ONLY
```

Set `BASE_DEPLOYMENT_ID` to the latest deployment ID just listed:

```bash
export BASE_DEPLOYMENT_ID=YOUR_LATEST_GROUP_DEPLOYMENT_ID
aws greengrassv2 get-deployment --deployment-id "$BASE_DEPLOYMENT_ID" \
  > previous-deployment.json
```

Create the deployment now:

```bash
python3 - <<'PYTHON'
import json,os
from pathlib import Path
base=json.loads(Path('previous-deployment.json').read_text())
assert base['targetArn']==os.environ['GROUP_ARN']
components=base.get('components',{}).copy()
version=json.loads(Path('release.json').read_text())['version']
components['com.arm.NXPIMX93.ZephyrExternalTemperature']={'componentVersion':version}
components['com.arm.NXPIMX93.ExternalTemperatureBridge']={'componentVersion':version,'configurationUpdate':{'merge':json.dumps({'serialDevice':'/dev/nxp-temperature'})}}
Path('deployment.json').write_text(json.dumps({'targetArn':os.environ['GROUP_ARN'],'deploymentName':'NXP FRDM i.MX 93 BMP280 telemetry','components':components},indent=2)+'\n')
PYTHON
export DEPLOYMENT_ID=$(aws greengrassv2 create-deployment   --cli-input-json file://deployment.json --query deploymentId --output text)
aws greengrassv2 list-effective-deployments --core-device-thing-name "$THING_NAME"
aws greengrassv2 list-installed-components --core-device-thing-name "$THING_NAME"
```

Wait for this deployment to succeed on this device and for both components to run. You can view the deployment progress on the AWS Console if desired. 

## Examine events on the board

After deployment fully completes on our board, we should see that our MCU is active and that we have new device files for temperature and MCU control:

```bash
nxp-mcore status
systemctl list-units --all --type=service --no-pager | grep -F NXPIMX93
journalctl -u ggl.core.ggdeploymentd.service -b --no-pager -n 100
ls -l /dev/nxp-temperature /dev/nxp-mcore-control
```

Lets check the status on each of the services for our two apps:

```bash
export FW_UNIT=`systemctl list-unit-files --type=service | grep NXPIMX93 | awk '{print $1}' | grep Zephyr`
export BRIDGE_UNIT=`systemctl list-unit-files --type=service | grep NXPIMX93 | awk '{print $1}' | grep Bridge`
export FW_WORK=$(systemctl show "$FW_UNIT" --property=WorkingDirectory --value)
export BRIDGE_WORK=$(systemctl show "$BRIDGE_UNIT" --property=WorkingDirectory --value)
journalctl -u "$FW_UNIT" -u "$BRIDGE_UNIT" -b -f
```
Expect FRDM Linux preflight `PASS` lines before remoteproc start, then `MCore started firmware=...` and bridge `Published sequence=... topic=nxp/imx93/temperature/external` messages. Do not run `cat` on the telemetry endpoint concurrently with the bridge. Press Ctrl+C to stop journal following; the applications keep running.

## Observe the external sensor in AWS

In **AWS IoT Core → MQTT test client**, subscribe to `nxp/imx93/temperature/external` using the same account/Region. Verify `thingName=MyNXPIMX93Device`, `sensor=BMP280`, advancing sequence/uptime, and plausible temperature. Gently warm the external module and observe the value change and recover.

A deployment status and journal entry do not replace a real observed message. Complete the removal/redeployment test on the next page.


## Additional detail: Observe the external sensor in AWS

| Failure | Inspect |
| --- | --- |
| S3 denied | Actual UTC/time source and diagnostic error code, then device role, prefix policy, bucket/Region, boundaries and encryption |
| Offline wheel install fails | Actual board Python version and AArch64 wheels declared in the recipe |
| MCU owner refuses startup | Correct image profile, offline core, and no stale owner record |
| RPMsg endpoints missing | Resource-table patch, vring/memory agreement, mailbox, cache settings and RPMSG_TTY |
| No sensor frames | BMP280 chip/address, board-specific bus/pins, pull-ups, and peripheral ownership |
| IPC denied | Recipe operation and exact topic policy |
| Nothing in IoT Core | Certificate publish permission, endpoint/Region and subscriber permissions |

## What you have learned

You can deploy the two Greengrass components, verify operations, and confirm a real external temperature JSON response in AWS IoT Core.
