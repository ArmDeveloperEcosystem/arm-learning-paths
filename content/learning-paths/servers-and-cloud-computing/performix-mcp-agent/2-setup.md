---
title: Build the Mandelbrot example on Arm Neoverse
description: Build the Mandelbrot C++ example on an Arm Neoverse target and confirm that the dedicated Arm Performix MCP server can use the configured target.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the profiling target

You'll build and profile the Mandelbrot C++ application used in the [Find code hotspots with Arm Performix](/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/) Learning Path on your remote Arm server and confirm that Arm Performix can reach the target.

## About the example application

The application generates a 1920×1080 bitmap of the Mandelbrot set by iterating a simple recurrence for each pixel and is compute-heavy enough to produce clear profiling signal without requiring a long-running workload. The single-threaded build is intentionally unoptimized so that the hotspot analysis surfaces a meaningful target for improvement.

You don't need to understand the Mandelbrot algorithm to follow the Learning Path.

## Confirm your Arm Performix target

For profiling, you'll target an AWS Graviton3-based metal instance (`m7g.metal`) with 64 Neoverse V1 cores. Any Arm Linux server with multiple cores works, but a metal instance gives you direct access to all hardware threads without the overhead of virtualization.

The dedicated Arm Performix MCP server uses targets that are already configured in Performix. Record the friendly target name because you'll give it to your AI assistant in the next section.

If you haven't added the target, follow [Set up Arm Performix](/learning-paths/servers-and-cloud-computing/performix-get-started/add_target/). Remote authentication uses SSH keys, and strict host-key checking requires the target and any jump-node keys in `known_hosts`.

Test the configured connection from the host running Arm Performix. Replace `<target-name>` with the friendly target name:

```bash
apx target test --target <target-name>
```

Continue when the test confirms that Performix can reach the intended target.

## Build the application on the remote server

Build the debug binary for the Mandelbrot C++ application, the sample workload that you'll profile in the next section.

Connect to the remote server over SSH and install the required build tools.

On `dnf`-based systems such as Amazon Linux 2023 or RHEL, run:

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

Note the absolute path to the binary on the remote server. You'll need this when configuring the Code Hotspots recipe in the next section. For the default setup, the path is:

```text
/home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread_debug
```

## What you've accomplished and what's next

You've now got everything in place for profiling: a compiled, debug-enabled binary on an Arm Neoverse target that Performix can reach.

Next, you'll ask your AI assistant to run the Code Hotspots recipe through the Arm Performix MCP server.
