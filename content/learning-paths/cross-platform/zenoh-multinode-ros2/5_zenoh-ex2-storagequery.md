---
title: Run a Zenoh storage and query example

weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

##  Query historical data using Zenoh’s storage engine

This example demonstrates Zenoh's data storage and query model which enables nodes to retrieve previously published values—even after the original publisher goes offline.

Building on the previous pub/sub example, you’ll now run a lightweight Zenoh daemon that stores key–value pairs in memory. Then, you’ll publish data with `z_put` and retrieve it using `z_get`.

This pattern is ideal for robotics and IIoT scenarios where devices intermittently connect or request snapshots of remote state.

For example, in a warehouse or factory:
- Robots can periodically publish position, temperature, or battery level.
- A central system or peer node can later query these values on demand.

Unlike Pub/Sub, which requires live, real-time message exchange, Zenoh's storage and query model enables asynchronous access to data that was published earlier, even if the original publisher is no longer online.

In this example, you’ll run the `zenohd` daemon with in-memory storage and use `z_put` to publish data and `z_get` to retrieve it.

This is especially useful for distributed systems where nodes may intermittently connect or request snapshots of state from peers.

## Start the Zenoh daemon with in-memory storage

On one Raspberry Pi, launch the Zenoh daemon with a configuration that enables in-memory storage for keys in the `demo/example/**` directory.

```bash
cd ~/zenoh/target/release/
./zenohd --cfg='plugins/storage_manager/storages/demo:{key_expr:"demo/example/**",volume:"memory"}' &
```

This starts the Zenoh daemon with in-memory storage support. 

You should see log messages indicating that the storage_manager plugin is loaded.

If port 7447 is already in use, either stop any previous Zenoh processes or configure a custom port using the `listen.endpoints.router` setting.

## Publish a value

On 2nd Raspberry Pi device, use `z_put` to send a key-value pair that will be handled by the `zenohd` storage.

```bash
cd ~/zenoh/target/release/examples
./z_put -k demo/example/test1 -p "Hello from storage!"
```

This command stores the string `Hello from storage!` under the key demo/example/test1.

## Query the stored value

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

{{% notice Tip %}}
If you have more than two Raspberry Pi devices, you can run the `z_get` command on a third device to validate that storage queries work seamlessly across a multi-node setup.
{{% /notice %}}

This example shows how Zenoh's storage with query model supports asynchronous data access and resilient state-sharing—critical capabilities in robotics and industrial IoT systems where network connectivity may be intermittent or system components loosely coupled.

## What's next?

Now that you've seen how Zenoh handles pub/sub and storage-based queries, you're ready to build reactive and intelligent edge nodes.

In the next example, you’ll implement a **Zenoh queryable** that responds to runtime parameters,such as battery level and temperature, by computing and returning a real-time health score. This showcases how Zenoh supports on-demand edge computation without needing to pre-store data.




