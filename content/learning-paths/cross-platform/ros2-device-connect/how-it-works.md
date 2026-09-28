---
title: Connect ROS 2 to Device Connect and call inspection RPCs
description: Learn the layered programming pattern behind the ros2-device-connect adapter, start it in D2D mode against a ROS 2 container, and call its ROS 2 inspection RPCs from a Python client.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The programming pattern: four layers around one ROS 2 command

The adapter doesn't add a new way to talk to ROS 2. It wraps the same `ros2` command you ran from your terminal in the setup section, one layer at a time. Each layer adds one thing to the layer beneath it:

| Layer | What it is | What it adds | Example |
|---|---|---|---|
| 1. ROS 2 command | A `ros2` CLI call run in the container from the host | The ROS 2 query itself | `docker exec ros2_test ... ros2 topic list` |
| 2. Python wrapper | `run_ros()` | The same command, called from Python and returning structured output | `run_ros("ros2 topic list")` |
| 3. RPC | An `@rpc` method on `Ros2InspectionMixin` | A named function that peers and agents can discover and call over the network | `get_ros_topics()` |
| 4. Device | A driver class run by `DeviceRuntime` | A device that bundles those RPCs and joins the network | `PuppyPiRos2Driver` |

Layer 1 is all you need when you have a shell on the machine. Layers 2 to 4 let a caller *without* shell access run the same query, safely and by name.

The code excerpts in this section are simplified to show the pattern. The full versions are in `ros2_common.py` and `puppypi_device.py` in the repository.

## Layer 1: run a ROS 2 command in the container

You've already used this layer. From the host, `docker exec` runs a `ros2` command inside the container after sourcing the ROS 2 environment:

```bash
docker exec ros2_test bash -lc 'source /opt/ros/humble/setup.bash && ros2 topic list'
```

```output
/chatter
/parameter_events
/rosout
```

Every RPC in this Learning Path ends up running a command like this one.

## Layer 2: wrap the command in Python

`run_ros()` in `ros2_common.py` builds that same `docker exec` command:

```python
def run_ros(command: str, timeout: float = 10.0) -> dict[str, Any]:
    script = f"source {ROS_SETUP} && source {WORKSPACE_SETUP} && {command}"
    return run(["docker", "exec", "-u", EXEC_USER, CONTAINER, "bash", "-lc", script], timeout=timeout)
```

The container name, user, and setup scripts come from environment variables, so the same function works with any ROS 2 container. It returns a dictionary with `ok`, `stdout`, and `stderr` instead of printed text, and a timeout stops a stalled ROS 2 command from hanging the adapter.

## Layer 3: expose the command as an RPC

`Ros2InspectionMixin` turns `run_ros()` calls into Device Connect RPCs. The `@rpc()` decorator is what makes a method discoverable and callable over the network:

```python
class Ros2InspectionMixin:
    @rpc()
    async def get_ros_topics(self, limit: int = 200, contains: str = "") -> dict[str, Any]:
        """List active ROS2 topics."""
        return lines(run_ros("ros2 topic list"), limit=limit, contains=contains)

    @rpc()
    async def get_topic_info(self, topic: str) -> dict[str, Any]:
        """Return read-only metadata for a specific ROS2 topic."""
        if not TOPIC_NAME_RE.fullmatch(topic):
            return {"ok": False, "error": "topic must match ^/[A-Za-z0-9_/]+$"}
        return run_ros(f"ros2 topic info {topic}")
```

This is also where you apply safety rules, because it's the boundary where remote input arrives. `get_ros_topics` caps and filters its output with the `lines()` helper. `get_topic_info` validates the topic name before it reaches a shell command.

The mixin provides six inspection RPCs in total, for nodes, topics, services, packages, interfaces, and topic info. They all follow the same pattern.

The table below shows how the Device Connect RPC names map back to the ROS 2 operations they run or wrap:

