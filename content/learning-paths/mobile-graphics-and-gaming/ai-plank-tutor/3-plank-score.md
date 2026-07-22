---
title: Add scoring logic for the plank pose
description: Convert MediaPipe pose landmarks into weighted joint angles and display a live plank-pose score in the Android app.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review the scoring data

The starter project already includes `data/PlankPoseData.kt`. This file contains the reference landmarks for the instructor plank image and a list of angle weights. The weights let the app make some joints more important than others when calculating the final score.

Open `data/PlankPoseData.kt`.

The file provides three pieces of data:

- `POSE_NAME`, which is the name used later in the LLM prompt.
- `referenceLandmarks`, which stores the instructor plank pose as MediaPipe landmarks.
- `angleWeights`, which stores the relative importance of each measured angle.

You don't need to edit this file. For a larger app, you'd capture this data from an instructor image or video as a preprocessing step, and load for different poses as needed. For this app, the data is hard-coded, so the Android app can stay focused on live inference and feedback.

## Extract joint angles

Open `ui/landmarker/PoseScoreHelper.kt`.

The file already contains landmark index constants and `KEY_JOINTS_COORDINATES`. Each entry in `KEY_JOINTS_COORDINATES` identifies three landmarks that form one angle. For example, an elbow angle uses shoulder, elbow, and wrist landmarks.

Replace the TODO in `extractAnglesFrom()` with the following code:

```kotlin
fun extractAnglesFrom(landmarks: List<NormalizedLandmark>): List<Double> {
    val angles = KEY_JOINTS_COORDINATES.map { coords ->
        calculateAngleFor(landmarks[coords[0]], landmarks[coords[1]], landmarks[coords[2]])
    }.toMutableList()

    val neck = midpoint(landmarks[IDX_L_SHOULDER], landmarks[IDX_R_SHOULDER])
    val midHips = midpoint(landmarks[IDX_L_HIP], landmarks[IDX_R_HIP])
    angles.add(calculateAngleFor(landmarks[IDX_NOSE], neck, midHips))

    return angles
}
```

The main list extracts wrist, elbow, shoulder, knee, ankle, and hip angles. The final angle estimates neck alignment by creating a midpoint between the shoulders and a midpoint between the hips, with the nose as the third landmark.

Replace the TODO in `midpoint()` with the following code for the neck joint helper function:

```kotlin
private fun midpoint(pointA: NormalizedLandmark, pointB: NormalizedLandmark) =
    NormalizedLandmark.create(
        (pointA.x() + pointB.x()) / 2,
        (pointA.y() + pointB.y()) / 2,
        (pointA.z() + pointB.z()) / 2
    )
```

MediaPipe landmarks are normalized coordinates. The `x` and `y` values are relative to the input image, and `z` gives relative depth.

While this app compares normalized landmarks from a fixed instructor reference, the score is still fairly view-dependent. The app works best when the learner is side-on to the camera, fully visible, and at a similar orientation to the reference image.

## Calculate a 3D angle

For each angle in `extractAnglesFrom()` it uses `calculateAngleFor()` - replace its TODO with the following code:

```kotlin
private fun calculateAngleFor(
    pointA: NormalizedLandmark,
    pointB: NormalizedLandmark,
    pointC: NormalizedLandmark
): Double {
    val bax = pointA.x() - pointB.x()
    val bay = pointA.y() - pointB.y()
    val baz = pointA.z() - pointB.z()

    val bcx = pointC.x() - pointB.x()
    val bcy = pointC.y() - pointB.y()
    val bcz = pointC.z() - pointB.z()

    val dotProduct = bax * bcx + bay * bcy + baz * bcz
    val magnitudeBA = sqrt(bax.pow(2) + bay.pow(2) + baz.pow(2))
    val magnitudeBC = sqrt(bcx.pow(2) + bcy.pow(2) + bcz.pow(2))
    val cosine = (dotProduct / (magnitudeBA * magnitudeBC)).toDouble().coerceIn(-1.0, 1.0)

    return Math.toDegrees(acos(cosine))
}
```

