---
title: Learn Device Connect and Strands architecture for edge devices
weight: 2

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Physical AI starts with connectivity

Natural language is becoming more than a software interface. Physical AI systems — robots, sensors, actuators — can now sense, decide, and act based on instructions from an LLM agent. But for that to work, the devices need to be reachable. They need a shared infrastructure for discovery, communication, and coordination.

[Device Connect](https://github.com/arm/device-connect) is Arm's device-aware framework for exactly that. Once devices register through a shared mesh, agents can discover and command any of them without caring where they run. A fleet of robot arms, a network of sensors, or a mix of physical and simulated devices all become equally reachable.

[Strands Robots](https://github.com/strands-labs/robots) is a robot SDK that integrates Device Connect with the [AWS Strands Agents SDK](https://github.com/strands-labs/sdk). Using Strands, an LLM can query the device mesh ("who's available?"), understand what each device can do, and dynamically invoke actions — turning natural language intent into real-world outcomes.

This Learning Path starts on a single machine, where a simulated robot and an agent discover each other automatically, then optionally extends to a Raspberry Pi joining the same device mesh over the network.

## How the pieces fit together

Two packages make this work.

**`device-connect-sdk`** is the device-side runtime. Any process that wraps a robot in a `DeviceDriver` and starts a `DeviceRuntime` joins the mesh: it registers itself, announces what it can do, and starts publishing state events. Zenoh handles low-level connectivity; in device-to-device mode no broker or environment configuration is needed.

**`device-connect-agent-tools`** is the agent-side runtime. It exposes `discover_devices()` and `invoke_device()` as plain Python functions. The `robot_mesh` tool in Strands Robots wraps the same interface as a Strands tool, so an LLM can call it too. Both use the same underlying transport, so the same calls work whether the caller is a script or an agent.

```
┌──────────────────────────────────────┐
│  Agent layer                         │
│  discover_devices · invoke_device    │
│  robot_mesh Strands tool             │
└──────────────┬───────────────────────┘
               │ Device Connect
               │ (device-to-device discovery & RPC)
┌──────────────▼───────────────────────┐
│  Device layer                        │
│  Simulated SO-100 arm                |
|           - so100-abc123             │
│  heartbeat · execute · getStatus     │
└──────────────────────────────────────┘
```

## What a device exposes

This Learning Path uses the SO-100 arm, a simulated robot arm from Hugging Face. When `Robot('so100').run()` starts, it registers on the mesh and exposes three callable functions. These are what `invoke_device()` on the agent side targets — calling `invoke_device("so100-abc123", "execute", {...})` routes a request over Zenoh to the robot process and executes the function there, returning the result back to the caller:

- `execute` — send a natural language instruction and a policy provider to the robot
- `getStatus` — query what the robot is currently doing
- `stop` — halt the current task, or `emergency_stop` to halt every device on the mesh at once

A motion policy is the component that translates a high-level instruction like "pick up the cube" into a sequence of joint movements. Different policy providers connect to different backends — from local model inference to remote policy servers. For this Learning Path, `policy_provider='mock'` is used, so `execute` accepts the task and returns immediately without running real motion. Replacing `'mock'` with a real provider like `'lerobot_local'` or `'groot'` is a one-line change once you have the connectivity working.

## What you'll learn in this Learning Path

By working through the remaining sections you'll:

- Clone the sample repository and install the Device Connect SDK, agent tools, and Strands robot runtime from source into a single virtual environment.
- Start a simulated robot that registers itself on the local device mesh.
- Discover and invoke the robot using `device-connect-agent-tools` directly.
- Discover and command the robot through the `robot_mesh` Strands tool, including an emergency stop.
- Optionally extend the setup to a Raspberry Pi connected over the network, discovering and commanding it from your laptop through the Device Connect infrastructure.

The next section covers the environment setup.