| Device Connect RPC | ROS 2 operation inside the container | Purpose |
|---|---|---|
| `get_ros_nodes()` | `ros2 node list` | List active ROS 2 nodes |
| `get_ros_topics()` | `ros2 topic list` | List active ROS 2 topics |
| `get_ros_services()` | `ros2 service list` | List active ROS 2 services |
| `get_ros_packages()` | `ros2 pkg list` | List installed ROS 2 packages |
| `get_ros_interfaces()` | `ros2 interface list` | List available ROS 2 message and service interfaces |
| `get_topic_info(topic)` | `ros2 topic info <topic>` | Inspect one topic after validating the topic name |
| `get_raw_image()` | Subscribe to `/image_raw`, then JPEG/base64 encode one frame | Expose a camera stream as a callable perception RPC |
| `run_action(action)` | Call `/puppy_control/runActionGroup` with an allowlisted action file | Run a pre-approved PuppyPi motion |
| `set_velocity(x, y, yaw_rate)` | Publish once to `/puppy_control/velocity` | Send a bounded PuppyPi velocity command |
| `stop()` | Publish a zero-velocity command | Stop PuppyPi motion |

Device Connect does not replace ROS 2. It wraps selected ROS 2 operations as discoverable, typed, remotely callable capabilities.

## Layer 4: build the device

The final layer is a driver class that inherits from both `Ros2InspectionMixin` and `DeviceDriver`. The mixin supplies the shared ROS 2 RPCs. `DeviceDriver` makes the class a Device Connect device, and you add any hardware-specific RPCs alongside the shared ones. The `rpi5` profile runs this driver from `puppypi_device.py`:

```python
class PuppyPiRos2Driver(Ros2InspectionMixin, DeviceDriver):
    device_type = os.getenv("DEVICE_TYPE", "quadruped")

    @rpc()
    async def echo(self, text: str) -> dict[str, str]:
        """Echo text for connectivity testing."""
        return {"echo": text}

    # get_status(), run_action(), set_velocity(), stop() ...


async def main() -> None:
    runtime = DeviceRuntime(driver=PuppyPiRos2Driver(), device_id=os.getenv("DEVICE_ID"))
    await runtime.run()
```

`DeviceRuntime` connects the driver to the messaging network and announces every `@rpc` method, both inherited and its own, to peers. To support new hardware, you write a new class at this layer. Layers 1 to 3 stay the same.

## Start the adapter

The `start_d2d.sh` launcher loads a profile, activates the `.venv` environment, sets D2D defaults (the Zenoh backend, TCP port 7447, and a device ID of `<profile>-d2d`), and runs the driver script that the profile names.

Open a terminal on your Arm-based Linux machine and start the adapter with the `rpi5` profile, pointing it at the `ros2_test` container:

```bash
cd ~/device_connect
DEVICE_PROFILE=rpi5 PROJECT_ROOT=$HOME/device_connect \
  ROS_CONTAINER=ros2_test WORKSPACE_SETUP=/opt/ros/humble/setup.bash \
  ./ros2-device-connect/start_d2d.sh
```

The inline variables override the values in `profiles/rpi5.env`. You need the `WORKSPACE_SETUP` override because the `rpi5` profile defaults to a robot workspace that doesn't exist in a plain `ros:humble` container.

The adapter stays in the foreground. Its log shows that it has joined the Zenoh network in D2D mode as `rpi5-d2d`:

```output
WARNING - Running in INSECURE mode (DEVICE_CONNECT_ALLOW_INSECURE=true). Do NOT use this in production!
INFO - Using ZENOH messaging backend
INFO - Driver connected: raspberry_pi
INFO - Subscribed to commands on device-connect.default.rpi5-d2d.cmd
INFO - D2D mode: skipping registry registration, using presence announcements
```

## Call the RPCs from a client

Open a second terminal on the same machine. In `~/device_connect`, create a file named `client.py`:

