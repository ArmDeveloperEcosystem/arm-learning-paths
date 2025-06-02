---
title: Use vcpkg
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use vcpkg

The following commands help you to work with `vcpkg`. The most important one is `activate` as this activates all tools specified by the configuration file.

### Activate vcpkg

#### Activate tools specified by vcpkg-configuration.json

```bash { output_lines = "2-8" }
vcpkg-shell activate

warning: vcpkg-artifacts is experimental and may change at any time.
Artifact                                Version Status    Dependency Summary                                             
arm:tools/open-cmsis-pack/cmsis-toolbox 2.0.0   installed            Arm distributed Open-CMSIS-Pack cli tools           
arm:compilers/arm/armclang              6.20.0  installed            Arm Compiler for Embedded                           
microsoft:tools/kitware/cmake           3.25.2  installed            Kitware's cmake tool                                
microsoft:tools/ninja-build/ninja       1.10.2  installed            Ninja is a small build system with a focus on speed.
```

#### Deactivate artifacts specified by vcpkg-configuration.json

```bash { output_lines = "2-4" }
vcpkg-shell deactivate

warning: vcpkg-artifacts is experimental and may change at any time.
Deactivating: /Users/myuser/projects/myproject
```

#### Activating tools without vcpkg-configuration.json

```bash { output_lines = "2-5" }
vcpkg-shell use cmsis-toolbox

warning: vcpkg-artifacts is experimental and may change at any time.
Artifact                                Version Status    Dependency Summary                                  
arm:tools/open-cmsis-pack/cmsis-toolbox 2.0.0   installed            Arm distributed Open-CMSIS-Pack cli tools
```

#### Retrieve all available versions of a tool

```bash { output_lines = "2-14" }
vcpkg-shell use open-cmsis-pack

warning: vcpkg-artifacts is experimental and may change at any time.
error: Unable to resolve artifact: open-cmsis-pack
Possible matches:
  arm:tools/open-cmsis-pack/cmsis-toolbox-2.0.0
  arm:tools/open-cmsis-pack/cmsis-toolbox-2.0.0-dev3
  arm:tools/open-cmsis-pack/cmsis-toolbox-2.0.0-dev2
  arm:tools/open-cmsis-pack/cmsis-toolbox-2.0.0-dev1
  arm:tools/open-cmsis-pack/cmsis-toolbox-2.0.0-dev0
  arm:tools/open-cmsis-pack/ctools-2.0.0-dev0
  arm:tools/open-cmsis-pack/ctools-1.7.0
  arm:tools/open-cmsis-pack/ctools-1.6.0
  arm:tools/open-cmsis-pack/ctools-1.5.0
```

### List available artifacts

#### For example, tools

```bash { output_lines = "2-16" }
vcpkg-shell find artifact tools

warning: vcpkg-artifacts is experimental and may change at any time.
Artifact                                    Version    Summary                                             
microsoft:tools/kitware/cmake               3.25.2     Kitwares cmake tool                                
microsoft:tools/ninja-build/ninja           1.10.2     Ninja is a small build system with a focus on speed.
microsoft:tools/arduino/arduino-cli         0.18.3     Arduino IDE                                         
microsoft:tools/microsoft/openocd           0.12.0     Free and open on-chip debugging                     
arm:tools/arm/cmsis-core-tools              5.2.0      Arm CMSIS Core Tools                                
arm:tools/open-cmsis-pack/cmsis-toolbox     2.0.0      Arm distributed Open-CMSIS-Pack cli tools           
arm:tools/open-cmsis-pack/ctools            2.0.0-dev0 Arm distributed Open-CMSIS-Pack cli tools           
arm:tools/arm/uv2csolution                  v1.0.0     *.uvprojx/*.uvmpw to csolution/cproject converter   
```

#### For example, compilers

```bash { output_lines = "2-9" }
vcpkg-shell find artifact compilers

warning: vcpkg-artifacts is experimental and may change at any time.
Artifact                                                         Version        Summary                              
microsoft:compilers/arm-none-eabi-gcc                            10.3.1-2021.10 GCC compiler for ARM CPUs.           
arm:compilers/arm/llvm-embedded                                  16.0.0         LLVM Embedded Toolchain for Arm CPUs.
arm:compilers/arm/arm-none-eabi-gcc                              12.2.1-mpacbti GCC compiler for ARM CPUs.           
arm:compilers/arm/armclang                                       6.20.0         Arm Compiler for Embedded            
```

### Working with the vcpkg-configuration.json file

#### Create a new vcpkg-configuration.json file

```shell
vcpkg-shell new --application
```

#### Add artifact to vcpkg-configuration.json file

```shell
 vcpkg-shell add artifact cmake
```

#### Remove artifact to vcpkg-configuration.json file

```shell
 vcpkg-shell remove microsoft:tools/kitware/cmake
```

#### Update a registry

For example, the `arm` registry:

```shell
vcpkg-shell x-update-registry arm
```

Before using the Arm Compiler, you need to activate a license. The next step shows how to do that.
