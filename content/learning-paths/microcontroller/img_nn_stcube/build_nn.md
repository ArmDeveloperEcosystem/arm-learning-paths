---
# User change
title: "1. Build an image classification NN model trained with the CIFAR-10 dataset"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this learning path, we will build a convolution neural network model for image classification. We will train the model with CIFAR-10 dataset, one of the most popular image datasets, which contains 60,000 images with 10 different categories. The model takes an RGB image and predicts the category of the image.

## Get Setup

On your Windows 10 development machine,  start by downloading all the project files you'll need to run the example in this learning path.
The zipped contents are available [here](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/microcontroller/img_nn_stcube/Project_Files/img_class_stcube.zip)

Then install Anaconda. Anaconda is a distribution of Python language for data science and machine learning. With Anaconda, you can easily install open-source machine learning packages. Here are the steps to install Anaconda on your machine.

### Install Anaconda

1. Visit the official Anaconda webpage: www.anaconda.com
2. On products, click Anaconda Distribution menu.
3. You can download the Anaconda Installer by clicking this button.
4. Open the Anaconda installer and install using default options.
5. Now, the installation is finished.

### Use Anaconda

With Anaconda installed, you will now install the necessary conda packages for building and training the NN model including [Jupyter notebook](https://jupyter.org/). Follow the steps as shown below:

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
conda install jupyter pandas tensorflow matplotlib numpy 
```

### Data Pre-processing

To create the NN model, there are certain data pre-processing steps that need to be performed.

First, open the Jupyter Notebook through an Anaconda Prompt.

```console
jupyter notebook
```

Now, open lab.ipynb from the extracted project files folder on the notebook. Then, execute the first code block to import the required packages

```console
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D, 
BatchNormalization, Activation

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import random

from PIL import Image

import os
```

Next, load the CIFAR-10 dataset. We can easily get the dataset because TensorFlow provides API for downloading well-known datasets, such as CIFAR-10 and MNIST. Execute the next code block to get the 
dataset.

```console
# Load data from TF Keras
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# CIFAR10 class names
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 
'Horse', 'Ship', 'Truck']
num_classes = len(class_names)
```

Then, we will save one image per class from the test set for testing with the board later. Execute the following code block to save the images.

```console
path_images = "./Data/images/"

# Create directory
if not os.path.exists(path_images):
 os.mkdir(path_images)

# Save one image per class 
ext=".jpg"
for image_index in range(0,100):
 im = Image.fromarray(x_test[image_index])
 im.save("./images/"+str(class_names[int(y_test[image_index])])+ext)
```

This code block below will visualize the saved images.

```console
# Show saved images
files = os.listdir(path_images) 
for img in files:
 if os.path.splitext(img)[1] == ext and os.path.splitext(img)[0] in class_names:
 #print(os.path.splitext(img)[0])
 plt.subplot(2,5,class_names.index(os.path.splitext(img)[0])+1)
 plt.xticks([])
 plt.yticks([])
 plt.grid(False)
 plt.imshow(mpimg.imread(path_images+img),)
 plt.xlabel(os.path.splitext(img)[0])
