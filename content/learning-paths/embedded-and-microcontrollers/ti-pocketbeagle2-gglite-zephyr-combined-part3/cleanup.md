---
title: "Cleaning up our deployment"
description: Revise desired deployment state, verify that firmware, bridge, and AWS IoTCore telemetry stop, and optionally try a clean redeployment to re-enable them.
weight: 8
layout: "learningpathall"
---

## Remove the application through deployment state

First, on the Ubuntu host, lets ensure we have the `jq` app installed:

```bash
sudo apt install -y jq
```

Now, again the Ubuntu host, retrieve the **latest** deployment for this group again. Then, we revise the deployment and remove the two components that are referenced within the deployment:

```bash
export CURRENT_DEPLOYMENT_ID=`aws greengrassv2 list-deployments --target-arn "$GROUP_ARN" --history-filter LATEST_ONLY | jq -r '.deployments[].deploymentId'`
aws greengrassv2 get-deployment --deployment-id "$CURRENT_DEPLOYMENT_ID" \
  > current-deployment.json
python3 - <<'PYTHON'
import json, os
from pathlib import Path
current = json.loads(Path('current-deployment.json').read_text())
assert current['targetArn'] == os.environ['GROUP_ARN']
components = current.get('components', {}).copy()
components.pop('com.arm.PocketBeagle2.ZephyrExternalTemperature', None)
components.pop('com.arm.PocketBeagle2.ExternalTemperatureBridge', None)
Path('remove-deployment.json').write_text(json.dumps({
    'targetArn': os.environ['GROUP_ARN'],
    'deploymentName': 'Remove PocketBeagle2 Part 3 temperature applications',
    'components': components
}, indent=2) + '\n')
PYTHON
export REMOVE_ID=$(aws greengrassv2 create-deployment \
  --cli-input-json file://remove-deployment.json --query deploymentId --output text)
aws greengrassv2 list-effective-deployments --core-device-thing-name "$THING_NAME"
aws greengrassv2 list-installed-components --core-device-thing-name "$THING_NAME"
```

Wait for `REMOVE_ID` to succeed. If another group deployment, a direct thing deployment, a local deployment, or another component dependency still requests either component, remove that request too. The two Part 3 recipes do not keep each other installed through dependencies. Canceling a deployment, deleting a component version, deleting the core-device cloud record, or merely removing thing-group membership does not provide this controlled teardown.

## Check the actual stop behavior

On PocketBeagle 2, in the SSH session retaining `FW_UNIT`, `BRIDGE_UNIT`, and the work paths:

```bash
pb2-m4 status
```

You should see a `state=offline` indicating that the zephyr app has been halted. 

On the AWS console, you should be able to confirm, via inspection, that your Greengrass deployment now has zero components associated with it.  This indicates that the deployment is empty and thus the removal was successful. 

## Prove the firmware can be deployed again

Either via the CLI or via the AWS console, the deployment can be `re-filled` with the two custom components that we created. Upon selecting both components and deploying the updated deployment, the pocketbeagle2 should start sending telemetry once again into IoTCore. 

If using the CLI, the required lifecycle acceptance test is **deploy → remove → deploy → remove**, without a board reset between these steps. Reapply the saved `deployment.json` only if its retained component selection is still current:

```bash
aws greengrassv2 create-deployment --cli-input-json file://deployment.json
```

Wait for both components to run again and observe new sensor messages. Then create a fresh removal revision using the latest deployment and repeat the cleanup checks. Successful repetition proves the new firmware handles the stop protocol and that the runtime can reinstall from artifacts. If this test fails, treat the integration as incomplete; do not describe a timeout, reset, or forced driver unbind as a successful component uninstall.

## What you have learned

You have learned how to remove both applications through revised deployment state and verify that the M4 stops, the bridge closes its resources, and installed application files are removed. You can test redeployment without rebooting, recognize an abnormal termination that needs recovery, and retire this path's cloud resources while preserving the Part 1 setup.
