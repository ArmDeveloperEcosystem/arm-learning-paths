---

title: Run the voice assistant
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous section, you built the Voice Assistant application. Now, you'll install it on your Android phone. The easiest way is to enable developer mode and use a USB cable to upload the application.

## Switch to developer mode

By default, Android devices ship with developer mode disabled. To enable it, follow [these instructions](https://developer.android.com/studio/debug/dev-options).

## Install the voice assistant

Once developer mode is enabled, connect your phone to your computer via USB. It should appear as a running device in the top toolbar. Select the device and click the Run button (a small red circle, as figure 4 below shows). This transfers the app to your phone and launches it.

In the picture below, a Pixel 6a phone is connected to the USB cable:
![example image alt-text#center](upload.png "Figure 5: Upload the Voice App")

## Launch the voice assistant

The Voice Assistant welcomes you with this screen:

![example image alt-text#center](voice_assistant_view1.png "Figure 6: Welcome Screen")

Tap **Press to Talk** at the bottom of the screen to begin speaking your request.

## Voice assistant controls

### View performance counters

You can toggle performance counters such as:
- Speech recognition time.
- LLM encode tokens per second.
- LLM decode tokens per second.
- Speech generation time.

Click the icon circled in red in the upper left corner to show or hide these metrics:

![example image alt-text#center](voice_assistant_view2.png "Figure 7: Performance Counters")

### Reset assistant context

To reset the assistant's conversation history, click the icon circled in red in the upper right:

![example image alt-text#center](voice_assistant_view3.png "Figure 8: Reset the Voice Assistant's Context")
