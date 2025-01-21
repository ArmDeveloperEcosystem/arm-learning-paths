---
# User change
title: "What is Code Coverage?"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Code coverage is a methodology for testing and verification of your application, and is often a requirement for certification of your product in safety critical and other fields.

A code coverage report highlights which areas of your code base have been run through by your tests. A common use case may be to verify that all cases of a C switch statement have been triggered.

Code coverage in MDK can be performed with the provided Fixed Virtual Platforms (FVPs) or with real target hardware. This Learning Path uses FVPs.

{{% notice Real hardware %}}
MDK uses instruction trace (ETM trace) from target hardware to generate this report. Your target hardware must therefore support trace functionality, and you must have access to [ulinkPro](https://www2.keil.com/mdk5/ulink/ulinkpro) or similar supported debug adapter to collect this data from the target.
{{% /notice %}}
