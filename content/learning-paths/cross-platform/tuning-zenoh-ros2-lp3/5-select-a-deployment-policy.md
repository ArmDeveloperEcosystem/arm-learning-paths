---
title: Select a deployment policy
weight: 6

layout: learningpathall
---

## Select a configuration for your deployment

The experiments show that the right configuration depends on which sensor data the remote application needs.

### Remote monitoring only: compression and access control

Use compression and access control when the remote station needs camera images and laser scans, but not the point cloud.

Enable `transport/unicast/compression` at both ends of the link. On the router, deny `*/camera/points/**` and its `*/camera/points/**/@adv/**` variant.

The camera runs at its full source rate, `/scan` remains available, and the point cloud consumes no link bandwidth. For a remote station that only needs to monitor the robot, these two settings are sufficient.

### Large messages required: compression and QoS

Use compression and QoS when complete point-cloud frames must reach the remote device.

Keep compression enabled and add the quality of service (QoS) `qos/network` block. Give important topics higher priority, and set `congestion_control: "block_first"` for payloads larger than 4096 bytes.

All three sensor streams can then share the link. The point cloud arrives at the rate the network supports, but each delivered frame is complete rather than a collection of unusable fragments.

### When compressed images still do not fit: downsampling

Use downsampling when the compressed camera stream still exceeds the available capacity.

Set the forwarded image rate below the sustained capacity of the link. This trades frame rate for steadier delivery and lower jitter.

## Summary

You have now:

- Measured message frequency, jitter, message bandwidth, and total Zenoh link traffic at the correct observation points
- Reproduced a constrained wireless link between two Docker containers with `tc` and `netem`
- Shown why small laser scans can survive while camera and point-cloud messages fail
- Reduced traffic with compression, access control, and downsampling
- Delivered complete large messages by replacing fragment-dropping behaviour with `block_first`
- Confirmed the policy effects on a Raspberry Pi over real Wi-Fi

The available bandwidth did not need to change. Zenoh changed which messages used it and whether those messages arrived in a form the ROS 2 receiver could use.
