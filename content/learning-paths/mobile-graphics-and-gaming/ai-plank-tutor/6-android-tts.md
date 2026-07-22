---
title: Connect coaching corrections to Android text-to-speech
description: Connect generated coaching corrections to Android TextToSpeech and synchronize each spoken phrase with its on-screen caption.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Initialize TextToSpeech

Android `TextToSpeech` uses the TTS engine and voices installed on the device. The exact voice, language support, and quality can vary by phone, but the app code is the same.

Open `ui/SpeechManager.kt`.

The starter file already includes the imports, state flows, and helper functions needed. The two pieces of state exposed by the class are:

- `idle`: whether Android TTS has finished speaking all queued phrases.
- `currentCaption`: the text that should be shown at the bottom of the screen.

Replace the TODO in the `init` block with the following code:

```kotlin
init {
    tts = TextToSpeech(context.applicationContext) { status ->
        if (status == TextToSpeech.SUCCESS) {
            tts.language = Locale.getDefault()
        } else {
            Log.w(TAG, "TextToSpeech initialization failed with status $status")
        }
    }

    tts.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
        override fun onStart(utteranceId: String?) {
            utteranceId?.let { id -> getQueuedCaption(id)?.let { setCaption(it) } }
            setIdle(false)
        }

        override fun onDone(utteranceId: String?) {
            finishUtterance(utteranceId)
        }

        @Suppress("OVERRIDE_DEPRECATION")
        override fun onError(utteranceId: String?) {
            finishUtterance(utteranceId)
        }
    })
}
```

The `TextToSpeech` callback sets the default device language when initialization succeeds. The `UtteranceProgressListener` is called by Android as each spoken phrase starts and finishes.

The listener callbacks aren't guaranteed to run on the main thread, so the provided `setCaption()` and `setIdle()` helpers update the flows through a main-thread coroutine.

## Queue speech

Replace the TODO in `launchSpeechGenerationAndPlaybackJob()` with the following code:

```kotlin
fun launchSpeechGenerationAndPlaybackJob(speech: String) {
    if (speech.isBlank()) return

    val utteranceId = UUID.randomUUID().toString()
    queueUtterance(utteranceId, speech)
    setIdle(false)
    val result = tts.speak(speech, TextToSpeech.QUEUE_ADD, null, utteranceId)
    if (result == TextToSpeech.ERROR) {
        Log.w(TAG, "TextToSpeech failed to queue utterance")
        finishUtterance(utteranceId)
    }
}
```

`TextToSpeech.QUEUE_ADD` is important here. The LLM output is streamed and split into complete sentences, so the app might receive another sentence while Android is still speaking the previous one. `QUEUE_ADD` makes Android speak the phrases in order instead of interrupting the current phrase.

Each phrase is queued with an utterance ID. `SpeechManager` keeps a small map from utterance ID to caption text so the app can show the caption only when that phrase starts speaking.

The `speak()` call is asynchronous. A successful return value means Android accepted the phrase into the TTS queue, not that speech has already finished. The progress listener is what tells the app when playback starts and ends.

## Finish each utterance

Replace the TODO in `finishUtterance()` with this code:

```kotlin
private fun finishUtterance(utteranceId: String?) {
    val queueIsEmpty = synchronized(queuedUtterances) {
        utteranceId?.let { queuedUtterances.remove(it) }
        queuedUtterances.isEmpty()
    }

    setCaption("")
    setIdle(queueIsEmpty)
}
```

When Android reports that an utterance has finished, `finishUtterance()` removes it from the queue map. The same helper is used if `tts.speak()` fails to queue an utterance. If no queued utterances remain, `idle` becomes `true`.

The existing `shutdown()` function stops and releases Android TTS when the activity is destroyed.

## Connect SpeechManager to MainActivity

Open `ui/MainActivity.kt`.

In the last section, you added a temporary sentences collector that put each LLM sentence directly into the caption view and logged it. Now replace that collector with this version:

```kotlin
launch {
    llmViewModel.sentences.collect { sentence ->
        mainViewModel.setSpeaking(true)
        speechManager.launchSpeechGenerationAndPlaybackJob(sentence.text)
    }
}
```

This sends each completed LLM sentence to Android TTS instead of writing it directly to the caption view.

Next, add a collector for `speechManager.idle`:

```kotlin
launch {
    speechManager.idle.collect { idle ->
        mainViewModel.setSpeaking(!idle)
    }
}
```

`MainViewModel` uses this state to avoid asking the LLM for another correction while the current spoken feedback is still playing.

Finally, add a collector for `speechManager.currentCaption`:

```kotlin
launch {
    speechManager.currentCaption.collect { caption ->
        captionTextView.text = caption
        captionTextView.visibility =
            if (caption.isBlank()) View.INVISIBLE else View.VISIBLE
    }
}
```

The caption is now controlled by Android TTS playback. It appears when Android starts speaking a phrase and disappears when that phrase finishes.

## Run the app

Build and run the app on your Android device.

Move into a plank position in front of the camera. The score should update, the local LLM should generate a short correction, and Android TTS should speak it. The same correction should appear as a caption while it is being spoken.

If captions appear but you don't hear speech, check the device media volume and confirm that a TTS voice is installed for the default language.

## What you've accomplished and what's next

You've now used Android's built-in `TextToSpeech` engine to update the app to speak each coaching correction from the local LLM. The app shows the same text as a caption while it's being spoken.

At this point, the app has the full on-device pipeline: camera input, pose landmarks, joint-angle scoring, local LLM feedback, and spoken output.

Next, you'll explore ways to improve and extend the app.
