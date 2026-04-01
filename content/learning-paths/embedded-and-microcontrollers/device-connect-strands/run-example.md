---
title: Run the example end to end
weight: 4

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

You'll run Device Connect's device-to-device discovery in this section. There are two ways to walk through this setup, with an option to connect an external device. 

### Option 1: run on a single machine

For a proof-of-concept, follow the steps using two terminal windows on your machine with the virtual environment set up.

### Option 2: run with real hardware

If you have access to an external device, you can use it with this setup as well. You'll need:

- Your machine with the virtual environment set up (referred to as the host)
- A Raspberry Pi (or any similar device) connected to the same network as your host machine (referred to as the target) 
- An SSH connection or keyboard and monitor attached to the target.

You'll need two terminal windows open at the same time: one to keep the simulated robot running, and one to invoke it from the agent side. Both terminals need the virtual environment activated.

| Machine | Terminal | Purpose |
|---------|----------|---------|
| Host or Target | 1 | Simulated robot - keep running throughout |
| Host | 2 | Agent tool invocations |

Make sure you are in the repository directory and that your virtual environment is activated:

```bash
cd ~/strands-device-connect/robots
source .venv/bin/activate
```

## Start the simulated robot

In terminal 1, run the following command to create and start the simulated SO-100 robot arm:

```python
python <<'PY'
import logging
logging.basicConfig(level=logging.INFO)
from strands_robots import Robot
r = Robot('so100')
r.run()
PY
```

When you create the `Robot('so100')` object, the SDK downloads the MuJoCo physics model for the SO-100 arm (on first run only, taking a minute or two). The SDK then starts the simulation and registers the robot on the Device Connect device mesh. The robot publishes a presence heartbeat every 0.5 seconds under a unique device ID, for example `so100-abc123`.

You should see INFO-level log output similar to:

```output
device_connect_sdk.device.so100-abc123 - INFO - Using ZENOH messaging backend
device_connect_sdk.device.so100-abc123 - INFO - Connected to ZENOH broker: []
device_connect_sdk.device.so100-abc123 - INFO - Driver connected: strands_sim
device_connect_sdk.device.so100-abc123 - INFO - Subscribed to commands on device-connect.default.so100-abc123.cmd
🤖 so100-abc123 is online. Ctrl+C to stop.
```

Leave this process running. The simulated robot becomes discoverable only while this process runs.

## Control the robot using the robot_mesh Strands tool

The `robot_mesh` tool wraps the same discovery and invocation primitives as a Strands agent tool. You can call it directly from a Python script or attach it to an LLM agent; the API is identical either way.

### Discover available robots on the device mesh

Start by confirming which robots are currently visible on the mesh:

```python
python <<'PY'
from strands_robots.tools.robot_mesh import robot_mesh
print(robot_mesh(action='peers'))
PY
```

The output is similar to:

```output
Discovered 1 device(s):
  [robot] so100-abc123 - idle
    Functions: execute, getFeatures, getStatus, reset, step, stop
```

Each run assigns a new peer ID at startup (for example `so100-abc123`). Note the actual ID shown in your terminal - you'll need it in the next step.

### Execute an instruction

Send a task to one of the discovered robots. Replace `so100-abc123` with the peer ID shown in your `peers` output:

```python
python <<'PY'
from strands_robots.tools.robot_mesh import robot_mesh
print(robot_mesh(
    action='tell',
    target='so100-abc123',
    instruction='pick up the cube',
    policy_provider='mock',
))
PY
```

You'll see output similar to:

```output
-> so100-abc123: pick up the cube
  {"status": "success", "content": [...]}
```

{{% notice Robot output in terminal 1 %}}
The robot logs event updates as it processes the task. Switch back to terminal 1 to see execution logs similar to:

```output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*** EVENT so100-abc123::stateUpdate [111aaabb]
    payload: sim_time=4.34, step_count=2070, running_policies={'so100': {'steps': 814, 'instruction': 'pick up the cube'}}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
{{% /notice %}}


### Broadcast emergency stop to all devices

The emergency stop broadcasts a halt command to every device on the mesh simultaneously. Use this when you want to stop all robots without knowing their individual peer IDs:

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

## Optional: discover and invoke the robot using the agent tools

The `device-connect-agent-tools` package gives you direct programmatic access to the mesh without involving an LLM. Use this for testing, scripting, or validating the stack before wiring it up to an agent. Open terminal 2, activate the virtual environment, then run:

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
    print(f'Execute result: {result}')

    status = invoke_device(devices[0]['device_id'], 'getStatus')
    print(f'Status: {status}')
PY
```

{{% notice About the snippet %}}
When an agent calls `execute(instruction="pick up the cup", policy_provider="groot")`, Device Connect handles the RPC delivery, and the policy handles the actual arm movement.

`discover_devices(device_type='')` returns all devices on the mesh regardless of type. If you pass `device_type='strands_robot'` you can filter to only `Robot()` instances. `invoke_device` sends an RPC to the named device; here `policy_provider='mock'` tells the robot to accept the task without executing real motion, which is appropriate for this connectivity test.
{{% /notice %}}


The output is similar to:

```output
Found 1 robot(s):
  so100-abc123 - idle
Execute result: {'success': True, 'result': {'status': 'success', 'content': [...]}}
Status: {'success': True, 'result': {...}}  # full sim state dict
```

## What you've learned and what's next

In this section you've:

- Started a simulated SO-100 robot that registered itself on the Device Connect device mesh
- Used `device-connect-agent-tools` to discover the robot and invoke an RPC call against it
- Used the `robot_mesh` Strands tool to list peers, send an instruction, and trigger an emergency stop

You've now seen how to set up a mesh on a local network. The next section extends the configuration to a Docker-based approach, opening up new possibilities for agent integration.