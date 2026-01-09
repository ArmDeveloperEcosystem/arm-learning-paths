---
title: Set up
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this Learning Path, you will build and deploy a simple project to an Android device. You will then explore device profiling techniques and examine the first few steps you might want to take when investigating your application's performance.

You will prepare three things before you can get going:

1. Install Unity (latest version recommended)
2. Add Android Build Support
3. Extract the sample project from this Learning Path

## Install Unity with Android build support

First off, if you haven't already got Unity, follow the steps to get the latest version. The simplest way to get Unity is via the installation manager called Unity Hub. Unity Hub will let you manage multiple installations of Unity and also provide quick access to your projects.

- Download Unity Hub now by following the instructions at [unity.com/download](https://unity.com/download)

- Run the Hub once it has downloaded. If you are not already logged in, you will be prompted to either log in or create an account.

- Once logged in, if you don't already have any editor versions installed, Unity may recommend the latest Long-Term Support version.

![Unity LTS suggested installation#center](images/unity-auto-suggested-install.png "Figure 1. Long Term Support version suggested by Unity Hub") 

- Go ahead and install the suggested editor. If you don't see the above screen, you can always install a version of Unity manually. Click on the _Installs_ tab on the left to see the list of installed editors (which will likely be empty):

![Empty installs windows#center](images/unity-no-installs.png "Figure 2. Unity Hub installation list (empty)") 

- Click on the recommended version. On the next screen you will add the Android module:

![Recommended editor version#center](images/install-6.3.png "Figure 3. Install recommended LTS version")

You should see a list of optional features to install with your editor. You can install Android build support now. In the list, click on "Android Build Support".

![Install Android Build Support module#center](images/install-android6.3.png "Figure 4. Add Android Build Support module") 

You now have Unity and Android support. If you forgot to tick Android Build Support or you already had a version of Unity without it, follow the next section to download Android support separately.

### Optional: Install Android build support on pre-existing versions of Unity

Follow these steps if you already have a version of Unity and just need to add the Android build support. Unity Hub lets you install modules on top of existing installations. Each editor version you install can have different modules installed on top.

- Click on the _Installs_ tab on the left to see your list of editor installations. Then click on the cog button and select _Add Modules_:

![Add Modules option#center](images/6.3-add.png "Figure 5. Select Add Modules on the editor for which you wish to add Android support") 

- You will be presented with the module list. Select _Android Build Support_ and any other modules you wish to install. Then click _Continue_.

- Once you have installed Android Build Support, you have everything you need for this Learning Path.

### Android SDK and NDK

Android Build Support installs and manages the Android SDK and Android NDK for you. If you ever need to access the SDK or NDK directly, you can find them in the _External Tools_ tab of Unity Editor Preferences (menu option _Edit->Preferences_).

![Android settings in preferences#center](images/external-tools6.3.png "Figure 6. Android settings in Preferences")

_Note that this will be within a project, not the hub_

## 3. Extract and open the Unity project

A simple project is provided to accompany this Learning Path. To open it in Unity, please follow these instructions:

- Unzip the [simple profiling example](supporting-files/simple-profiling-example.zip) to your computer. 
  Save this to your local disk only. Using cloud storage (e.g. OneDrive, iCloud) may cause errors later on

- In Unity Hub, from the _Projects_ tab, select _Add project from disk_ from the drop-down menu:

![Add project from disk#center](images/add-disk.png "Figure 7. Add the sample project to Unity Hub")

- Navigate to your unzipped project directory and click "Add project"

You will see your project listed in the _Projects_ tab in Unity Hub.

- You can now click on the project to open it. The sample was created with Unity 2022.3.18f1; if you use a different version, you will get a warning. The project is very simple and should be safe to convert. However, if in doubt, install 2022.3.18f1 via the Unity Hub as already shown.

- The project will now open in Unity. Once loaded (the first time can take a while) find the scene folder, open the sample scene, and then click the _Play_ button to run the sample. This will run the project inside the editor. You will see a spinning cube.

![Spinning cube sample#center](images/app-running-slowly.png "Figure 8. The spinning cube sample running in the editor")

- In the top right of the _Game_ window, click on _Stats_ to show the _Statistics_ popup. You will notice the frame rate is much lower than you might expect. For such a simple example you could reasonably expect to hit the maximum rate of the display, e.g., 60fps or better.

Later you'll use the Profiler to investigate but, before that, you'll deploy to Android to check if the behavior is the same.
