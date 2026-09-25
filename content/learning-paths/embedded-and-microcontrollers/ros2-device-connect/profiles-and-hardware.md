---
title: Use deployment profiles and try the adapter on real hardware
description: Learn how ros2-device-connect profiles select drivers for different hardware, and how to run the adapter on a Raspberry Pi 5 with a camera or on a ROS 2 robot.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How profiles select the hardware configuration

In the previous section, you overrode the `rpi5` profile to point at a generic ROS 2 container. Each profile in `profiles/` is a shell file that describes one deployment. It sets which driver runs, which container the driver talks to, and which ROS 2 setup scripts it sources.

| Profile | Driver | Default container | ROS 2 distribution | RPCs added to the shared inspection RPCs |
|---|---|---|---|---|
| `rpi5` | `puppypi_device.py` | `test` | Humble | The PuppyPi RPCs, which have no effect without a robot, so this profile works as a general test target |
| `rpi_camera` | `camera_device.py` | `pi_ros` | Jazzy | `get_raw_image(quality)` |
| `puppypi` | `puppypi_device.py` | `puppypi_ros2` | Humble | `run_action(action)`, `set_velocity(x, y, yaw_rate)`, `stop()` |

For example, `profiles/rpi_camera.env` contains:

```bash
export DEVICE_PROFILE="rpi_camera"
export PROJECT_ROOT="${PROJECT_ROOT:-${HOME}/device_connect}"
export VENV_DIR="${VENV_DIR:-.venv}"
export DEVICE_TYPE="${DEVICE_TYPE:-sentinel_camera}"
export DRIVER_SCRIPT="${DRIVER_SCRIPT:-camera_device.py}"
export ROS_CONTAINER="${ROS_CONTAINER:-pi_ros}"
export ROS_EXEC_USER="${ROS_EXEC_USER:-root}"
export ROS_SETUP="${ROS_SETUP:-/opt/ros/jazzy/setup.bash}"
export WORKSPACE_SETUP="${WORKSPACE_SETUP:-${ROS_SETUP}}"
```

Every value uses the `${VAR:-default}` form, so you can override any setting inline, as you did with `ROS_CONTAINER` and `WORKSPACE_SETUP`. For a new deployment, you can also point the launcher at your own profile file:

```bash
PROFILE_FILE=/path/to/my-robot.env ./ros2-device-connect/start_d2d.sh
```

## Try a Raspberry Pi 5 with a camera

The `rpi_camera` configuration is the lowest-risk real hardware example in this Learning Path. It exposes a sensor capability, not a motion capability: a ROS 2 image topic becomes a Device Connect RPC that any peer or agent can call for a photo. The caller does not need to know the ROS 2 topic name, QoS settings, camera container, or image encoding details.

The camera must appear as a V4L2 video device, such as `/dev/video0`. A USB webcam works without extra setup.

{{% notice Note %}}
Raspberry Pi Camera Modules connected by ribbon cable use the libcamera stack, and they don't always expose a frame-ready `/dev/video0` that `v4l2_camera` can read. If `v4l2_camera` can't read frames from your Pi Camera Module, start with a USB webcam, or set `VIDEO_DEVICE` to the video node your camera stack provides.
{{% /notice %}}

On the Raspberry Pi 5, set up the same `~/device_connect` workspace as in the setup section, then bring up the camera stack:

```bash
cd ~/device_connect
./ros2-device-connect/start_camera_ros2.sh
```

The `start_camera_ros2.sh` script is idempotent and does the following:

- creates a `ros:jazzy` container named `pi_ros` with the camera passed through using `--device=/dev/video0`
- installs `ros-jazzy-v4l2-camera`, `ros-jazzy-cv-bridge`, and `python3-opencv` inside the container
- copies `capture_frame.py` into the container and starts `v4l2_camera_node` in the background
- verifies that the `/image_raw` topic is being published

Start the adapter with the camera profile:

```bash
cd ~/device_connect
DEVICE_PROFILE=rpi_camera ./ros2-device-connect/start_d2d.sh
```

The device is announced as `rpi_camera-d2d`. It exposes the same inspection RPCs as before, plus `get_raw_image`:

```python
@rpc(labels={"category": "camera", "direction": "read", "safety": "informational"})
async def get_raw_image(self, quality: int = DEFAULT_JPEG_QUALITY) -> dict[str, Any]:
    ...
    result = run_ros(
        f"python3 {CAPTURE_SCRIPT_PATH} --topic {CAMERA_TOPIC} "
        f"--timeout {CAPTURE_TIMEOUT_S} --quality {quality_int}",
        timeout=CAPTURE_EXEC_TIMEOUT_S,
    )
```

