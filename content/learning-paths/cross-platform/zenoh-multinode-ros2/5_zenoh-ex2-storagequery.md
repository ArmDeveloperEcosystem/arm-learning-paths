---
title: Run a Zenoh storage and query example

weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example 2: Storage and query

The second example adds Zenoh's data storage and querying capabilities by enabling nodes to retrieve historical values on demand.

Building on the previous pub/sub example, you’ll now explore how Zenoh supports persistent data storage and on-demand querying, a powerful feature for robotics and IIoT applications.

In a typical warehouse or factory scenario, autonomous robots can periodically publish sensor data,such as position, temperature, or battery level—that a central system or peer robot may later need to query.


Unlike Pub/Sub, which requires live, real-time message exchange, Zenoh's storage and query model enables asynchronous access to data that was published earlier, even if the original publisher is no longer online.

In this example, you’ll run the `zenohd` daemon with in-memory storage and use `z_put` to publish data and `z_get` to retrieve it.

This is especially useful for distributed systems where nodes may intermittently connect or request snapshots of state from peers.

### Step 1: Start the Zenoh daemon with in-memory storage

On one Raspberry Pi, launch the Zenoh daemon with a configuration that enables in-memory storage for keys in the `demo/example/**` directory.

```bash
cd ~/zenoh/target/release/
./zenohd --cfg='plugins/storage_manager/storages/demo:{key_expr:"demo/example/**",volume:"memory"}' &
```

This starts the Zenoh daemon with in-memory storage support. 

You should see log messages indicating that the storage_manager plugin is loaded.

If port 7447 is already in use, either stop any previous Zenoh processes or configure a custom port using the `listen.endpoints.router` setting.

### Step 2: Publish data

On 2nd Raspberry Pi device, use `z_put` to send a key-value pair that will be handled by the `zenohd` storage.

```bash
cd ~/zenoh/target/release/examples
./z_put -k demo/example/test1 -p "Hello from storage!"
```

This command stores the string `Hello from storage!` under the key demo/example/test1.

### Step 3: Query the data

Back on first Raspberry Pi, you can now query the stored data from any Zenoh connected node.

```bash
cd ~/zenoh/target/release/examples
./z_get -s demo/example/test1
```

You should see an output similar to:

```bash
Sending Query 'demo/example/test1'...
>> Received ('demo/example/test1': 'Hello from storage!')
```

The result is shown below:

![img2 alt-text#center](zenoh_ex2.gif "Figure 2: Storage and Query")

{{% notice tip %}}
If you have more than two Raspberry Pi devices, you can run the `z_get` command on a third device to validate that storage queries work seamlessly across a multi-node setup.
{{% /notice %}}

This example shows how Zenoh's storage with query model supports asynchronous data access and resilient state-sharing—critical capabilities in robotics and industrial IoT systems where network connectivity may be intermittent or system components loosely coupled.

