---
# User change
title: "Build and run Matter examples on Arm Virtual Hardware"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Fork Matter repository to your personal GitHub account

So that you can manage the development with GitHub actions later, you must create a personal fork of the public repository.

Browse to the Matter repository on Github:
```console
https://github.com/project-chip/connectedhomeip/fork
```
Create a fork in your own repository area, most likely at:
```
https://github.com/YOUR_GITHUB_USERNAME/connectedhomeip
```
## Clone your forked repository on your Raspberry Pi 4 AVH instances

Return to the `Console` tab of each of your Virtual Hardware instances, and clone your fork of the repository.
```console
git clone https://github.com/YOUR_GITHUB_USERNAME/connectedhomeip
cd connectedhomeip
```
A number of submodules must also be cloned, which can be done with a provided script:
```console
./scripts/checkout_submodules.py --shallow --platform linux
```
Repeat on other Virtual Hardware instance. You can set up each instance in parallel.

## Prepare Matter Development Environment

Configure the Matter development environment on each instance, which again can be done with a provided script(s):
```console
./scripts/build/gn_bootstrap.sh
source scripts/activate.sh
```
These will take a few minutes to complete. Don't forget to run scripts on each instance, which you can perform in parallel. You should see
```output
Environment looks good, you are ready to go!
```
when complete.

Full [documentation](https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/BUILDING.md) on the build environment is provided in the Matter repository.

## Build the examples

You are now ready to build the examples.

In the first Virtual Hardware instance you shall build `chip-tool`, a Matter controller implementation that allows to commission a Matter device into the network and to communicate with it using Matter messages.
```console
cd examples/chip-tool
gn gen out/debug
ninja -C out/debug
```
Full [documentation](https://github.com/project-chip/connectedhomeip/tree/master/examples/chip-tool) for `chip-tool` is provided in the repository.

In the other instance you shall build the reference `lighting-app` for Linux, which will be controlled by the above `chip-tool`.
```console
cd examples/lighting-app/linux
gn gen out/debug
ninja -C out/debug
```
Full [documentation](https://github.com/project-chip/connectedhomeip/tree/master/examples/lighting-app/linux) for `lighting-app` is provided in the repository.

Again, these builds can be performed in parallel. Confirm that both builds complete.

## Launch the lighting-app

In the `lighting-app` instance, run that application.
```console
./out/debug/chip-lighting-app
```
The application will initialize, and you will see boot log echoed in the console. You will see in the log:
```output
[TIMESTAMP][INSTANCEID] CHIP:DL: PlatformBlueZInit init success
```
Confirming it is ready to use (other messages in the log can be ignored).

Leave the `lighting-app` application running on this instance.

## Pair chip-tool

On the `chip-tool` instance, pair `chip-tool` with the `lighting-app` instance, using:
```console
./out/debug/chip-tool pairing onnetwork-long 0x11 20202021 3840
```
You will see a long stream of messages echoed in console of both instances. Wait for this command to complete and return.

If you wish to confirm success, you can see this in the logs (you will need to scroll back).

In `chip-tool`, you will see:
```
[TIMESTAMP][INSTANCEID] CHIP:TOO: Device commissioning completed with success
```
In `lighting-app`:
```
[TIMESTAMP][INSTANCEID] CHIP:ZCL: Commissioning complete, notify platform driver to persist network credentials.
```
Other messages in the log(s) can be ignored.

## Control lighting-app with chip-tool

The `lighting-app` can now be controlled with `chip-tool`, simulating remote control of a light bulb.

In the `chip-tool` instance, send a message to turn the light ON, using the command:
```console
./out/debug/chip-tool onoff on 0x11 1
```
Observe in the `lighting-app` log (you may need to scroll back a little) that this state is reflected with:
```output
[TIMESTAMP][INSTANCEID] CHIP:ZCL: Toggle ep1 on/off from state 0 to 1
[TIMESTAMP][INSTANCEID] CHIP:ZCL: On Command - OffWaitTime :  0
```
Similarly to turn the light OFF, in the `chip-tool` instance use:
```console
./out/debug/chip-tool onoff off 0x11 1
```
And observe in the `lighting-app` log:
```output
[TIMESTAMP][INSTANCEID] CHIP:ZCL: Toggle ep1 on/off from state 1 to 0
[TIMESTAMP][INSTANCEID] CHIP:ZCL: Setting on/off to OFF due to level change
```
Congratulations! You have successfully enabled two Virtual Hardware instances to communicate to each other via `Matter`.