plt.show()
```

The expected output is shown below

![output1](Images/lab4_1.PNG)

Next, we will normalize all the training and testing data to have values between 0 and 1. This normalization facilitates machine learning. Each RGB value ranges from 0 to 255, so we divide the training and testing data by 255.

```console
# Normalize pixel values to be between 0 and 1
x_train = x_train.astype(np.float32)/255
x_test = x_test.astype(np.float32)/255
# Convert class vectors to binary class matrices.
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)
# Print arrays shape
print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)
print('x_test shape:', x_test.shape)
print('y_test shape:', y_test.shape)
```

The expected output is shown below:

```console
x_train shape: (50000, 32, 32, 3)
y_train shape: (50000, 10)
x_test shape: (10000, 32, 32, 3)
y_test shape: (10000, 10)
```

### Create the Model

We are going to create a small convolutional neural network for image classification. The image size of CIFAR10 is 32 by 32, and the number of colour channels is 3. So, the input shape of the first convolution layer is (32, 32, 3). Since the number of classes is 10, so the last dense layer should have 10 units.

Here is an image illustrating the network architecture. Note that only convolution and dense layers are illustrated in this image.

![output2](Images/lab4_2.PNG)

Execute the code blocks below to create a sequential model and add the layers

```console
# Hyperparameters
batch_size = 32
num_classes = len(class_names)
epochs = 1
img_rows, img_cols = x_train.shape[1], x_train.shape[2]
input_shape = (x_train.shape[1], x_train.shape[2], 1)
```

```console
# Creating a Sequential Model and adding the layers
model = Sequential()
model.add(Conv2D(16, (3, 3), padding='same', input_shape=(32,32,3)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(16, (3, 3),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2),strides=(2, 2)))
model.add(Dropout(0.2))
model.add(Conv2D(32, (3, 3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2),strides=(2, 2)))
model.add(Dropout(0.3))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2),strides=(2, 2)))
model.add(Dropout(0.4))
model.add(Flatten())
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10)) #The number of classes we have
model.add(Activation('softmax'))
```

Execute the code blocks below to compile and train the model. If we use tens of epochs, the training could take more than 10 hours because the dataset has 50,000 training images. Therefore, the model trained for 50 epochs is provided for testing (File: ‘Data/models/cifar10_model.h5’). You can use the model if you don't have enough time to train your own model. 

```console
# Check model structure and the number of parameters
model.summary()
# Let's train the model using Adam optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam', 
metrics=['accuracy'])
# Train model
history = model.fit(x=x_train,
 y=y_train,
 batch_size=batch_size,
 epochs=epochs, 
 validation_data=(x_test, y_test))
```

Let's save the model and evaluate the model. Note that since we trained the model for 1 epoch only, the accuracy would not be that good. Please try a larger number of epochs later to obtain better performance.

```console
# Save keras model
path_models = "./Data/models/"
path_keras_model = path_models + "own_cifar10_model.h5"
# Create directory
if not os.path.exists(path_models):
 os.mkdir(path_models)
model.save(path_keras_model)
# Score trained model.
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
```

### Save Data for Testing

Finally, we are going to save the validation data and the labels for testing. This code block will sample 50 images from the dataset and save them in CSV format. Execute the code block to save the test data.

```console
path_csv = "./Data/"
path_csv_file = path_csv+"own_cifar10_validation_20image.csv"
# Create directory
if not os.path.exists(path_csv):
 os.mkdir(path_csv)
# Remove old csv file
if os.path.exists(path_csv_file):
 os.remove(path_csv_file)
# Load data from TF Keras
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
# CIFAR10 class names
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 
'Horse', 'Ship', 'Truck']
# Normalize pixel values to be between 0 and 1
x_train = x_train.astype(np.float32)/255
x_test = x_test.astype(np.float32)/255
# Print arrays shape
print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)
print('x_test shape:', x_test.shape)
print('y_test shape:', y_test.shape)
 
# Save csv file that contain pixel's value
num_sample = 50
rx = random.sample(range(0,len(x_test)),num_sample)
for i in range(0,num_sample):
 data = x_test[rx[i]]
 #print(data.shape)
data = data.flatten()
 output = y_test[rx[i]]
 data=np.append(data,output)
 data = np.reshape(data, (1,data.shape[0]))
 #print(data.shape)
 with open(path_csv_file, 'ab') as f:
 np.savetxt(f, data, delimiter=",")
```

This code block will save the list of image classes. Execute the code block to save the label file.

```console
path_labels = "./Data/labels/”
path_labels_file = path_labels+"own_cifar10_labels.txt"
# Create directory
if not os.path.exists(path_labels):
 os.mkdir(path_labels)
 
# Remove old label file
if os.path.exists(path_labels_file):
 os.remove(path_labels_file)
# Create label file
for i in range(0,len(class_names)):
 with open(path_labels_file, 'a') as f:
 f.write(str(i)+","+class_names[i]+"\n")
```

We have now completed the steps to create the model and are ready to deploy it on the ST board.

