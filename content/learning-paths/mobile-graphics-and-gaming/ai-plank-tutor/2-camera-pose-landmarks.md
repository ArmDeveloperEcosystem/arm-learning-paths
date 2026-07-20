---
title: Get pose landmarks from camera
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Objective

In this section, you will connect the Android camera to MediaPipe Pose Landmarker.

You will:

- Bind a CameraX preview to the app UI.
- Add an `ImageAnalysis` use case for live camera frames.
- Configure MediaPipe Pose Landmarker in live-stream mode.
- Convert each CameraX `ImageProxy` into a MediaPipe `MPImage`.
- Send the first detected pose landmark list to `MainViewModel`.

At the end of this section, the app opens the front camera and passes live pose landmarks into the app. The score will still be incomplete until you add pose scoring in the next section.

## Configure CameraX

Open `ui/MainActivity.kt`.

The starter project already requests camera permission and calls `setUpCamera()` from `onCreate()`. Replace the TODO in `setUpCamera()` with the following code:

```kotlin
private fun setUpCamera() {
    val cameraProviderFuture = ProcessCameraProvider.getInstance(this)
    cameraProviderFuture.addListener(
        {
            cameraProvider = cameraProviderFuture.get()
            bindCameraUseCases()
        }, Dispatchers.Main.asExecutor()
    )
}
```

`ProcessCameraProvider` owns the camera use cases for the activity. When the provider is ready, the app stores it and calls `bindCameraUseCases()`.

## Bind preview and image analysis

The app needs two CameraX use cases:

- `Preview`, which displays the camera feed in the `PreviewView`.
- `ImageAnalysis`, which receives frames for pose detection.

In `MainActivity.kt`, replace the TODO at the end of `bindCameraUseCases()` with this code:

```kotlin
val preview = Preview.Builder()
    .setResolutionSelector(resolutionSelector)
    .setTargetRotation(targetRotation)
    .build()

val imageAnalyzer = ImageAnalysis.Builder()
    .setResolutionSelector(resolutionSelector)
    .setTargetRotation(targetRotation)
    .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
    .setOutputImageFormat(ImageAnalysis.OUTPUT_IMAGE_FORMAT_RGBA_8888)
    .build()
    .also {
        it.setAnalyzer(
            Dispatchers.Default.limitedParallelism(1).asExecutor()
        ) { image -> detectPose(image) }
    }

cameraProvider.unbindAll()

try {
    cameraProvider.bindToLifecycle(
        this, cameraSelector, preview, imageAnalyzer
    )

    preview.surfaceProvider = cameraPreview.surfaceProvider
} catch (exc: Exception) {
    Log.e(TAG, "Use case binding failed", exc)
}
```

The analyzer uses `STRATEGY_KEEP_ONLY_LATEST` because pose detection should work on the most recent frame. If the device is busy, old frames are dropped instead of queued.

The output image format is `RGBA_8888`, which makes the frame data easy to copy into a `Bitmap` before passing it to MediaPipe.

The analyzer runs on a background executor with one worker. That keeps camera frame conversion off the UI thread and serializes calls into the landmarker helper, which is useful because live-stream inference is driven by timestamped frames.

## Send frames to the landmarker

In `bindCameraUseCases()` we just set `ImageAnalysis` to call `detectPose()` for every analyzed frame. Now, replace the TODO in `detectPose()` with this code:

```kotlin
private fun detectPose(imageProxy: ImageProxy) {
    if (!this::poseLandmarkerHelper.isInitialized || poseLandmarkerHelper.isClosed) {
        imageProxy.close()
        return
    }

    if (imageAnalysisEnabled) {
        poseLandmarkerHelper.detectLiveStream(
            imageProxy = imageProxy,
            isFrontCamera = true
        )
    } else {
        imageProxy.close()
    }
}
```

This code checks that the MediaPipe helper is ready before using it. If the helper is not ready, it closes the `ImageProxy` immediately.

{{% notice Note %}}
Every `ImageProxy` from CameraX must be closed. In this app, `PoseLandmarkerHelper.detectLiveStream()` closes the image after copying its pixels. If the frame is skipped, `detectPose()` closes it directly.
{{% /notice %}}

Now replace the TODO in `onResults()` with this code:

```kotlin
override fun onResults(landmarks: List<NormalizedLandmark>?) {
    mainViewModel.handleUserPose(landmarks)
}
```

This is a callback from `PoseLandmarkerHelper` and sends the live landmarks onto the ViewModel. The next page will convert those landmarks into joint angles and a pose score.

## Configure MediaPipe Pose Landmarker

What happens between `detectPose()` and `onResults()`? Open `ui/landmarker/PoseLandmarkerHelper.kt`.

