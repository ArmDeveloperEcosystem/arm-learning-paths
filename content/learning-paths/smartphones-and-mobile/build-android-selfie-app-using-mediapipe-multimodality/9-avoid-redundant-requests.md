---
title: Avoid duplicated photo capture requests
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

So far, we have implemented the core logic for mediating MediaPipe's face and gesture task results and executing photo captures. However, the view controller does not communicate its execution results back to the view model. This introduces risks such as photo capture failures, frequent or duplicate requests, and other potential issues.

## Introduce camera readiness state

It is a best practice to complete the data flow cycle by providing callbacks for the view controller's states. This ensures that the view model does not emit values in undesired states, such as when the camera is busy or unavailable.

1. Navigate to `MainViewModel` and add a `MutableStateFlow` named `_isCameraReady` as a  private member variable. This keeps track of whether the camera is busy or unavailable.

```kotlin
    private val _isCameraReady = MutableStateFlow(true)
```

2. Update the `captureEvents` by combining `_bothOk` and `_isCameraReady`. This ensures that whenever a capture event is dispatched, the camera readiness state is set to false, therefore preventing the next capture event from being dispatched again.

```kotlin
    val captureEvents: SharedFlow<Unit> =
        combine(_bothOk, _isCameraReady) { bothOk, cameraReady -> bothOk to cameraReady}
            .debounce(CONDITION_CHECK_STABILITY_THRESHOLD)
            .filter { (bothOK, cameraReady) -> bothOK && cameraReady }
            .onEach { _isCameraReady.emit(false) }
            .map {}
            .shareIn(viewModelScope, SharingStarted.WhileSubscribed())
```

3. Add a photo capture callback named `onPhotoCaptureComplete()`, which restores the camera readiness state back to true, so that the `captureEvents` resumes emitting once the conditions are met again.

```kotlin
    fun onPhotoCaptureComplete() {
        viewModelScope.launch {
            _isCameraReady.emit(true)
        }
    }
```

4. Navigate to `MainActivity` and invoke `onPhotoCaptureComplete()` method inside `onImageSaved` callback:

```kotlin
                    override fun onImageSaved(outputFileResults: ImageCapture.OutputFileResults) {
                        val savedUri = outputFileResults.savedUri
                        Log.i(TAG, "Photo capture succeeded: $savedUri")

                        viewModel.onPhotoCaptureComplete()
                    }
```


## Introduce camera cooldown

The duration of image capture can vary across Android devices due to hardware differences. Additionally, consecutive image captures place a heavy load on the CPU, GPU, camera, and flash memory buffer.

To address this, implementing a simple cooldown mechanism after each photo capture can enhance the user experience while conserving computing resources.

1. Add the following constant value to `MainViewModel`'s companion object. This defines a `3` sec cooldown before marking the camera available again.

```kotlin
    private const val IMAGE_CAPTURE_DEFAULT_COUNTDOWN = 3000L
```

2. Add a `delay(IMAGE_CAPTURE_DEFAULT_COUNTDOWN)` before updating `_isCameraBusy` state. You may need to import `kotlinx.coroutines.delay` function.

```kotlin
    fun onPhotoCaptureComplete() {
        viewModelScope.launch {
            delay(IMAGE_CAPTURE_DEFAULT_COUNTDOWN)
            _isCameraBusy.emit(false)
        }
    }
```

3. Build and run the app again. Now you should notice that photo capture cannot be triggered as frequently as before. Good job!

    i. Furthermore, if you remove the `viewModel.onPhotoCaptureComplete()` to simulate something going wrong upon photo capture, the camera won't become available ever again. 
    
    ii. However, silently failing without notifying the user is not a good practice for app development. Error handling is omitted in this learning path for the sake of simplicity.

