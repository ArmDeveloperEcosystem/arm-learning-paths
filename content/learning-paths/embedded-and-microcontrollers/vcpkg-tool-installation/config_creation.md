---
title: Create a vcpkg-configuration.json file
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a vcpkg-configuration.json file

A configuration file ensures a consistent installation of tools across all platforms. It installs the correct binaries depending on the platform (host OS and architecture). Thus, the first step is to create such a configuration file.

{{% notice Notice of Product License Terms %}}
Your use of an Arm tool is subject to your acceptance of the End User License Agreement for Arm Software Development Tools, located within the `license_terms` folder of the downloaded archive. By installing and using the Arm tool, you agree to be bound by the terms and conditions of the End User License Agreement.
{{% /notice %}}

Create a new file called `vcpkg-configuration.json`. The following template gives a good starting point for your own configuration file:

```json {line_numbers="true"}
{
  "registries": [
    {
      "kind": "artifact",
      "location": "https://artifacts.tools.arm.com/vcpkg-ce-registry/registry.zip",
      "name": "arm"
    }
  ],
  "requires": {
    "arm:tools/kitware/cmake": "^3.25.2",
    "arm:tools/ninja-build/ninja": "^1.10.2",
    "arm:tools/open-cmsis-pack/cmsis-toolbox": "^2.0.0-0",
    "arm:compilers/arm/armclang": "^6.20.0",
    "arm:compilers/arm/arm-none-eabi-gcc": "^12.2.1-0"
  }
}
```

{{% notice Note %}}
If you are using the [conversion flow for MDK v5 uvprojx files](/learning-paths/embedded-and-microcontrollers/uvprojx-conversion/), a configuration file is automatically created.
{{% /notice %}}

### Anatomy of the JSON file

- The `registries` section starting at line 2 specifies the locations containing the tools you want to install.
- The `requires` section starting at line 9 contains the tools you want to install. You can select specific versions of the tools in case you do not want to update automatically once a newer version is available. The entry `^6.20.0` specifies that the minimal version is 6.20.0 but all other version above are accepted as well.
- The [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox) requires at least one `compiler` (Arm Compiler for Embedded or GCC) to be installed, as well as `cmake` and `ninja`.

{{% notice Tip %}}
- Refer to the [vcpkg-configuration.json reference](https://learn.microsoft.com/en-gb/vcpkg/reference/vcpkg-configuration-json) for more information.
- You can also use vcpkg commands to work with the configuration file. Refer to [Working with the vcpkg-configuration.json file](/learning-paths/embedded-and-microcontrollers/vcpkg-tool-installation/usage#working-with-the-vcpkg-configurationjson-file)
{{% /notice %}}

You can now start using the vcpkg environment.
