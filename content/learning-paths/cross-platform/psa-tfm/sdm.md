---
# User change
title: Demonstrate Authenticated Debug

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
If you built the binaries with authenticated debug enabled in the previous step, you can demonstrate this with [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) (2022.2 or later).

See [Install Guide](http://localhost:1313/install-guides/armds/) for instructions on how to install and set up Development Studio if needed.

Connect the MPS3 board to your host via an appropriate [DSTREAM](https://developer.arm.com/Tools%20and%20Software/DSTREAM-ST#Editions) debug adapter.

## Secure Debug Manager

On the machine where Development Studio is installed, clone the [Secure Debug Manager](https://github.com/ARM-software/secure-debug-manager) library repository.
```command
git clone https://github.com/ARM-software/secure-debug-manager
```
This contains a ready-to-use Development Studio configuration database.

## Add configdb to Arm Development Studio

Open Arm Development Studio IDE, and (optionally) create a new workspace.

Navigate to `Window` > `Preferences` > `Arm DS` > `Configuration Database`, and click on `Add`, to add a new `User Configuration Database`.

Browse to the above repository, and (optionally) give a meaningful name.
```output
secure-debug-manager/arm_ds/DB
```
This adds a new debug configuration, `MPS3_Corstone-1000_ADAC`.

Click `Rebuild Database`, then `Apply and Close`.

## Create Debug Connection

Using the `MPS3_Corstone-1000_ADAC` configuration, create a [debug connection](https://developer.arm.com/documentation/101469/latest/Debugging-code/Configuring-a-connection-to-a-bare-metal-hardware-target) to the `Cortex-A35` processor on the MPS3 development board.

When you attempt to connect, you will be prompted for a key-chain pair. Failing to provide such a pair will result in a failure to connect.

An example pair are provided in the `secure-debug-manager` repository:
```console
/secure-debug-manager/tree/master/example/data/keys/EcdsaP256Key-3.pem
/secure-debug-manager/tree/master/example/data/chains/chain.EcdsaP256-3
```
