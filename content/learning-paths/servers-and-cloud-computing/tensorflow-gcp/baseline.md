---
title: Test TensorFlow baseline performance on Google Axion C4A 
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Perform baseline testing

This section helps you confirm that TensorFlow is installed and working correctly on your Google Axion C4A Arm virtual machine (VM). You'll run tests to check that your CPU can perform TensorFlow operations and basic neural network training.

## Check available devices

List the hardware devices TensorFlow can use, such as CPU or GPU. On most VMs, only the CPU is available:

```console
python -c "import tensorflow as tf; print(tf.config.list_physical_devices())"
```

The output is similar to:

```output
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
```

## Run a computation test

Multiply two large matrices to verify TensorFlow computations on your CPU and measure execution time:

```console
python -c "import tensorflow as tf; import time; \
a = tf.random.uniform((1000,1000)); b = tf.random.uniform((1000,1000)); \
start = time.time(); c = tf.matmul(a,b); end = time.time(); \
print('Computation time:', end - start, 'seconds')"
```

The output is similar to:

```output
Computation time: 0.008263111114501953 seconds
```

This provides a baseline measurement for CPU performance.

## Test neural network execution

Create a file named `test_nn.py` with the following code:

```python
import keras
from keras import layers
import numpy as np

# Dummy data
x = np.random.rand(1000, 20)
y = np.random.rand(1000, 1)

# Define the model
model = keras.Sequential()
model.add(keras.Input(shape=(20,)))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train for 1 epoch
model.fit(x, y, epochs=1, batch_size=32)
```

This script creates and trains a basic neural network using random data to verify that TensorFlow's deep learning functions work on the Arm platform.

## Run the neural network test

Execute the script:

```console
python test_nn.py
```

TensorFlow displays training progress similar to:

```output
32/32 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - loss: 0.1024
```

TensorFlow is working correctly on your Arm-based VM for both basic computations and neural network training. Your environment is ready for benchmarking.
