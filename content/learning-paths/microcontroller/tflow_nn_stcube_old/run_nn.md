---
# User change
title: "2. Run the letter recognition NN model on STM32 B-L475E-IOT01A2 board"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this section, you will deploy the model on the ST board using STM Cube AI and STM Cube IDE. STM Cube AI is an extension software of STM Cube MX. So you will need to install both STM Cube MX and the extension software, STM Cube AI.

## Install STM Cube MX and ST CUbe AI

1. Download the Windows installer of STM32 Cube MX from [here](https://www.st.com/en/development-tools/stm32cubemx.html)
2. Run the Windows installer and install in desired location of your Windows Machine.
3. Open STM Cube MX.
4. Click [Access to Board Selector]. Find your board and click [Start Project].
5. First you need to configure the project. Go to [Project Manager]. Write the project name and select the project location where the project will be saved.
6. This figure shows the configuration of pinouts. On [Pinout] menu, click [Clear pinouts].
7. Now install Cube AI and enable it for your project.
8. On [Software Packs] menu, click [Select Components].
9. Click [Install] button. Expand the menu and enable Cube AI. For device application, choose [Validation].
10. You can see that Cube AI is now enabled.

## Validate the NN model

You will now validate the NN model built in the previous section on the ST board.

Follow the steps shown below:

1. On the ST Cube AI menu, click [Add network]. Here, you can load your model, validation input, and validation output.
2. Click [Analyze], then it will generate a detailed report on the model. You can check the number of parameters, the size of the weights, and the amount of memory to be used.
3. Click [Show graph], then it visualizes your model.
4. Click [Validate on Desktop], then it validates the model with the provided input and output on your desktop.
5. To validate the model on the target, you need to first generate code and install the code on the target.
6. Click [Generate Code], then it automatically generates the code for validating the model on the board.
7. Open STM Cube IDE. On this menu, choose [STM32 Project from an Existing STM32CubeMX Configuration File]. Then navigate to the project folder and select the ioc file. Install the code with [Run As]. Now it is installing the Cube AI application to the board.
8. Go back to STM Cube MX and press [Validate on target].

## Generate Cube AI Application

Now the model is validated, implement an application with the model.

1. Open the list of Software Packages. Change the device application as [Application].
2. Click [Generate Code] again, then the project is updated.
3. Open STM Cube IDE. Since you re-generated the code again, you need to delete the existing project and import the project again.
4. Open X-CUBE-AI/App/app_x-cube-ai.c. This is the auto-generated code by STM Cube MX.
5. Between USER_CODE_BEGIN and USER_CODE_END, you can write code for your application.
6. There are two main functions that you should fill. The first function is [acquire_and_process_data]. This function is for getting data from sensors and processing the data, for example, extracting features. The second function is [postprocess] for postprocessing the output.

## Demo with the sample application

1. For demonstrations, a sample application was provided so that you can test the application with your board.
2. Open any terminal application to see the output from the board. I will use [Tera Term] in this lab. Set up the serial connection. The speed is 115200.
3. Import the application. Click the File tab and click [Import]. Select [Existing project into workspace]. Go to [tf_stm32] and select [MCU_Activity_Recognition].
4. Open X-CUBE-AI/App/app_x-cube-ai.c. Note the supplied functions for data acquisition from the accelerometer sensor and feature extraction. Install the code with [Run As].
5. Now you can see the output on the terminal.
6. Press the blue button on the board, draw a letter, then press the button again.

