---
title: Build the Voice Assistant
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the Voice Assistant

```BASH
git clone https://git.gitlab.arm.com/kleidi/kleidi-examples/real-time-voice-assistant.git voice-assistant.git
```

## Build the Voice Assistant

Open Android Studio and open the project that you just downloaded in the preceding step:

![example image alt-text#center](open_project.png "Figure 2: Open the project in Android Studio.")

Build the application with its default settings by clicking the little hammer
"Make Module 'VoiceAssistant.app'" button in the upper right corner:

![example image alt-text#center](build_project.png "Figure 3: Build the project.")

Android Studio will start the build, which may take some time if it needs to
download some dependencies of the Voice Assistant app:

![example image alt-text#center](build_success.png "Figure 4: Successful build!")