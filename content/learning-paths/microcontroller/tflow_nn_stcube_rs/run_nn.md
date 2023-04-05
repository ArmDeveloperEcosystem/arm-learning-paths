---
# User change
title: Run the model on development board

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this section, we will deploy the model directly on the STM32 board.

## Install STM32CubeMX and STM32Cube.AI

[STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html) is a graphical tool for configuring STM32 microcontrollers.\
[STM32Cube.AI](https://www.st.com/content/st_com/en/campaigns/stm32cube-ai.html) is an extension of STM32CubeMX to import ML models.

1. Download the Windows installer of STM32CubeMX from [here](https://www.st.com/en/development-tools/stm32cubemx.html)
2. Run the Windows installer and install in desired location of your Windows Machine.
3. Open STM32CubeMX IDE.
4. Click [Access to Board Selector]. Find your `B-L475E-IOT01A` board and click `Start Project`.
5. Go to `Project Manager`. Enter a project name and select the project location where the project will be saved.
6. Under `Pinout & Configuration`, expand `Pinout` menu, and click `Clear pinouts`.
7. Now we are going to install Cube AI and enable it for your project.
8. Expand `Software Packs` menu, and click `Select Components`.
9. Locate `X-CUBE-AI`, and click its `Install` button.
10. Expand the menu and enable `X-CUBE-AI` > `Core`. For device application, choose `Validation`. If the status shows a yellow warning, click `Resolve` to install any necessary dependencies.
12. Click `OK` when done.

## Validate the NN model

We will now validate the NN model we built in the previous section on the desktop and the development board.

### Validate on desktop

1. On the STM32CubeAI menu, locate `X-CUBE-AI` configuration from the list of `Categories`.
2. click `Add network`. Browse to the generated model (`.h5` file). You can also specify other values, such as validation input, and validation output. Leave as default for now.
3. Click `Analyze`, then it will generate a detailed report on the model. You can check the number of parameters, the size of the weights, and the amount of memory to be used.
4. Click `Show graph` to visualize your model.
5. Click `Validate on Desktop` to validate the model with the provided input and output on your desktop.

### Validate on development board

To validate the model on the target, we need to first generate code and install the code on the target.

6. Click `Validate on target`, and enable `Automatic compilation and download`. Select the appropriate toolchain (`STM32CubeIDE`), and click `OK`.


## Demonstrate example application
# RONAN TO DO
Stuck in `__io_putchar()`??


## Demo with the sample application

A sample application is provided, so you can test the application with your board.

1. Using a terminal application (such as `PuTTY`), set up the serial connection to the board. `COM` number will be as before. The speed is 115200.
2. Import our application. Click the File tab and click `Import`. Select `Existing project into workspace`. Go to `tf_stm32` folder and select `MCU_Activity_Recognition`.
3. Open `X-CUBE-AI/App/app_x-cube-ai.c`. We provide functions for data acquisition from the accelerometer sensor and feature extraction.
4. Build application and flash to target with `Run As`.
5. Obseve output on the terminal.
6. Press the blue button on the board, draw a letter, then press the button again.

## Create your own application
# RONAN TO DO
Flow slightly different with latest version of STM32CubeMX

1. Open the list of Software Packages. Change the device application as `Application`.
2. Click `Generate Code` again, then the project is updated.
3. Open `STM32CubeIDE`. Since we re-generated the code again, we need to delete the existing project and import the project again.
4. Open `X-CUBE-AI/App/app_x-cube-ai.c`. This is the auto-generated code by `STM32CubeMX`.
5. Between `USER_CODE_BEGIN` and `USER_CODE_END`, you can write code for your application.

There are two main functions that you should implement:
 * `acquire_and_process_data()` is for getting data from sensors and processing the data, for example, extracting features.
 * `postprocess()` is for postprocessing the output