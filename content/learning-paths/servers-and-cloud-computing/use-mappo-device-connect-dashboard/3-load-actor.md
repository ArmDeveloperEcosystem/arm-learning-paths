---
title: Load and validate the MAPPO actor
description: Use the dashboard to download the exported actor, arm it for the simulated device, and run an inference smoke test.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Browse the model source

The launcher advertises the local model server to the simulated device. The browser asks the device to browse that source, so the request follows the same Device Connect path used by a remote deployment.

In the **Load from Cloud AI** panel, confirm that **Source** shows **local checkpoint server — local model server**. Select **Browse** if the actor list hasn't appeared automatically.

The actor list shows your `.npz` filename and the message **served by mappo-model-server**. This response confirms that the simulated device can reach the model source.

## Load the actor onto the simulated device

Select **Use** beside your exported actor. Its address appears in the first **Source** field.

Enter `trained_mappo_actor_part2.npz` in **Install as**. The new name prevents a collision if the disposable package already contains a checkpoint with the exporter's default filename.

Select **Load onto robot**. In this simulation-only workflow, the destination is the disposable policy package rather than physical hardware.

The result reports these checks:

```output
loaded trained_mappo_actor_part2.npz
sha256         <actor checksum>
rays           12
trained range  0.35
runnable now   yes

Not armed. Arm it in the table above when you want the next run to use it.
```

The filename and checksum depend on your actor. Don't continue unless the result says `runnable now   yes`.

## Arm the actor

Find the downloaded actor in **Checkpoints on the robot**. It should have the **ready** state.

Select **Arm** beside the actor. The state changes to **armed**, and the **Armed checkpoint** column in the fleet row shows the same filename.

Loading and arming are separate operations. The dashboard inspects a downloaded file before it changes `model_path`, and an armed model takes effect only when the next policy process starts.

Press the **E** key to open the event drawer. Look for the `model downloaded` and `checkpoint armed` events. These events record both changes made through Device Connect.

## Stop the dashboard

Return to the cloud SSH terminal running `start-dashboard.sh` and press **Ctrl+C**. The launcher stops the model server, simulated driver, and web server together.

The output names each process as it stops:

```output
stopping checkpoint server
stopping driver
stopping dashboard
```

## Run an inference smoke test

The disposable policy package now points to the actor you armed. Run its installation check:

```bash
source "$HOME/venvs/mappo-dashboard/bin/activate"
python "$DASHBOARD_PACKAGE/basic_test.py"
```

The output identifies your checkpoint and ends with:

```output
checkpoint       trained_mappo_actor_part2.npz
trained on       1910000 frames, 3 agents
ActionOutput(...)
PASS
```

The action values depend on your actor. `PASS` confirms that the policy package loaded the armed arrays, constructed an 18-value observation, and completed one inference step.

## What you've accomplished

You have served an exported MAPPO actor, transferred it through Device Connect, armed it in a disposable policy package, and validated inference. The complete workflow used a simulated device and did not connect to or move physical hardware.
