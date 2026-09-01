---
title: Measure with real Wi-Fi
weight: 5

description: Measure Zenoh policy effects on ROS 2 sensor traffic between an Arm server and a Raspberry Pi over Wi-Fi.

layout: learningpathall
---

## Experiment B: real Wi-Fi

Experiment B changes one part of the topology:

```text
Experiment A: robot container ── Docker network ── control container
Experiment B: robot container ── Arm server ── Wi-Fi ── Raspberry Pi
```

Configure your Raspberry Pi to connect to an existing Wi-Fi network that also contains the Arm server. Using 2.4 GHz makes the effects clearer. Follow the [Raspberry Pi connection procedure from the preceding Learning Path](/learning-paths/cross-platform/distributed-ros2-zenoh-lp2/3-connect-the-raspberry-pi/) to connect it as a Zenoh client.

## Restore the B0 router configuration

Before starting, return the router configuration to a clean state. Open `~/container_data/ROUTER_CONFIG.json5` in a terminal within the `robot` container desktop and ensure the following:

- Set `transport/unicast/compression/enabled` to `false`
- Keep `access_control`, `downsampling`, and `qos` commented out

Restart the router on the `robot` container desktop after saving the file. Confirm that the emulated link is no longer active:

```bash
just network_normal
```

Experiment B uses the physical wireless link. Do not run `just network_limit` during these scenarios.

## Record scenario B0

Open three SSH sessions to the Raspberry Pi. In each session, open a bash shell in the `pi_edge` container and source ROS 2:

```bash
docker exec -it pi_edge /bin/bash
source /opt/ros/jazzy/setup.bash
```

Run one receiver command in each bash shell that has been opened in the `pi_edge` container:

```bash
ros2 topic hz /scan
```

```bash
ros2 topic hz /camera/image_raw
```

```bash
ros2 topic bw /camera/points
```

Run `just iftop_router` in a terminal within the `robot` container desktop. Wait 60–90 seconds and complete the B0 row:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| **B0** untuned | 7.90 Hz | 4.2 Hz | nothing (wasting ~28 Mbps) | ~62 Mbps, nearly half of it wasted |

A common B0 pattern is an intact laser scan, a reduced or irregular camera rate, and no complete point-cloud frames. `iftop` can show substantial point-cloud traffic even while `ros2 topic bw` remains silent. Those bytes belong to incomplete frames.

Real Wi-Fi results vary with signal strength, distance, interference, access-point load, and other devices using the same channel. Record what you observe rather than treating the reference values as targets.

Stop the three measurements and `iftop` with **Ctrl+C**.

## Enable compression (B1)

Keep the three bash shells in the `pi_edge` container on the Raspberry Pi open after stopping the B0 measurements. In the `robot` container desktop, enable compression in `~/container_data/ROUTER_CONFIG.json5`. Keep `access_control`, `downsampling`, and `qos` commented out.

Enable compression in each Pi shell:

```bash
export ZENOH_CONFIG_OVERRIDE="${ZENOH_CONFIG_OVERRIDE};transport/unicast/compression/enabled=true"
```

Confirm that the override includes compression:

```bash
echo $ZENOH_CONFIG_OVERRIDE
```

Stop and restart the router on the `robot` container desktop so that it reads the new configuration. Restart the same three measurements in the Raspberry Pi `pi_edge` container used for B0. Run `just iftop_router` in the `robot` container desktop. Collect data for 60–90 seconds.

Record your measurements and compare them with the reference result:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| **B1: Compression** | **7.85 Hz** | **11.87 Hz — source rate** | **Nothing received** (~26 Mbps wasted) | **~55.7 Mbps** |

Compression allows the camera images to fit the real Wi-Fi link, restoring the source frame rate. The point cloud still fails because the default congestion policy discards fragments before a complete frame arrives.

## Downsample the camera (B2)

Stop the B1 measurements and `iftop`. In the router configuration, disable compression and enable only the `downsampling` block from A4. Keep `access_control` and `qos` commented out.

The current Pi shells still contain the compression override from B1. Exit each of the three container shells into `pi_edge` and open fresh ones. Then source ROS 2:

```bash
exit
docker exec -it pi_edge /bin/bash
source /opt/ros/jazzy/setup.bash
```

Do not enable compression in these new shells. Stop and restart the router on the `robot` container desktop. Restart the measurements in the three `pi_edge` shells. Run `just iftop_router` in the `robot` container desktop. Collect data for 60–90 seconds.

Record your measurements and compare them with the reference result:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| **B2: Downsampling** | **7.94 Hz** | **2.37 Hz — steady** | **Nothing received** despite using 58–61 Mbps | **~64 Mbps** |

The camera settles near the 3 Hz target with less jitter. The point-cloud connection uses the bandwidth released by the camera and still delivers no complete frames. More available bandwidth has not solved the large-message problem.

## Compress and block the point cloud (B3)

Stop the B2 measurements and `iftop`. In the router configuration, disable downsampling, enable compression, and enable the `access_control` block from A3. Keep `qos` commented out.

Enable compression in each Pi shell:

```bash
export ZENOH_CONFIG_OVERRIDE="${ZENOH_CONFIG_OVERRIDE};transport/unicast/compression/enabled=true"
```

Stop and restart the router on the `robot` container desktop. Restart the measurements in the three `pi_edge` shells. Run `just iftop_router` in the `robot` container desktop. Collect data for 60–90 seconds.

Record your measurements and compare them with the reference result:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| **B3: Compression and access control** | **7.85 Hz** | **11.89 Hz** | **Blocked** | **~29 Mbps, all useful** |

The point cloud now consumes no link bandwidth, while the camera and scan remain available. This configuration suits remote monitoring when the operator does not need three-dimensional data.

## Compress and deliver complete large messages (B4)

Stop the B3 measurements and `iftop`. In the router configuration, comment out the access-control block, keep compression enabled, and enable the `qos` block from A5. Keep downsampling disabled.

The Pi shells already have compression enabled, so no client-side change is needed. Stop and restart the router on the `robot` container desktop. Restart the measurements in the three `pi_edge` shells. Run `just iftop_router` in the `robot` container desktop. Collect data for 60–90 seconds.

Record your measurements and compare them with the reference result:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| **B4: Compression and QoS** | **7.89 Hz** | **11.88 Hz, std dev 0.019 s** | **~1 complete frame/s** | **~63 Mbps, all useful** |

The point-cloud terminal now reports complete 7.37 MB frames at the rate supported by the Wi-Fi connection. The camera and scan continue alongside it.

## Compare the Experiment B results

The complete comparison shows that similar link rates can carry very different amounts of useful ROS 2 data:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| B0: Untuned | 7.90 Hz | 4.2 Hz | Nothing received | ~62 Mbps, nearly half wasted |
| B1: Compression | 7.85 Hz | 11.87 Hz | Nothing received | ~55.7 Mbps |
| B2: Downsampling | 7.94 Hz | 2.37 Hz, steady | Nothing received | ~64 Mbps |
| B3: Compression and access control | 7.85 Hz | 11.89 Hz | Blocked | ~29 Mbps, all useful |
| B4: Compression and QoS | 7.89 Hz | 11.88 Hz, steady | ~1 complete frame/s | ~63 Mbps, all useful |


## What you've accomplished and what's next

You've repeated the policy comparison over real Wi-Fi. Compression restored the camera rate, access control removed an unwanted flow, downsampling produced a steady lower-rate stream, and `block_first` delivered complete point-cloud frames.

The comparison shows that tuning does not need to increase the available bandwidth. It changes how the bandwidth is used and which complete messages reach the receiver. Next, you'll select a configuration for the needs of your deployment.
