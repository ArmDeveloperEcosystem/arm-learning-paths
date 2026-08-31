---
title: Tune Zenoh on an emulated wireless link
weight: 4

description: Emulate a constrained wireless link and measure how Zenoh traffic-control policies affect ROS 2 sensor delivery.

layout: learningpathall
---

## Apply network constraints 

After measuring a baseline, emulate a wireless link and tune Zenoh. 

Linux traffic control (`tc`) decides how packets leave a network interface. Its network emulator (`netem`) can add delay, loss, duplication, corruption, and reordering. Together, they let you reproduce a difficult network without moving the containers to Wi-Fi.

In a terminal within the `robot` container desktop, run:

```bash
source ~/workshop_env.bash
just network_limit
```

The output is similar to:

```output
WiFi medium connection simulation applied to 172.1.0.3:
 - Rate: 25mbit
 - Latency: 20ms ± 10ms
 - Packet loss: 0.5%
 - Reordering: 1% 25%
 - Duplicates: 0.1%
 - Corruptions: 0.01%
```

The 25 Mbps rate is a maximum. It's not a guaranteed result. TCP can send less than the limit when it reacts to loss and reordering.

Restart the measurements and record:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Constrained | 7.94 Hz — unaffected | 0.88 Hz (std 0.577 s, max gap 6.3 s) | Nothing received | ~23.5 Mbps (at the cap) |

The scan is untouched: it's small, and it has a connection of its own.
`/camera/image_raw` slows down, becomes irregular, or receives no complete frames during the window. The point cloud disappears.

Stop all four measurement commands with **Ctrl+C**.

## Apply compression

