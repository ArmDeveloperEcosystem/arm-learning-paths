---
title: Zenoh Example-1 Simple Pub/Sub
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example 1: Simple Pub/Sub

This first test demonstrates Zenoh’s real-time publish/subscribe model using two Raspberry Pi devices.

The following command is to initiate a subscriber for a key expression `demo/example/**`, i.e. a set of topics starting with the path `demo/example`.

### Step 1: Run Subscriber

Log in to Pi using any of the methods:

```bash
cd ~/zenoh/target/release/examples
./z_sub
```

### Step 2: Run Publisher

Then, log in to another machine Pi.

```bash
cd ~/zenoh/target/release/examples
./z_pub
```

The result will look like: 
![img1 alt-text#center](zenoh_ex1.gif "Figure 1: Simple Pub/Sub")

In the left-side window, I have logged into the device Pi4 and run the z_sub program. 
It receives values with the key `demo/example/zenoh-rs-pub` continuously published by z_pub running on Pi in the right-side window.

This basic example shows Zenoh’s zero-config discovery and low-latency pub/sub across physical nodes.
