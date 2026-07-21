---
title: Set up AI Plank Tutor
description: Clone and inspect the AI Plank Tutor starter project in Android Studio to understand the on-device camera, pose scoring, LLM, and speech pipeline.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you will build

You'll build an on-device AI fitness tutor app for Android called AI Plank Tutor.

The app watches a learner hold a plank and compares their body position with a stored instructor reference. It asks a local LLM for one short correction, and speaks the correction using Android text-to-speech.

This project is based on [AI Yoga Tutor](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/ai-yoga-tutor). You'll use the same core pipeline, but the project narrows the app to one static pose. By building an app focused on one pose, you can focus on how a pipeline that includes Android camera, pose detector, local LLM, and speech output fits together.

![AI Plank Tutor app comparing a reference plank on the left with the learner's live camera view on the right. The app displays a pose score of 60 and coaching feedback below the two images.#center](screenshot.jpg "AI Plank Tutor comparing a reference pose with the learner's live plank")

The finished app has two main visual areas:

- An instructor plank image on the left.
- A live front-camera preview on the right.

The app overlays a pose score and a short caption that matches the spoken coaching feedback.

You'll start with a starter project that has MediaPipe and camera integration mostly set up. To learn about this setup from an empty project, see the [Build a Hands-Free Selfie Android Application with MediaPipe](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-android-selfie-app-using-mediapipe-multimodality/) Learning Path.

## App pipeline

The app uses a small pipeline of on-device components:

```text
reference image and camera view
        -> CameraX live frames
        -> Pose landmarks
        -> joint-angle scoring
        -> compact text prompt
        -> Arm AI Chat + LLM
        -> Text-To-Speech
```

Each stage passes structured data to a subsequent stage. The LLM doesn't receive camera frames or images. It receives a short text prompt describing the largest joint-angle differences between the learner and the reference plank pose.

This keeps the LLM prompt small, reduces latency, and makes the behavior easier to tune.

## Clone the starter project

Clone the `PlankTutor` Learning Path code example repository:

```console
git clone https://gitlab.arm.com/learning-code-examples/code-examples.git
```

The starter app for this Learning Path is in `code-examples/learning-paths/mobile-graphics-and-gaming/ai-plank-tutor/android`.

{{% notice Note %}}
The starter project contains the app structure, layout, image asset, MediaPipe pose model, and several Kotlin shell files. You'll fill in the missing code in the following sections.
{{% /notice %}}

## Open the project in Android Studio

To open the project in Android Studio: 

1. Start Android Studio.
2. Select **Open**.
3. Open `code-examples/learning-paths/mobile-graphics-and-gaming/ai-plank-tutor/android`.
4. Wait for Gradle sync to finish.

If Android Studio prompts you to trust the project, accept the prompt.

The starter app is intentionally incomplete, but it should sync successfully before you add code. If the `ai-plank-tutor/android` directory is missing, check that you cloned the `PlankTutor` branch.

## Inspect the provided files

Start by looking at the provided files.

Open `app/build.gradle` and confirm that the Android, CameraX, lifecycle, and MediaPipe dependencies are already present.

Arm's AI Chat dependency isn't included yet. You'll add it later, when you implement local LLM inference.

Also note the `packaging { jniLibs { useLegacyPackaging = true } }` setting. The AI Chat library that you'll add later uses native libraries. This packaging setting lets the app load those libraries correctly.

Open `app/src/main/AndroidManifest.xml` and confirm that the app requests camera access:

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

The app package is `com.arm.demo.AIPlankTutor`. You'll use that package name later when copying the LLM model into the app-specific external files directory with `adb`.

Open `app/src/main/res/layout/activity_main.xml` and review the main UI. The layout already contains:

- An `ImageView` for the instructor plank image.
- A `PreviewView` for the live camera.
- A score label.
- A caption label for spoken feedback.

Open `app/src/main/res/drawable/plank.jpg` and review the instructor reference image.

The code is under the long path `app/src/main/java/com/arm/demo/AIPlankTutor`. Copy this path exactly, including the capitalized `AIPlankTutor` package directory. In the directory, open `data/PlankPoseData.kt` and note the hard-coded plank reference data. This file contains the instructor's reference landmarks and angle weights used by the scoring step. This was generated from the reference plank image in an offline step so it doesn't need any runtime compute.

## What you've accomplished and what's next 

You've now set up the AI Plank Tutor project by downloading a starter project and inspecting the files.

Next, you'll inspect Android code in the `MainActivity.kt` file and connect the camera to the MediaPipe pose landmarker.