Zenoh uses [LZ4 compression](https://lz4.org/) to reduce the bytes sent over a unicast connection. LZ4 was chosen for speed rather than ratio, because compression must not become a latency source. Compression is negotiated when a client connects, so the router and the client must both enable it.

In a terminal on the `robot` container desktop, open the router configuration:

```bash
nano ~/container_data/ROUTER_CONFIG.json5
```

Find the existing `transport/unicast/compression` section and set `enabled` to `true`:

```json5
compression: {
  enabled: true,
},
```

Don't add a second `transport` block. Ignore the commented example and edit only the active value.

In a terminal on the `control` container desktop, open the client configuration:

```bash
nano ~/container_data/SESSION_CONFIG.json5
```

Find the same compression setting and set it to `true`.

Save each file with **Ctrl+O** and **Enter**, then exit Nano with **Ctrl+X**.

The router reads its configuration only at startup. 

In the `robot` container desktop, find the terminal running the router, press **Ctrl+C**, then restart it:

```bash
just router
```

Restart the four measurements and record:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Compression | 7.95 Hz (link traffic ~380 Kbps → ~200 Kbps) | 0.5–2.8 Hz, drifting | Nothing received | ~23.5 Mbps, still at the cap |

The scan's rate is unchanged but its bytes on the link roughly halve, with LZ4 achieving about 1.8× on this data. The image improves, but the reading drifts between measurements, while incomplete point-cloud fragments still compete for the link. An unstable reading is expected.

The total TX rate (Link traffic) can remain close to the constrained link’s capacity. Compression reduces individual messages, but publishers continue supplying more data than the link can carry.

Stop all four measurement commands with **Ctrl+C**. Keep compression enabled and keep the network limit active for the next scenario.

## Add an access-control rule 

A monitoring station doesn't always need the point cloud. Zenoh access control can stop that topic at the router while local robot nodes continue to use it.

Open the router configuration in the `robot` container desktop:

```bash
nano ~/container_data/ROUTER_CONFIG.json5
```

Add the following `access_control` block at the top level of the file:

```json5
access_control: {
  enabled: true,
  default_permission: "allow",
  rules: [
    {
      id: "deny_points_cloud",
      permission: "deny",
      messages: [
        "put", "delete", "declare_subscriber",
        "query", "reply", "declare_queryable",
        "liveliness_token", "liveliness_query", "declare_liveliness_subscriber",
      ],
      flows: ["egress", "ingress"],
      key_exprs: [
        "*/camera/points/**",
        "*/camera/points/**/@adv/**",
      ],
    },
  ],
  subjects: [
    { id: "ALL" },
  ],
  policies: [
    {
      id: "deny_points_cloud_to_all",
      rules: ["deny_points_cloud"],
      subjects: ["ALL"],
    },
  ],
},
```
Don't place the block inside `transport`.

The first key expression matches the point-cloud data. The `@adv` form matches the additional keys used to advertise topics with transient-local durability.

Save the file, stop the router with **Ctrl+C**, and restart it on the `robot` container desktop:

```bash
just router
```

Restart the three measurements in `control` and `just iftop_router` in `robot`, and wait 60–90 seconds:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Compression and access control | 7.97 Hz | 0.84 Hz (still bursty, max gap 11.4 s) | Blocked, and the connection drops to zero | ~9.4 Mbps (The link is no longer saturated)|

Verify the asymmetry from both sides:

```bash
# control container: nothing arrives
ros2 topic bw /camera/points

# robot container: unchanged
ros2 topic hz /camera/points
```

The control container receives nothing while the robot's own nodes still exchange the point cloud at about 12 Hz. The rule governs what crosses the router, not what happens inside the robot.

Note that `/camera/points` still appears in the remote `ros2 topic list` even though no data arrives. The block stops the data.

Stop all measurement commands with **Ctrl+C**. Keep compression, access control, and the network limit active.

## Downsample the image 

Downsampling drops publications on the egress path to a target frequency.

Keep the access-control block active. Open the router configuration in `robot` container desktop:

```bash
nano ~/container_data/ROUTER_CONFIG.json5
```

Add the following block at the top level:

```json5
downsampling: [
  {
    messages: ["put", "reply"],
    flows: ["egress"],
    rules: [
      { key_expr: "*/camera/image_raw/**", freq: 3.0 },
      { key_expr: "*/camera/image_raw/**/@adv/**", freq: 3.0 },
    ],
  },
],
```

The rule sets a maximum egress rate of 3 Hz for the image and its transient-local advertisement keys.

Save the file, stop the router, and restart it on the `robot` container desktop:

```bash
just router
```

Restart the measurements and record:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Compression, access control, and downsampling | 8.0 Hz | 2.6 Hz, std dev 0.06 s — steady | Blocked | ~6.8 Mbps |

The remote camera rate should settle near, but not necessarily exactly at, 3 Hz. Compare its standard deviation with access control. A lower standard deviation means the frames arrive more regularly instead of in bursts.

A steady rate less than the connection’s usable capacity gives the transmit queue time to drain between frames. A stable 2.6 Hz stream can be more useful to an operator than a lower average made from short bursts and long pauses.

Stop all measurement commands with **Ctrl+C**.

## Apply priority and congestion control 

The remaining problem is the point cloud, which has only been blocked and never delivered. Restore the point-cloud traffic. Then, change the congestion policy.

Open `~/container_data/ROUTER_CONFIG.json5` in the `robot` container desktop. Comment out the `access_control` and `downsampling` blocks.

Add the following block for quality of service (QoS) at the top level:

```json5
qos: {
  network: [
    {
      interfaces: ["eth0"],
      key_exprs: ["**/map/**", "**/scan/**"],
      messages: ["put", "query"],
      overwrite: { priority: "interactive_high" }
    },
    {
      interfaces: ["eth0"],
      key_exprs: ["**/robot_description/**"],
      messages: ["put", "query"],
      overwrite: { priority: "interactive_low" }
    },
    {
      interfaces: ["eth0"],
      key_exprs: ["**/camera/image_raw/**"],
      messages: ["put"],
      overwrite: { priority: "data_low" }
    },
    {
      interfaces: ["eth0"],
      key_exprs: ["**/camera/points/**"],
      messages: ["put"],
      overwrite: { priority: "background" }
    },
    {
      interfaces: ["eth0"],
      payload_size: "4096..",
      messages: ["put"],
      overwrite: { congestion_control: "block_first" }
    },
  ],
},
```

Verify the state of all three blocks before restarting:

```bash
grep -n "access_control\|downsampling\|qos\|block_first" ~/container_data/ROUTER_CONFIG.json5
```

Restart the router on the `robot` container desktop and the measurements.

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Compression and QoS | 7.9 Hz | 4.4 Hz, std dev 0.08 s | Delivered: 2.0–3.0 MB/s, a complete 7.37 MB frame every ~3 s | ~17.2 Mbps, all of it useful|

For the first time under the constrained link, `ros2 topic bw /camera/points` should report complete 7.37 MB messages. The average bandwidth will be much lower than the baseline because a complete frame can take several seconds to arrive.

When the queue is full, `block_first` waits for the first matching message to progress and can drop later matching messages. This favors complete point-cloud frames over fragments from several competing frames. Fewer frames arrive, but the received frames are usable.

Stop the measurements with **Ctrl+C**. Restore the normal Docker network in the `robot` container desktop:

```bash
just network_normal
```

## Compare the results of the experiment

The complete comparison shows how each policy changes the traffic delivered over the same constrained link:

| Scenario | `/scan` | `/camera/image_raw` | `/camera/points` | Link traffic |
|---|---|---|---|---|
| Baseline | 7.97 Hz | 11.85 Hz | ~88 MB/s | ~810 Mbps |
| Constrained | 7.94 Hz | 0.88 Hz | Nothing received | ~23.5 Mbps |
| Compression | 7.95 Hz | 0.5–2.8 Hz, drifting | Nothing received | ~23.5 Mbps |
| Compression and access control | 7.97 Hz | 0.84 Hz, bursty | Blocked | ~9.4 Mbps |
| Compression, access control, and downsampling | 8.0 Hz | 2.6 Hz, steady | Blocked | ~6.8 Mbps |
| Compression and QoS | 7.9 Hz | 4.4 Hz, steady | 2.0–3.0 MB/s | ~17.2 Mbps |

## What you've accomplished and what's next

You've reproduced a constrained wireless link and measured how each Zenoh policy changes the result. Compression reduced the bytes sent but couldn't deliver the point cloud by itself. Access control removed unwanted traffic, downsampling made the camera stream steadier, and `block_first` allowed complete point-cloud frames to arrive.

Next, you'll repeat the comparison with a Raspberry Pi over real Wi-Fi.
