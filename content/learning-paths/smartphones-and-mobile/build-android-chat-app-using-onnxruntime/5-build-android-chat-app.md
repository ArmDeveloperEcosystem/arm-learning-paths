---
title: Build and Run Android chat app
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build Android chat app

Another way to run the model is to use a GUI Android app.
You can use the Android demo application included in [onnxruntime-inference-examples repository](https://github.com/microsoft/onnxruntime-inference-examples) to demonstrate local inference.

### Clone the repo

``` bash
git clone https://github.com/microsoft/onnxruntime-inference-examples
cd onnxruntime-inference-examples
```

{{% notice Note %}}
These steps have been tested with the commit `009920df0136d7dfa53944d06af01002fb63e2f5`.
{{% /notice %}}

### Build the app using Android Studio

Open `mobile\examples\phi-3\android` directory with Android Studio.

#### (Optional) In case you want to use ONNX Runtime AAR you built

Copy ONNX Runtime AAR you built before if needed

```bash
Copy onnxruntime\build\Windows\Release\java\build\android\outputs\aar\onnxruntime-release.aar mobile\examples\phi-3\android\app\libs
```

Update build.gradle.kts (:app) as below:

``` kotlin
// ONNX Runtime with GenAI
//implementation("com.microsoft.onnxruntime:onnxruntime-android:latest.release")
implementation(files("libs/onnxruntime-release.aar"))
```

After that, click `File`->`Sync Project with Gradle`

#### Build and run the app

When you press Run, the build will be executed, and then the app will be transferred and installed on the Android device. This app will automatically download the Phi-3-mini model during the first run. After the download, you can input the prompt in the text box and execute it to run the model.

You should now see a running app on your phone that looks like this:

![App screenshot](screenshot.png)
