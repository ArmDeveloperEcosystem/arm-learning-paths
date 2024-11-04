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

Select `Next` to continue. 

Finish the new project creation by accepting all defaults until the project is created. 

## About the Game Activity

GameActivity is a Jetpack library designed to assist Android games in processing app cycle commands, input events, and text input in the application's C/C++ code. 

GameActivity is a direct descendant of NativeActivity and shares a similar architecture:

![Game Activity Architecture #center](./images/GameActivityArchitecture.png "Game Activity Architecture")

With GameActivity, you can focus on your core game development and avoid spending excessive time dealing with the Java Native Interface (JNI) code.

GameActivity performs the following functions:

* Interacts with the Android framework through the Java-side component.
* Passes app cycle commands, input events, and input text to the native side.
* Renders into a SurfaceView, making it easier for games to interact with other UI components.

{{% notice Tip %}}
You can find more information about Android Game Activity and its capabilities in the [Game Activity documentation](https://developer.android.com/games/agdk/game-activity).
{{% /notice %}}

## Upgrade the application to include Dawn

The Android Game Activity framework uses OpenGLES3 for graphics. 

You can remove this dependency and replace it with WebGPU. 

Start by including the [webgpu.hpp](https://github.com/varunchariArm/Android_DawnWebGPU/blob/main/app/src/main/cpp/webgpu/include/webgpu/webgpu.hpp) header file in the project:

1. In Android Studio, navigate to the project view and find the `app` --> `cpp` folder.

Open terminal in Android Studio. You should be in the MyApplication directory.

2. Create a new directory and download the WebGPU header file from GitHub

Run the commands below to download the `webgpu.hpp` header file:

```console
mkdir -p app/src/main/cpp/webgpu/include/webgpu
cd app/src/main/cpp/webgpu/include/webgpu
wget https://raw.githubusercontent.com/varunchariArm/Android_DawnWebGPU/refs/heads/main/app/src/main/cpp/webgpu/include/webgpu/webgpu.hpp
cd ../..
```

3. Next copy the remaining files in the [webgpu](https://github.com/varunchariArm/Android_DawnWebGPU/tree/main/app/src/main/cpp/webgpu) directory to corresponding directory in your project.

```console
wget https://raw.githubusercontent.com/varunchariArm/Android_DawnWebGPU/refs/heads/main/app/src/main/cpp/webgpu/CMakeLists.txt
wget https://raw.githubusercontent.com/varunchariArm/Android_DawnWebGPU/refs/heads/main/app/src/main/cpp/webgpu/FetchDawn.cmake
wget https://raw.githubusercontent.com/varunchariArm/Android_DawnWebGPU/refs/heads/main/app/src/main/cpp/webgpu/fetch_dawn_dependencies.py
wget https://raw.githubusercontent.com/varunchariArm/Android_DawnWebGPU/refs/heads/main/app/src/main/cpp/webgpu/webgpu.cmake
```

Notice the [FetchDawn.cmake](https://github.com/varunchariArm/Android_DawnWebGPU/blob/main/app/src/main/cpp/webgpu/FetchDawn.cmake) uses a stable `chromium/6536` branch of Dawn repository. 

{{% notice Note %}}
WebGPU is constantly evolving standard and hence its implementation, Dawn is also under active development. For sake of stability, we have chosen a stable branch for our development. Updating to latest or different branch may cause breakage.
{{% /notice %}}

To add Dawn to our application, we have 2 options:

* Create a shared/static library from the Dawn source and use it in application.
* Download the source as a dependency and build it as part of the project build

We are choosing the second option, since it provides more debug flexibility.

The [webgpu/webgpu.cmake](https://github.com/varunchariArm/Android_DawnWebGPU/blob/main/app/src/main/cpp/webgpu/webgpu.cmake) and [CMakeLists.txt](https://github.com/varunchariArm/Android_DawnWebGPU/blob/main/app/src/main/cpp/CMakeLists.txt) file facilitates downloading and building WebGPU with Dawn implementation and integrating Dawn into our main project

Run the build:

```console
cmake .
make -C _deps/dawn-build
```

This section doesn't seen needed, just information:

```bash
#Set Dawn build options
option(DAWN_FETCH_DEPENDENCIES "" ON)
option(DAWN_USE_GLFW "" ON)
option(DAWN_SUPPORTS_GLFW_FOR_WINDOWING "" OFF)
option(DAWN_USE_X11 "" OFF)
option(ENABLE_PCH "" OFF)
```

4. Add WebGPU to the project.

Edit the file `CMakeLists.txt` to remove the WebGL and add `webgpu` libraries. 

``` bash
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

The project is now ready to build. 

The `webgpu.hpp` header file acts like an interface, exposing all WebGPU functions and variables to the main Application.
