---
title: Launch the Device Connect dashboard
description: Start the MAPPO model server, simulated device driver, and browser dashboard on the Arm cloud instance.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Forward the dashboard port

The dashboard has no login. Keep it bound to the cloud instance's loopback interface and use SSH port forwarding instead of exposing it to the internet.

Open another terminal on your local computer and connect to the cloud instance. Replace the username and address with your SSH details:

```bash
ssh -N -o ExitOnForwardFailure=yes \
    -L 8080:127.0.0.1:8080 \
    ubuntu@<cloud-instance-address>
```

Keep this SSH connection open while you use the dashboard.

## Start the dashboard services

Return to the SSH terminal where you set `ACTOR_OUTPUT`, `MAPPO_DEMO`, and `DASHBOARD_PACKAGE`. Start the dashboard without `--allow-motion`:

```bash
cd "$MAPPO_DEMO"
./dashboard/start-dashboard.sh \
    --python "$HOME/venvs/mappo-dashboard/bin/python" \
    --package "$DASHBOARD_PACKAGE" \
    --models-dir "$(dirname "$ACTOR_OUTPUT")"
```

The launcher starts three processes:

- The model server publishes the `.npz` files in the actor export directory
- The simulated driver exposes model-management functions through Device Connect
- The web server presents the fleet and checkpoint controls in your browser

The output ends with lines similar to:

```output
http://127.0.0.1:8080
fleet       sim
motion      DISABLED (status and checkpoints only).
Ctrl-C stops all three.
```

{{% notice Note %}}
The launcher deliberately leaves motion disabled. The simulated device is sufficient to validate the model distribution and selection workflow.
{{% /notice %}}

## Open the dashboard

On your local computer, open [the forwarded Device Connect dashboard](http://127.0.0.1:8080/) in a browser.

The following screenshot shows the dashboard's complete multi-robot layout. Use it to locate the **Fleet**, **Checkpoints on the robot**, and **Load from Cloud AI** panels. It was captured from a different, motion-enabled demonstration, so its header states **MOTION ENABLED** and **MESH DOWN**.

![Arm Device Connect dashboard showing the robot fleet, motion controls, camera feed, installed MAPPO checkpoints, and Cloud AI model source. Use the Fleet and checkpoint panels as interface landmarks; this screenshot comes from a different demonstration with motion enabled and the mesh disconnected.#center](images/device-connect-dashboard.webp "Arm Device Connect dashboard interface reference")

{{% notice Warning %}}
Don't reproduce the motion state shown in the screenshot. Your simulation-only session must show **MESH UP** and **MOTION DISABLED** before you continue.
{{% /notice %}}

Confirm that the interface shows:

- **MESH UP** in the header
- `mappo-sim` with a **LIVE** state in the **Fleet** table
- **MOTION DISABLED** in the header
- `mappo-sim` selected under **Focus**

The fleet row proves that the browser server discovered the simulated driver through the Device Connect mesh. The header also confirms that this run cannot issue motion commands.

## What you've accomplished

You have started the model server, Device Connect driver, and dashboard without exposing an unauthenticated port or enabling motion. Next, you will load and arm your exported actor through the dashboard.
