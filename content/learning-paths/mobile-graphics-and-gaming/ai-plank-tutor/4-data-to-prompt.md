---
title: Turn pose data into a prompt
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Objective

In this section, you will turn pose and score data into a compact text prompt for the local LLM.

You will:

- Compare the instructor and learner angle lists.
- Sort the largest joint-angle differences.
- Filter out small differences so the prompt stays short.
- Format the remaining differences as plain text.
- Expose the generated prompt from `MainViewModel`.

The LLM will not receive images or raw landmarks. It will receive a short list of the largest pose differences, such as:

```text
I'm doing Plank pose. My joints have the following significant angle differences to the teacher's: Left hip flexion: -18, Right shoulder: 12
```

This keeps the prompt small and gives the model only the facts it needs to produce one coaching cue.

This is the main design pattern in the app: the vision model turns camera frames into structured pose data, deterministic Kotlin code turns that data into a small set of facts, and the LLM only handles the language generation step.

## Format the largest angle differences

Open `ui/landmarker/PoseScoreHelper.kt`.

The file already contains `KEY_ANGLE_NAMES`, which maps each calculated angle to a human-readable joint name. The order of `KEY_ANGLE_NAMES` matches the order of the angles returned by `extractAnglesFrom()`.

Replace the TODO in `angleDifference()` with this code:

```kotlin
fun angleDifference(
    correctAngles: List<Double>,
    userAngles: List<Double>,
    filter: Double = -1.0,
    maxEntries: Int = Int.MAX_VALUE
): Map<String, String> {
    require(correctAngles.isNotEmpty()) { "Correct angles cannot be empty." }
    require(correctAngles.size == userAngles.size) { "Correct and user angle counts must match." }

    return correctAngles.zip(userAngles)
        .zip(KEY_ANGLE_NAMES) { (correct, user), name ->
            val difference = correct - user
            Triple(name, difference, "%.0f".format(difference))
        }
        .filter { (_, difference, _) -> filter <= 0 || abs(difference) >= filter }
        .sortedByDescending { abs(it.second) }
        .take(maxEntries)
        .associate { (name, _, formatted) -> name to formatted }
}
```

This function pairs each reference angle with the corresponding learner angle, calculates the difference, and sorts by the absolute size of that difference.

The returned map uses the joint name as the key and a rounded string angle difference as the value. The string value is useful because the next function can insert it directly into the prompt.

{{% notice Note %}}
The sign of the difference is important. `difference = reference - learner`, so a positive value means the learner's angle is smaller than the reference and usually needs to straighten. A negative value means the learner's angle is larger than the reference and usually needs to bend more.
{{% /notice %}}

## Generate the LLM prompt

Replace the TODO in `generateLlmPromptFrom()` with this code:

```kotlin
fun generateLlmPromptFrom(
    referenceAngles: List<Double>,
    userAngles: List<Double>,
    poseName: String
): String {
    val filteredAngles = angleDifference(
        referenceAngles,
        userAngles,
        JOINT_DIFF_FILTER,
        MAX_ENTRIES
    )

    if (filteredAngles.isEmpty()) {
        return "I'm doing $poseName pose. My joint angles are close to the teacher's reference; give me one brief plank alignment cue."
    }

    val angleSummary = filteredAngles.entries.joinToString { (name, angleDiff) ->
        "$name: $angleDiff"
    }
    return "I'm doing $poseName pose. My joints have the following significant angle differences to the teacher's: $angleSummary"
}
```

This function calls `angleDifference()` with values that ensure it filters out small differences using `JOINT_DIFF_FILTER` and limits the prompt to `MAX_ENTRIES` joint differences.

The fallback prompt handles the case where the learner is already close to the reference pose. The LLM still creates a useful instruction, but it is not forced to invent a large correction from tiny angle changes. In the full AI Yoga Tutor this fallback won't be hit as a different "praise" prompt is given when the score is high (greater than 70).

## Emit prompts from the ViewModel

Open `ui/viewmodels/MainViewModel.kt`.

Replace the TODO in `userPosePrompt` with this code:

```kotlin
val userPosePrompt: Flow<Pair<String, Double>> =
    sharedUserPoseResults
        .filter { !_isSpeaking.value }
        .map { userResult ->
            generateLlmPromptFrom(
                referenceAngles = userResult.referenceAngles,
                userAngles = userResult.userAngles,
                poseName = poseName
            ) to userResult.scoreVal
        }
        .flowOn(Dispatchers.Default)
```

The prompt is paired with the score because fuller app versions might use both values when deciding what feedback is spoken. In this Learning Path, the LLM step uses the prompt text.

The `_isSpeaking` filter prevents the app from generating more feedback while the previous correction is still being spoken. Speech is added later, but keeping the filter here makes the data flow ready for that final step.

The `flowOn(Dispatchers.Default)` call keeps prompt formatting off the main thread. The work is small, but keeping camera, scoring, prompt generation, LLM inference, and speech on clear execution paths makes the pipeline easier to tune.

## Check the prompt in Logcat

The local LLM is added in the next section. For now, add a temporary collector so you can see the prompt in Logcat.

Open `MainActivity.kt` and update `collectAppState()` so it also collects `userPosePrompt`:

```kotlin
private suspend fun collectAppState() = coroutineScope {
    launch {
        mainViewModel.userPoseScore.collect {
            score.text = getString(R.string.score) + it
        }
    }

    launch {
        mainViewModel.userPosePrompt.collect { prompt ->
            Log.d(TAG, "Pose prompt: ${prompt.first}")
        }
    }
}
```

This Logcat collector is only for checking this section. In the next section, you will replace it with code that sends the prompt to the local LLM.

## Run the app

Build and run the app on your Android device.

Open Logcat and filter for `MainActivity`. As you move in front of the camera, expect short prompts that describe the largest differences from the reference plank pose.

This Logcat check is the validation step for the prompt stage. Expect compact text prompts, not raw landmarks or image data.

The app now has the complete input side of the tutor pipeline:

```text
Camera frame -> pose landmarks -> angle score -> text prompt
```

In the next section, you will add Arm's AI Chat library and send this prompt to a local LLM.