This function calculates the angle at `pointB`. It treats `pointA - pointB` and `pointC - pointB` as two 3D vectors, then uses their dot product to calculate the angle between them.

The `coerceIn(-1.0, 1.0)` call protects the `acos()` calculation from small floating-point rounding errors.

## Calculate a weighted score

Replace the TODO in `calculatePoseScore()` with the following code:

```kotlin
fun calculatePoseScore(
    correctAngles: List<Double>,
    userAngles: List<Double>,
    angleWeights: List<Float>,
    maxDifference: Double = MAX_ANGLE_DIFFERENCE
): Double {
    require(correctAngles.isNotEmpty()) { "Correct angles cannot be empty." }
    require(correctAngles.size == userAngles.size) { "Correct and user angle counts must match." }
    require(correctAngles.size == angleWeights.size) { "Angle and weight counts must match." }

    val weightedScoreSum = correctAngles.indices.sumOf { index ->
        val difference = abs(correctAngles[index] - userAngles[index])
        val normalizedScore = ((maxDifference - difference) / maxDifference)
            .coerceIn(0.0, 1.0) * HIGHEST_SCORE
        normalizedScore * angleWeights[index]
    }

    return weightedScoreSum / angleWeights.sum().toDouble()
}
```

For each angle, the score starts at 100 and drops as the learner's angle differs from the reference angle. Differences at or above `MAX_ANGLE_DIFFERENCE` contribute zero for that angle.

The final score is the weighted average across all measured angles.

{{% notice Note %}}
This score is a pose-matching signal for the app. It's not a clinical, safety, or fitness-quality assessment.
{{% /notice %}}

## Emit score data from the ViewModel

Open `ui/viewmodels/MainViewModel.kt`.

Replace the TODO inside the `userPoseResults` mapping block with the following code:

```kotlin
val referenceAngles = extractAnglesFrom(PlankPoseData.referenceLandmarks)
val userAngles = extractAnglesFrom(userLandmarks)
val score = calculatePoseScore(
    correctAngles = referenceAngles,
    userAngles = userAngles,
    angleWeights = PlankPoseData.angleWeights
)

UserPoseResult(referenceAngles, userAngles, score)
```

The code calculates angles for the instructor reference and the learner's live pose. It then stores both angle lists with the score. You'll reuse the angle lists when you build the LLM prompt.

Now, replace the TODO in `userPoseScore` with the following code:

```kotlin
val userPoseScore: Flow<String> =
    sharedUserPoseResults.map { it.scoreVal.roundToInt().toString() }
```

The UI needs a rounded string score. The underlying `UserPoseResult` keeps the full `Double` value for later use.

## Display the score

Open `ui/MainActivity.kt`.

The starter project keeps `collectAppState()` as a safe no-op so the app can run before you implement scoring and speech. Replace that function with the following code:

```kotlin
private suspend fun collectAppState() = coroutineScope {
    launch {
        mainViewModel.userPoseScore.collect {
            score.text = getString(R.string.score) + it
        }
    }
}
```

Add the following import near the other coroutine imports:

```kotlin
import kotlinx.coroutines.coroutineScope
```

The existing `repeatOnLifecycle(Lifecycle.State.STARTED)` block already calls `collectAppState()`. Changing the function to `suspend` is valid because `repeatOnLifecycle` runs its block from a coroutine.

You'll add more `launch { ... }` collectors inside this same `coroutineScope` block in the following sections.

## Run the app

Build and run the app on your Android device.

When you move in front of the camera, the score should update as MediaPipe detects your landmarks. The score will vary with camera angle and distance from the device, but mainly with how closely your body position matches the reference plank pose.

If the score stays blank, verify that `onResults()` is receiving landmarks and that your body remains inside the camera frame. If the score jumps sharply, try a steadier side-on camera angle.

## What you've accomplished and what's next

You've now turned MediaPipe pose landmarks into a plank score. At this point, the app can detect and score the plank pose. 

Next, you'll convert the largest angle differences into a short text prompt for the local LLM.
