---
title: Add AI Chat Library
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Your freshly created Android Studio project should already have top-level repositories including `google()` and `mavenCentral()` in `settings.gradle.kts`, but check that it does, to ensure the app can find the library.

## Add the Maven Dependency
We need to add the AI Chat library in the app module build file, `app/build.gradle.kts` (not the project `build.gradle.kts` in the root of the project).

In here we add into the `dependencies` section at the bottom:
```kotlin
    implementation("com.arm:ai-chat:0.1.0")
```

This adds the library to your project, and all the LLM functionality. Also in this file, check that:
- `targetSdk` and `compileSdk` are 36
- the Java version in `compileOptions` is `JavaVersion.VERSION_17`
- the `jvmTarget` in `kotlinOptions` is 17

In `libs.version.toml` we need to change the `kotlin` version to `2.2.20`, as the library requires a more recent version than the default.

Finally, there will be a banner at the top of these settings files saying the "Gradle files have changed since last project sync." Choose the option to "Sync Now", and let the project update. 

## Adjust the Manifest
We need to adjust the `AndroidManifest.xml` file, which is in `app\src\main`.

Most of the file is an xml tag `<application ...>`. Within the tag are several `android:` options. Add in an additional flag to load the needed llama.cpp native libraries:
```xml
<application
    ...
    android:extractNativeLibs="true"
    ... >
```
