---
title: Set up the Development Environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Download Android Studio

Start by downloading and installing the latest version of [Android Studio](https://developer.android.com/studio/) on your host machine.

The instructions for this learning path were tested on a host machine running macOS, but you can use any of the supported hardware systems listed on the [Install Android Studio](https://developer.android.com/studio/install) webpage on the Android Developer website. 

After installation, open Android Studio and do the following:

* Accept license agreements.
* Download all the required assets.
* Select the default or recommended settings. 

{{% notice Tips %}}
Before you start coding, here are some useful tips:

1. To navigate to a file, simply press the Shift key twice, input the file name, select the correct result using the up and down arrow keys, and then press Enter.

2. Every time after you copy-and-paste a code block from this Learning Path, ensure that you import the correct classes and resolve any errors. For more information, see the [Auto import](https://www.jetbrains.com/help/idea/creating-and-optimizing-imports.html) web page.
{{% /notice %}}

## Create a new Android project

1. Navigate to **File** > **New** > **New Project**.

2. Select **Empty Views Activity** in the **Phone and Tablet** gallery as Figure 1 shows, then select **Next**.
![Empty Views Activity.png alt-text#center](images/2/empty%20project.png "Figure 1: Select Empty Views Activity.")

3. Choose a project name, and select the default configurations as Figure 2 shows. 

    Make sure that the **Language** field is set to **Kotlin**, and the **Build configuration language** field is set to **Kotlin DSL**.
![Project configuration.png alt-text#center](images/2/project%20config.png "Figure 2: Project Configuration.")

## Add CameraX dependencies

[CameraX](https://developer.android.com/media/camera/camerax) is a Jetpack library, built to help make camera app development easier. It provides a consistent, easy-to-use API that works across the vast majority of Android devices with great backward-compatibility.

1. Wait for Android Studio to sync project with Gradle files. This might take several minutes.

2. Once the project is synced, navigate to `libs.versions.toml` in your project's root directory. See Figure 3. This file serves as the version catalog for all dependencies that the project uses.

![Version Catalog.png alt-text#center](images/2/dependency%20version%20catalog.png "Figure 3: Version Catalog.")

{{% notice Info %}}

For more information on version catalogs, see [Migrate your build to version catalogs](https://developer.android.com/build/migrate-to-catalogs).

{{% /notice %}}

3. Append the following line to the end of `[versions]` section. This defines the version of CameraX libraries that you will be using.
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

5. Navigate to `build.gradle.kts` in your project's `app` directory, then insert the following lines into `dependencies` block. This introduces the dependencies listed above into the `app` subproject:

```kotlin
    implementation(libs.camera.core)
    implementation(libs.camera.camera2)
    implementation(libs.camera.lifecycle)
    implementation(libs.camera.view)
```

## Enable view binding

1. Within the above `build.gradle.kts` file, append the following lines to the end of `android` block to enable the view binding feature:

```kotlin
    buildFeatures {
        viewBinding = true
    }
```

2. You should see that a notification appears. See Figure 4. Click **Sync Now** to sync your project.

![Gradle sync.png alt-text#center](images/2/gradle%20sync.png "Figure 4: Gradle Sync.")

{{% notice Tip %}}

You can also click the **Sync Project with Gradle Files** button in the toolbar, or enter the corresponding shortcut to start a sync.

![Sync Project with Gradle Files](images/2/sync%20project%20with%20gradle%20files.png)
{{% /notice %}}

3. Navigate to the `MainActivity.kt` source file and make the changes that Figure 5 shows in the View Binding screenshot. 

    This inflates the layout file into a view binding object, and stores it in a member variable within the view controller for easier access later.

![view binding alt-text#center](images/2/view%20binding.png "Figure 5: View Binding.")

## Configure CameraX preview

1. Within the layout file `activity_main.xml`, replace the placeholder "Hello World!" in `TextView` with a camera preview view:

```xml
    <androidx.camera.view.PreviewView
        android:id="@+id/view_finder"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:scaleType="fillStart" />
```


2. Add the following member variables to `MainActivity.kt` to store camera-related objects:

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

4. Implement the `bindCameraUseCases()` method:

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

5. Add a [companion object](https://kotlinlang.org/docs/object-declarations.html#companion-objects) to `MainActivity.kt`, and declare a `TAG` constant value for `Log` calls to work correctly. This companion object is useful in enabling you to define all the constants and shared values accessible across the entire class.

```kotlin
    companion object {
        private const val TAG = "MainActivity"
    }
```

In the next section, you will build and run the app to ensure that the camera works as expected.
