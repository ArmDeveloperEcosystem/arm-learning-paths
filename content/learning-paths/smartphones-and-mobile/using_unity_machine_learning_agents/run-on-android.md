---
title: Run on Android
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Getting it running on an Android device
1. Make sure your Android device is in [developer mode](https://developer.android.com/studio/debug/dev-options#enable). This will allow Unity to deploy to it. If you Android phone is from a company not mentioned in the aforementioned link, you may have to search their site for how to set developer mode.

2. Attach your Android device to your computer via USB cable.

3. You will probably have pop-ups to accept on the phone: “Allow usb debugging” and “Allow access to phone data”. Accept them if so.

4. If you need to troubleshoot your connection to the Android phone, there is a utility `adb` you can run from the command-line. This gets installed with the Unity Android options, but you may need to add its path to your *System Path* in your *Environment Variables*. If you've installed Unity to the default location on Windows, the path to add will be `C:\Program Files\Unity\2021.3.11f1\Editor\Data\PlaybackEngines\AndroidPlayer\SDK\platform-tools`. The adb command to run to check connection will then be:

`adb devices`

And then your phone should be listed.

5. Within the Unity Editor got to _File->Build Settings_.

![File Build Settings Menu](build-settings-menu.png "Figure 1. File Build Settings Menu")

6. Within the _Build Settings_ dialog select _Android_ from the _Platform_ list on the left.

7. In the bottom right of the dialog click the _Switch Platform_ button.

![Build Settings Dialog](build-settings-dialog.png "Figure 2. Build Settings Dialog")

8. Unity will take 1 or 2 minutes to switch platforms and prepare the assets for the mobile device.

9. Once switched the Unity icon will appear next to _Android_. On the bottom right the _Build_ button will be visible and the _Build and Run_ button will not be disabled.

![Platform Switched to Android](build-settings-platform-switched.png "Figure 3. Platform Switched to Android")

10. Now click _Build and Run_ to build and deploy the game to your Android device. It may take a few minutes the first time to go through the whole process. Subsequent Build and Runs should be much faster.

11. The game should now be running on your Android device.

![ML Gameplay](ml-gameplay.png "Figure 4. ML Gameplay")