---
title: Preparation
weight: 4

layout: learningpathall
---

## Create a blank project
You'll need Unity installed with Android build support. Read [Get started with Unity on Android](/learning-paths/mobile-graphics-and-gaming/get-started-with-unity-on-android) for help installing Unity, as well as building and deploying to an Android device.

Although the sample application is itself a project, you will still need to create a blank project to import it into.

1. Open the Unity Hub

2. Log in (if you are not already)

3. Select _New Project_

4. Select the _3D (URP) Core_ template 
 
   ![Display URP Template#center](images/urp.png "Figure 1. URP 3D template")
  
5. Enter a project name (this will be used as the name of the project folder)

6. Enter a location (the path of your project on disk)

7. Select _Create Project_

Note that [Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.0/manual/index.html) projects are recommended for mobile applications.

Unity will take a moment to create your new project and build the default assets.

## Download and install the sample application
Once Unity has loaded, you will be presented with a template project. You can ignore all of the assets provided by Unity; you only need to focus on the files from the sample project.

1. Open a web browser

2. Open the [sample project page](https://assetstore.unity.com/packages/essentials/tutorial-projects/optimizing-collisions-with-burst-and-neon-intrinsics-196303)

3. You will need to log in (if you haven’t already)

4. On the asset (Optimizing Collisions with Burst and Neon Intrinsics) page, select the _Add to my assets_ button

5. The button will change to _Open in Unity_. Select it.

6. A pop-up window will ask to open the asset in Unity. Select the _Open Unity Editor_ button.

7. If Unity fails to open the asset or no pop-up appears, select the _My Assets_ button in the top-right of the page:

    a. Your assets should appear in a list

    b. Find the entry for _Optimizing Collisions with Burst and Neon Intrinsics_

    c. Select the _Open in Unity_ button

    d. A pop-up will appear as in step 6 above
    
    e. Select _Open Unity Editor_

8. The Unity Editor will come to the foreground and display the _Package Manager_
 
   ![Open Project manager#center](images/pm.png "Figure 2. Package Manager with asset showing.")

9. You will see the sample project listed and highlighted. Select _Download_.

10. Select _Import_

11. A warning message will appear because the sample project will replace the project settings in your current project. Since this is a newly created project, it is fine to overwrite them. Select _Import_.

12. A further warning may appear because the sample project has additional dependencies that your blank project hasn’t activated yet. Select _Install/Upgrade_.

13. The Import Unity Package window will appear. It allows individual files and folders to be imported or ignored. You will need all of the files in the project. Leave all items ticked and select _Next_.

    ![Import sample project#center](images/import-window-step-1.png "Figure 3. Import the sample project using the Package Manager.")

14. A second window will open listing the project settings that will be overwritten. You want the settings from the sample project, so leave all items ticked and select _Import_.

    ![Overwrite project settings#center](images/import-window-step-2.png "Figure 4. Overwrite project settings with the settings from the imported sample project.")

## Set up the project
Once the sample project has been imported, you will see some errors and warnings.

1. Open the _File_ menu and select _Build Profiles_

2. Select _Android_ from the Platform list

3. Select _Switch Platform_, as you did in the [previous Learning Path](/learning-paths/mobile-graphics-and-gaming/get-started-with-unity-on-android/3-test-on-android/)

   ![Build-Profile-Menu#center](images/bp-menu.webp "Figure 5. Build Profile menu.")

Unity will take a moment to build the assets for the Android platform.

The errors will disappear, but some warnings regarding unreachable code may appear. These will be explained later and can be safely ignored for now.

Your Scene view should look something like this:

   ![Scene view#center](images/sample-project-default-scene-view.png "Figure 6. Default scene view of the sample project.")

If it does not, the next steps should help identify the issue.

## Run the project inside the editor
It is worth checking that everything has been imported and built correctly.

1. Close the _Build Profiles_ window

2. In the Project tab (usually at the bottom in the default layout), you will see the list of asset files.
 
   ![Scenes Folder#center](images/bad-load.png "Figure 7. Assets area")

3. Open the *BurstNeonCollisions* folder

4. Open the *Scenes* folder

5. Open the scene called _SampleScene_

6. Select the _Play_ (triangle) button to launch the program.

The game will launch, and you will see an empty environment begin to fill with more and more characters (capsules) over time. It will look something like this:

![Screenshot at runtime#center](images/game-view.png "Figure 8. Sample running in Game view.")

## Deploy to Android
You will now deploy the sample to your Android device. Your device must already be set up for development. For detailed instructions, read the learning path [Get started with Unity on Android](/learning-paths/mobile-graphics-and-gaming/get-started-with-unity-on-android).

1. Open _Build Profiles_ from the _File_ menu

2. Tick the _Development Build_ option
 
  ![Import sample project#center](images/bp-menu-build.webp "Figure 9. Development Build.")

3. Select _Add Open Scenes_ to add the demo scene to your _Scenes in Build_ list

4. Plug your Android device into your computer

5. Once recognized, your device will appear in the drop-down menu next to _Run Device_

6. The screenshot above shows the demo device selected as the _Run Device_. You will see your own device listed here

7. Select _Build and Run_

8. Enter a name for the APK (the Android package) and select _Save_

Unity will take a moment to build the Android version and then automatically deploy it to your connected Android device. Depending on your setup, the build and deployment process may take several minutes.

This is an example of what the scene could look like on your device:

![Running on Android#center](images/android-plain-mode.webp "Figure 10. Sample application running on Android.")
