---
title: Measure Zenoh traffic policy effects with real Wi-Fi
weight: 5

description: Measure Zenoh policy effects on ROS 2 sensor traffic between an Arm server and a Raspberry Pi over Wi-Fi.

layout: learningpathall
---

## Connect the Raspberry Pi over Wi-Fi

In the first experiment, you used the Docker network and the `robot` and `control` containers to emulate a wireless link. You'll now connect your Raspberry Pi to the same Wi-Fi network as the Arm server. You'll use the real Wi-Fi connection to test the same policy changes as the first experiment.

Using a 2.4 GHz Wi-Fi connection makes the effects clearer. To connect your Raspberry Pi as a Zenoh client, follow the Raspberry Pi connection procedure in [Distribute a ROS 2 robotic system across Arm devices with Zenoh](/learning-paths/cross-platform/distributed-ros2-zenoh-lp2/3-connect-the-raspberry-pi/).

## Restore the router configuration

Before starting, return the router configuration to a clean state. Open `~/container_data/ROUTER_CONFIG.json5` in a terminal within the `robot` container desktop and ensure the following:

- Set `transport/unicast/compression/enabled` to `false`
- Keep `access_control`, `downsampling`, and `qos` commented out

Restart the router on the `robot` container desktop after saving the file. Confirm that the emulated link is no longer active:

```bash
just network_normal
```

Use the physical wireless link for this experiment. Don't run `just network_limit`.

## Record an untuned baseline 

Open three SSH sessions to the Raspberry Pi. In each session, open a bash shell in the `pi_edge` container and source ROS 2:

```bash
docker exec -it pi_edge /bin/bash
source /opt/ros/jazzy/setup.bash
```

Run one receiver command in each bash shell that has been opened in the `pi_edge` container:

```bash
ros2 topic hz /scan
```

Measure the camera image rate in the second shell:

```bash
ros2 topic hz /camera/image_raw
```

Measure the point-cloud bandwidth in the third shell:

```bash
ros2 topic bw /camera/points
```

Run `just iftop_router` in a terminal within the `robot` container desktop. Wait 60–90 seconds:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Untuned | 7.90 Hz | 4.2 Hz | Nothing (wasting ~28 Mbps) | ~62 Mbps, nearly half of it wasted |

A common baseline pattern is an intact laser scan, a reduced or irregular camera rate, and no complete point-cloud frames. `iftop` can show substantial point-cloud traffic even while `ros2 topic bw` remains silent. Those bytes belong to incomplete frames.

Real Wi-Fi results vary with signal strength, distance, interference, access-point load, and other devices using the same channel. Record the values that you observe.

Stop the three measurements and `iftop` with **Ctrl+C**.

## Enable compression 

Keep the three bash shells in the `pi_edge` container on the Raspberry Pi open after stopping the baseline measurements. In the `robot` container desktop, enable compression in `~/container_data/ROUTER_CONFIG.json5`. Keep `access_control`, `downsampling`, and `qos` commented out.

Enable compression in each Pi shell:

```bash
export ZENOH_CONFIG_OVERRIDE="${ZENOH_CONFIG_OVERRIDE};transport/unicast/compression/enabled=true"
```

Confirm that the override includes compression:

```bash
echo $ZENOH_CONFIG_OVERRIDE
```

Stop and restart the router on the `robot` container desktop so that it reads the new configuration. Restart the same three measurements in the Raspberry Pi `pi_edge` container used for the baseline. Run `just iftop_router` in the `robot` container desktop. Collect data for 60–90 seconds.

Record your measurements and compare them with the reference result:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Compression | 7.85 Hz | 11.87 Hz — source rate | Nothing received (~26 Mbps wasted) | ~55.7 Mbps |

Compression allows the camera images to fit the real Wi-Fi link, restoring the source frame rate. The point cloud still fails because the default congestion policy discards fragments before a complete frame arrives.

## Downsample the camera 

Stop the compression measurements and `iftop`. In the router configuration, disable compression and enable only the `downsampling` block. Keep `access_control` and `qos` commented out.

Exit the current three `pi_edge` container shells. Open fresh `pi_edge` shells, then source ROS 2 in each one:

```bash
exit
docker exec -it pi_edge /bin/bash
source /opt/ros/jazzy/setup.bash
```

Don't enable compression in these new shells. Stop and restart the router on the `robot` container desktop. Restart the measurements in the three `pi_edge` shells. Run `just iftop_router` in the `robot` container desktop. Collect data for 60–90 seconds.

Record your measurements and compare them with the reference result:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Downsampling | 7.94 Hz | 2.37 Hz — steady | Nothing received despite using 58–61 Mbps | ~64 Mbps |

The camera settles near the 3 Hz target with less jitter. The point-cloud connection uses the bandwidth released by the camera and still delivers no complete frames. More available bandwidth hasn't solved the large-message problem.

## Compress and block the point cloud 

Stop the downsampling measurements and `iftop`. In the router configuration, disable downsampling, enable compression, and enable the `access_control` block. Keep `qos` commented out.

Enable compression in each Pi shell:

```bash
export ZENOH_CONFIG_OVERRIDE="${ZENOH_CONFIG_OVERRIDE};transport/unicast/compression/enabled=true"
```

Stop and restart the router on the `robot` container desktop. Restart the measurements in the three `pi_edge` shells. Run `just iftop_router` in the `robot` container desktop. Collect data for 60–90 seconds.

Record your measurements and compare them with the reference result:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Compression and access control | 7.85 Hz | 11.89 Hz | Blocked | ~29 Mbps, all useful |

The point cloud now consumes no link bandwidth, while the camera and scan remain available. This configuration suits remote monitoring when the operator doesn't need three-dimensional data.

## Compress and deliver complete large messages 

Stop the compression and access control measurements and `iftop`. In the router configuration, comment out the access-control block, keep compression enabled, and enable the quality of service (QoS) block. Keep downsampling disabled.

The Pi shells already have compression enabled, so no client-side change is needed. Stop and restart the router on the `robot` container desktop. Restart the measurements in the three `pi_edge` shells. Run `just iftop_router` in the `robot` container desktop. Collect data for 60–90 seconds.

Record your measurements and compare them with the reference result:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Compression and QoS  | 7.89 Hz | 11.88 Hz, std dev 0.019 s | ~1 complete frame/s | ~63 Mbps, all useful |

The point-cloud terminal now reports complete 7.37 MB frames at the rate supported by the Wi-Fi connection. The camera and scan continue alongside it.

## Compare the experiment results

The complete comparison shows that similar link rates can carry very different amounts of useful ROS 2 data:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Untuned baseline | 7.90 Hz | 4.2 Hz | Nothing received | ~62 Mbps, nearly half wasted |
| Compression | 7.85 Hz | 11.87 Hz | Nothing received | ~55.7 Mbps |
| Downsampling | 7.94 Hz | 2.37 Hz, steady | Nothing received | ~64 Mbps |
| Compression and access control | 7.85 Hz | 11.89 Hz | Blocked | ~29 Mbps, all useful |
| Compression and QoS | 7.89 Hz | 11.88 Hz, steady | ~1 complete frame/s | ~63 Mbps, all useful |


## What you've accomplished and what's next

You've repeated the policy comparison over real Wi-Fi. Compression restored the camera rate and access control removed an unwanted flow. Downsampling produced a steady lower-rate stream, and `block_first` delivered complete point-cloud frames.

The comparison shows that tuning doesn't need to increase the available bandwidth. It changes how the bandwidth is used and which complete messages reach the receiver. 

Next, you'll select a configuration for the needs of your deployment.