```python
import json

from device_connect_agent_tools import connect, discover
from device_connect_agent_tools.tools import invoke

DEVICE = "rpi5-d2d"

CALLS = [
    ("echo", {"text": "hello from arm"}),
    ("get_status", {}),
    ("get_ros_topics", {}),
    ("get_ros_packages", {"contains": "std_msgs"}),
    ("get_topic_info", {"topic": "/chatter"}),
    ("get_topic_info", {"topic": "bad;rm"}),
]

connect()

found = discover("device(*)")
print("discovered:", [d["device_id"] for d in found["results"]])

for function, params in CALLS:
    result = invoke(f"device({DEVICE}).function({function})", params=params)
    print(f"--- {function}", json.dumps(result, indent=2))
```

The client uses two calls from the agent tools. `discover("device(*)")` lists every device on the network, and `invoke()` calls one function on a named device using a `device(<id>).function(<name>)` selector. The client doesn't know about ROS 2 or Docker. It only sees the device and its RPCs.

Set the client's connection settings and run it:

```bash
cd ~/device_connect
export MESSAGING_BACKEND=zenoh
export ZENOH_CONNECT=tcp/127.0.0.1:7447
export DEVICE_CONNECT_DISCOVERY_MODE=d2d
export DEVICE_CONNECT_ALLOW_INSECURE=true
export TENANT=default
.venv/bin/python client.py
```

`ZENOH_CONNECT` points the client at the adapter's Zenoh endpoint. To reach the adapter from another machine on your LAN, replace `127.0.0.1` with the adapter host's IP address.

The output is similar to the following, shortened here for readability:

```output
discovered: ['rpi5-d2d']
--- echo {
  "success": true,
  "device_id": "rpi5-d2d",
  "function": "echo",
  "result": {
    "echo": "hello from arm"
  }
}
--- get_status {
  ...
  "result": {
    "device": "puppypi",
    "container": "ros2_test",
    "container_status": "running",
    "ros_ok": false,
    "ros_output": [
      "ROS_DISTRO=humble"
    ],
    ...
  }
}
--- get_ros_topics {
  ...
  "result": {
    "ok": true,
    "count": 3,
    "items": [
      "/chatter",
      "/parameter_events",
      "/rosout"
    ],
    "truncated": false,
    ...
  }
}
--- get_ros_packages {
  ...
  "result": {
    "ok": true,
    "count": 1,
    "items": [
      "std_msgs"
    ],
    ...
  }
}
--- get_topic_info {
  ...
  "result": {
    "ok": true,
    "topic": "/chatter",
    "stdout": "Type: std_msgs/msg/String\nPublisher count: 1\nSubscription count: 0\n",
    "stderr": ""
  }
}
--- get_topic_info {
  ...
  "result": {
    "ok": false,
    "error": "topic must match ^/[A-Za-z0-9_/]+$"
  }
}
```

Here's what each result shows:

- `echo` confirms the full round trip from the client over Zenoh to the adapter.
- `get_ros_topics` returns the same three topics you saw at layer 1. It's the same `ros2 topic list` command, reached through all four layers. `get_topic_info` adds the message type of `/chatter`.
- `get_ros_packages` shows the `contains` filter reducing the package list to `std_msgs`.
- The second `get_topic_info` call is rejected at layer 3, so no command runs in the container.
- `get_status` reports that the container is running ROS 2 Humble. `ros_ok` is `false` because this driver's health check looks for PuppyPi robot packages, which aren't in a plain `ros:humble` container. This is expected.

## Clean up

Stop the adapter with `Ctrl+C` in its terminal. If you started it in the background, stop it with:

```bash
pkill -f puppypi_device.py
```

The `ros2_test` container keeps running. When you no longer need it, remove it:

```bash
docker rm -f ros2_test
```

## What you've accomplished and what's next

You've learned the adapter's four-layer pattern: a ROS 2 command run in the container, a Python wrapper around it, an `@rpc` method that exposes it, and a driver class that inherits from `Ros2InspectionMixin` and `DeviceDriver` to bundle those RPCs into a device. You started the adapter in D2D mode and called its RPCs from a Python client that knows nothing about ROS 2.

Next, you'll see how other profiles reuse layers 1 to 3 with different layer 4 drivers for real hardware, such as a Raspberry Pi 5 with a camera.
