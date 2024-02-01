---
title: Install Unity and the project
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Getting started

The Unity ML Agents toolkit provides a C# API for use in your project and Python scripts to run outside of Unity. We'll need Python itself and a few extra libraries.

We need the Python tools before we can run our training stage, but to get going quickly we'll just install Unity for now.

## The tools we will need

We will install Unity via the Unity Hub. The Unity Hub provides an easy way to manage multiple installations of Unity. It also provides a straightforward way of adding the extra support modules we'll need. Here is what we'll end up with:

* Unity Hub
* Unity
* Visual Studio Community Edition (Unity support module)
* Dr Arm Unity project files (the accompanying zip file)
* [_only for deploying to an Android device_] Android build support (Unity support module)

The installation instructions in the next section will take us through the above steps one by one, starting with the Unity Hub.

## Installing Unity Hub, Unity and support modules

Assuming you don't already have Unity installed:

1. Download and install the [Unity Hub](https://unity3d.com/get-unity/download?ref=personal)

    Note that Personal licenses are free, and if running on Windows you will need Windows 10 or 11 and a GPU with DirectX 10 capabilities. If running Unity on a Mac or Linux, please follow the instructions for your platform.

1. In your Unity Hub download and install Unity. The latest LTS (Long Term Support) release should work but this project has been tested on 2022.3.12f1.

    1. In Unity Hub go to **Installs** and click **Install Editor**

    1. Go to the _Archive_ page and find version 2022.3.12f1. Select the "Unity Hub" download button rather than downloading the Unity Editor directly

    1. The install will require several gigabytes (including Android deployment options) so please check your available disk space first

1. Add Android Build support

    1. Click the _Settings_ icon and choose _Add Modules_

        ![Unity Hub Installs](images/UnityHubInstalls.png "Figure 1. List of Unity versions installed")

    1. Under **Dev Tools**, choose _Microsoft Visual Studio Community 2022_ if you wish to install it. This integrates well with Unity as a code editor, but any editor will do for editing scripts

    1. Under **Platforms**, choose _Android Build Support_. Also make sure to choose _OpenJDK_ and _Android SDK & NDK Tools_ as well

        ![Unity Hub Add Modules](images/unity-hub-add-modules.png "Figure 2. Tick the modules you want installed")

    1. Press _Continue_, and then agree to the Android SDK and NDK License Terms to install everything

    1. If you prefer to use an alternative script editor, you might want to check your editor is active; see section below _Check active script editor in Unity_

## Download and open the Dr Arm Unity project

1. Download and extract the accompanying Unity project from the [supporting zip file](../files/MLAgentsWorkshopSupportingFiles.zip).

1. Open Unity Hub

1. From the Unity Hub, under the Projects tab, click the down-arrow next to Open and select "Add project from disk".

1. Choose the location of your workshop files (the directory that contains the _Assets_ folder)

1. The project will appear in the list. Click it to open the project in Unity.

1. It may take a few minutes for Unity to process the asset files.

## Check active script editor in Unity

Depending on your setup, it is possible that the default script editor is not set to your preferred editor:

1. In Unity select _Edit_ menu and then _Preferences_

1. In the _Preferences_ window, select _External Tools_ on the left

1. Select your desired editor from the drop-down menu next to _External Script Editor_

    ![External script editor window](images/unity-external-script-editor.jpg "Figure 3. External tool options in Unity")
