---
title: About Function Multiversioning
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is function multiversioning, and how does it work?

Function multiversioning enables the compiling of several implementations of a function into the same binary, and then selects the most appropriate version at runtime. The benefit of this is that you can use hardware features to accelerate applications at function level.

To specify a function version, you can annotate its declaration with either of  `__attribute__((target_version("name")))` or `__attribute__((target_clones("name",...)))`, where "name" denotes one or more architectural features separated by '+'. 

This annotation implies a dependency between a function version and the feature set it is specified for. The compiler generates optimized versions of the function for the specified targets. The `target_clones` attribute behaves in the same way as `target_version`, but specifies multiple versions for the same function definition. The former is suitable for functions that the compiler can optimize differently depending on the requested features, whereas the latter allows the user to manually optimize a version at source level using intrinsics or inline assembly.

A hardware platform is able to support multiple architectural features from the dependency sets, or it might not support any. 

Function multiversioning provides a convenient way to select the most appropriate version of a function at runtime. The selection is permanent for the lifetime of the process and works as follows:

1. Select the most specific version (the one with most features), else
2. Select the version with the highest priority, as indicated by the [mapping table](https://arm-software.github.io/acle/main/acle.html#mapping), else
3. Select a default version if no other versions are suitable.

The `default` version is the version of the function that is generated without these attributes.

Imagine your application has a hot function with a vectorizable loop. Your application must be deployed on hardware which only supports Armv8 instructions, but also on hardware which supports SVE instructions as well. By providing two function versions, a default and an SVE- specific, you can ensure optimal performance on either platform using the same binary.

See the [Arm C Language Extensions](https://arm-software.github.io/acle/main/acle.html#mapping) for a list of supported features and their priorities.
