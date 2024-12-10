---
title: Mediate flows to trigger photo capture
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now you have two independent Flows indicating the conditions of face landmark detection and gesture recognition. The simplest multimodality strategy is to combine multiple source Flows into a single output Flow, which emits consolidated values as the [single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth) for its observers (collectors) to carry out corresponding actions.

## Combine two Flows into a single Flow

1. Navigate to `MainViewModel` and append the following constant values to its companion object. 

    i. The first constant defines how frequently we sample the conditions from each Flow.

    ii. The second constant defines the debounce threshold of the stability check on whether to trigger a photo capture.

```kotlin
        private const val CONDITION_CHECK_SAMPLING_INTERVAL = 100L
        private const val CONDITION_CHECK_STABILITY_THRESHOLD = 500L
```

2. Add a private member variable named `_bothOk`. Note that you might need to add `@OptIn(FlowPreview::class)` annotation since `sample` is still in preview.

```kotlin
    private val _bothOk =
        combine(
            _gestureOk.sample(CONDITION_CHECK_SAMPLING_INTERVAL),
            _faceOk.sample(CONDITION_CHECK_SAMPLING_INTERVAL),
        ) { gestureOk, faceOk -> gestureOk && faceOk }
            .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), false)
```

3. Expose a `SharedFlow` variable which emits a `Unit` whenever the face and gesture conditions are met and stay stable for a while, i.e. `500`ms as defined above. Again, add `@OptIn(FlowPreview::class)` if needed.

```kotlin
    val captureEvents: SharedFlow<Unit> = _bothOk
        .debounce(CONDITION_CHECK_STABILITY_THRESHOLD)
        .filter { it }
        .map { }
        .shareIn(viewModelScope, SharingStarted.WhileSubscribed())
```

If this code looks confusing to you, please see the explanations below for Kotlin beginners.

#### Keyword "it"

The operation `filter { it }` is simplified from `filter { bothOk -> bothOk == true }`. 

Since Kotlin allows for implictly calling the single parameter in a lambda `it`, `{ bothOk -> bothOk == true }` is equivalent to `{ it == true }`, and again  `{ it }`. 

See [this doc](https://kotlinlang.org/docs/lambdas.html#it-implicit-name-of-a-single-parameter) for more details.

#### "Unit" type
This `SharedFlow` has a generic type `Unit`, which doesn't contain any value. You may think of it as a "pulse" signal.

The operation `map { }` simply maps the upstream `Boolean` value emitted from `_bothOk` to `Unit` regardless their values are true or false. It's simplified from `map { bothOk -> Unit }`, which becomes `map { Unit } ` where the keyword `it` is not used at all. Since an empty block already returns `Unit` implicitly, we don't need to explicitly return it.

If this still looks confusing, you may also opt to use `SharedFlow<Boolean>` and remove the `map { }` operation. Just note that when you collect this Flow, it doesn't matter whether the emitted `Boolean` values are true or false. In fact, they are always `true` due to the `filter` operation.

## Configure ImageCapture use case

1. Navigate to `MainActivity` and append a `ImageCapture` use case below the other camera related member variables:

```kotlin
    private var imageCapture: ImageCapture? = null
```

2. Configure this `ImageCapture` in `bindCameraUseCases()` method:

```kotlin
        // Image Capture
        imageCapture = ImageCapture.Builder()
            .setCaptureMode(ImageCapture.CAPTURE_MODE_MINIMIZE_LATENCY)
            .setTargetRotation(targetRotation)
            .build()
```

3. Again, don't forget to append this use case to `bindToLifecycle`.

```kotlin
            camera = cameraProvider.bindToLifecycle(
                this, cameraSelector, preview, imageAnalyzer, imageCapture
            )
```

## Execute photo capture with ImageCapture

1. Append the following constant values to `MainActivity`'s companion object. They define the file name format and the [MIME type](https://en.wikipedia.org/wiki/Media_type).

```kotlin
        // Image capture
        private const val FILENAME = "yyyy-MM-dd-HH-mm-ss-SSS"
        private const val PHOTO_TYPE = "image/jpeg"
```

2. Implement the photo capture logic with a new method named `executeCapturePhoto()`:

```kotin
    private fun executeCapturePhoto() {
        imageCapture?.let { imageCapture ->
            val name = SimpleDateFormat(FILENAME, Locale.US)
                .format(System.currentTimeMillis())
            val contentValues = ContentValues().apply {
                put(MediaStore.MediaColumns.DISPLAY_NAME, name)
                put(MediaStore.MediaColumns.MIME_TYPE, PHOTO_TYPE)
                if (Build.VERSION.SDK_INT > Build.VERSION_CODES.P) {
                    val appName = resources.getString(R.string.app_name)
                    put(
                        MediaStore.Images.Media.RELATIVE_PATH,
                        "Pictures/${appName}"
                    )
                }
            }

            val outputOptions = ImageCapture.OutputFileOptions
                .Builder(
                    contentResolver,
                    MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
                    contentValues
                )
                .build()

            imageCapture.takePicture(outputOptions, Dispatchers.IO.asExecutor(),
                object : ImageCapture.OnImageSavedCallback {
                    override fun onError(error: ImageCaptureException) {
                        Log.e(TAG, "Photo capture failed: ${error.message}", error)
                    }

                    override fun onImageSaved(outputFileResults: ImageCapture.OutputFileResults) {
                        val savedUri = outputFileResults.savedUri
                        Log.i(TAG, "Photo capture succeeded: $savedUri")
                    }
                })
        }
    }
```

3. Append the following code to `repeatOnLifecycle(Lifecycle.State.RESUMED)` block in `onCreate` method.

```kotlin
                launch {
                    viewModel.captureEvents.collect {
                        executeCapturePhoto()
                    }
                }
```
4. Now, even though the photo capture has already been implemented, it's still quite inconvenient for us to check out the logs afterwards to find out whether the photo capture has been successfully executed. Let's add a flash effect UI to explicitly show the users that a photo has been captured.

## Add a flash effect upon capturing photo

1. Navigate to `activity_main.xml` layout file and insert the following `View` element **between** the two overlay views and two `SwitchCompat` views. This is essentially just a white blank view covering the whole surface.

```
    <View
        android:id="@+id/flashOverlay"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="@android:color/white"
        android:visibility="gone" />
```

2. Append the constant value below to the companion object of `MainActivity`, then add a private method named `showFlashEffect()` to animate the above `flashOverlay` view from hidden to shown in `100`ms and then again from shown to hidden in `100`ms.

```kotlin
    private const val IMAGE_CAPTURE_FLASH_DURATION = 100L
```

```kotlin
    private fun showFlashEffect() {
        viewBinding.flashOverlay.apply {
            visibility = View.VISIBLE
            alpha = 0f

            // Fade in and out animation
            animate()
                .alpha(1f)
                .setDuration(IMAGE_CAPTURE_FLASH_DURATION)
                .withEndAction {
                    animate()
                        .alpha(0f)
                        .setDuration(IMAGE_CAPTURE_FLASH_DURATION)
                        .withEndAction {
                            visibility = View.GONE
                        }
                }
        }
    }
``` 

3. Invoke `showFlashEffect()` method in `executeCapturePhoto()` method, **before** invoking `imageCapture.takePicture()`

4. Build and run the app. Try keeping up a smiling face while presenting thumb-up gestures. When you see both switches turn on and stay stable for approximately half a second, the screen should flash white and then a photo should be captured and shows up in your album, which may take a few seconds depending on your Android device's hardware. Good job!
