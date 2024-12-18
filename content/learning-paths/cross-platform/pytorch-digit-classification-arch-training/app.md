---
# User change
title: "Run the Application"

weight: 10

layout: "learningpathall"
---

You are now ready to run the Android application. You can use an emulator or a physical device. 

The screenshots below show an emulator. 

To run the app in Android Studio using an emulator, follow these steps:

1. Configure the Emulator:
* Go to Tools > Device Manager (or click the Device Manager icon on the toolbar).
* Click Create Device to set up a new virtual device (if you haven’t done so already).
* Choose a device model, such as Pixel 4, and click Next.
* Select a system image, such as Android 11, API level 30, and click Next.
* Review the settings and click Finish to create the emulator.

2. Run the App:
* Make sure the emulator is selected in the device dropdown menu in the toolbar (next to the “Run” button).
* Click the Run button (a green triangle). Android Studio will build the app, install it on the emulator, and launch it.

3. View the App on the Emulator: Once the app is installed, it will automatically open on the emulator screen, allowing you to interact with it as if it were running on a real device.

Once the application is started, click the Load Image button. It will load a randomly selected image. Then, click Run Inference to recognize the digit. The application will display the predicted label and the inference time as shown below:

![img](Figures/05.png)

![img](Figures/06.png)

In the next step you will learn how to further optimize the model.
