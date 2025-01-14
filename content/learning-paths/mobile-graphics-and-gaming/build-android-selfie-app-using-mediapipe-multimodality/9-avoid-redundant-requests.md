---
title: Avoid duplicate photo capture requests
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

So far you have implemented the core logic for MediaPipe's face and gesture task results and photo capture execution. 

However, the view controller is not communicating its execution results back to the view model, which raises the risk for photo capture failures, frequent or duplicate requests, and other potential issues.

### Introduce camera readiness state

It is best practice to complete the data flow cycle by providing callbacks for the states of the view controller. This ensures that the view model does not emit values in undesired states, such as when the camera is busy or unavailable.

1. Navigate to `MainViewModel` and add a `MutableStateFlow` named `_isCameraReady` as a  private member variable. This tracks whether the camera is busy or unavailable. 

Copy in the following:

```kotlin
    private val _isCameraReady = MutableStateFlow(true)
```

2. Update `captureEvents` by combining `_bothOk` and `_isCameraReady`. This ensures that whenever a capture event is dispatched, the camera readiness state is set to false, which prevents the next capture event from being dispatched again.

```kotlin
    val captureEvents: SharedFlow<Unit> =
        combine(_bothOk, _isCameraReady) { bothOk, cameraReady -> bothOk to cameraReady}
            .debounce(CONDITION_CHECK_STABILITY_THRESHOLD)
            .filter { (bothOK, cameraReady) -> bothOK && cameraReady }
            .onEach { _isCameraReady.emit(false) }
            .map {}
            .shareIn(viewModelScope, SharingStarted.WhileSubscribed())
```

3. Add a photo capture callback named `onPhotoCaptureComplete()`, which restores the camera readiness state back to true, so that the `captureEvents` resumes emitting once the conditions are met again:

```kotlin
    fun onPhotoCaptureComplete() {
        viewModelScope.launch {
            _isCameraReady.emit(true)
        }
    }
```

4. Navigate to `MainActivity` and invoke the `onPhotoCaptureComplete()` method inside the `onImageSaved` callback:

```kotlin
                    override fun onImageSaved(outputFileResults: ImageCapture.OutputFileResults) {
                        val savedUri = outputFileResults.savedUri
                        Log.i(TAG, "Photo capture succeeded: $savedUri")

                        viewModel.onPhotoCaptureComplete()
                    }
```


## Introduce a camera cooldown mechanism

The differences in hardware mean that the duration of an image capture varies across Android devices. Additionally, consecutive image captures place a heavy load on the CPU, GPU, camera, and flash memory buffer.

To address this, you can implement a simple cooldown mechanism after each photo capture that can both enhance the user experience whilst also conserving computing resources.

1. Add the following constant value to `MainViewModel`'s companion object. This defines a three-second cooldown before making the camera available again.

```kotlin
    private const val IMAGE_CAPTURE_DEFAULT_COUNTDOWN = 3000L
```

2. Add a `delay(IMAGE_CAPTURE_DEFAULT_COUNTDOWN)` before updating `_isCameraBusy` state.

```kotlin
    fun onPhotoCaptureComplete() {
        viewModelScope.launch {
            delay(IMAGE_CAPTURE_DEFAULT_COUNTDOWN)
            _isCameraBusy.emit(false)
        }
    }
```

{{% notice Info %}}
You might need to import the `kotlinx.coroutines.delay` function.
{{% /notice %}}

3. Build and run the app again. You should notice that now the photo capture cannot be triggered as frequently as before. Good job!

{{% notice Note %}}

Furthermore, if you remove the `viewModel.onPhotoCaptureComplete()` to simulate something going wrong during photo capture, the camera will not become available again.

However, silently failing without notifying the user is not a good practice for app development. Error handling is omitted in this learning path only for the sake of simplicity.

{{% /notice %}}

## Further resource for support: complete sample code on GitHub

If you run into any difficulties completing this Learning Path, you can check out the [complete sample code](https://github.com/hanyin-arm/sample-android-selfie-app-using-mediapipe-multimodality) on GitHub and import it into Android Studio.

If you discover a bug, encounter an issue, or have suggestions for improvement, please feel free to [open an issue](https://github.com/hanyin-arm/sample-android-selfie-app-using-mediapipe-multimodality/issues/new) with detailed information.
