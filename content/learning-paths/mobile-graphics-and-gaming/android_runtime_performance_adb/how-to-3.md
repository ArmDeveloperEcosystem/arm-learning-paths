---
title: Instrument and install reference application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the reference application
You need an application to profile, and for the Learning Path you'll use this reference application: [PhotoTalk](https://github.com/google-ai-edge/litert-samples/tree/main/samples/litert/phototalk_sample_app), an open-source LiteRT-LM sample application for interactive image-based conversation. Download it onto your host machine so you can measure its runtime performance. You can also adapt all the steps to your own application to measure its runtime performance assuming it is LiteRT-LM based.

Clone the repository into your working directory:
``` bash
cd $WORK
git clone https://github.com/google-ai-edge/litert-samples.git
```

## Modify the reference application
PhotoTalk doesn’t log LiteRT-LM model performance metrics by default. Modify its Conversation API calls to log these metrics. You can apply the same approach to other applications that use the LiteRT-LM Conversation API.

Navigate to the PhotoTalk source directory, then open `LiteRtLmHelper.kt` in your preferred editor:

```text
litert-samples/samples/litert/phototalk_sample_app/android/app/src/main/java/com/google/aiedge/examples/phototalk/LiteRtLmHelper.kt
```

Make sure that the following imports are present:
``` java
import android.util.Log
import com.google.ai.edge.litertlm.ExperimentalApi
import com.google.ai.edge.litertlm.ExperimentalFlags
```
Immediately before the class definition, add:
```java
@OptIn(ExperimentalApi::class)
```

Find the line that says `newEngine.initialize()` and just before it add:
```java
ExperimentalFlags.enableBenchmark = true
```
Finally, you need to locate the call to `sendMessageAsync`. In the case of PhotoTalk it appears as follows:
```java
conv.sendMessageAsync(prompt, object : MessageCallback {
            override fun onMessage(message: Message) {
                trySend(message.toString())
            }
            override fun onDone() {
                close()
            }
            override fun onError(throwable: Throwable) {
                close(throwable)
            }
        })
```
Here an object called `MessageCallback` is passed as an action argument to `sendMessageAsync`. This is the function call to the model. `MessageCallback` executes its methods each time this function is called.

Firstly add this line just before `conv.sendMessageAsync(...)` to log the inference start timestamp:
```java
val inferenceStartUnixMilliseconds = System.currentTimeMillis()
```

Then edit the `onDone()` method by adding these three lines before `close()`:
```java
val metrics = conv.getBenchmarkInfo()
val completionUnixMilliseconds = System.currentTimeMillis()
Log.i("LiteRtPerformance","LLM_INFERENCE_CSV $inferenceStartUnixMilliseconds, $completionUnixMilliseconds, ${prompt.length}, ${metrics.lastPrefillTokenCount}, ${metrics.lastDecodeTokenCount}, ${metrics.timeToFirstTokenInSecond}, ${metrics.lastPrefillTokensPerSecond}, ${metrics.lastDecodeTokensPerSecond}")
```
Save and close the file after making the edits. Now each time the model is called the application will write these metrics to the log:
- Prompt length
- Prefill speed
- Decode speed
- Time to first token (TTFT)

The monitoring script you will use automatically collects these log entries.

The reference application comes with its own Gradle-based build wrapper, which will automatically install any missing Android build tools or libraries. The build will automatically use the wireless connection you have previously established:
``` bash
cd $WORK/litert-samples/samples/litert/phototalk_sample_app/android
./gradlew installDebug
```
You should now have the PhotoTalk application installed on your target device.

{{% notice Disclaimer%}}
The PhotoTalk build might need additional Android SDK packages. Gradle downloads missing packages when the required SDK licences have been accepted. If the build reports a missing package or licence, install or accept it using the Android CLI, then run the command again.
For example:

`android --sdk="$ANDROID_HOME" sdk install PACKAGE`
{{% /notice %}}

## Download and push a LiteRT-LM model
PhotoTalk automatically scans your Android device's `/sdcard/Download/` folder for compatible `.litertlm` models. Supported model families include:
- Gemma 4 E2B
- Gemma 3 1B
- FastVLM (0.5B)

You will use Gemma 4 E2B for this Learning Path, which can be downloaded from [Hugging Face](https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm).

{{% notice Note %}}
Downloading the model can take around 30 minutes, depending on your network connection.
{{% /notice %}}
```bash
mkdir -p "$WORK/models"
hf download litert-community/gemma-4-E2B-it-litert-lm gemma-4-E2B-it.litertlm --local-dir "$WORK/models"
```

After you download the model, push it to the appropriate location on the Android device:
```bash
adb push $WORK/models/gemma-4-E2B-it.litertlm /sdcard/Download/
```
Validate that the model was pushed successfully:
```bash
adb shell 'ls -lh /sdcard/Download/*.litertlm'
```

{{% notice Disclaimer%}}
Make sure to use a test device or provide only non-sensitive prompts and images. Also note that the model will remain in `/sdcard/Download/` after the tutorial until removed.
{{% /notice %}}

## What you've accomplished and what's next
You have modified the PhotoTalk application to expose Large language model (LLM) activity and uploaded it, along with a LiteRT-LM model, onto your target Android device. Proceed to the next section where you will prepare the performance monitoring infrastructure.
