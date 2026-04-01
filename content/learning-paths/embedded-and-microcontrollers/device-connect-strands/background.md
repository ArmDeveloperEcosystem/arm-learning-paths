---
title: Learn Device Connect and Strands architecture for edge devices
weight: 2

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why connect AI agents to edge devices?

Arm processors are at the heart of a remarkable range of systems - from Cortex-M microcontrollers in industrial sensors to Neoverse servers running in the cloud. That breadth of hardware is one of Arm's greatest strengths, but it raises a practical question for AI developers: how do you give an agent structured, safe access to devices that are physically distributed and built on different software stacks?

Device Connect is Arm's answer to that question. It's a platform layer that handles device registration, discovery, and remote procedure calls across a network of devices, with no bespoke networking code required. Strands is an open-source agent SDK from AWS that takes a model-driven approach to building AI agents - an LLM calls Python tools in a structured reasoning loop, and the SDK handles the rest. When you combine them, an agent can ask "which devices are online and what can they do?" and then invoke a function on a specific device, turning natural language intent into physical action.

You'll start with a single machine, for example a laptop, where a simulated robot and an agent discover each other automatically, then extend to a two-machine setup where a Raspberry Pi joins the same device mesh over the network.

## Device Connect architecture layers

**Device layer**

A device is any process that registers itself on the mesh and exposes callable functions. In this Learning Path you'll create a simulated robot arm, namely the simulated robotic arm SO-100 from Hugging Face, from the `strands-robots` SDK. When you create this object, it registers on the local network under a unique device ID (for example, `so100_sim-abc23`) and begins publishing a presence heartbeat. No explicit registration call is required. Device Connect uses Zenoh as its underlying messaging transport, which handles low-level connectivity and routing automatically.

**Agent layer**

Two interfaces sit at this layer. The `device-connect-agent-tools` package exposes `discover_devices()` and `invoke_device()` as plain Python functions you can call directly from a script or REPL, with no LLM involved. The `robot_mesh` tool from `robots` wraps the same capabilities as a Strands agent tool, which means an LLM can also call them during a reasoning loop. Both share the same underlying Device Connect transport, so anything you can do with one you can do with the other.

The diagram below shows how these layers communicate at runtime:

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

## How device discovery works

When you start the `SO-100 arm` instance, Device Connect automatically announces the device on the local network. Processes running `discover_devices()` or `robot_mesh(action='peers')` on the same network hear the announcement and add the device to their live table of available hardware.

## What the simulated robot provides

When you run `Robot('so100')`, the SDK downloads the MuJoCo physics model for the SO-100 arm (on first run only) and starts a local simulation. The robot exposes three functions that any agent can call via RPC:

- `execute` - start a task with a given instruction and policy provider
- `getStatus` - query the current task state
- `stop` - halt the current task

For this Learning Path, you'll use the `policy_provider='mock'` argument, which means `execute` accepts the call and returns `{'status': 'accepted'}` without actually running a motion policy. Focusing on connectivity and invocation patterns rather than robotics keeps the examples clear.

Once you have the flow working end to end, replacing `'mock'` with a real policy is a one-line change.

## What you'll learn in this Learning Path

By working through the remaining sections you'll:

- Clone the sample repository and install the Device Connect SDK, agent tools, and Strands robot runtime from source into a single virtual environment.
- Start a simulated robot that registers itself on the local device mesh.
- Discover and invoke the robot using `device-connect-agent-tools` directly.
- Discover and command the robot through the `robot_mesh` Strands tool, including an emergency stop.
- Optionally extend the setup to a Raspberry Pi connected over the network, discovering and commanding it from your laptop through the Device Connect infrastructure.

The next section covers the environment setup.