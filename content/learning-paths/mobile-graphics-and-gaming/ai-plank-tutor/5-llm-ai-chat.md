---
title: Run the LLM locally with AI Chat
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Objective

In this section, you will add Arm's AI Chat library and use it to run a local GGUF model on the Android device.

You will:

- Add the AI Chat dependency.
- Import the Phi-4-mini GGUF model file onto the device.
- Create an AI Chat inference engine.
- Load the model and set the tutor system prompt.
- Send the pose prompt from the previous section to the local LLM.
- Convert streamed LLM tokens into complete `Sentence` objects.

At the end of this section, the app will produce short text coaching corrections and show them as captions. Speech output is added in the next section.

## Add the AI Chat dependency

Open `app/build.gradle`.

Add the AI Chat dependency to the end of the `dependencies` block:

```groovy
implementation("com.arm:ai-chat:0.1.0")
```

Sync the project with Gradle.

The AI Chat library provides the Android inference API used by this project and by the [Arm AI Chat app](https://play.google.com/store/apps/details?id=com.arm.aichat&hl=en_GB). It uses `llama.cpp` for GGUF inference, and `llama.cpp` integrates Arm [KleidiAI](https://developer.arm.com/ai/kleidi-libraries) kernels. Q4_0 GGUF models work particularly well with these kernels and can get strong acceleration on phones with [SME2](https://www.arm.com/technologies/sme2), SVE2, and Neon support.

## Add the model file to the device

The app expects a Q4_0 GGUF model file named:

```text
Phi-4-mini-instruct-Q4_0.gguf
```

Download [microsoft_Phi-4-mini-instruct-Q4_0.gguf](https://huggingface.co/bartowski/microsoft_Phi-4-mini-instruct-GGUF/blob/main/microsoft_Phi-4-mini-instruct-Q4_0.gguf) from Hugging Face. The model is 3.8B parameters, and around 2.2GB. Remove the "microsoft_" off the front of the name.

The provided `LlmModelStore.kt` helper looks for the model in a few import locations. The most useful location while developing is the app-specific external files directory:

```text
/sdcard/Android/data/com.arm.demo.AIPlankTutor/files/llm/Phi-4-mini-instruct-Q4_0.gguf
```

With your device connected over USB, create the directory:

```console
adb shell mkdir -p /sdcard/Android/data/com.arm.demo.AIPlankTutor/files/llm
```

Then push the model file:

```console
adb push Phi-4-mini-instruct-Q4_0.gguf /sdcard/Android/data/com.arm.demo.AIPlankTutor/files/llm/
```

When the app first loads the model, `LlmModelStore` copies it into the app's internal files directory. Later runs use the internal copy.

{{% notice Note %}}
If the model cannot be found, check Logcat for `LlmModelStore`. The error message lists every model path that was checked.
{{% /notice %}}

## Wire AI Chat into MainActivity

Open `ui/MainActivity.kt`.

Add these imports:

```kotlin
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewmodel.CreationExtras
import com.arm.aichat.AiChat
import com.arm.demo.AIPlankTutor.llm.LlmModelStore
import com.arm.demo.AIPlankTutor.ui.viewmodels.LlmViewModel
```

Add an `llmViewModel` property below the existing `mainViewModel` property:

```kotlin
private val mainViewModel: MainViewModel by viewModels()
private val llmViewModel: LlmViewModel by viewModels {
    object : ViewModelProvider.Factory {
        @Suppress("UNCHECKED_CAST")
        override fun <T : ViewModel> create(modelClass: Class<T>, extras: CreationExtras): T {
            val inferenceEngine = AiChat.getInferenceEngine(applicationContext)
            val modelStore = LlmModelStore(applicationContext)
            return LlmViewModel(inferenceEngine, modelStore) as T
        }
    }
}
```

`AiChat.getInferenceEngine()` creates the inference engine used by the ViewModel. `LlmModelStore` is the helper that finds or imports the GGUF model file. Now we need to make the `LlmViewModel` accept those parameters.

## Add AI Chat to LlmViewModel

Open `LlmViewModel.kt`.

Add these imports:

```kotlin
import android.util.Log
import androidx.lifecycle.viewModelScope
import com.arm.aichat.InferenceEngine
import com.arm.demo.AIPlankTutor.llm.LlmModelStore
import kotlinx.coroutines.flow.onCompletion
import kotlinx.coroutines.launch
```

Change the class declaration so the ViewModel receives the AI Chat inference engine and model store:

```kotlin
class LlmViewModel(
    private val inferenceEngine: InferenceEngine,
    private val llmModelStore: LlmModelStore,
) : ViewModel() {
```

Add this `init` block at the very start of the class body:

```kotlin
init {
    viewModelScope.launch {
        _isBusy.emit(true)
        loadModelAndSystemPrompt()
        _isBusy.emit(false)
        _systemPromptProcessed.emit(true)
    }
}
```

When the ViewModel is created, this loads the model and sends the system prompt. The existing `_isBusy` state will also be used to avoid starting another LLM generation while one is already running.

## Load the model and system prompt

Replace the TODO in `loadModelAndSystemPrompt()` with this code:

```kotlin
private suspend fun loadModelAndSystemPrompt() {
    val modelFile = llmModelStore.getModelFile()
    inferenceEngine.loadModel(modelFile.absolutePath)
    inferenceEngine.setSystemPrompt(TUTOR_SYSTEM_PROMPT)
}
```

You can read `TUTOR_SYSTEM_PROMPT` at the bottom of the file. The system prompt tells the model to act as a concise yoga teacher, use the joint-angle facts, and return one short correction.

## Send a prompt to AI Chat

Replace the TODO in `sendUserPrompt()` with this code:

```kotlin
fun sendUserPrompt(
    plainTextMessage: String,
    generationLimit: Int = LLM_GENERATION_LIMIT,
) {
    if (_isBusy.value) return

    viewModelScope.launch {
        if (_isBusy.value) return@launch

        Log.d(TAG, "Sending:\n$plainTextMessage")

        _isBusy.emit(true)

        var tokenCount = 0

        inferenceEngine.sendUserPrompt(plainTextMessage, predictLength = generationLimit)
            .onCompletion { cause ->
                _isBusy.emit(false)
                if (sentence.isNotEmpty()) {
                    _tokens.emit(".")
                }
                if (cause != null) {
                    Log.d(TAG, "> Token collection aborted! $cause")
                } else if (tokenCount == 0) {
                    Log.d(TAG, "> No tokens collected!")
                } else {
                    Log.d(TAG, "> Token collection complete.")
                }
            }
            .collect { token ->
                tokenCount++
                _tokens.emit(token)
            }
    }
}
```

The two `_isBusy` checks prevent the app from starting a second generation if a new prompt arrives just before image analysis is disabled. The `onCompletion` block emits a final full stop if the model stops before ending the current sentence. That lets the sentence splitter flush the last partial sentence.

## Split streamed tokens into sentences

AI Chat returns a stream of tokens. Android TTS works better with complete phrases or sentences, so split the stream before page 6 consumes it.

Replace the TODO in the `sentences` Flow with this code:

```kotlin
val sentences: Flow<Sentence> = _tokens
    .filterNot { it.isNewLine() }
    .map { word ->
        if (sentence.isEmpty()) {
            if (word.isPunctuation()) return@map null
        }

        sentence.append(if (sentence.isEmpty()) word.trimStart() else word)

        if (sentence.isNotEmpty() && word.isPunctuation()) {
            sentence.run { toString().also { setLength(0) } }
        } else null
    }
    .filterNotNull()
    .map { text -> Sentence(text) }
    .flowOn(Dispatchers.Default)
```

The ViewModel now exposes a `Flow<Sentence>` instead of raw tokens. Page 6 will collect this Flow and send each sentence to Android text-to-speech.

## Send pose prompts to the LLM

Return to `MainActivity.kt`.

In the previous section, you logged each pose prompt to Logcat. Replace that temporary prompt collector in `collectAppState()` with this version:

```kotlin
launch {
    mainViewModel.userPosePrompt.collect {
        if (imageAnalysisEnabled && llmViewModel.systemPromptProcessed.value) {
            llmViewModel.sendUserPrompt(it.first)
        }
    }
}
```

Add another collector to pause image analysis while the model is busy:

```kotlin
launch {
    llmViewModel.isBusy.collect {
        imageAnalysisEnabled = !it
    }
}
```

This prevents the app from generating a new prompt for every camera frame while the LLM is already responding.

Finally, add a temporary sentence collector so you can show the generated correction in the caption area and check it in Logcat:

```kotlin
launch {
    llmViewModel.sentences.collect { sentence ->
        captionTextView.text = sentence.text
        captionTextView.visibility = View.VISIBLE
        Log.d(TAG, "Tutor correction: ${sentence.text}")
    }
}
```

The next section will replace this direct caption update with `SpeechManager`, so the caption stays synchronized with Android text-to-speech playback.

## Run the app

Build and run the app on your Android device. You should see the tutor's advice now at the bottom of the screen.

To see what's happening behind the scenes, open Logcat and filter for `LlmViewModel` or `MainActivity`. The app should load the model, send pose prompts, and print short tutor corrections. 

The first run can take longer because the model file may be copied into the app's internal storage and loaded into memory. Later runs should start faster.

At this point, the app can generate local text feedback. The next section uses Android `TextToSpeech` to speak each completed sentence and show it as a caption.
