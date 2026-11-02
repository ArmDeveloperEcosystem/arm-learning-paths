---
title: "Deploy both components and verify live telemetry"
description: Preserve the existing group deployment, add both custom components, and observe real sensor JSON in AWS IoT Core.
weight: 7
layout: "learningpathall"
---

## Preserve the existing group selection

On the Ubuntu AWS workstation, retain the variables from the publishing page:

```bash
export GROUP_ARN=$(aws iot describe-thing-group --thing-group-name "$THING_GROUP" \
  --query thingGroupArn --output text)
aws iot list-things-in-thing-group --thing-group-name "$THING_GROUP"
aws greengrassv2 list-deployments --target-arn "$GROUP_ARN" --history-filter LATEST_ONLY
```

Confirm `MyPocketBeagle2` is a member. Save the current group deployment rather than replacing its component selection blindly. Set `BASE_DEPLOYMENT_ID` to the latest deployment ID just listed:

```bash
export BASE_DEPLOYMENT_ID=YOUR_LATEST_GROUP_DEPLOYMENT_ID
aws greengrassv2 get-deployment --deployment-id "$BASE_DEPLOYMENT_ID" \
  > previous-deployment.json
```

If Part 1's group has no deployment because it was never deployed, first complete Part 1. If its latest revision removes Hello World, an empty `components` object is valid. The following update preserves whichever components remain in that latest revision, including Hello World if retained:

```bash
python3 - <<'PYTHON'
import json, os
from pathlib import Path
base = json.loads(Path('previous-deployment.json').read_text())
assert base['targetArn'] == os.environ['GROUP_ARN']
components = base.get('components', {}).copy()
components['com.arm.PocketBeagle2.ZephyrExternalTemperature'] = {
    'componentVersion': '1.0.0'
}
components['com.arm.PocketBeagle2.ExternalTemperatureBridge'] = {
    'componentVersion': '1.0.0',
    'configurationUpdate': {'merge': json.dumps({'serialDevice': '/dev/ttyS7'})}
}
request = {
    'targetArn': os.environ['GROUP_ARN'],
    'deploymentName': 'PocketBeagle2 external temperature Part 3',
    'components': components
}
Path('deployment.json').write_text(json.dumps(request, indent=2) + '\n')
PYTHON
python3 -m json.tool deployment.json
```

Change `serialDevice` only if the board checks identified a different MAIN_UART0 device. The generated request is the complete desired selection for **this target**. Check other group memberships and direct thing deployments as well; each can independently request components or constrain versions.

## Deploy from the cloud

```bash
export DEPLOYMENT_ID=$(aws greengrassv2 create-deployment \
  --cli-input-json file://deployment.json --query deploymentId --output text)
aws greengrassv2 get-deployment --deployment-id "$DEPLOYMENT_ID"
aws greengrassv2 list-effective-deployments --core-device-thing-name "$THING_NAME"
aws greengrassv2 list-installed-components --core-device-thing-name "$THING_NAME"
```

Wait for this deployment ID to report `SUCCEEDED` on the device, and both version `1.0.0` components to report running. A group's `ACTIVE` deployment status alone is insufficient. In the console, the equivalent workflow is to revise the existing group's deployment, retain its other components, and add both custom component versions.

During delivery, Lite fetches the ELF, scripts, and wheels from S3, validates artifacts, runs each `install`, and starts its `run` unit. No manual `scp`, `pb2-m4 load`, board-side pip download, or separately enabled application service is part of deployment.

## Inspect the component units on the board

On the pocketbeagle2 via SSH as root:

```bash
systemctl list-units --all --type=service --no-pager | grep -F PocketBeagle2
pb2-m4 status
```
Output should resemble:

```output
ggl.com.arm.PocketBeagle2.ExternalTemperatureBridge.install.service loaded    active   exited  ExternalTemperatureBridge
ggl.com.arm.PocketBeagle2.ExternalTemperatureBridge.service         loaded    active   running ExternalTemperatureBridge
ggl.com.arm.PocketBeagle2.ZephyrExternalTemperature.install.service loaded    active   exited  ZephyrExternalTemperature
ggl.com.arm.PocketBeagle2.ZephyrExternalTemperature.service         loaded    active   running ZephyrExternalTemperature
device=/sys/class/remoteproc/remoteproc0 name=5000000.m4fss state=running firmware=pb2-gg-temperature-4a067009bc6f802a.elf
```

## Observe the AWS IoT Core messages

In the same account and Region, open **AWS IoT Core > MQTT test client**, subscribe to `ti/pocketbeagle2/temperature/external`, and wait for successive JSON messages. The console identity needs its own test-client permissions. Verify:

1. `thingName` identifies this board, `sensor` is `BMP280`, and `location` is `external`.
2. `sequence` and `mcuUptimeMs` advance, with a normal interval near five seconds.
3. The value is plausible for the external module's location. Gently warm the sensor package with a fingertip and observe the value rise, then recover after you release it.
4. Linux stays reachable, Greengrass stays healthy, and Hello World continues if retained.

Disconnect power before changing sensor wiring. After a powered-down sensor disconnection and subsequent redeployment, sensor reads should fail and no fabricated temperature messages should appear. Reconnect with power off, then repeat deployment. A missing-sensor test is optional; the real-temperature response and the removal test on the next page are required.

## Diagnose failures

| Symptom | Check |
| --- | --- |
| S3 artifact `AccessDenied` | Existing role alias points to the role with the new prefix-scoped S3 policy; bucket/key/Region, boundaries, and bucket encryption match |
| No matching platform | Manifest contains `os=linux`, `architecture=aarch64`, and `runtime=aws_nucleus_lite` |
| Offline pip install fails | All pinned wheels are declared artifacts; `awscrt` is AArch64 and compatible with Python 3.12/glibc |
| Firmware manager refuses to run | M4 is offline, no other loader owns it, and no stale ownership record remains |
| M4 running, no valid samples | Sensor model/address, 3.3 V pull-ups, GPIO ownership, P2.07-to-P1.32 jumper, correct UART, and UART diagnostics |
| IPC unauthorized | Bridge recipe access-control key, operation, and exact topic |
| IPC accepted but nothing in test client | Certificate `iot:Publish` policy, endpoint/account/Region, connection logs, and test-client subscription permissions |
| Stop times out | New ELF contains mailbox shutdown handling and WFI; no old heartbeat or second mailbox consumer is running |

For service and kernel errors, inspect `journalctl -u ggl.core.iotcored.service -b` and `dmesg`. Preserve error details before revising the deployment. A cloud status or a single log entry is not a substitute for observing real messages and completing the stop test.

## What you have learned

You have learned how to add both components to the existing thing-group deployment while retaining its other components. You can verify delivery on the board, inspect the component journals, observe changing BMP280 temperature in IoT Core, and diagnose failures along the sensor-to-cloud path.
