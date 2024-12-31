---
title: Create a new Android project
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This learning path will teach you to architect an app following [modern Android architecture](https://developer.android.com/courses/pathways/android-architecture) design with a focus on the [UI layer](https://developer.android.com/topic/architecture/ui-layer).

## Development environment setup

Download and install the latest version of [Android Studio](https://developer.android.com/studio/) on your host machine.

The instructions for this learning path were tested on a Apple Silicon host machine running macOS, but you may choose any of the supported hardware systems as described [here](https://developer.android.com/studio/install).

Upon first installation, open Android Studio and proceed with the default or recommended settings. Accept license agreements and let Android Studio download all the required assets.

Before you proceed to coding, here are some tips that might come handy:

{{% notice Tip %}}
1. To navigate to a file, simply double-tap `Shift` key and input the file name, then select the correct result using `Up` & `Down` arrow keys and then tap `Enter`.

2. Every time after you copy-paste a code block from this learning path, make sure you **import the correct classes** and resolved the errors. Refer to [this doc](https://www.jetbrains.com/help/idea/creating-and-optimizing-imports.html) to learn more.
{{% /notice %}}

## Create a new Android project

1. Navigate to File > New > New Project....

2. Select Empty Views Activity in the Phone and Tablet gallery as shown below, then click Next.
![Empty Views Activity](images/2/empty%20project.png)

3. Enter a project name and use the default configurations as shown below. Make sure that Language is set to Kotlin, and that Build configuration language is set to Kotlin DSL.
![Project configuration](images/2/project%20config.png)

### Introduce CameraX dependencies

[CameraX](https://developer.android.com/media/camera/camerax) is a Jetpack library, built to help make camera app development easier. It provides a consistent, easy-to-use API that works across the vast majority of Android devices with a great backward-compatibility.

1. Wait for Android Studio to sync project with Gradle files, this make take up to several minutes.

2. Once project is synced, navigate to `libs.versions.toml` in your project's root directory as shown below. This file serves as the version catalog for all dependencies used in the project.

![version catalog](images/2/dependency%20version%20catalog.png)

{{% notice Info %}}

For more information on version catalogs, please refer to [this doc](https://developer.android.com/build/migrate-to-catalogs).

{{% /notice %}}

3. Append the following line to the end of `[versions]` section. This defines the version of CameraX libraries we will be using.
```toml
camerax = "1.4.0"
```

4. Append the following lines to the end of `[libraries]` section. This declares the group, name and version of CameraX dependencies.

```toml
camera-core = { group = "androidx.camera", name = "camera-core", version.ref = "camerax" }
camera-camera2 = { group = "androidx.camera", name = "camera-camera2", version.ref = "camerax" }
camera-lifecycle = { group = "androidx.camera", name = "camera-lifecycle", version.ref = "camerax" }
camera-view = { group = "androidx.camera", name = "camera-view", version.ref = "camerax" }
```

5. Navigate to `build.gradle.kts` in your project's `app` directory, then insert the following lines into `dependencies` block. This introduces the above dependencies into the `app` subproject.

```kotlin
    implementation(libs.camera.core)
    implementation(libs.camera.camera2)
    implementation(libs.camera.lifecycle)
    implementation(libs.camera.view)
```

## Enable view binding

1. Within the above `build.gradle.kts` file, append the following lines to the end of `android` block to enable view binding feature.

```kotlin
    buildFeatures {
        viewBinding = true
    }
```

2. You should be seeing a notification shows up, as shown below. Click **"Sync Now"** to sync your project.

![Gradle sync](images/2/gradle%20sync.png)

{{% notice Tip %}}

You may also click the __"Sync Project with Gradle Files"__ button in the toolbar or pressing the corresponding shortcut to start a sync.

![Sync Project with Gradle Files](images/2/sync%20project%20with%20gradle%20files.png)
{{% /notice %}}

3. Navigate to `MainActivity.kt` source file and make following changes. This inflates the layout file into a view binding object and stores it in a member variable within the view controller for easier access later.

![view binding](images/2/view%20binding.png)

## Configure CameraX preview

1. **Replace** the placeholder "Hello World!" `TextView` within the layout file `activity_main.xml` with a camera preview view:

```xml
    <androidx.camera.view.PreviewView
        android:id="@+id/view_finder"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:scaleType="fillStart" />
```


2. Add the following member variables to `MainActivity.kt` to store camera related objects:

```kotlin
    // Camera
    private var camera: Camera? = null
    private var cameraProvider: ProcessCameraProvider? = null
    private var preview: Preview? = null
```

3. Add two new private methods named `setupCamera()` and `bindCameraUseCases()` within `MainActivity.kt`:

```kotlin
    private fun setupCamera() {
        viewBinding.viewFinder.post {
            cameraProvider?.unbindAll()

            ProcessCameraProvider.getInstance(baseContext).let {
                it.addListener(
                    {
                        cameraProvider = it.get()

                        bindCameraUseCases()
                    },
                    Dispatchers.Main.asExecutor()
                )
            }
        }
    }

    private fun bindCameraUseCases() {
        // TODO: TO BE IMPLEMENTED
    }
```

4. Implement the above `bindCameraUseCases()` method:

```kotlin
private fun bindCameraUseCases() {
        val cameraProvider = cameraProvider
            ?: throw IllegalStateException("Camera initialization failed.")

        val cameraSelector =
            CameraSelector.Builder().requireLensFacing(CameraSelector.LENS_FACING_FRONT).build()

        // Only using the 4:3 ratio because this is the closest to MediaPipe models
        val resolutionSelector =
            ResolutionSelector.Builder()
                .setAspectRatioStrategy(AspectRatioStrategy.RATIO_4_3_FALLBACK_AUTO_STRATEGY)
                .build()
        val targetRotation = viewBinding.viewFinder.display.rotation

        // Preview usecase.
        preview = Preview.Builder()
            .setResolutionSelector(resolutionSelector)
            .setTargetRotation(targetRotation)
            .build()

        // Must unbind the use-cases before rebinding them
        cameraProvider.unbindAll()

        try {
            // A variable number of use-cases can be passed here -
            // camera provides access to CameraControl & CameraInfo
            camera = cameraProvider.bindToLifecycle(
                this, cameraSelector, preview,
            )

            // Attach the viewfinder's surface provider to preview use case
            preview?.surfaceProvider = viewBinding.viewFinder.surfaceProvider
        } catch (exc: Exception) {
            Log.e(TAG, "Use case binding failed", exc)
        }
    }
```

5. Add a [companion object](https://kotlinlang.org/docs/object-declarations.html#companion-objects) to `MainActivity.kt` and declare a `TAG` constant value for `Log` calls to work correctly. This companion object comes handy for us to define all the constants and shared values accessible across the entire class.

```kotlin
    companion object {
        private const val TAG = "MainActivity"
    }
```

In the next section, you will build and run the app to make sure the camera works well.
