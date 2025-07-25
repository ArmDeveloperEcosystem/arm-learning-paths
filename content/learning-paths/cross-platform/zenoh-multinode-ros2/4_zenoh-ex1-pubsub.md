---
title: Run a simple Zenoh pub/sub example
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test Zenoh pub/sub across two devices

This example demonstrates Zenoh's real-time publish/subscribe model across two Raspberry Pi devices.

The subscriber listens for all data published under the key expression `demo/example/**`, which matches any topic beginning with `demo/example/`.

## Start the subscriber node

Run the subscriber example on one of the Raspberry Pi systems.

```bash
cd ~/zenoh/target/release/examples
./z_sub
```

## Start the publisher node

Then, log in to the other Raspberry Pi and run the publisher.

```bash
cd ~/zenoh/target/release/examples
./z_pub
```

{{% notice Tip %}}
You can run both `z_sub` and `z_pub` on the same device for testing, but running them on separate Raspberry Pis demonstrates Zenoh’s distributed discovery and cross-node communication.
{{% /notice %}}

## Observe the pub/sub data flow

The result is shown below:

![img1 Zenoh subscriber receiving messages from a publisher in a two-terminal view#center](zenoh_ex1.gif "Simple Pub/Sub")

The left-side window shows the `z_sub` program. 

It receives values with the key `demo/example/zenoh-rs-pub` continuously published by `z_pub` running in the right-side window.

This example confirms that Zenoh’s zero-configuration peer discovery and real-time pub/sub communication are working correctly across physical nodes.

