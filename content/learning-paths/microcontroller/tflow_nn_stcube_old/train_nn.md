---
# User change
title: "1. Build the letter recognition NN model using Tensorflow"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this learning path, we will build a neural network model with TensorFlow and deploy the model on the [STM32 B-L475E-IOT01A2 board](https://www.st.com/en/evaluation-tools/b-l475e-iot01a.html). This board has an MCU based on the Arm Cortex-M4 core. We will implement a letter recognition model which takes accelerometer data from the board and predicts the letter based on the accelerometer data. 

## Get Setup

On your Windows 10 development machine, start by downloading all the project files you'll need to run the example in this learning path.
The zipped contents are available [here](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/microcontroller/tflow_nn_stcube/Project_Files/tf_stm32.zip)

start by installing Anaconda. Anaconda is a distribution of Python language for data science and machine learning. With Anaconda, you can easily install open-source machine learning packages. Here are the steps to install Anaconda on your machine.


### Install Anaconda

1. Visit the official Anaconda webpage: www.anaconda.com
2. On products, click Anaconda Distribution menu.
3. You can download the Anaconda Installer by clicking this button.
4. Open the Anaconda installer and install using default options.
5. Now, the installation is finished.

### Use Anaconda

With Anaconda installed, you will now install the necessary conda packages for data collection and machine learning including [Jupyter notebook](https://jupyter.org/). Follow the steps as shown below:

1. First open Anaconda Prompt
2. Create an environment by typing:
```console
conda create -n ml_lab python=3.8
```
3. Activate your environment by typing:
```console
conda activate ml_lab
```
4. Add conda-forge channel to install packages:
```console
conda config --add channels conda-forge
```
5. Then install python packages:
```console
conda install jupyter pandas pyserial scikit-learn tensorflow matplotlib
```

### Prepare the data collection

Next, you need to program the STM32 B-L475E-IOT01A2 board to acquire accelerometer data for your neural network model. We have already implemented the data collection code for this learning path, so you can just import the code and program the board using STM Code IDE.

To do so, you need to download STM32 Cube IDE on your Windows machine. 

### Install STM32 Cube IDE

Download the software from the official [STMicroelectronics website](https://www.st.com/en/development-tools/stm32cubeide.html). Choose the Windows installer to download from the Get Software section of the page.

### Program the board 

Now with STM32 Cube IDE installed, follow the steps below:

1. Click [Import project] and select the MCU Dataset Creation folder inside the tf_stm32 folder.
2. Plug the board into your computer with a USB cable. You may need to reset your board before you program the board. Click the black button on the board for the reset.
3. Right click the project and select [Run As]. Then it compiles and installs the code into your board.
4. Now your board is ready to collect the sensor data.

### Open Jupyter Notebook

In the same environment you activated using Anaconda earlier, run the steps shown to open your jupyter noteboook

1. Navigate to the folder where lab.ipynb is located:
```console
cd Documents/lab
```
2. Open Jupyter notebook by typing:
```console
jupyter notebook lab.ipynb
```

## Train the neural network model

You are now ready to train your first neural network model with TensorFlow and deploy the inference with STM Cube AI. 

First, import necessary packages by executing the first code block.

```console
import serial.tools.list_ports
import sklearn
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, random

base_dir = os.getcwd()
samples_dir = os.path.join(base_dir, 'Samples')
```

### Connect the board

Next we are going to connect the board for data collection. Make sure that you plugged the board into your computer via the USB ST-LINK port, not the USB OTG port. Execute this code block and check which port the board is connected to. In our case the board is connected to COM3 port. Enter the port number.

```console
print('Com ports list:')
comPorts = list(serial.tools.list_ports.comports())
for comPort in comPorts:
    print(comPort)
chooseComPort = input('Please insert port number: ')
ser = serial.Serial('COM{}'.format(chooseComPort), 115200)
```

Now we have the serial connection with the board. This code block contains several helper functions for computation. Execute the code block to have these functions.

```console
def convert_to_list(value):
    value = value.replace("b' ", "")
    vals = value.split(", ")
    del vals[-1]
    results = list(map(int, vals))
    return results

def convert_list_to_df(lst):
    x = lst[0::3]
    y = lst[1::3]
    z = lst[2::3]
    df = pd.DataFrame({'X': x, 'Y': y, 'Z': z})
    return df
```

### Acquire the dataset

Now we are ready to acquire the dataset. Execute the code block shown below. This code block will acquire sensor data from the board and save training samples for machine learning. 

```console
letter = input('Please insert letter to collect data: ')
stride = 30
f = os.path.join(samples_dir, 'letter_{}_stride_{}.csv'.format(letter, stride))
if os.path.exists(f):
    print('File exists and data will be appended...')
    xyz_df = pd.read_csv(f)
else:
    print('New sample, starting blank...')
    xyz_df = pd.DataFrame(columns=['X', 'Y', 'Z'])

while input('1 - acquire sample, 2 - exit: ') == '1':
    line = ser.readline()
    lineList = convert_to_list(str(line))
    new_df = convert_list_to_df(lineList)
    print('New data acquired:\n', new_df.describe())
    xyz_df = pd.concat([xyz_df, new_df], ignore_index=True)
    print('Total Data count:', int(xyz_df.shape[0]/stride))

print('Saving data to:', f)
print('Total data of sample {}:\n'.format(letter), xyz_df.describe())
xyz_df.to_csv(f, index=False)
```

1. Enter a lower case letter which you want to collect samples for. This is going to be the label of the samples.
2. Then draw the letter with the board and press the blue button on the board.
3. Enter 1 in the box to save the accelerometer data.
4. You may repeat this process until you get enough samples. The more data samples you collect, the better model you will probably get.
5. Enter 2 when you want to finish the acquisition.
6. You can execute this code block again for other letters. So try collecting the accelerometer data for other letters such as A and U. 

### Load the dataset

Let's check the dataset you collected. Execute this code block to load the dataset. In my dataset, We used the letter o and letter s. The label for letter o is 0 and the label for letter s is 1. 

```console
data_files = [file for file in os.listdir(samples_dir) if '.csv' in file]

stride = 30
data = []
labels = []
for idx, file in enumerate(data_files):
    df = pd.read_csv(os.path.join(samples_dir, file))
    x = df['X'].to_numpy()
    y = df['Y'].to_numpy()
    z = df['Z'].to_numpy()
    
    for i in range(int(df.shape[0]/stride)):
        base_idx = i * stride
        batch = np.array([x[base_idx:base_idx+stride], y[base_idx:base_idx+stride], z[base_idx:base_idx+stride]])
        batch = batch.reshape((3, stride))
        data.append(batch)
        labels.append(idx)
        
    print('Added {} data to the data list with label: {}'.format(file, idx))
```

This code block will show one training sample. This is the accelerometer data of one training sample.

```console
def plot_single_sample(data_sample, label='Not Specified'):
    plt.clf()
    scaling = 2**10 # The STM ADC is 10bit so scale to get [g]
    fig, axs = plt.subplots(3)
    t = np.linspace(0, data_sample.shape[1] * 100, data_sample.shape[1])
    # Accelerometer sampled with 100 ms
    axs[0].set_title(label='Single Data Sample of Label {}'.format(label))
    axs[0].plot(t, data_sample[0]/scaling, c='m')
    axs[0].set_ylabel('X [g]')
    plt.setp(axs[0].get_xticklabels(), visible=False)
    axs[1].plot(t, data_sample[1]/scaling, c='m')
    axs[1].set_ylabel('Y [g]')
    plt.setp(axs[1].get_xticklabels(), visible=False)
    axs[2].plot(t, data_sample[2]/scaling, c='m')
    axs[2].set_ylabel('Z [g]')
    plt.xlabel('Time [ms]')
    plt.show()
    
idx = random.randint(0, len(data)-1)
plot_single_sample(data_sample=data[idx], label=labels[idx])
```

Expected output is shown below:

![output1](Images/output1.PNG)

### Create a model

Now we are going to train a multi-layer perceptron model with the dataset.  First, we define a multi-layer perceptron model with 3 dense layers.

```console
x_train, y_train = sklearn.utils.shuffle(np.array(data), np.array(labels))
y_train = tf.keras.utils.to_categorical(y_train, len(np.unique(y_train)))

model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=(3, stride)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(30, activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(20, activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(len(np.unique(y_train)), activation="softmax")
        ]
    )

model.summary()
```

Compile the model. Then you can see the model has 3392 parameters in total. We train the model for 200 epochs. We will explain why we chose 200 for the number of epochs after the training is finished. 

```console
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(x_train, y_train, batch_size=1, epochs=200, validation_split=0.4)

model.save('raw_model.h5')
```

Now, let us plot the training and validation accuracy over epoch. You can see that the training and validation accuracy start to converge after around 150 epochs. This means that the 200 epochs are enough to train the model. If we train the model for too many epochs, then the validation accuracy may drop due to overfitting.

![output2](Images/output2.PNG)

### Learning Rate

For training the model,  we used the default learning rate. But how will the model change with different learning rates? If the learning rate is too high, the model is more likely to overshoot the minima, meaning that the model cannot converge to the minima. On the other hand, if the learning rate is too low, the model reaches the minima too slowly, requiring more training time.

Let's first try a high learning rate. Here, I set the learning rate of the optimizer as 1000. Execute the code block. This graph shows the training and validation loss values over epoch. You can see that the loss values fluctuate a lot so the model has difficulty in reaching the minima.

```console
# High learning rate (lr = 1000)
model_hlr = tf.keras.models.clone_model(model)

optimizer = tf.optimizers.Adam(learning_rate = 1000)
model_hlr.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history = model_hlr.fit(x_train, y_train, batch_size=32, epochs=100, validation_split=0.4)

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0, 1000])
plt.legend(loc='lower right')
```

Expected output shown below:

![output3](Images/output3.PNG)

Now let's try a lower learning rate, which is 0.0001. Execute the code block. The graph shows the training and validation loss values decrease much more slowly. So, it is important to use a proper learning rate in training.

```console
# Low learning rate (lr = 0.0001)
model_llr = tf.keras.models.clone_model(model)

optimizer = tf.optimizers.Adam(learning_rate = 0.0001)
model_llr.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history = model_llr.fit(x_train, y_train, batch_size=32, epochs=100, validation_split=0.4)

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0, 1000])
plt.legend(loc='lower right')
```

Expected output shown below:

![output4](Images/output4.PNG)

With the model trained, we are now ready to test it.

## Test the model

To test the model we trained, run the code block shown below. 

```console
input('Press Enter once MCU is ready')
line = ser.readline()
lineList = convert_to_list(str(line))
new_df = convert_list_to_df(lineList)
print('New data acquired:\n', new_df.describe())

x = new_df['X'].to_numpy()
y = new_df['Y'].to_numpy()
z = new_df['Z'].to_numpy()

inf_data = np.array([x, y, z])
plot_single_sample(data_sample=inf_data.reshape((3, stride)))

# For inference we have to explicitly tell that the data has a batch size of 1
inf_data = inf_data.reshape((1, 3, stride))

pred = model.predict(inf_data)
print('Model Prediction: ', np.argmax(pred))
```

1. Press enter when you are ready to draw a letter.
2. Draw a letter and press the blue button on the board.
3. Check whether the prediction is correct or not.

## Extract features

Until now, we trained and tested the model with the raw accelerometer data. Now, we are going to extract features from the data and train a model which makes prediction based on the extracted features. Here, we are going to use the mean and standard deviation of each axis as features.

First, we extract the features from the collected dataset and save the features for training. You can check the extracted features with this code block. These are the extracted features from one data sample.

```console
data_files = [file for file in os.listdir(samples_dir) if '.csv' in file]

stride = 30
slidingWindowExt = 6
feature_data = []
feature_labels = []
for idx, file in enumerate(data_files):
    df = pd.read_csv(os.path.join(samples_dir, file))
    x = df['X'].to_numpy()
    y = df['Y'].to_numpy()
    z = df['Z'].to_numpy()
    
    for i in range(int(df.shape[0]/stride)):
	base_idx = i * stride

        # Mean feature
        x_mean_ext = np.array([np.mean(x[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        y_mean_ext = np.array([np.mean(y[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        z_mean_ext = np.array([np.mean(z[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        # STD feature
        x_std_ext = np.array([np.std(x[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        y_std_ext = np.array([np.std(y[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        z_std_ext = np.array([np.std(z[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        
        batch = np.array([x_mean_ext, y_mean_ext, z_mean_ext, x_std_ext, y_std_ext, z_std_ext])
        feature_data.append(batch)
        feature_labels.append(idx)
        
    print('Added {} data to the feature data list with label: {}'.format(file, idx))
```

Expected output shown below:

![output5](Images/output5.PNG)

Then, we create a new multi-layer perceptron model for the features. The new model has 1592 parameters because it uses a smaller input than the previous model. Train the model and check the accuracy. 

```console
x_train, y_train = sklearn.utils.shuffle(np.array(feature_data), np.array(feature_labels))
y_train = tf.keras.utils.to_categorical(y_train, len(np.unique(y_train)))

data_shape = x_train[0].shape
model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=data_shape),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(data_shape[0] * data_shape[1], activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(20, activation="relu"),
            tf.keras.layers.Dense(len(np.unique(y_train)), activation="softmax")
        ]
    )

model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=500, validation_split=0.4)
```

You can see the accuracy improved with the feature extraction. You can test the new model with this code block to check if the model generates better results. 

```console
input('Press Enter once MCU is ready')
line = ser.readline()
lineList = convert_to_list(str(line))
new_df = convert_list_to_df(lineList)
print('New data acquired:\n', new_df.describe())

x = new_df['X'].to_numpy()
y = new_df['Y'].to_numpy()
z = new_df['Z'].to_numpy()

# Mean feature
x_mean_ext = np.array([np.mean(x[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
y_mean_ext = np.array([np.mean(y[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
z_mean_ext = np.array([np.mean(z[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
# STD feature
x_std_ext = np.array([np.std(x[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
y_std_ext = np.array([np.std(y[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
z_std_ext = np.array([np.std(z[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])

inf_data = np.array([x_mean_ext, y_mean_ext, z_mean_ext, x_std_ext, y_std_ext, z_std_ext])
# For inference we have to explicitly tell that the data has a batch size of 1
plot_single_feature_sample(data_sample=inf_data)
inf_data = inf_data.reshape((1, data_shape[0], data_shape[1]))

pred = model.predict(inf_data)
print('Model Prediction: ', np.argmax(pred))
```

Finally, save the model by executing this code block.

```console
with open('test.npy', 'wb') as f:
    np.save(f, x_train)

with open('test_out.npy', 'wb') as f:
    np.save(f, y_train)
    
model.save('feature_mlp.h5')
```

