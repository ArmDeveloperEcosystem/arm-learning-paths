---
# User change
title: "Debugging with Arm Fast Models"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Arm Fast Models](https://developer.arm.com/Tools%20and%20Software/Fast%20Models) are accurate, flexible programmer's view models of Arm IP. They are used to build a virtual platform, either standalone, or as part of Hybrid Simulation environment within EDA partner environments. Use the virtual platform for software development and verification throughout the development process, even long before any real hardware is available.

You can connect the [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) debugger to your virtual platform and interact with it as if were real hardware.

## Prerequisites

It is assumed you have installed Arm Development Studio and configured your license. For full instructions see [here](/install-tools/armds/).

It is also assumed you have installed Arm Fast Models and configured your license and build tools. For full instructions see [here](/install-tools/fm/).

### If Fast Models are not available

If you do not have access to Arm Fast Models, you can still learn how to connect to a custom virtual platform, using the same FVP as supplied with Development Studio (`bin` directory) instead.

## Build Fast Model example

A number of ready made example systems are provided with Arm Fast Models, including all of the Fixed Virtual Platform (FVP) examples.

We shall use the supplied `FVP_MPS2_Cortex-M3` Fast Models example, which is installed in the
```
FastModelsPortfolio_<version>\examples\LISA\FVP_MPS2\Build_Cortex-M3
```
directory of your Fast Models installation.

In Arm Fast Models `System Canvas`, use `File` > `Load project`, and navigate to the `FVP_MPS2_Cortex-M3.sgproj` project as above. Click `Build`.

## Create a Model Configuration for your Virtual Platform

In the `Arm Development Studio IDE` menu, select `File` > `New` > `Other` > `Configuration Database` > `Configuration Database`, and give it a meaningful name. This creates a project folder where the debugger stores all user-made configurations.

Then select `File` > `New` > `Other` > `Configuration Database` > `Model Configuration`, which will be the actual configuration we wish to create. When prompted, select the above `Configuration Database` to store in. Click `Next`.

You will be prompted to ask which debug interface to use, `Iris` or `CADI`. `Iris` is the default and recommended interface. Click `Next`.

You are then prompted to either launch the model, or browse for an already running model:

### Launch and connect to specific model

If this is selected, click `Next`, and browse for the Fast Model executable. The debugger will append necessary command options to enable debug. This is the most straight forward option, and recommended for first time users.

### Browse for model running on local host

If this is selected, you must previously have launched the Fast Model either from the command line, else via `System Canvas` > `Run` dialog, with `-I` option to start the Iris server in the model. If no port number (`--port-number`) is specified, recommend adding `-p` to output the port number used.

### Browse for model running on remote host

If this is selected (where the virtual platform is running on a different machine on the network), you must previously have launched the Fast Model either from the command line, else via `System Canvas` > `Run` dialog, with `-I -A` options to start the Iris server in the model and allow remote access. If no port number (`--port-number`) is specified, recommend adding `-p` to output the port number used. You will be prompted for the server address (the machine running the virtual platform) and port number.

Regardless of how you connect to the model, a `.mdf` file will be created. Specify an appropriate manufacturer and platform name, and click Import.

## Import Software example

If not previously imported, use `File` > `Import...` > `Arm Development Studio` > `Examples and Programming Libraries`, and browse for `startup_Cortex-M3_AC6` (use the text filter box to easily locate this).

Although this project is pre-configured to be debugged with the FVP supplied with Arm Development Studio, we shall instead debug on the newly built FVP.

## Create a new Debug Configuration for your Virtual Platform

Select `File` > `New` > `Model Connection`, and give it a meaningful name. It is recommended to associate with the specific project (`startup_Cortex-M3_AC6`).

Select the model configuration you created above (the text filter can assist if many targets defined), and click Finish.

You can again select to launch a new instance of the model (recommended) or connect to an already running model.

### Launch a new model

No further configuration needed.

### Browse for model running on local host

If this is selected, you must launch the Fast Model either from the command line, else via `System Canvas` > `Run` dialog, with `-I` option to start the Iris server in the model. If no port number (`--port-number`) is specified, recommend adding `-p` to output the port number used.

Specify the connection address as `localhost:<port>`

### Browse for model running on remote host

If this is selected (where the virtual platform is running on a different machine on the network), you must launch the Fast Model either from the command line, else via `System Canvas` > `Run` dialog, with `-I -A` options to start the Iris server in the model and allow remote access. If no port number (`--port-number`) is specified, recommend adding `-p` to output the port number used. You will be prompted for the server address (the machine running the virtual platform) and port number.

Specify the connection address as `hostname:<port>`

## Load image

Navigate to the `Files` tab, and browse (within Workspace) to the `startup_Cortex-M3_AC6.axf` pre-built image. Then, in the `Debugger` tab, select `Debug from entry point`.

If connecting to an already running model with a loaded image (`-a <image>`), select `Load symbols from file` from the `Files` tab. In this scenario, in the `Debugger` tab, select `Connect Only`.

Click `Debug` to connect to the virtual platform, and commence your debug session.
