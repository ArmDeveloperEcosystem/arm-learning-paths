---
title: Enable ArmNG Unreal plugin
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Install the required tools and dependencies

Before enabling the Arm neural-graphics-for-unreal plugin, make sure that all required tools and dependencies are installed and configured. For complete setup instructions, see [Set up the development environment](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/2-set_up_the_development_environment/).


## Set up Arm neural-graphics-for-unreal

If you cloned `armng-unreal` outside your Unreal project directory, create a symbolic link in the project's `Plugins` folder. The symbolic link allows Unreal Engine to detect the plugin as part of your project.

Run the following command in Command Prompt. Replace the paths with your project path and the location of the `armng-unreal` clone:

```console
mklink /D "C:\Path\To\YourProject\Plugins\armng-unreal" "C:\Path\To\armng-unreal"
```

After creating the symbolic link, regenerate your Visual Studio solution so Unreal Engine can detect the plugin. Use one of the following methods:

1. Use the Windows context menu: Select your `.uproject` file in File Explorer, then select **Generate Visual Studio project files**.

2. Use the command line: Open Command Prompt and run the following command, replacing the paths with your Unreal Engine installation path and project path.

```console
"C:\Program Files\Epic Games\UE_5.6\Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.exe" -projectfiles -project="C:\PathToYourProject\YourProject.uproject" -game -engine
```

After regenerating the Visual Studio solution, follow [Set up the Unreal project](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/3-set_up_the_unreal_project/) to enable the plugin in your `.uproject` file or through the Unreal Editor Plugins window, rebuild the project, confirm that it uses Vulkan RHI, and verify that NFRU functions correctly.

## What you've learned and what's next

You created a symbolic link to the plugin source and regenerated the Visual Studio solution. This configuration enables Unreal Engine to detect and load the Arm neural-graphics-for-unreal plugin.

Next, follow [Analyze NFRU enablement artifacts](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/3-analyze_nfru_enablement_artifacts/) to validate NFRU functionality and analyze its visual quality and performance impact.

