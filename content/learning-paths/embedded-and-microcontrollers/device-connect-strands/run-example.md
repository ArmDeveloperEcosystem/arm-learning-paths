---
title: Run the example end to end
weight: 4

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This section runs entirely on your local machine using Device Connect's device-to-device discovery. You will need two terminal windows open at the same time: one to keep the simulated robot running, and one to invoke it from the agent side. Both terminals need the virtual environment activated.

| Terminal | Purpose |
|----------|---------|
| 1 | Simulated robot — keep running throughout |
| 2 | Agent tool invocations |

Make sure you are in the workspace directory you created during setup and that your virtual environment is activated:

```bash
cd ~/strands-device-connect
source .venv/bin/activate
```

## Start the simulated robot

In terminal 1, run the following command to create and start the simulated SO-100 robot arm:

```python
python <<'PY'
import logging
logging.basicConfig(level=logging.INFO)
from strands_robots import Robot
Robot('so100')
PY
```

When the `Robot('so100')` object is created, the SDK downloads the MuJoCo physics model for the SO-100 arm (this download happens only on the first run and takes a minute or two), then starts the simulation and registers the robot on the Device Connect device mesh. The robot publishes a presence heartbeat every 0.5 seconds under a unique device ID, for example `so100_sim-abc123`.

You should see INFO-level log output similar to:

```output
INFO:strands_robots.mesh:Zenoh session started
INFO:strands_robots.mesh:Peer ID: so100_sim-abc123
INFO:strands_robots.mesh:Heartbeat thread started
```

Leave this process running. The simulated robot is only discoverable as long as this process is alive.

## Discover and invoke the robot using the agent tools

The `device-connect-agent-tools` package gives you direct programmatic access to the mesh, without involving an LLM. This is useful for testing, scripting, or validating the stack before wiring it up to an agent. Open terminal 2, activate the virtual environment, then run:

```python
python <<'PY'
from device_connect_agent_tools import connect, discover_devices, invoke_device

connect()

devices = discover_devices(device_type='')
print(f'Found {len(devices)} robot(s):')
for d in devices:
    print(f'  {d["device_id"]}')

if devices:
    result = invoke_device(
        devices[0]['device_id'],
        'execute',
        {'instruction': 'pick up the cube', 'policy_provider': 'mock'},
    )
    print(f'Result: {result}')
PY
```

`discover_devices(device_type='')` returns all devices on the mesh regardless of type. If you pass `device_type='strands_robot'` you can filter to only `Robot()` instances. `invoke_device` sends an RPC to the named device; here `policy_provider='mock'` tells the robot to accept the task without executing real motion, which is appropriate for this connectivity test.

The output is similar to:

```output
Found 1 robot(s):
  so100_sim-abc123
Result: {'success': True, 'result': {'status': 'accepted'}}
```

## Control the robot using the robot_mesh Strands tool

The `robot_mesh` tool wraps the same discovery and invocation primitives as a Strands agent tool. You can call it directly from a Python script or attach it to an LLM agent; the API is identical either way.

### List peers

Start by confirming which robots are currently visible on the mesh:

```python
python <<'PY'
from strands_robots.tools.robot_mesh import robot_mesh
print(robot_mesh(action='peers'))
PY
```

The output is similar to:

```output
Found 2 robot(s):
  so100_sim-abc123 — idle
  so100_sim-def456 — idle
```

The peer ID (for example `so100_sim-abc123`) is assigned at startup and changes each run. Note the actual ID shown in your terminal - you will need it in the next step.

### Execute an instruction

Send a task to one of the discovered robots. Replace `so100_sim-abc123` with the peer ID shown in your `peers` output:

```python
python <<'PY'
from strands_robots.tools.robot_mesh import robot_mesh
print(robot_mesh(
    action='tell',
    target='so100_sim-abc123',
    instruction='pick up the cube',
    policy_provider='mock',
))
PY
```

You will see the following output:

```output
Result: {'success': True, 'result': {'status': 'success', 'content': [{'text': "🚀 Policy started on 'so100' (async)"}]}}
```

{{% notice Robot output in terminal 1 %}}
The robot also logs event updates as it processes the task. If you switch back to terminal 1, it logs the execution of the task, similar to:

```output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*** EVENT so100_sim-abc123::stateUpdate [111aaabb]
    payload: sim_time=4.34, step_count=2070, running_policies={'so100': {'steps': 814, 'instruction': 'pick up the cube'}}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
{{% /notice %}}


### Emergency stop

The emergency stop broadcasts a halt command to every device on the mesh simultaneously. This is useful when you want to stop all robots without knowing their individual peer IDs:

```python
python <<'PY'
from strands_robots.tools.robot_mesh import robot_mesh
print(robot_mesh(action='emergency_stop'))
PY
```

The output is similar to:

```output
E-STOP: 1/1 devices stopped
```

## What you've accomplished and what's next

In this section you:

- Started a simulated SO-100 robot that registered itself on the Device Connect device mesh.
- Used `device-connect-agent-tools` to discover the robot and invoke an RPC call against it.
- Used the `robot_mesh` Strands tool to list peers, send an instruction, and trigger an emergency stop.

This showcases the ease of setting up a mesh on a local network. In the next section, you can optionally set up a Raspberry Pi or any other device, opening up a new category of possibilites with agent integration.