---
title: Manage UI state with ViewModel
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The `ViewModel` class is a [business logic or screen level state holder](https://developer.android.com/topic/architecture/ui-layer/stateholders). It exposes state to the UI and encapsulates related business logic. Its principal advantage is that it caches state and persists it through configuration changes. This means that your UI doesn’t have to fetch data again when navigating between activities, or following configuration changes, such as when rotating the screen.

## Introduce Jetpack Lifecycle dependency

1. Navigate to `libs.versions.toml` and append the following line to the end of `[versions]` section. This defines the version of the Jetpack Lifecycle libraries we will be using.

```toml
lifecycle = "2.8.7"
```

2. Insert the following line to `[libraries]` section, ideally between `androidx-appcompat` and `material`. This declares Jetpack Lifecycle ViewModel Kotlin extension.

```toml
androidx-lifecycle-viewmodel = { group = "androidx.lifecycle", name = "lifecycle-viewmodel-ktx", version.ref = "lifecycle" }
```

3. Navigate to `build.gradle.kts` in your project's `app` directory, then insert the following line into `dependencies` block, ideally between `implementation(libs.androidx.constraintlayout)` and `implementation(libs.camera.core)`. 

```kotlin
implementation(libs.androidx.lifecycle.viewmodel)
```

## Access the helper via a ViewModel

1. Create a new file named `MainViewModel.kt` and place it into the same directory of `MainActivity.kt` and other files, then copy the code below into it.

```kotlin
package com.example.holisticselfiedemo

import android.app.Application
import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch

class MainViewModel : ViewModel(), HolisticRecognizerHelper.Listener {

    private val holisticRecognizerHelper = HolisticRecognizerHelper()

    fun setupHelper(context: Context) {
        viewModelScope.launch {
            holisticRecognizerHelper.apply {
                listener = this@MainViewModel
                setup(context)
            }
        }
    }

    fun shutdownHelper() {
        viewModelScope.launch {
            holisticRecognizerHelper.apply {
                listener = null
                shutdown()
            }
        }
    }

    fun recognizeLiveStream(imageProxy: ImageProxy) {
        holisticRecognizerHelper.recognizeLiveStream(
            imageProxy = imageProxy,
        )
    }

    override fun onFaceLandmarkerResults(resultBundle: FaceResultBundle) {
        Log.i(TAG, "Face result: $resultBundle")
    }

    override fun onFaceLandmarkerError(error: String, errorCode: Int) {
        Log.e(TAG, "Face landmarker error $errorCode: $error")
    }

    override fun onGestureResults(resultBundle: GestureResultBundle) {
        Log.i(TAG, "Gesture result: $resultBundle")
    }

    override fun onGestureError(error: String, errorCode: Int) {
        Log.e(TAG, "Gesture recognizer error $errorCode: $error")
    }

    companion object {
        private const val TAG = "MainViewModel"
    }
}
```

{{% notice Info %}}
You might have noticed that success and failure messages are logged with different APIs. For more information on log level guidelines, please refer to [this doc](https://source.android.com/docs/core/tests/debug/understanding-logging#log-level-guidelines). 
{{% /notice %}}

2. Bind `MainViewModel` to `MainActivity` by inserting the following line into `MainActivity.kt`, above the `onCreate` method. Don't forget to import `viewModels` [extension function](https://kotlinlang.org/docs/extensions.html#extension-functions) via `import androidx.activity.viewModels`.

```kotlin
    private val viewModel: MainViewModel by viewModels()
```

3. Setup and shutdown the helper's internal MediaPipe tasks upon the app becomes [active and inactive](https://developer.android.com/guide/components/activities/activity-lifecycle#alc).

```kotlin
    private var isHelperReady = false

    override fun onResume() {
        super.onResume()
        viewModel.setupHelper(baseContext)
        isHelperReady = true
    }

    override fun onPause() {
        super.onPause()
        isHelperReady = false
        viewModel.shutdownHelper()
    }
```

## Feed camera frames into livestream recognition

1. Add a new member variable named `imageAnalysis` to `MainActivity`, along with other camera related member variables:

```kotlin
private var imageAnalysis: ImageAnalysis? = null
```

2. Within `MainActivity`'s `bindCameraUseCases()` method, insert the following code after building `preview`, above `cameraProvider.unbindAll()`:

```kotlin
        // ImageAnalysis. Using RGBA 8888 to match how MediaPipe models work
        imageAnalysis =
            ImageAnalysis.Builder()
                .setResolutionSelector(resolutionSelector)
                .setTargetRotation(targetRotation)
                .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
                .setOutputImageFormat(ImageAnalysis.OUTPUT_IMAGE_FORMAT_RGBA_8888)
                .build()
                // The analyzer can then be assigned to the instance
                .also {
                    it.setAnalyzer(
                        // Forcing a serial executor without parallelism
                        // to avoid packets sent to MediaPipe out-of-order
                        Dispatchers.Default.limitedParallelism(1).asExecutor()
                    ) { image ->
                        if (isHelperReady)
                            viewModel.recognizeLiveStream(image)
                    }
                }
```

{{% notice Note %}}

`isHelperReady` flag is a lightweight mechanism to prevent camera image frames being sent to helper once we have started shutting down the helper.

{{% /notice %}}

3. Append `imageAnalysis` along with other use cases to `camera`:

```kotlin
            camera = cameraProvider.bindToLifecycle(
                this, cameraSelector, preview, imageAnalysis
            )
```

4. Build and run the app again. Now you should be seeing `Face result: ...` and `Gesture result: ...` debug messages in your [Logcat](https://developer.android.com/tools/logcat), which proves that MediaPipe tasks are functioning properly. Good job!

