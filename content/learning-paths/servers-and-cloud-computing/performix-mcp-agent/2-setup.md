---
title: Build the example application and configure the target
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## About the example application

This Learning Path profiles the same Mandelbrot C++ application used in the [Find code hotspots with Arm Performix](/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/) Learning Path. It generates a 1920×1080 bitmap of the Mandelbrot set by iterating a simple recurrence for each pixel and is compute-heavy enough to produce clear profiling signal without requiring a long-running workload. The single-threaded build is intentionally unoptimized so that the hotspot analysis surfaces a meaningful target for improvement.

You don't need to understand the Mandelbrot algorithm to follow this Learning Path. It's used here as a convenient, reproducible benchmark for profiling on Arm Neoverse.

## Connect to your Arm target

This Learning Path targets an AWS Graviton3 metal instance (`m7g.metal`) with 64 Neoverse V1 cores. Any Arm Linux server with multiple cores works for the parallelization step, but a metal instance gives you direct access to all hardware threads without the overhead of virtualization.

You connect to the remote target via SSH through the Arm MCP Server. The `apx_recipe_run` tool accepts the target host IP address and SSH username directly as parameters, so there is no separate target configuration step required. Ensure your remote Arm server is reachable over SSH from the machine running your AI coding assistant, and follow the [Configure your MCP client](https://github.com/arm/mcp?tab=readme-ov-file#2-configure-your-mcp-client) instructions in the Arm MCP Server repository before continuing.

## Build the application on the remote server

In this section you'll build the debug binary for the Mandelbrot C++ application, the sample workload you'll profile in the next section.

Connect to the remote server over SSH and install the required build tools. On `dnf`-based systems such as Amazon Linux 2023 or RHEL, run:

```bash
sudo dnf update && sudo dnf install -y git gcc-c++ make
```

Clone the Mandelbrot repository and prepare the build directories. The repository is available under the [Arm Education License](https://github.com/arm-university/Mandelbrot-Example?tab=License-1-ov-file) for teaching and learning:

```bash
git clone https://github.com/arm-education/Mandelbrot-Example.git
cd Mandelbrot-Example
mkdir -p images build
```

Before building, update the output path in `src/main_single_thread.cpp`. Replace the first argument to `myplot.draw()` with the absolute path to your images directory:

```cpp
myplot.draw("/home/ec2-user/Mandelbrot-Example/images/green.bmp", Mandelbrot::Mandelbrot::GREEN);
```

{{% notice Note %}}
Replace `/home/ec2-user` with your actual home directory path if it differs.
{{% /notice %}}

Now build the single-threaded debug binary. The `DEBUG=1` flag disables compiler optimizations (`-O0`) and includes debug symbols (`-g`) and frame pointers (`-fno-omit-frame-pointer`), both of which are required for accurate flame graphs:

```bash
make single_thread DEBUG=1
```

This produces the binary at `./build/mandelbrot_single_thread_debug`. Confirm it exists before continuing:

```bash
ls -lh build/mandelbrot_single_thread_debug
```

## Verify the binary path for Performix

Note the absolute path to the binary on the remote server. You'll need this when configuring the Code Hotspots recipe in the next section. For the default setup the path is:

```text
/home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread_debug
```

You now have everything in place: a compiled, debug-enabled binary on an Arm Neoverse target that Performix can reach. In the next section, you'll create a GitHub Copilot prompt file to drive the Code Hotspots recipe through the Arm MCP Server.
