---
title: Set up Open AD Kit
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Execute Autoware Open AD Kit on an Arm Neoverse platform

Leveraging the high-performance computing power of Arm Neoverse CPUs and their comprehensive software ecosystem, you can run automotive software simulations on any Neoverse computing platforms.

You can use either an Arm Cloud Instance or on-premise servers to run Open AD Kit.
The example has been tested on [AWS EC2](https://aws.amazon.com/ec2/) and an [Ampere Altra workstation](https://www.ipi.wiki/products/ampere-altra-developer-platform), allowing you to choose the most suitable setup based on your needs.

## Installation

You need Docker to run Open AD Kit. Refer to the [Docker install guide](/install-guides/docker/) to learn how to install Docker on an Arm platform.

First, verify Docker is installed on your development computer by running:

```bash
docker --version
```

If Docker is installed, it will display version information similar to the output below:

```output
Docker version 28.0.4, build b8034c0
```

Clone the demo repository using:

```bash
git clone https://github.com/odincodeshen/openadkit_demo.autoware.git
```

The project is containerized in three Docker images, so you do not need to install any additional software.

## Understanding the Open AD Kit Demo Packages

The Open AD Kit demo consists of three core components: `simulator`, `planning-control`, and `visualizer`, each serving a distinct function.

### Simulator: Generating the Scenario

The simulator is responsible for creating a virtual driving environment to test and validate autonomous driving functionalities. It can simulate various driving scenarios, road conditions, and traffic situations, providing a realistic testbed for planning and control modules.

The Key Functions of Simulator are:

- Simulates autonomous driving environments
- Generates sensor data (LiDAR, cameras, radar, IMU)
- Publishes vehicle state information (position, speed, heading) via ROS 2 topics for other components to process
- Feeds data to planning-control for trajectory planning
- Acts as a data source for visualizer to render the simulation

Interaction with Other Components:
- Provides vehicle states and sensor data to planning-control
- Acts as the primary data source for visualizer

The command below starts a new Docker container named `simulator`, ensuring it runs in interactive mode with a terminal and is automatically removed upon stopping, while using a predefined Docker image pulled from the GitHub Container Registry.

```bash
docker run --name simulator --rm -it ghcr.io/autowarefoundation/demo-packages:simulator
```

### Planning-Control

The planning-control module is responsible for path planning and vehicle control. It uses data from the simulator to determine the optimal path and send control commands (steering, acceleration, braking) back to the simulator.

The Key Functions of Planning-Control:
- Receives sensor data and map information from simulator
- Computes motion planning and generates optimal trajectories
- Generates control commands (steering, acceleration, braking) and sends them to the simulator for execution in the virtual environment
- Acts as the decision-making unit for vehicle movement

Interaction with Other Components:
- Receives sensor inputs and vehicle states from simulator
- Sends planned trajectories and control commands back to simulator
- Feeds trajectory and control data to visualizer for display

This command starts a new Docker container named `planning-control`, ensuring it runs in interactive mode with a terminal and is automatically removed upon stopping, while using a predefined Docker image pulled from the GitHub Container Registry. Additionally, it connects to the host network to enable seamless ROS 2 communication with other components, such as the simulator and visualizer.

```bash
docker run --name planning-control --rm -it --network host ghcr.io/autowarefoundation/demo-packages:planning-control
```

### Visualizer

The visualizer provides real-time visualization of the simulation, including vehicle movement, planned trajectories, sensor outputs, and the driving environment. It enables developers to analyze and debug system behavior visually.

The Key Functions of Visualizer:
- Subscribes to ROS topics from simulator and planning-control
- Displays vehicle position, planned trajectories, and sensor readings
- Uses RViz & VNC for rendering visual outputs
- Supports remote access via Ngrok or VNC

Interaction with Other Components:
- Receives sensor and vehicle state data from simulator
- Receives planned trajectories and control commands from planning-control
- Presents a visual representation of all ROS 2 topic data

This command starts a new Docker container named `visualizer`, ensuring it runs in interactive mode with a terminal and is automatically removed upon stopping. It maps port 6080 from the container to the host, enabling remote visualization via a web browser, allowing users to view real-time simulation data using VNC-based visualization tools.

```bash
docker run --name visualizer --rm -it -p 6080:6080 ghcr.io/autowarefoundation/demo-packages:visualizer
```

After gaining a basic understanding of Open AD Kit, the next section will guide you through running three containers simultaneously on a single physical machine.
