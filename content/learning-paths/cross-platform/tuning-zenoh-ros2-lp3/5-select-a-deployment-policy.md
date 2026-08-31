---
title: Select a deployment policy
weight: 6

description: Select a Zenoh deployment policy for remote monitoring, large-message delivery, or constrained camera traffic.

layout: learningpathall
---

## Select a configuration for your deployment

The experiments show that the right configuration depends on which sensor data the remote application needs. The available bandwidth didn't need to change. Zenoh changed which messages used it and whether those messages arrived in a form the ROS 2 receiver could use.

### Compression and access control 

Use compression and access control when the remote station needs camera images and laser scans, but not the point cloud.

Enable `transport/unicast/compression` at both ends of the link. On the router in the `robot` desktop, deny `*/camera/points/**` and its `*/camera/points/**/@adv/**` variant.

The camera runs at its full source rate, `/scan` remains available, and the point cloud consumes no link bandwidth. For a remote station that only needs to monitor the robot, these two settings are sufficient.

### Compression and quality of service 

Use compression and quality of service (QoS) when complete point-cloud frames must reach the remote device.

Keep compression enabled and add the QoS `qos/network` block. Give important topics higher priority, and set `congestion_control: "block_first"` for payloads larger than 4096 bytes.

All three sensor streams can then share the link. The point cloud arrives at the rate the network supports. Each delivered frame is complete rather than a collection of unusable fragments.

### Downsampling 

Use downsampling when the compressed camera stream still exceeds the available capacity.

Set the forwarded image rate less than the sustained capacity of the link. This trades frame rate for steadier delivery and lower jitter.

## What you've accomplished

You've learned what Zenoh deployment policy you should select depending on your application requirements. 

Apply the policy that matches your deployment, then use this measurement workflow to validate its results.
