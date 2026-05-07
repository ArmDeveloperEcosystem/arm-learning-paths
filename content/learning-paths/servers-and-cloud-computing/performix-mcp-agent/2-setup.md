---
title: Build the Mandelbrot example on Arm Neoverse
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the profiling target

In this section, you'll build the Mandelbrot C++ application on your remote Arm server and confirm that Arm Performix can reach the target.

## About the example application

This Learning Path profiles the same Mandelbrot C++ application used in the [Find code hotspots with Arm Performix](/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/) Learning Path. It generates a 1920×1080 bitmap of the Mandelbrot set by iterating a simple recurrence for each pixel and is compute-heavy enough to produce clear profiling signal without requiring a long-running workload. The single-threaded build is intentionally unoptimized so that the hotspot analysis surfaces a meaningful target for improvement.

You don't need to understand the Mandelbrot algorithm to follow this Learning Path.

## Connect to your Arm target

For profiling, the Learning Path targets an AWS Graviton3 metal instance (`m7g.metal`) with 64 Neoverse V1 cores. Any Arm Linux server with multiple cores works for the parallelization step, but a metal instance gives you direct access to all hardware threads without the overhead of virtualization.

You connect to the remote target via SSH through the Arm MCP Server. The `apx_recipe_run` tool accepts the target host IP address and SSH username directly as parameters, so there is no separate target configuration step required. Ensure your remote Arm server is reachable over SSH from the machine running your AI coding assistant, and follow the [Configure your MCP client](https://github.com/arm/mcp?tab=readme-ov-file#2-configure-your-mcp-client) instructions in the Arm MCP Server repository before continuing.

## Build the application on the remote server

In this section you'll build the debug binary for the Mandelbrot C++ application, the sample workload you'll profile in the next section.

Connect to the remote server over SSH and install the required build tools. On `dnf`-based systems such as Amazon Linux 2023 or RHEL, run:

```bash
sudo dnf update && sudo dnf install -y git gcc-c++ make
```

Clone the Mandelbrot repository. The repository is available under the [Arm Education License](https://github.com/arm-university/Mandelbrot-Example?tab=License-1-ov-file) for teaching and learning:

```bash
git clone https://github.com/arm-education/Mandelbrot-Example.git
cd Mandelbrot-Example
make single_thread DEBUG=1
```

The command produces the binary at `./build/mandelbrot_single_thread_debug`. Confirm it exists before continuing:

```bash
ls -lh build/mandelbrot_single_thread_debug
```

## Verify the binary path for Performix

Note the absolute path to the binary on the remote server. You'll need this when configuring the Code Hotspots recipe in the next section. For the default setup the path is:

```text
/home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread_debug
```

You now have everything in place: a compiled, debug-enabled binary on an Arm Neoverse target that Performix can reach. In the next section, you'll create a GitHub Copilot prompt file to drive the Code Hotspots recipe through the Arm MCP Server.
