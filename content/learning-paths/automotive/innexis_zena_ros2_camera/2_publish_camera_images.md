---
title: Publish virtual camera frames to ROS 2
description: Start a camera publisher and check the type, metadata, and arrival rate of the ROS 2 image topic.
weight: 3
layout: learningpathall
---

## Publish virtual camera frames to ROS 2

In the **Zena guest**, start the camera publisher as a background container:

```bash
podman run -d --name zena-camera-publisher --net=host --device=/dev/video0 localhost/zena-ros-camera:jazzy bash -lc 'source /opt/ros/jazzy/setup.bash ; exec ros2 run image_tools cam2image'
```

`--device=/dev/video0` gives the container access to the guest camera. `--net=host` lets ROS 2 use the guest network. `ros2 run image_tools cam2image` starts the publisher that reads the camera and emits `/image`.

### Inspect the image topic

Enter the running publisher container and load the ROS 2 environment:

```bash
podman exec -it zena-camera-publisher bash
source /opt/ros/jazzy/setup.bash
```

List the available topics and their message types:

```bash
ros2 topic list -t
```

Look for this line in the output:

```output
/image [sensor_msgs/msg/Image]
```

This shows that ROS 2 discovered the image topic. Next, inspect its endpoints:

```bash
ros2 topic info /image -v
```

The relevant fields in the reference run were:

```output
Type: sensor_msgs/msg/Image
Publisher count: 1
Node name: cam2image
Endpoint type: PUBLISHER
QoS profile:
  Reliability: RELIABLE
```

Check that `cam2image` is publishing `/image`. This command also shows subscriber endpoints and QoS settings; the subscriber count can change as you run later steps. To confirm that a reader can receive a frame, request one message without printing its pixel array:

```bash
ros2 topic echo /image --once --no-arr
```

Selected fields from the received message were:

```output
  frame_id: camera_frame
height: 480
width: 640
encoding: bgr8
step: 1920
```

The 640 × 480 dimensions and `bgr8` encoding describe the delivered ROS 2 image. Finally, measure how frequently a subscriber receives messages:

```bash
ros2 topic hz /image
```

For example, the reference VP session reported:

```output
average rate: 27.185
average rate: 27.528
```

Your rate can differ. This is the ROS 2 message arrival rate in the VP, not a physical camera performance result. After several reports, press **Ctrl+C** to stop `ros2 topic hz`. Run `exit` to leave the container shell; the background publisher remains active.

### ROS 2 command reference

| Command | What it tells you |
| --- | --- |
| `ros2 topic list -t` | Shows discoverable topic names and message types. Look for `/image [sensor_msgs/msg/Image]`. |
| `ros2 topic info /image -v` | Shows the publisher, subscriber, and QoS endpoints for `/image`. |
| `ros2 topic echo /image --once --no-arr` | Receives one image message and displays its metadata without printing the pixel array. Check `width`, `height`, `encoding`, `step`, and `frame_id`. |
| `ros2 topic hz /image` | Subscribes to the image topic and reports its arrival rate. This checks message delivery to a ROS 2 reader, not the physical camera's performance. |

## What you have learned

You have checked both the ROS 2 image topic and actual message delivery from the virtual camera. Next, subscribe to those images from an application node.
