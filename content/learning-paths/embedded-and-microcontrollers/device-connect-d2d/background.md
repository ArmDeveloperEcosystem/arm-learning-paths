---
title: Why device-to-device at the edge
weight: 2

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why device-to-device matters at the edge

Arm processors sit at the heart of a remarkable range of systems, from Cortex-M microcontrollers in industrial sensors, to Cortex-A boards driving robots and appliances, to Neoverse servers in the cloud. Many edge applications need these devices to cooperate: a sensor publishes a reading, a supervisor reacts, a controller adjusts an actuator. The obvious way to wire that up is through a central broker or a cloud service, but both add latency, operational overhead, and a single point of failure you may not want in a lab, a vehicle, or a factory cell.

Direct device-to-device (D2D) communication sidesteps that. Devices on the same local network discover each other, exchange typed events, and call each other's functions directly, with no broker, no registry, and no cloud round-trip. It is a good fit for:

- prototyping sensor networks and local automation flows
- small fleets (roughly 50-100 devices) on a shared network
- lab setups, demos, and time-sensitive edge applications where a cloud hop would be wasteful

## Where Device Connect fits

Device Connect is Arm's open-source framework for structured edge communication. It gives every device a common language for four core capabilities:

- **Discovery**: devices advertise themselves and can be found by ID, type, or capability
- **RPC**: peers and agents invoke functions on a device and get a structured response
- **Status**: each device publishes a live availability and health signal
- **Events**: devices emit readings, state changes, or alerts as pub/sub messages

Device Connect supports more than one deployment shape. In this Learning Path you'll use its **D2D mode**: a peer-to-peer deployment where device runtimes find each other over the local network using Zenoh-backed multicast discovery. For larger, multi-network deployments, Device Connect also offers a full infrastructure mode with a central registry, but you do not need any of it to ship a working D2D application.

## D2D architecture at a glance

In D2D mode, every participant is a peer. Each device runtime joins the same pub/sub transport and takes part in discovery, events, and RPC on equal footing.

```
┌──────────────────────────────────────────────┐
│  Sensor device                               │
│  - device_id: sensor-001                     │
│  - @rpc  get_reading                         │
│  - @emit reading_ready  ─┐                   │
└──────────────────────────┼───────────────────┘
                           │ pub/sub (Zenoh)
                           │ discovery · RPC
┌──────────────────────────▼───────────────────┐
│  Threshold monitor                           │
│  - device_id: monitor-001                    │
│  - @on   reading_ready                       │
│  - @emit alert_raised                        │
│  - @rpc  get_recent_alerts                   │
└──────────────────────────────────────────────┘
```

No central server sits between the sensor and the monitor. They advertise themselves, find each other by event name, and exchange typed payloads directly.

## What you'll learn

By the end of this Learning Path you will:

- set up a Python project with uv, the Device Connect runtime, and the agent tools
- write two cooperating drivers: a simulated sensor and a threshold monitor that reacts to it
- run both as independent device runtimes on one machine
- use the Device Connect agent tools to discover both peers and invoke their RPCs

The next section covers the developer model.
