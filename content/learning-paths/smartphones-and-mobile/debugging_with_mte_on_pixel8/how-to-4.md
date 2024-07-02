---
title: Debugging in Android Studio with MTE
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Debugging in Android Studio
Your are now ready to debug the MTE Test application in Android Studio.
Connect your Google Pixel 8 smatphone to your computer with the MTE Test project opened in Android Studio.
You should see the device name in the box shown in the picture below.

![alt-text-2](pictures/05_android_sutio_device_connected.png "Device recognized by Android Studio.")

Press the *Debug* button as shown in the picture above to build and start debugging the application. Look at your device where the application is about to start. You will see the message below in your screen. Just wait until the application interface shopws up.

![alt-text-2](pictures/06_waiting_for_debugger.png "Waiting for Debugger message.")

Press the *Debug* button at the botton of the Android Studio window as shown in the picture below. This will open the debug console. The first time it could take around a minute for the console to show that Android Studio is "connected to the target VM".


![alt-text-2](pictures/07_debug_console.png "Debug terminal shows that Android Studio is connected to the target VM")

At this point you are ready to debug the application. Look at your device where the application is running.
Press any of the buttons of the application, for example, the first button that implements the case *Use After Free*.  As MTE is enabled, it detects a missmatch between the tag in the address and the tag in memory and the application crashes. The debug process will take you to the line inmediatly before to the instruction that triggers the memory safety bug, as shown in the picture below.

![alt-text-2](pictures/08_debugger_shows_memory_bug.png "Debugger signals the memory bug.")

Press the red square button at the top right to stop debugging.