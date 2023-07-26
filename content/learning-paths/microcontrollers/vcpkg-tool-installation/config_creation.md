---
title: Create a vcpkg-configuration.json file
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a vcpkg-configuration.json file

A configuration file ensures a consistent installation of tools across all platforms. It installs the correct binaries depending on the platform (host OS and architecture). Thus, the first step is to create such a configuration file.

{{% notice Note %}}
If you are using the [conversion flow for MDK v5 uvprojx files](../../uvprojx-conversion/), a configuration file is automatically created.
{{% /notice %}}

Create a new file called `vcpkg-configuration.json`. The following template gives a good starting point for your own configuration file:

```json {line_numbers="true"}
{
  "registries": [
    {
      "kind": "artifact",
      "location": "https://aka.ms/vcpkg-ce-default",
      "name": "microsoft"
    },
    {
      "kind": "artifact",
      "location": "https://artifacts.keil.arm.com/vcpkg-ce-registry/registry.zip",
      "name": "arm"
    }
  ],
  "requires": {
    "arm:tools/open-cmsis-pack/cmsis-toolbox": "^2.0.0-0",
    "arm:compilers/arm/armclang": "^6.20.0",
    "arm:compilers/arm/arm-none-eabi-gcc": "^12.2.1-0",
    "microsoft:tools/kitware/cmake": "^3.25.2",
    "microsoft:tools/ninja-build/ninja": "^1.10.2"
  }
}
```

### Anatomy of the JSON file

- The `registries` section starting at line 2 specifies the locations containing the tools you want to install.
- The `requires` section starting at line 14 contains the tools you want to install. You can select specific versions of the tools in case you do not want to update automatically once a newer version is available. The entry `^6.20.0` specifies that the minimal version is 6.20.0 but all other version above are accepted as well.
- The [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox) requires at least one `compiler` (Arm Compiler for Embedded or GCC) to be installed, as well as `cmake` and `ninja`.

{{% notice Tip %}}
- Refer to the [vcpkg-configuration.json reference](https://learn.microsoft.com/en-gb/vcpkg/reference/vcpkg-configuration-json) for more information.
- You can also use vcpkg commands to work with the configuration file. Refer to [Working with the vcpkg-configuration.json file](../usage#working-with-the-vcpkg-configurationjson-file)
{{% /notice %}}

You can now start using the vcpkg environment.
