---
title: Build the Voice Assistant
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section you will build the Voice Assistant application to run on your Android phone.

## Download the Voice Assistant

Start by cloning the repository with the complete example application code:

```bash
git clone https://git.gitlab.arm.com/kleidi/kleidi-examples/real-time-voice-assistant.git voice-assistant.git
```

## Build the Voice Assistant

Open Android Studio and open the project that you downloaded in the previous step:

![example image alt-text#center](open_project.png "Figure 2: Open the project in Android Studio.")

Build the application with its default settings by clicking the little hammer
"Make Module `VoiceAssistant.app`" button in the upper right corner:

![example image alt-text#center](build_project.png "Figure 3: Build the project.")

Android Studio will start the build. The build may take some time if it needs to
download some dependencies for the Voice Assistant app that are not already installed:

![example image alt-text#center](build_success.png "Figure 4: Successful build!")

Now that you have successfully built the Android application, you will run it in the next step.
