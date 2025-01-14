---
title: "Optimizing"
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimizing

Developers can see [our ray tracing best practices](https://developer.arm.com/documentation/101897/latest/Ray-tracing) to learn more about how to optimize ray tracing content. 

[Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio) provides developers with a set of tools to help you ensure everything works correctly and efficiently:

-   [RenderDoc for Arm GPUs](https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs), with support for Ray Query, can help you debug your effects.

-   [Streamline Performance Analyzer](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) contains useful counters to optimize your ray tracing content, and verify you have a coherent and efficient ray traversal.

-   [Mali Offline Compiler](https://developer.arm.com/Tools%20and%20Software/Mali%20Offline%20Compiler) is an extremely useful tool. It is recommended that you use it to check the behavior of your ray tracing shaders. For ray tracing, it is important to ensure that ray traversal is hardware accelerated and not emulated.

See the [Arm Performance Studio learning path](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/ams) for more information about these tools.

On some occasions, like conditionally evaluating Ray Query, Arm GPUs are not able to use the ray tracing hardware and will instead use a slower solution using software emulation. Mali Offline compiler can help to detect this problem. Check that your shaders do not produce this line `Has slow ray traversal: true`. Proper hardware ray tracing should show this line `Has slow ray traversal: false`.