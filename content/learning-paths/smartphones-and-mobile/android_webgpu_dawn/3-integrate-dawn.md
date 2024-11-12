---
title: Create an application which includes Dawn
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up Android Project

You can start by creating a new Android Studio project.

Open Android studio, click `New Project` and select `Game Activity (C++)` as shown below:

![New Game Activity #center](./images/android_studio_new_game_activity.png "New C++ Game Activity")

Set the `Name` to be `dawnwebgpu`. 

Select `Next` to continue. 

Finish the new project creation by accepting all defaults until the project is created. 

The project is created in `~/AndroidStudioProjects`.

## About the Game Activity

GameActivity is a Jetpack library designed to assist Android games in processing app cycle commands, input events, and text input in the application's C/C++ code. 

GameActivity is a direct descendant of NativeActivity and shares a similar architecture:

![Game Activity Architecture #center](./images/GameActivityArchitecture.png "Game Activity Architecture")

With GameActivity, you can focus on your game development and avoid spending excessive time dealing with the Java Native Interface (JNI) code.

GameActivity performs the following functions:

* Interacts with the Android framework through the Java-side component.
* Passes app cycle commands, input events, and input text to the native side.
* Renders into a SurfaceView, making it easier for games to interact with other UI components.

{{% notice Tip %}}
You can find more information about Android Game Activity and its capabilities in the [Game Activity documentation](https://developer.android.com/games/agdk/game-activity).
{{% /notice %}}

## Download project source files

To create a WebGPU application, a number of files from GitHub are doing to be added to your Game Activity project. The objective is to show you how to take the Game Activity template and modify it to become a WebGPU application. 

To get started, open a terminal, create a new directory, and download the project files:

```bash
mkdir ~/webgpu-files ; cd ~/webgpu-files
wget https://github.com/varunchariArm/Android_DawnWebGPU/archive/refs/heads/main.zip
```

Unzip the project files:

```bash
unzip main.zip
```

Yow now have a directory named `Android_DawnWebGPU-main` in your `webgpu-files` directory. 

During the next sections you will copy some of the required files from the `Android_DawnWebGPU-main` directory to your Game Activity project to learn how to create WebGPU applications.

## Upgrade the application to include Dawn

Return to Android Studio and start work on the WebGPU application. 

The Android Game Activity framework uses OpenGLES3 for graphics. 

You can remove this dependency and replace it with WebGPU. 

Add WebGPU to the project using the following steps:

1. In Android Studio, navigate to the project view and find the `app` --> `cpp` folder.

Open terminal in Android Studio. You should be in the `dawnwebgpu` directory.

2. Create a new directory and download the WebGPU header file from GitHub

Run the commands below to download the `webgpu.hpp` header file:

```console
mkdir -p app/src/main/cpp/webgpu/include/webgpu
cd app/src/main/cpp/webgpu/include/webgpu
cp ~/webgpu-files/Android_DawnWebGPU-main/app/src/main/cpp/webgpu/include/webgpu/webgpu.hpp .
cd ../..
```

3. Next copy the remaining WebGPU files to your project. 

```console
cp ~/webgpu-files/Android_DawnWebGPU-main/app/src/main/cpp/webgpu/CMakeLists.txt .
cp ~/webgpu-files/Android_DawnWebGPU-main/app/src/main/cpp/webgpu/FetchDawn.cmake .
cp ~/webgpu-files/Android_DawnWebGPU-main/app/src/main/cpp/webgpu/fetch_dawn_dependencies.py .
cp ~/webgpu-files/Android_DawnWebGPU-main/app/src/main/cpp/webgpu/webgpu.cmake .
cd ..
```

Notice that `FetchDawn.cmake` uses a stable `chromium/6536` branch of Dawn repository. 

{{% notice Note %}}
WebGPU is constantly evolving standard and hence its implementation, Dawn is also under active development. For sake of stability, we have chosen a stable branch for our development. Updating to latest or different branch may cause breakage.
{{% /notice %}}

To add Dawn to our application, there are 2 options:

* Create a shared/static library from the Dawn source and use it in application.
* Download the source as a dependency and build it as part of the project build.

You will use the second option, since it provides more debug flexibility.

The files `webgpu/webgpu.cmake` and `CMakeLists.txt` facilitate downloading and building WebGPU with Dawn implementation and integrating Dawn into the project.

4. Add WebGPU to the project.

WebGPU is added to the project in the file `CMakeLists.txt`.

Copy the updated file by running the command:

```bash
cp ~/webgpu-files/Android_DawnWebGPU-main/app/src/main/cpp/CMakeLists.txt .
```

Review `CMakeLists.txt` and see that the `options`, `include`, and `add_subdirectory` are added from the original Game Activity file.

```output
#Set Dawn build options
option(DAWN_FETCH_DEPENDENCIES "" ON)
option(DAWN_USE_GLFW "" ON)
option(DAWN_SUPPORTS_GLFW_FOR_WINDOWING "" OFF)
option(DAWN_USE_X11 "" OFF)
option(ENABLE_PCH "" OFF)

include(utils.cmake)
add_subdirectory(webgpu)
```

Also look at the `CMakeLists.txt` file and see that the `target_link_libraries` is changed to remove the WebGL components and add the `webgpu` libraries. 

```output
# Configure libraries CMake uses to link your target library.
target_link_libraries(dawnwebgpu
        # The game activity
        game-activity::game-activity

        # webgpu dependency
        webgpu
        jnigraphics
        android
        log)
```


The `webgpu.hpp` header file acts like an interface, exposing all WebGPU functions and variables to the main Application.

Navigate to the next section to continue building the WebGPU application. 
