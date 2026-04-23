---
title: The developer model
weight: 3

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Device Connect developer model

### Device Connect Edge SDK

The [`device-connect-edge`](https://pypi.org/project/device-connect-edge/) package is the Python SDK you install on every device that joins a Device Connect network. It provides the building blocks for creating a device runtime: the `DeviceDriver` base class you subclass to describe a device, the decorators used to expose its capabilities to peers and agents, and the `DeviceRuntime` that brings a driver online on the network.

You describe a device by subclassing `DeviceDriver` from `device_connect_edge.drivers`, then annotating methods and properties with primitives. The runtime wires them into discovery, pub/sub, and RPC for you.

In this Learning Path you'll use these primitives to write two cooperating drivers: a **sensor** runtime that publishes temperature and humidity readings on a schedule, and a **threshold monitor** runtime that reacts to those readings and raises alerts when a threshold is crossed. The subsections below walk through the identity, decorators, and runtime you'll use to build them, and the agent tools package you'll use to invoke them from a separate client.

#### Identity and status

Every driver declares who it is and how it is doing. These are properties, not decorators:

- `identity` returns a `DeviceIdentity` (device type, manufacturer, model, description). This is what peers see during discovery.
- `status` returns a `DeviceStatus` (availability, location, optional health fields). This is the live signal other peers use to decide if the device is reachable and usable.

#### Behavior decorators

- `@rpc()`: exposes a method as a remote procedure. Other peers or agents call it by device ID and method name; the return value is serialized back to the caller.
- `@emit()`: declares that the method is an event publisher. Calling it inside the driver emits the event to any peer subscribed to it.
- `@periodic(interval=<seconds>)`: runs the method on a fixed schedule once the runtime starts. Useful for sampling, heartbeats, or housekeeping.
- `@on(event_name=<name>, device_type=<type>)`: subscribes the method to events emitted by other devices. The runtime delivers matching events as method calls with the source device id, event name, and a payload dict.

#### Runtime

`DeviceRuntime(driver=..., device_id=..., allow_insecure=...)` wraps your driver in a process that joins the pub/sub transport, advertises identity and status, and dispatches incoming RPCs and events to the decorated methods. You call `await runtime.run()` to keep it alive.

### Device Connect Agent tools

The [`device-connect-agent-tools`](https://pypi.org/project/device-connect-agent-tools/) package is the companion SDK for the client side of a Device Connect network: anything that wants to interact with devices on the mesh, from a short script or REPL to a full AI agent. It exposes a small set of functions that mirror the core capabilities of the protocol:

- `connect()`: joins the same pub/sub transport as the devices, so the following calls can see and reach them
- `discover_devices(device_type=..., device_id=...)`: returns a list of devices visible on the mesh, optionally filtered by type or ID
- `invoke_device(device_id, method_name, ...)`: calls an `@rpc` method on a specific device and returns the response

Any Python process that imports this package can find and drive devices without running a device runtime itself. In this Learning Path you'll use it from a third terminal to verify that the sensor and monitor runtimes are discoverable and callable.

## What you'll build

In this Learning Path you will build two cooperating simulated devices on the same local network:

- a **sensor** driver that publishes temperature and humidity readings on a schedule using `@rpc`, `@emit`, and `@periodic`
- a **threshold monitor** driver that uses `@on` to subscribe to the sensor's readings, emits its own `alert_raised` event when a reading crosses a threshold, and exposes the alert history through an `@rpc` method

You will run both devices as independent runtimes on one machine and watch the monitor react to the sensor in real time. Finally, you will use the agent tools package to discover both devices and query their RPCs from a separate terminal.

By the end, you will have a working D2D deployment where two devices find each other automatically and communicate through typed events and RPCs. This is the same pattern you would use to model a real sensor and a real supervisor on an edge network.

The next section walks through the full setup and test.
