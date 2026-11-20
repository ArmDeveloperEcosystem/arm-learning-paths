---
title: Enable the Arm Neural Graphics plugin
description: Prepare your Unreal Engine project for NFRU evaluation using the Arm Neural Graphics plugin and the existing integration setup guides.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare your Unreal project for NFRU evaluation

Project Moku is an internal Arm project and is not currently available to external developers. Its captures provide the case-study scenarios; you can follow the setup and evaluation workflow with your own Unreal Engine project.

Follow the [NFRU integration Learning Path](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/) for current plugin compatibility and setup requirements. Use an existing compatible Unreal Engine C++ project, or create the template project described in that guide.

Follow the relevant setup instructions:

- [Set up the development environment](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/2-set_up_the_development_environment/) for tools, plugin source, dependencies, and Windows ML emulation layers
- [Set up the Unreal project with NFRU enabled](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/3-set_up_the_unreal_project/) for installing the complete plugin folder, rebuilding the project, selecting Vulkan, and configuring the backbuffer and NFRU settings

Use the complete plugin copy described in the integration guide. If your project already contains a plugin copy, check its version before replacing it. Keep the plugin and SDK from the same checkout.

## Confirm your test configuration

Open your project and confirm that the plugin loads with NFRU enabled. Use [Validate NFRU in Unreal Engine](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/4-validate_nfru_in_unreal_engine/) for the initial activation check and troubleshooting.

Record the plugin commit, SDK submodule revision, and Unreal Engine version with your test results. This identifies the build behind your captures when you compare visual quality or performance across versions.

Choose a scene with camera or object movement that you can replay consistently. You can use the Moku comparisons as visual references while capturing your own scene.

Next, use Streamline and RenderDoc to validate NFRU and inspect generated frames in your project.
