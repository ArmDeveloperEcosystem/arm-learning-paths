---
title: Zenoh Example-1 Simple Pub/Sub
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example 1: Simple pub/sub

This first test demonstrates the real-time publish/subscribe model using two Raspberry Pi devices.

The following command is to initiate a subscriber for a key expression `demo/example/**`, a set of topics starting with the path `demo/example`.

### Step 1: Run subscriber

Run the subscriber example on one of the Raspberry Pi systems.

```bash
cd ~/zenoh/target/release/examples
./z_sub
```

### Step 2: Run publisher

Then, log in to the other Raspberry Pi and run the publisher.

```bash
cd ~/zenoh/target/release/examples
./z_pub
```

The result is shown below:

![img1 alt-text#center](zenoh_ex1.gif "Figure 1: Simple Pub/Sub")

The left-side window shows the `z_sub` program. 

It receives values with the key `demo/example/zenoh-rs-pub` continuously published by `z_pub` running in the right-side window.

This basic example shows Zenoh's zero-config discovery and low-latency pub/sub across physical nodes.
