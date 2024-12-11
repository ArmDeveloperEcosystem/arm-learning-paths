---
title: Handle camera permission
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the app on your device

1. Connect your Android device to your computer via a USB **data** cable. If this is your first time running and debugging Android apps, follow [this guide](https://developer.android.com/studio/run/device#setting-up) and double check this checklist:
    
    1. You have enabled **USB debugging** on your Android device following [this doc](https://developer.android.com/studio/debug/dev-options#Enable-debugging). 
    
    2. You have confirmed by tapping "OK" on your Android device when an **"Allow USB debugging"** dialog pops up, and checked "Always allow from this computer".

    ![Allow USB debugging dialog](https://ftc-docs.firstinspires.org/en/latest/_images/AllowUSBDebugging.jpg)


2. Make sure your device model name and SDK version correctly show up on the top right toolbar. Click the **"Run"** button to build and run, as described [here](https://developer.android.com/studio/run).

3. After waiting for a while, you should be seeing success notification in Android Studio and the app showing up on your Android device. 

4. However, the app shows only a black screen while printing error messages in your [Logcat](https://developer.android.com/tools/logcat) which looks like this:

```
2024-11-20 11:15:00.398 18782-18818 Camera2CameraImpl       com.example.holisticselfiedemo      E  Camera reopening attempted for 10000ms without success.
2024-11-20 11:30:13.560   667-707   BufferQueueProducer     pid-667                              E  [SurfaceView - com.example.holisticselfiedemo/com.example.holisticselfiedemo.MainActivity#0](id:29b00000283,api:4,p:2657,c:667) queueBuffer: BufferQueue has been abandoned
2024-11-20 11:36:13.100 20487-20499 isticselfiedem          com.example.holisticselfiedemo      E  Failed to read message from agent control socket! Retrying: Bad file descriptor
2024-11-20 11:43:03.408  2709-3807  PackageManager          pid-2709                             E  Permission android.permission.CAMERA isn't requested by package com.example.holisticselfiedemo
```

5. Worry not. This is expected behavior because we haven't correctly configured this app's [permissions](https://developer.android.com/guide/topics/permissions/overview) yet, therefore Android OS restricts this app's access to camera features due to privacy reasons. 

## Request camera permission at runtime

1. Navigate to `manifest.xml` in your `app` subproject's `src/main` path. Declare camera hardware and permission by inserting the following lines into the `<manifest>` element. Make sure it's **outside** and **above** `<application>` element.

```xml
    <uses-feature
        android:name="android.hardware.camera"
        android:required="true" />
    <uses-permission android:name="android.permission.CAMERA" />
```

2. Navigate to `strings.xml` in your `app` subproject's `src/main/res/values` path. Insert the following lines of text resources, which will be used later.

```xml
    <string name="permission_request_camera_message">Camera permission is required to recognize face and hands</string>
    <string name="permission_request_camera_rationale">To grant Camera permission to this app, please go to system settings</string>
```

3. Navigate to `MainActivity.kt` and add the following permission related values to companion object:

```kotlin
        // Permissions
        private val PERMISSIONS_REQUIRED = arrayOf(Manifest.permission.CAMERA)
        private const val REQUEST_CODE_CAMERA_PERMISSION = 233
```

4. Add a new method named `hasPermissions()` to check on runtime whether camera permission has been granted:

```kotlin
    private fun hasPermissions(context: Context) = PERMISSIONS_REQUIRED.all {
        ContextCompat.checkSelfPermission(context, it) == PackageManager.PERMISSION_GRANTED
    }
```

5. Add a condition check in `onCreate()` wrapping `setupCamera()` method, to request camera permission on runtime.

```kotlin
        if (!hasPermissions(baseContext)) {
            requestPermissions(
                arrayOf(Manifest.permission.CAMERA),
                REQUEST_CODE_CAMERA_PERMISSION
            )
        } else {
            setupCamera()
        }
```

6. Override `onRequestPermissionsResult` method to handle permission request results:

```kotlin
    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        when (requestCode) {
            REQUEST_CODE_CAMERA_PERMISSION -> {
                if (PackageManager.PERMISSION_GRANTED == grantResults.getOrNull(0)) {
                    setupCamera()
                } else {
                    val messageResId =
                        if (shouldShowRequestPermissionRationale(Manifest.permission.CAMERA))
                            R.string.permission_request_camera_rationale
                        else
                            R.string.permission_request_camera_message
                    Toast.makeText(baseContext, getString(messageResId), Toast.LENGTH_LONG).show()
                }
            }
            else -> super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        }
    }
```

## Verify camera permission

1. Rebuild and run the app. Now you should be seeing a dialog pops up requesting camera permissions! 

2. Tap `Allow` or `While using the app` (depending on your Android OS versions), then you should be seeing your own face in the camera preview. Good job!  

{{% notice Tip %}}
Sometimes you might need to restart the app to observe the permission change take effect.
{{% /notice %}}

In the next chapter, we will introduce MediaPipe vision solutions.
