---
title: Understand Device Connect server capabilities
weight: 2

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## From device-to-device (D2D) to server

The [device-to-device Learning Path](/learning-paths/embedded-and-microcontrollers/device-connect-d2d/) showed Device Connect in its simplest shape. Each runtime is a peer on the same local network. Devices find each other automatically, exchange typed events, and call each other's remote procedure calls (RPCs) directly. There is no broker, registry, or cloud service to run.

That model is useful when everything is close together. It works well for prototypes, lab demos, and small fleets on one local area network (LAN). It is also a good fit when a cloud round-trip would add unnecessary delay.

As soon as the fleet grows, D2D mode starts to run out of road. You may need devices on different networks to talk to each other. You may need a registry that remembers devices after they disconnect. You may also need stronger identity, credential rotation, or audit logs.

Use a Device Connect server when you need:

- a **persistent registry** that survives device reboots and lets new clients list known devices
- **distributed state** shared between devices and agents, with leases and watches
- **multi-network reach** for devices and agents on different LANs, behind network address translation (NAT), or in the cloud
- **fleet-wide operations** such as commissioning devices and rotating credentials
- **stronger security controls** such as per-device identity, JSON Web Token (JWT) credentials, role-based access control lists (ACLs), and audit logs

The [`device-connect-server`](https://github.com/arm/device-connect/tree/main/packages/device-connect-server) package is the layer that adds those capabilities on top of the edge software development kit (SDK) you already know.

## What the server adds

The server doesn't change how you write device code. Devices still use `DeviceDriver`, `@rpc`, `@emit`, `@periodic`, and `@on`. Clients and AI agents still use `discover_devices()` and `invoke_device()`.

The server changes how devices find and trust each other. In D2D mode, each runtime discovers nearby peers directly. With a server, every device and agent connects to a shared service.

That shared service gives you a few fleet-level building blocks:

- **routing** so devices on different networks can join the same mesh
- **registry** so clients can see known devices, their capabilities, and their last-known status
- **shared state** so devices and agents can coordinate through a common store
- **commissioning** so each device gets its own trusted credential
- **security controls** such as Transport Layer Security (TLS), mutual TLS (mTLS), JSON Web Token (JWT) authentication, role-based access control, and audit logging

Device Connect supports different messaging backends, including Zenoh, NATS, and Message Queuing Telemetry Transport (MQTT). In this Learning Path, you'll use the hosted portal with NATS credentials. That lets you focus on the device and agent code instead of running the server yourself.

## A note on commissioning

Commissioning means giving a device or agent a trusted identity before it joins the mesh. Without commissioning, a process is just code trying to connect. With commissioning, the server can decide whether that process is allowed to publish, subscribe, register itself, or call an RPC.

The credential format depends on the messaging backend:

- with **Zenoh**, commissioning means issuing the device a client TLS certificate signed by a shared certificate authority (CA)
- with **NATS**, commissioning means issuing the device a JWT credential bound to its tenant

In both cases, the credential answers the same question: is this identity allowed on this mesh?

In this Learning Path, you'll use the [Device Connect portal](https://portal.deviceconnect.dev/) to download NATS credentials for three default identities on your tenant. Two identities will run simulated robot arms. The third identity will run the Python client or agent.

## Where this sits in the architecture

In the diagram, pub/sub means publish/subscribe, KV means key-value, LC means LangChain, and MCP means Model Context Protocol.

```
┌──────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  Devices         │     │  Device Connect      │     │  AI agents          │
│  (edge SDK)      │     │  server              │     │  (agent-tools)      │
│  DeviceDriver    │◄───►│  Pub/sub  ·  Registry│◄───►│  discover_devices() │
│  @rpc  @emit     │     │  KV       ·  Security│     │  invoke_device()    │
│  @periodic  @on  │     │                      │     │  Strands / LC / MCP │
└──────────────────┘     └──────────────────────┘     └─────────────────────┘
```

Devices and agents still talk to each other through the same primitives (`@rpc`, `@emit`, `discover_devices`, `invoke_device`). The Device Connect server runs the publish/subscribe messaging, the persistent registry, the shared key-value store, and the security layer in one place.

The animation shows a complete workflow: a Device Connect server runs in Berlin, robot arms in San Francisco and Tokyo register with it using `device-connect-edge`, and an AI agent in Bangalore orchestrates both robots using `device-connect-agent-tools`. Every `invoke_device` call and event flows through the server, demonstrating how the server enables multi-network device coordination.

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