The RPC runs `capture_frame.py` inside the container. The script subscribes to `/image_raw`, takes one frame, and returns it as a base64-encoded JPEG. It subscribes with ROS 2's `qos_profile_sensor_data` because `v4l2_camera` publishes with best-effort QoS. A subscriber that uses the default reliable QoS would never match the publisher, and the capture would silently time out.

This is the perception side of the robotics pattern: a ROS 2 sensor stream is converted into a typed Device Connect capability. The PuppyPi profile below uses the same pattern for the action side of robotics.

From a client, call the RPC and save the image. Use the same client environment variables as in the previous section, replacing `127.0.0.1` with the Raspberry Pi's IP address if you run the client on another machine:

```python
import base64
from device_connect_agent_tools import connect
from device_connect_agent_tools.tools import invoke

connect()
reply = invoke("device(rpi_camera-d2d).function(get_raw_image)", params={"quality": 80})
with open("capture.jpg", "wb") as f:
    f.write(base64.b64decode(reply["result"]["jpeg_base64"]))
```

The repository's `view_image.py` script does the same thing against a device in fabric mode.

## Try a ROS 2 robot

The `puppypi` profile targets a [Hiwonder PuppyPi quadruped](https://www.hiwonder.com/products/puppypi), a small four-legged robot built around Raspberry Pi-class hardware and a ROS 2 control stack. In this Learning Path, PuppyPi serves as the real robot example: the same Device Connect adapter pattern used for camera perception is extended to selected locomotion capabilities.

It shows how you can add motion control safely:

- `run_action` accepts only a fixed allowlist of pre-recorded moves, such as `sit`, `stand`, and `wave`, and rejects any other value.
- `set_velocity` rejects out-of-range values instead of clamping them.
- `stop` publishes a zero-velocity command.

Robot bring-up includes starting `puppy_control` and enabling servo torque. For those steps and the full safety model, see the [ros2-device-connect README](https://github.com/odincodeshen/ros2-device-connect#startup-checklist).

The important design point is that the adapter does not expose arbitrary ROS 2 control. It turns a reviewed subset of the robot's ROS 2 graph into Device Connect capabilities: read-only diagnostics, allowlisted actions, bounded velocity, and an explicit stop command.

## Build a profile for your own ROS 2 system

To connect a different ROS 2 system, follow the same pattern:

1. Create a driver class that combines `Ros2InspectionMixin` with `DeviceDriver`, and add only the hardware-specific RPCs you've reviewed.
2. Validate every caller-supplied value before it reaches `run_ros()`, as `get_topic_info` and `get_raw_image` do.
3. Add a `profiles/<name>.env` file that sets `DRIVER_SCRIPT`, `ROS_CONTAINER`, `ROS_EXEC_USER`, `ROS_SETUP`, and `WORKSPACE_SETUP`.

When the device needs to be reachable beyond your local network, run `start_fabric.sh` instead of `start_d2d.sh` with a device credentials file. This connects the device through a Device Connect server rather than Zenoh D2D discovery. For more information, see [Deploy multi-network device meshes using Device Connect server and NATS](/learning-paths/embedded-and-microcontrollers/device-connect-server/).

{{% notice Warning %}}
D2D mode runs with `DEVICE_CONNECT_ALLOW_INSECURE=true` and no transport authentication. Anyone on the same network segment can discover the device and call its RPCs. Use D2D mode only on a trusted network, and add authentication before you expose motion-control RPCs such as `set_velocity` on a less trusted network.
{{% /notice %}}

## What you've learned

In this Learning Path, you:

- learned how the ros2-device-connect adapter makes an unchanged ROS 2 system discoverable and callable through Device Connect, by wrapping ROS 2 CLI calls in `@rpc` methods run with `docker exec`
- set up a ROS 2 Humble container and the Device Connect Python packages on an Arm-based Linux machine
- ran the adapter in D2D mode and called read-only inspection RPCs from a Python client, including one call rejected by input validation
- saw how profiles reuse the same shared core for a Raspberry Pi 5 camera and a ROS 2 robot, and how to add a profile for your own hardware

To go further, try driving the adapter from an AI agent with [Connect AI agents to edge devices using Device Connect and Strands](/learning-paths/embedded-and-microcontrollers/device-connect-strands/), or build a larger ROS 2 workload on Arm with [Build a ROS 2 and Zenoh simulation environment on an Arm server](/learning-paths/cross-platform/ros2-zenoh-arm/).