The starter file already contains the MediaPipe imports, model path, confidence values, and the `LandmarkerListener` interface for the callbacks to `MainActivity`.

Replace the TODO in `setupPoseLandmarker()` with this code:

```kotlin
fun setupPoseLandmarker(context: Context) {
    try {
        val baseOptions = BaseOptions.builder()
            .setDelegate(Delegate.GPU)
            .setModelAssetPath(MODEL_PATH)
            .build()

        val options = PoseLandmarker.PoseLandmarkerOptions.builder()
            .setBaseOptions(baseOptions)
            .setNumPoses(1)
            .setMinPoseDetectionConfidence(MIN_POSE_DETECTION_CONFIDENCE)
            .setMinTrackingConfidence(MIN_POSE_TRACKING_CONFIDENCE)
            .setMinPosePresenceConfidence(MIN_POSE_PRESENCE_CONFIDENCE)
            .setRunningMode(RunningMode.LIVE_STREAM)
            .setResultListener(this::returnLiveStreamResult)
            .setErrorListener(this::returnLiveStreamError)
            .build()

        poseLandmarker = PoseLandmarker.createFromOptions(context, options)
    } catch (exception: IllegalStateException) {
        listener.onError("Pose Landmarker failed to initialize. See logs for details.")
        Log.e(TAG, "MediaPipe failed to load the pose landmarker", exception)
    } catch (exception: RuntimeException) {
        listener.onError("Pose Landmarker failed to initialize. See logs for details.")
        Log.e(TAG, "MediaPipe failed to create the pose landmarker", exception)
    }
}
```

The app uses `RunningMode.LIVE_STREAM` because frames arrive continuously from the camera. In this mode, MediaPipe returns results through callbacks instead of returning them directly from the detection call.

The app also requests one pose with `setNumPoses(1)`. This keeps the example focused on a single learner.

The `Delegate.GPU` option asks MediaPipe to use the device GPU for the pose model. If initialization fails on a particular device, the error listener and Logcat message are the first places to check.

## Convert camera frames to MPImage

When we call from `MainActivity`, it is with a CameraX `ImageProxy`, but the MediaPipe analyzer expects an `MPImage`.

Replace the TODO in `detectLiveStream()` with this code to convert between the two and start the Pose Landmarker analysis:

```kotlin
fun detectLiveStream(
    imageProxy: ImageProxy,
    isFrontCamera: Boolean
) {
    val frameTime = SystemClock.uptimeMillis()
    val imageWidth = imageProxy.width
    val imageHeight = imageProxy.height
    val rotationDegrees = imageProxy.imageInfo.rotationDegrees

    val bitmapBuffer = Bitmap.createBitmap(
        imageWidth,
        imageHeight,
        Bitmap.Config.ARGB_8888
    )

    imageProxy.use { image ->
        bitmapBuffer.copyPixelsFromBuffer(image.planes[0].buffer)
    }

    val matrix = Matrix().apply {
        postRotate(rotationDegrees.toFloat())
        if (isFrontCamera) {
            postScale(-1f, 1f, imageWidth.toFloat(), imageHeight.toFloat())
        }
    }

    val rotatedBitmap = Bitmap.createBitmap(
        bitmapBuffer,
        0,
        0,
        bitmapBuffer.width,
        bitmapBuffer.height,
        matrix,
        true
    )

    val mpImage = BitmapImageBuilder(rotatedBitmap).build()
    poseLandmarker?.detectAsync(mpImage, frameTime)
}
```

The call to `imageProxy.use { ... }` closes the frame after its pixels are copied.

The matrix rotates the image using the camera frame metadata. For the front camera, it also mirrors the image so the detected pose matches the preview the learner sees.

`SystemClock.uptimeMillis()` provides a monotonic timestamp for the frame. MediaPipe requires timestamps for video and live-stream inputs, and `detectAsync()` returns immediately; the result arrives later through the result listener configured above.

## Return the first detected pose

Finally, replace the TODO in `returnLiveStreamResult()` with this code:

```kotlin
private fun returnLiveStreamResult(
    result: PoseLandmarkerResult,
    @Suppress("UNUSED_PARAMETER") input: MPImage
) {
    listener.onResults(result.landmarks().firstOrNull())
}
```

MediaPipe returns a list of detected poses. This app asks for one pose, so it forwards only the first landmark list.

## Run the app

Build and run the app on your Android device.

When prompted, allow camera access. Expect to see the front camera preview in the right side of the app.

The score will not update yet. At this point, the app is collecting pose landmarks and passing them to `MainViewModel`; the scoring logic is added in the next section.

If the preview opens but no landmarks are produced later, make sure your full body is visible in the frame and check Logcat for `PoseLandmarkerHelper`.
