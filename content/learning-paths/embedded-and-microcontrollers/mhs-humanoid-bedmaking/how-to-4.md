---
title: How the two humanoids coordinate over MHS
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Each robot is an MHS device

In the demo, each G1 is a **Model Hardware Standard device**: a driver object that advertises the procedures it can perform and the events it emits. In the MHS Python SDK a device is an `MhsDriver` subclass; methods marked `@rpc` are callable procedures, and methods marked `@emit` are events published on the fabric. This driver model is the one MHS absorbed from Arm Device Connect, so the decorators keep the same names.

A simplified peer looks like this:

```python
from mhs import MhsDriver, rpc, emit

class BedMakingG1(MhsDriver):
    device_type = "unitree_g1_bed_making"

    @rpc()
    async def pickUpBedSheet(self, corner: str) -> dict:
        # grip the sheet at the given corner
        ...
        return {"holding": corner}

    @rpc()
    async def askForHelp(self, corner: str) -> dict:
        # advertise that this corner needs a second robot
        await self.help_requested(corner=corner)
        return {"asked": corner}

    @emit()
    async def help_requested(self, corner: str):
        """Emitted when this robot needs a peer to take a corner."""
```

## Peers, not a master

Both robots run this driver and join the same fabric. Neither is in charge. Each pursues the shared goal *"the bed is made"* and exposes the same procedures, including:

| Procedure | What a peer can ask this robot to do |
| --- | --- |
| `pickUpBedSheet` / `putDownBedSheet` | Grip or release the sheet at a corner |
| `walkToNextCorner` | Move to the next unclaimed corner |
| `askForHelp` / `offerHelp` | Request a second robot at a corner, or volunteer for one |
| `getStatus` / `getGoalState` | Report the robot's state, or how much of the goal is done |
| `listPeers` / `getEventHistory` / `getHelpHistory` | Discover other robots and read the shared event and help streams |
| `emergencyStopAll` | Fail-closed stop broadcast to every peer |

Coordination emerges from these calls: a robot claims a corner, emits an event, and — when a corner needs two hands — calls `askForHelp`; the other robot sees the event, calls `offerHelp`, and walks over. A peer finds the others and calls them through the SDK's fleet API — discover who is on the fabric, then invoke a procedure on a specific peer:

```python
peers = await self.fleet.discover()                 # the peer robots on the fabric
await self.fleet.invoke(peers[0].device_id, "offerHelp", corner="head-left")
```

## Loopback versus a real fabric

The transport under this coordination is selectable at run time, which is why the same demo code runs two ways:

- **`--loopback`** (the default you used) wires the peers through an **in-process MHS message bus**. Nothing leaves the machine; it is the self-contained way to run and reproduce the demo.
- **`--broker`** registers both robots on a **real NATS fabric** (`nats://...`) using credential files. On a real fabric the peers are visible to any other MHS tool on the network, and to agents driving the fleet.

The driver code does not change between the two — only the transport the SDK connects does. That separation of *what a device exposes* from *how it is reached* is the point of an MHS device layer, and it is what lets one bed-making driver run offline in simulation today and on a broker across a real fleet tomorrow.

{{% notice Note %}}
**Where this comes from.** The `MhsDriver` base and the `@rpc`/`@emit` decorators are the driver framework Arm Device Connect contributed to MHS. If you have seen a Device Connect driver, this is the same shape — `DeviceDriver` became `MhsDriver`, and a device you register on the fabric is discovered and invoked the same way. Migrating a robot connector from Device Connect onto MHS is an import change, not a rewrite.
{{% /notice %}}

Continue to the next step to look at the reinforcement-learning policy that keeps each robot balanced while it reaches.
