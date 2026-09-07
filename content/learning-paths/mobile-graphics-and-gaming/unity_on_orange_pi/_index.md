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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:29:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 01e106be6f9e1748ae217eed10b16a972fef98a05effd3e41db0f46d3a40ebb6
  summary_generated_at: '2026-08-21T17:29:17Z'
  summary_source_hash: 01e106be6f9e1748ae217eed10b16a972fef98a05effd3e41db0f46d3a40ebb6
  faq_generated_at: '2026-08-21T17:29:17Z'
  faq_source_hash: 01e106be6f9e1748ae217eed10b16a972fef98a05effd3e41db0f46d3a40ebb6
  summary: >-
    You'll prepare an Orange Pi 5 to run a Unity game on Droid OS, then create and install the game’s
    Android APK. First, you'll download the Droid OS image and the required `SDDiskTool_v1.72` on Windows,
    write the image to a microSD card, and start the board. Then, you'll configure Unity for Android, build
    the APK, transfer it to the board, and install it from Droid OS.
  faqs:
  - question: Where do I get the Droid OS image for Orange Pi 5?
    answer: >-
      Go to the Orange Pi 5 support page and select **Orange Pi OS(Droid) > TF Card Image**. In
      Google Drive, download the latest image for Orange Pi 5.
  - question: How do I write the Droid OS image to the microSD card?
    answer: >-
      On Windows, extract the downloaded `.tar.gz`, then the resulting `.tar`, to produce a `.img`
      file. Use `SDDiskTool_v1.72` to write the `.img` file to the microSD card.
  - question: What should I check if Android isn't available in Unity Build Settings?
    answer: >-
      In Unity Hub, select **Installs**, find the Unity version for your project, select its three-dot
      menu, then select **Add Modules**. Select **Android Build Support** and all its sub-items.
      In Unity, select **File > Build Settings**, choose **Android**, and restart Unity when prompted.
  - question: What output file should I expect from the Unity build?
    answer: >-
      When you build for Android, choose a folder for the generated APK file. Transfer that APK
      to the Orange Pi 5 and install it on Droid OS.
  - question: How can I transfer the APK to the Orange Pi 5?
    answer: >-
      Use a USB thumb drive if its file system is compatible with Droid OS, copy the file onto
      the microSD card if formats are compatible, or upload it to a cloud drive and download it
      on the Orange Pi. If you use a cloud service, ensure the board has network access.
# END generated_summary_faq

author: Gabriel Peterson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Gaming
armips:
    - Cortex-A
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
