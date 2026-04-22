---
title: Configure the AI Chat library dependency
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Your freshly created Android Studio project should already have top-level repositories including `google()` and `mavenCentral()` in `settings.gradle.kts`. Verify that both repositories are present to ensure the app can find the AI Chat library.

## Add the Maven dependency

Add the AI Chat library in the app module build file `app/build.gradle.kts` (not the project-level `build.gradle.kts` in the root of the project).

In the `dependencies` section at the bottom, add:
```kotlin
    implementation("com.arm:ai-chat:0.1.0")
```

This adds the library to your project along with all LLM functionality. Also in this file, verify that:
- `targetSdk` and `compileSdk` are 36
- the Java version in `compileOptions` is `JavaVersion.VERSION_17`
- the `jvmTarget` in `kotlinOptions` is 17

In `libs.version.toml`, check that:
- `kotlin` version is `2.2.20`

Finally, there will be a banner at the top of these settings files saying the "Gradle files have changed since last project sync." Select the option to "Sync Now" and let the project update.

## Configure the manifest

Adjust the `AndroidManifest.xml` file, which is in `app\src\main`.

Most of the file consists of an XML tag `<application ...>`. Within the tag are several `android:` options. Add an additional flag to enable loading of the required llama.cpp native libraries:
```xml
<application
    ...
    android:extractNativeLibs="true"
    ... >
```

Your project is now configured with the AI Chat library dependency and the necessary manifest settings to load native libraries. In the next section, you'll create the user interface layouts and message adapter for the chat functionality.
