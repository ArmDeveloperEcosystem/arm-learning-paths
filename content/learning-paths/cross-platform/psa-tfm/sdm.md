---
# User change
title: Demonstrate Authenticated Debug

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
If you built the binaries with authenticated debug enabled in the previous step, you can demonstrate this with Arm Development Studio.

See [Install Guide](http://localhost:1313/install-guides/armds/) for instructions on how to install and set up Development Studio if needed.

## Secure Debug Manager

On the machine where Development Studio is installed, clone [Secure Debug Manager](https://github.com/ARM-software/secure-debug-manager) library repository.
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
Click `Rebuild Database`, then `Apply and Close`.

## Create Debug Connection



### Build SDM library (for your own application)
```console
cmake -S . -B build
cmake --build build/ --target install
```