---
title: Update the application and check its output
description: Change one motion-detection threshold, rerun the ROS 2 node, compare the observed behavior, and stop the VP.
weight: 5
layout: learningpathall
---

## Update the application and check its output

The first run used `DEFAULT_THRESHOLD = 8.0`. Preserve its log and program before editing:

In the **Zena guest**, run:

```bash
podman logs zena-motion-detector > /root/zena-ros-camera/results/motion-before.log
cp /root/zena-ros-camera/motion_event.py /root/zena-ros-camera/motion_event.before.py
```

Use your guest text editor to change this line in `/root/zena-ros-camera/motion_event.py`:

```python
DEFAULT_THRESHOLD = 2.0
```

The lower threshold marks smaller differences between adjacent frames as motion. Confirm that this is the only program change and that Python accepts the edited file:

```bash
diff -u /root/zena-ros-camera/motion_event.before.py /root/zena-ros-camera/motion_event.py
python3 -m py_compile /root/zena-ros-camera/motion_event.py
```

The expected diff changes `DEFAULT_THRESHOLD` from `8.0` to `2.0`. The tested source passed the syntax check.

### Run the updated node

Remove the old detector container and start a new one that reads the edited file from the guest directory. Keep `zena-camera-publisher` running:

```bash
podman rm -f zena-motion-detector
podman run -d --name zena-motion-detector --net=host --ipc=container:zena-camera-publisher -v /root/zena-ros-camera:/work:rw localhost/zena-ros-camera:jazzy bash -lc 'source /opt/ros/jazzy/setup.bash ; exec python3 /work/motion_event.py'
podman logs --tail 10 zena-motion-detector
```

The log should report `threshold=2.0` and then continue recording `frame` and `mean_delta`. Check a message from the new node:

```bash
podman exec -it zena-motion-detector bash
source /opt/ros/jazzy/setup.bash
ros2 topic echo /motion --once
exit
```

One observed response was:

```output
data: true
---
```

`ros2 topic echo /motion --once` receives one result, so you can check that the new node still delivers Bool data. An individual value depends on the current video frame. Save the updated node log in the **Zena guest**:

```bash
podman logs zena-motion-detector > /root/zena-ros-camera/results/motion-after.log
```

Compare the saved logs to see how the lower threshold changes the motion events. The video can be at different positions during the two runs, so event counts are not an accuracy metric or a controlled performance comparison.

### Stop the application and virtual platform

In the **Zena guest**, stop the application and camera publisher, then stop the guest camera bridge:

```bash
podman stop zena-motion-detector zena-camera-publisher
systemctl stop virtualcam-bridge@1.service
```

In ANA Lab Manager, stop the VP. This stops the virtual platform after you have saved the application source and logs.

## What you have learned

You have updated a ROS 2 application in the Zena VP, checked that the new process publishes results, and preserved the before and after logs. This demonstrates an application development loop in the virtual platform; it does not predict physical-silicon performance or motion-detection accuracy.
