---
title: Manage Camera Permissions
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the app on your device

1. Connect your Android device to your computer with a USB data cable. 

    If this is your first time running and debugging Android apps, follow the guidance on the webpage [Set up a device for development](https://developer.android.com/studio/run/device#setting-up) on the Android Developer website, and check that you have done these two steps:
    
    * You have enabled USB debugging on your Android device following this webpage [Enable USB debugging on your device](https://developer.android.com/studio/debug/dev-options#Enable-debugging), also on the Android Developer website. 
    
    * You have confirmed that you have enabled USB debugging by tapping **OK** on your Android device when the **Allow USB debugging** dialog pops up, and that you have checked **Always allow from this computer**.

    ![AllowUSBDebugging alt-text#center](https://ftc-docs.firstinspires.org/en/latest/_images/AllowUSBDebugging.jpg "Figure 6: Allow USB Debugging.")


2. Make sure that your device model name and SDK version correctly show up on the top-right toolbar. Click the **Run** button to build and run the app.

3. After a while, you should see a success notification in Android Studio and the new app will be displayed on your Android device. 

4. However, you will see that the app shows a black screen while printing error messages in your [Logcat](https://developer.android.com/tools/logcat), which looks like this:

```
2024-11-20 11:15:00.398 18782-18818 Camera2CameraImpl       com.example.holisticselfiedemo      E  Camera reopening attempted for 10000ms without success.
2024-11-20 11:30:13.560   667-707   BufferQueueProducer     pid-667                              E  [SurfaceView - com.example.holisticselfiedemo/com.example.holisticselfiedemo.MainActivity#0](id:29b00000283,api:4,p:2657,c:667) queueBuffer: BufferQueue has been abandoned
2024-11-20 11:36:13.100 20487-20499 isticselfiedem          com.example.holisticselfiedemo      E  Failed to read message from agent control socket! Retrying: Bad file descriptor
2024-11-20 11:43:03.408  2709-3807  PackageManager          pid-2709                             E  Permission android.permission.CAMERA isn't requested by package com.example.holisticselfiedemo
```

5. This is expected behavior because you haven't yet correctly configured the app's [permissions](https://developer.android.com/guide/topics/permissions/overview). Android OS restricts this app's access to camera features due to privacy constraints.

## Request camera permission at runtime

1. Navigate to `manifest.xml` in your `app` subproject's `src/main` path. 

    Declare the camera hardware and set the permissions by inserting the following lines into the `<manifest>` element. Ensure that it is declared outside and above the `<application>` element.

```xml
    <uses-feature
        android:name="android.hardware.camera"
        android:required="true" />
    <uses-permission android:name="android.permission.CAMERA" />
```

2. Navigate to `strings.xml` in your `app` subproject's `src/main/res/values` path.            
   Insert the following lines of text resources, which you will use at a later stage.

```xml
    <string name="permission_request_camera_message">Camera permission is required to recognize face and hands</string>
    <string name="permission_request_camera_rationale">To grant Camera permission to this app, please go to system settings</string>
```

3. Navigate to `MainActivity.kt` and add the following permission-related values to companion 
   object:

```kotlin
        // Permissions
        private val PERMISSIONS_REQUIRED = arrayOf(Manifest.permission.CAMERA)
        private const val REQUEST_CODE_CAMERA_PERMISSION = 233
```

4. Add a new method named `hasPermissions()` to check on runtime whether the camera permission has 
   been granted:

```kotlin
    private fun hasPermissions(context: Context) = PERMISSIONS_REQUIRED.all {
        ContextCompat.checkSelfPermission(context, it) == PackageManager.PERMISSION_GRANTED
    }
```

5. Add a condition check in `onCreate()` wrapping `setupCamera()` method, to request camera 
   permission on runtime.

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

1. Rebuild and run the app. Now you should see a dialog pop up requesting camera permissions. 

2. Depending on your Android OS version, tap **Allow** or **While using the app**(). Then you should see your own face in the camera preview. Good job!  

{{% notice Tip %}}
You might need to restart the app to observe the permission change take effect.
{{% /notice %}}

In the next section, you will learn how to integrate MediaPipe vision solutions. 
