---
title: Test TensorFlow baseline performance on Google Axion C4A Arm virtual machines
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Perform baseline testing

This section helps you verify that TensorFlow is properly installed and working on your Google Axion C4A VM. You'll run tests to confirm that your CPU can perform TensorFlow operations correctly.

### Check available devices

This command shows which hardware devices TensorFlow can use, such as CPU or GPU. On most VMs, you'll see only CPU listed:

```console
python -c "import tensorflow as tf; print(tf.config.list_physical_devices())"
```

The output is similar to:

```output
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
```

### Run a computation test

This test multiplies two large matrices to verify that TensorFlow computations work correctly on your CPU and measures execution time:

```console
python -c "import tensorflow as tf; import time; 
a = tf.random.uniform((1000,1000)); b = tf.random.uniform((1000,1000));
start = time.time(); c = tf.matmul(a,b); end = time.time(); 
print('Computation time:', end - start, 'seconds')"
```

This checks CPU performance for basic operations and provides a baseline measurement.

The output is similar to:

```output
Computation time: 0.008263111114501953 seconds
```

### Test neural network execution

Use a text editor to create a new file named `test_nn.py` for testing a simple neural network.

Add the following code to create and train a basic neural network using random data:

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
model.add(layers.Dense(64,activation="relu"))
model.add(layers.Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train for 1 epoch
model.fit(x, y, epochs=1, batch_size=32)
```

This script creates a simple neural network to verify that TensorFlow's deep learning functions work properly on the Arm platform.

### Run the neural network test

Execute the script:

```console
python test_nn.py
```

TensorFlow displays training progress similar to:

```output
32/32 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - loss: 0.1024
```

This confirms that TensorFlow is working correctly on your Arm VM and can perform both basic computations and neural network training.
