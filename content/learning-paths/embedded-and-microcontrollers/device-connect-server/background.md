---
title: Learn when to use Device Connect server for multi-network deployments
weight: 2

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## From device-to-device (D2D) to server

### The D2D model

The [device-to-device Learning Path](/learning-paths/embedded-and-microcontrollers/device-connect-d2d/) showed Device Connect in its simplest form. Each runtime is a peer on the same local network. Devices find each other automatically, exchange typed events, and call each other's remote procedure calls (RPCs) directly. There's no broker, registry, or cloud service to run.

This model works well for:
- Prototypes and lab demos
- Small fleets on one local area network (LAN)
- Scenarios where cloud round-trips would add unnecessary delay

### When D2D isn't enough

As your fleet grows beyond a single local network, D2D mode has limitations. You might need devices in different sites or regions to find and call each other, or a registry that remembers devices after they disconnect. You might also need stronger identity controls, credential rotation, or audit logs.

### When to add a server

Use a Device Connect server when you need:

- **Persistent registry** - survives device reboots and lets new clients list known devices
- **Distributed state** - shared between devices and agents, with leases and watches
- **Multi-network reach** - for devices and agents on different LANs, behind NAT, or in the cloud
- **Fleet-wide operations** - commissioning devices and rotating credentials
- **Stronger security** - per-device identity, JWT credentials, role-based ACLs, and audit logs

The [`device-connect-server`](https://github.com/arm/device-connect/tree/main/packages/device-connect-server) package is the layer that adds those capabilities on top of the edge software development kit (SDK) you already know.

## What the server adds

### Your device code stays the same

The server doesn't change how you write device code. Devices still use `DeviceDriver`, `@rpc`, `@emit`, `@periodic`, and `@on`. Clients and AI agents still use `discover_devices()` and `invoke_device()`.

### What changes: device discovery and trust

In D2D mode, each runtime discovers nearby peers directly. With a server, every device and agent connects to a shared service that handles:

- **Routing** - devices on different networks can join the same mesh
- **Registry** - clients can see known devices, their capabilities, and their last-known status
- **Shared state** - devices and agents coordinate through a common store
- **Commissioning** - each device gets its own trusted credential
- **Security controls** - TLS, mutual TLS (mTLS), JWT authentication, role-based access control, and audit logging

### Messaging backend options

Device Connect supports different messaging backends, including Zenoh, NATS, and Message Queuing Telemetry Transport (MQTT). In this Learning Path, you'll use the hosted portal with NATS credentials. That lets you focus on the device and agent code instead of running the server yourself.

## Commissioning: trusted device identity

Commissioning means giving a device or agent a trusted identity before it joins the mesh.

**Without commissioning**: A process is just code trying to connect.

**With commissioning**: The server can decide whether that process is allowed to publish, subscribe, register itself, or call RPCs.

### Credential formats by backend

- **Zenoh** - issues client TLS certificates signed by a shared certificate authority (CA)
- **NATS** - issues JWT credentials bound to your tenant

Both answer the same question: is this identity allowed on this mesh?

### What you'll use in this Learning Path

In this Learning Path, you'll use the [Device Connect portal](https://portal.deviceconnect.dev/) to download NATS credentials for three default identities on your tenant. Two identities will run simulated robot arms. The third identity will run the Python client or agent.

## Multi-network deployment architecture

### How components connect

The Device Connect server acts as the central coordination point for devices and agents across different networks.

In the diagram, pub/sub means publish/subscribe, KV means key-value, LC means LangChain, and MCP means Model Context Protocol.

**Device Connect server architecture**

```
┌──────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  Devices         │     │  Device Connect      │     │  AI agents          │
│  (edge SDK)      │     │  server              │     │  (agent-tools)      │
│  DeviceDriver    │◄───►│  Pub/sub  ·  Registry│◄───►│  discover_devices() │
│  @rpc  @emit     │     │  KV       ·  Security│     │  invoke_device()    │
│  @periodic  @on  │     │                      │     │  Strands / LC / MCP │
└──────────────────┘     └──────────────────────┘     └─────────────────────┘
```

*The Device Connect server acts as the central hub, routing messages and managing security between edge devices and AI agents.*

Devices and agents still talk to each other through the same primitives (`@rpc`, `@emit`, `discover_devices`, `invoke_device`). The Device Connect server runs the publish/subscribe messaging, the persistent registry, the shared key-value store, and the security layer in one place.

### Real-world example: global device coordination

The animation demonstrates a complete multi-network workflow: a Device Connect server runs in Berlin, robot arms in San Francisco and Tokyo register with it using `device-connect-edge`, and an AI agent in Bangalore orchestrates both robots using `device-connect-agent-tools`. Every `invoke_device` call and event flows through the server, demonstrating how the server enables secure, multi-network device coordination.

<video width="100%" controls muted playsinline>
  <source src="https://raw.githubusercontent.com/kavya-chennoju/arm-learning-path-assets/main/videos/device-connect-server-overview.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## What you'll do in this Learning Path

In the rest of this Learning Path you'll:

- sign in to the Device Connect portal and identify your tenant slug
- download credentials for the three default device identities
- run two simulated robot arms with `device-connect-edge`
- discover and invoke both devices from a Python client using `device-connect-agent-tools`
- optionally attach a Strands AI agent to the same tenant

The next section walks through the setup.
