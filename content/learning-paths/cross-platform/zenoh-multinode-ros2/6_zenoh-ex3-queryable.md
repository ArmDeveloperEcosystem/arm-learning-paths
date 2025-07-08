---
title: Zenoh Example-3 Computation on Query using Queryable
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example 3: Computation on Query using Queryable

Next, you’ll explore Zenoh's queryable capability, which lets a node dynamically respond to data queries by executing a custom computation or data generation function in this example.

Unlike zenohd which simply returns stored data, a queryable node can register to handle a specific key expression and generate responses at runtime. This is ideal for distributed computing at the edge, where lightweight devices—such as Raspberry Pi nodes—can respond to requests with calculated values (e.g., sensor fusion, AI inference results, or diagnostics).

### Use Case: On-Demand Battery Health Estimation

Imagine a robot fleet management system where the central planner queries each robot for its latest battery health score, which is not published continuously but calculated only when queried.

This saves bandwidth and enables edge compute optimization using Zenoh's Queryable.

### Step 1: Launch a Queryable Node

On one Raspberry Pi device, run the built-in Zenoh example to register a queryable handler.

```bash
cd ~/zenoh/target/release/examples
./z_queryable
```

You'll see the output like:

```
pi@raspberrypi:~/zenoh/target/release/examples$ ./z_queryable
Opening session...
Declaring Queryable on 'demo/example/zenoh-rs-queryable'...
Press CTRL-C to quit...
```

The node is now ready to accept queries on the key demo/example/zenoh-rs-queryable and respond with a predefined message.

### Step 2: Trigger a Query from Another Node

On another Raspberry Pi device, run:

```bash
cd ~/zenoh/target/release/examples
./z_get -s demo/example/zenoh-rs-queryable
```

You should see:

```
./z_get -s demo/example/zenoh-rs-queryable
Opening session...
Sending Query 'demo/example/zenoh-rs-queryable'...
>> Received ('demo/example/zenoh-rs-queryable': 'Queryable from Rust!')
```

The result will look like: 
![img3 alt-text#center](zenoh_ex3.gif "Figure 3: Computation on Query using Queryable")

The value you receive comes not from storage, but from the computation inside the queryable handler.

### Real-World Application: Distributed Inference & Computation

This model enables edge-based intelligence, such as:
- Executing custom logic in response to a query (e.g., “calculate load average”)
- Triggering ML inference (e.g., “classify image X on demand”)
- Decentralized diagnostics (e.g., “report actuator status”)

Queryable is a key feature for data-in-use scenarios, allowing fine-grained, on-demand compute inside your Zenoh-powered architecture.

Next, you’ll extend this Queryable pattern to perform parameterized computation — simulating edge diagnostics and adaptive inference.