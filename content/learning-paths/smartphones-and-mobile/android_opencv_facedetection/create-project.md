---
# User change
title: "Create a project, add OpenCV and read camera frames"

weight: 3

layout: "learningpathall"
---
## Before you begin
You will need a development computer with [Android Studio](https://developer.android.com/studio) installed (we have used Android Studio Jellyfish | 2023.3.1 Patch 1). 

## Create a project
Follow these steps to create a project and add OpenCV:

1. Open Android Studio on your development machine and then click the **+ New Project** icon:

![img1](Figures/01.png)

2. In the New Project window, select **Empty Views Activity**:

![img2](Figures/02.png)

3. Configure the project as follows (see figure below):
- Name: **Arm64.OpenCV.FaceDetection**
- Package name: **com.example.arm64opencvfacedetection**
- Save location: **select location**
- Language: **Kotlin**
- Minimum SDK: **API 24**
- Build configuration language: **Kotlin DSL**

![img3](Figures/03.png)

4. Click the **Finish** button. 

## Add OpenCV support
To add OpenCV for arm64, open the *build.gradle.ts (Module: app)*, and add the following line under the dependencies:

```JSON
implementation("org.opencv:opencv:4.10.0")
```

Then, click the **Sync Now** link in the top pane that appears.

From now on, you can use OpenCV in your application. In the next step, we will initialize OpenCV. To do so, we will slightly modify the application view to display the OpenCV initialization status in the TextView.

## Use OpenCV to retrieve camera frames
You will now initialize OpenCV and prepare the application to stream frames from the front camera. In the next step you will process the frames to detect faces in the video stream.

Start by creating the 
1. Under the Project (left window) double-click *app/res/layout/activity_main.xml*. This opens the view designer. 
2. Click the highglighted icon in the top right corner to switch to the XML view.

![img4](Figures/04.png)

3. Open the *AndroidManifest.xml* and add the following declarations (make sure to add them above the application tag):
```XML
<uses-permission android:name="android.permission.CAMERA"/>
<uses-feature android:name="android.hardware.camera"/>
```

4. Modify the *activity_main.xml* as shown below:

```XML
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="center"
        android:layout_marginTop="16dp">

        <!-- Start Preview Button -->
        <Button
            android:id="@+id/buttonStartPreview"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="Start"
            android:layout_marginEnd="8dp" />

        <!-- Stop Preview Button -->
        <Button
            android:id="@+id/buttonStopPreview"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="Stop"
            android:layout_marginStart="8dp"/>
    </LinearLayout>

    <org.opencv.android.JavaCameraView
        android:id="@+id/cameraView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_weight="0"
        android:scaleType="centerCrop"
        android:visibility="visible" />

</LinearLayout>
```

5. Open *MainActivity.kt* (*app/kotlin+java/com.example.arm64opencvcamera*), and replace the file contents with the following code:

```kotlin
package com.example.arm64opencvfacedetection

import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import org.opencv.android.CameraBridgeViewBase
import org.opencv.android.OpenCVLoader
import org.opencv.core.Mat

class MainActivity : AppCompatActivity(), CameraBridgeViewBase.CvCameraViewListener2 {
    private lateinit var buttonStartPreview: Button
    private lateinit var buttonStopPreview: Button

    private lateinit var openCvCameraView: CameraBridgeViewBase

    private var isPreviewActive = false
    private var isOpenCvInitialized = false

    private val cameraPermissionRequestCode = 100

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        buttonStartPreview = findViewById(R.id.buttonStartPreview)
        buttonStopPreview = findViewById(R.id.buttonStopPreview)

        openCvCameraView = findViewById(R.id.cameraView)

        isOpenCvInitialized = OpenCVLoader.initLocal()

        // Request access to camera
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
            != PackageManager.PERMISSION_GRANTED) {
            // Permission is not granted, request it
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.CAMERA),
                cameraPermissionRequestCode
            )
        }

        openCvCameraView.setCvCameraViewListener(this)
        openCvCameraView.setCameraIndex(1)

        buttonStartPreview.setOnClickListener {
            openCvCameraView.setCameraPermissionGranted()
            openCvCameraView.enableView()

            updateControls()
        }

        buttonStopPreview.setOnClickListener {
            openCvCameraView.disableView()

            updateControls()
        }

        updateControls()
    }

    private fun updateControls() {
        if(!isOpenCvInitialized) {
            buttonStartPreview.isEnabled = false
            buttonStopPreview.isEnabled = false
        } else {
            buttonStartPreview.isEnabled = !isPreviewActive
            buttonStopPreview.isEnabled = isPreviewActive
        }
    }

    override fun onCameraViewStarted(width: Int, height: Int) {
        isPreviewActive = true
    }

    override fun onCameraViewStopped() {
        isPreviewActive = false
    }

    override fun onCameraFrame(inputFrame: CameraBridgeViewBase.CvCameraViewFrame?): Mat {
        return inputFrame!!.rgba()
    }
}
```

The above Kotlin code first imports necessary Android and OpenCV libraries, including those for handling permissions and camera views. MainActivity extends AppCompatActivity and implements CameraBridgeViewBase.CvCameraViewListener2 for handling camera frames. There are several variables:

- buttonStartPreview and buttonStopPreview: Buttons to start and stop the camera preview.
- openCvCameraView: An instance of CameraBridgeViewBase for displaying camera frames.
- isPreviewActive and isOpenCvInitialized: Flags to track the preview state and OpenCV initialization status.
- cameraPermissionRequestCode: A constant for the camera permission request.

The onCreate method initializes the buttons and camera view. Checks and requests camera permission if not already granted. Then, it initializes OpenCV using OpenCVLoader.initLocal(). Then, we set the camera index to 1 to get an access to the front camera. Subsequently, we configure onClickListeners for the buttons to start and stop the camera preview.

Finally, we call updateControls(), which updates the enabled state of the start and stop preview buttons based on whether OpenCV is initialized and if the preview is active.

The above code also declares CameraBridgeViewBase.CvCameraViewListener2 methods: onCameraViewStarted, onCameraViewStopped, and onCameraFrame. The first two will be called when the camera view starts or stops. Here, we use these methods to set the isPreviewActive variable. The last method will be called for each frame from the camera. Here, we just pass the camera frame as OpenCV's Mat object. In the next step we will extend this implementation to detect faces.

We have just prepared the application to stream camera frames. You can run the application as in this [learning path](/content/learning-paths/smartphones-and-mobile/android_opencv_camera). After running the application, give it an access to the camera, and click the Start button. You will see the images from the front device's camera.