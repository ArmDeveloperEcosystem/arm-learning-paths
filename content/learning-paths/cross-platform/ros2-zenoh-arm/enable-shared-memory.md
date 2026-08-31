---
title: Enable Zenoh shared-memory transport
description: Enable shared memory in the Zenoh router and session configurations, then compare point-cloud latency and loopback traffic.
weight: 9

layout: "learningpathall"
---

## Understand the shared-memory experiment

After observing simulation resource usage, enable shared memory in both Zenoh configuration files. Then, restart the relevant processes and repeat the measurement.

By default, processes on the same machine exchange data over TCP loopback. Zenoh shared-memory transport places large messages in `/dev/shm` and avoids the network stack. Applications don't need code changes or loaned buffers, and Zenoh falls back to TCP if shared memory is unavailable.

## Measure the TCP-loopback baseline

Before enabling shared memory, measure the default TCP-loopback baseline.

Stop Navigation2 in the third bash shell in the `robot` container. The latency measurement needs wall-clock timestamps, and Navigation2 doesn't operate in this mode.

Stop the current simulation. Restart it in second bash shell with wall-clock time and without the Gazebo viewer:

```bash
just rox_simu use_wall_time:=True no_gui
```

Open a new bash shell in the `robot` container and measure the point-cloud latency:

```bash
just cam_latency
```

On the supplied reference system, the point-cloud latency is around `9–10 ms`:

```output
Mean : 9.40 ms | Std : 0.82 ms | Min : 7.91 ms | Max : 12.15 ms
```

Record the mean for comparison.

## Enable shared memory in both configurations

Open the following working files using your choice of editor in one of the `robot` bash shells:

- `~/container_data/ROUTER_CONFIG.json5`
- `~/container_data/SESSION_CONFIG.json5`

In each file, find the `transport/shared_memory` block and change its `enabled` value to `true`.

{{% notice Important %}}
Both files contain multiple `enabled` fields. In both `ROUTER_CONFIG.json5` and `SESSION_CONFIG.json5`, change only the `enabled` value inside the `shared_memory` block.
{{% /notice %}}

The router and ROS 2 sessions read these files when their processes start. 

Stop the router and simulation processes with **Ctrl+C**, then restart them so they load the updated setting.

Restart the router in the first bash shell:

```bash
# Router bash shell
just router
```

Restart the simulation in the second bash shell:

```bash
# Simulation bash shell
just rox_simu use_wall_time:=True no_gui
```

Run the latency measurement again from another bash shell in the `robot` container:

```bash
just cam_latency
```

The supplied reference system produced these results:

| Measurement | TCP loopback (default) | Shared memory |
|---|---|---|
| Mean latency | `9.3–10.2 ms` | `6.3–7.4 ms` |
| Standard deviation | Approximately `1.0 ms` | Approximately `0.65 ms` |
| `/dev/shm` usage | `8 KB` | `247 MB` |

The reference mean latency improves by approximately 30%, with lower jitter. Your result depends on the server, workload, and run conditions. Compare the two measurements from your own system.

## Verify the transport change

Check the shared-memory directory and loopback traffic:

```bash
ls /dev/shm
just iftop_lo
```

`.zenoh` files appear under `/dev/shm` for Zenoh processes using shared memory. The large loopback flows should also disappear because the data now moves through memory.

## Restore the environment for the next Learning Path

Keep the shared-memory configuration enabled. In the second bash shell, press **Ctrl+C** to stop the temporary wall-time simulation if it's still running.

Keep the Zenoh router running in the first bash shell. If it has stopped, restart it after re-sourcing the environment:

```bash
source ~/workshop_env.bash
just router
```

In the second bash shell, source the environment if needed and start the normal headless simulation:

```bash
source ~/workshop_env.bash
just rox_simu no_gui
```

In the third bash shell, source the environment if needed and restart Navigation2:

```bash
source ~/workshop_env.bash
just rox_nav2
```

Confirm that the router is running, the simulation starts without errors, and Navigation2 reports `Managed nodes are active`. Leave these three processes running for the next Learning Path.

## What you've accomplished

You've built a ROS 2 Jazzy simulation environment on an Arm server, observed Zenoh discovery behavior, navigated and controlled a Neobotix ROX robot, measured resource use, and compared TCP-loopback communication with shared-memory transport.

Next, complete the [Distribute a ROS 2 robotic system across Arm devices with Zenoh](/learning-paths/cross-platform/distributed-ros2-zenoh-lp2/) Learning Path.
