---
title: Install a Unity Game on a single board computer (Orange Pi 5)
description: Learn how to build and install a Unity game on an Orange Pi 5 single-board computer running Droid OS.
minutes_to_complete: 40

who_is_this_for: This is an introductory topic for software developers who want to build and run a Unity game on an Arm-based single board computer. 

learning_objectives:
    - Install Droid OS on an Orange Pi 5
    - Create a build of a Unity game to run on an Orange Pi
    - Install the Unity game on the Orange Pi

prerequisites:
    - A Windows PC to use Orange Pi's imaging software, which is only available for Windows
    - An Orange Pi 5
    - A microSD card (16GB or greater; class 10 or faster)
    - An ethernet connection
    - A mouse and keyboard connected to the Orange Pi

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:08:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: dea8c3e15cca703f075c8fa9ba3daf873a90e3eb2ee9975dd05b973dad744b54
  summary_generated_at: '2026-06-02T02:59:30Z'
  summary_source_hash: dea8c3e15cca703f075c8fa9ba3daf873a90e3eb2ee9975dd05b973dad744b54
  faq_generated_at: '2026-06-03T00:08:53Z'
  faq_source_hash: dea8c3e15cca703f075c8fa9ba3daf873a90e3eb2ee9975dd05b973dad744b54
  summary: >-
    This introductory Learning Path shows how to install Droid OS on an Arm-based Orange Pi 5,
    build a Unity game for Android, and deploy the resulting APK to the board. You will use a
    Windows PC to obtain the Orange Pi OS (Droid) TF Card image from the Orange Pi 5 support page
    and write it to a microSD card with SDDiskTool, using 7‑Zip as needed for archives. Then you
    will configure Unity Build Settings for Android, add Android Build Support in Unity Hub if
    required, and produce an APK. Finally, you will transfer the APK to the Orange Pi 5 (for example
    via USB, microSD, or a cloud drive over Ethernet) and install it. Prerequisites are explicitly
    listed.
  faqs:
  - question: Do I need a Windows PC to flash Droid OS to the microSD card?
    answer: >-
      Yes. The Orange Pi imaging software used in this path is only available for Windows, so
      the flashing step must be done on a Windows PC.
  - question: Where do I download the correct Droid OS image for Orange Pi 5?
    answer: >-
      Go to the Orange Pi 5 support page, select Orange Pi OS (Droid) > TF Card Image, and download
      the latest release. An example filename provided is OrangePI-OS_Droid_orangepi5_en_v0.0.6_beta.tar.gz.
  - question: Which Unity components are required to build for the Orange Pi 5?
    answer: >-
      In Unity Hub, add the Android Build Support module for the Unity version used by your project.
      In Build Settings, select Android (Unity may prompt a restart), and ensure all needed Android
      subcomponents are included.
  - question: What microSD card should I use for Droid OS on the Orange Pi 5?
    answer: >-
      Use a microSD card that is 16GB or larger and Class 10 or faster. This capacity and speed
      are listed as prerequisites for the path.
  - question: How can I move my Unity APK onto the Orange Pi 5?
    answer: >-
      You can copy the APK via a USB thumb drive if the file systems are compatible, place it
      directly on the microSD card if formats allow, or upload it to a cloud drive and download
      it from Droid OS on the board.
# END generated_summary_faq

author: Gabriel Peterson

### Tags
skilllevels: Introductory
subjects: Gaming
armips:
    - Cortex-A76
    - Cortex-A55
operatingsystems:
    - Android
tools_software_languages:
    - Unity
    - 7-Zip
    - SDDiskTool

further_reading:
    - resource:
        title: Build your application for Android
        link: https://docs.unity3d.com/2022.2/Documentation/Manual/android-BuildProcess.html
        type: documentation
    - resource:
        title: Orange Pi OS Droid
        link: http://www.orangepi.org/html/softWare/orangePiOS/droid.html
        type: website
    - resource:
        title: Unity Learn
        link: https://learn.unity.com/
        type: website




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

