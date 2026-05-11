---
title: Why add a Device Connect server
weight: 2

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## What D2D mode gives you, and where it stops

In device-to-device (D2D) mode, every Device Connect runtime is a peer on the same local network. Devices find each other through the messaging backend's local discovery (Zenoh's multicast scouting, or NATS running in a peer-to-peer configuration), exchange typed events, and call each other's RPCs directly. There is no central process to provision or maintain.

That is a great fit for prototyping, for small fleets on a shared LAN, and for time-sensitive applications where a cloud round-trip would be wasteful. It stops being a great fit when you need any of the following:

- a **persistent registry** that survives device reboots and lets a new client list every device that has ever connected, not just the ones online right this second
- **distributed state** shared between devices and agents, with leases and watches (for example, "which experiment is each device currently running?")
- **multi-network reach** for devices and agents on different LANs, behind NAT, or in the cloud
- **fleet-wide operations** like commissioning new devices, rotating credentials, or auditing every RPC that has ever been issued
- **security guarantees** beyond TLS on the wire, including per-device cryptographic identity, PIN-based onboarding, role-based ACLs, and audit logs

The [`device-connect-server`](https://github.com/arm/device-connect/tree/main/packages/device-connect-server) package is the layer that adds those capabilities on top of the edge SDK you already know.

## What the server adds

The server runtime ships as a small set of services you run alongside (or instead of) raw D2D scouting:

- a **messaging router** (Zenoh by default; NATS or MQTT as alternatives) so devices on different networks can reach the same mesh
- a **device registry service** that records every device, its identity, capabilities, and last-known status, in a persistent store
- an **etcd-backed distributed state store** that any device or agent can read and write through the Python API
- a **device commissioning flow** with PIN-based onboarding and per-device cryptographic identity (covered later in this Learning Path)
- optional **security infrastructure**: TLS/mTLS for Zenoh, JWT auth for NATS, role-based access control, audit logging

You can adopt these incrementally: run the dev-mode Docker Compose to get a router and registry running locally with no auth, then layer in TLS or JWT once you have the basics working.

## A note on commissioning

In a serious deployment, no device joins the mesh until it has been **commissioned**, meaning it has been given a cryptographic identity that the server trusts. The shape of that identity depends on the messaging backend:

- with **Zenoh**, commissioning means issuing the device a client TLS certificate signed by a shared CA
- with **NATS**, commissioning means issuing the device a JWT credential bound to its tenant

In both cases, the credential answers the question "is this device allowed on this tenant's mesh?" and prevents anyone else from impersonating it. In this Learning Path you will use the [Device Connect portal](https://portal.deviceconnect.dev/) to mint NATS credentials for your devices and your agent, then point each runtime at the tenant's NATS server. That replaces the local Docker setup with a hosted server you do not need to operate yourself.

## Where this sits in the architecture

```
┌──────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  Devices         │     │  Device Connect      │     │  AI agents          │
│  (edge SDK)      │     │  server              │     │  (agent-tools)      │
│  DeviceDriver    │◄───►│  Pub/sub  ·  Registry│◄───►│  discover_devices() │
│  @rpc  @emit     │     │  KV       ·  Security│     │  invoke_device()    │
│  @periodic  @on  │     │                      │     │  Strands / LC / MCP │
└──────────────────┘     └──────────────────────┘     └─────────────────────┘
```

Devices and agents still talk to each other through the same primitives (`@rpc`, `@emit`, `discover_devices`, `invoke_device`). The Device Connect server runs the pub/sub messaging, the persistent registry, the shared key-value store, and the security layer in one place.

The animation below shows the same idea end to end: a Device Connect server runs in Berlin (with Zenoh, NATS, or MQTT as the messaging backend), robots in San Francisco and Tokyo install `device-connect-edge` and register with it, and an AI agent in Bangalore installs `device-connect-agent-tools` and drives both robots through the server. Every `invoke_device` call and every event flows through Berlin.

<video width="100%" controls muted playsinline>
  <source src="https://raw.githubusercontent.com/kavya-chennoju/arm-learning-path-assets/main/videos/device-connect-server-overview.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## What you'll do in this Learning Path

In the rest of this Learning Path you will:

- start the server stack locally with Docker Compose
- connect a simulated number-generator device to it
- discover the registered device from a short Python client using `device-connect-agent-tools`
- attach a Strands AI agent that subscribes to events on the mesh

The next section walks through the setup.
