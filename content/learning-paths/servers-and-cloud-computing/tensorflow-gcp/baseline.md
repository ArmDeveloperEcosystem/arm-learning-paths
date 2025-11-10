---
title: TensorFlow Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## TensorFlow Baseline Testing on GCP SUSE VMs
This section helps you check if TensorFlow is properly installed and working on your **Google Axion C4A Arm64 VM**. You will run small tests to confirm that your CPU can perform TensorFlow operations correctly.


### Verify Installation
This command checks if TensorFlow is installed correctly and prints its version number.

```console
python -c "import tensorflow as tf; print(tf.__version__)"
```
### List Available Devices
This command shows which hardware devices TensorFlow can use — like CPU or GPU. On most VMs, you’ll see only CPU listed.

```console
python -c "import tensorflow as tf; print(tf.config.list_physical_devices())"
```

You should see an output similar to:
```output
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
```

### Run a Simple Computation
This test multiplies two large matrices to check that TensorFlow computations work correctly on your CPU and measures how long it takes.

```python
python -c "import tensorflow as tf; import time; 
a = tf.random.uniform((1000,1000)); b = tf.random.uniform((1000,1000));
start = time.time(); c = tf.matmul(a,b); end = time.time(); 
print('Computation time:', end - start, 'seconds')"
```
- This checks **CPU speed** and the correctness of basic operations.
- Note the **computation time** as your baseline.

You should see an output similar to:
```output
Computation time: 0.008263111114501953 seconds
```
### Test Neural Network Execution
Create a new file for testing a simple neural network:

```console
vi test_nn.py
```
This opens a new Python file where you’ll write a short TensorFlow test program.
Paste the code below into the `test_nn.py` file:

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Dummy data
x = np.random.rand(1000, 20)
y = np.random.rand(1000, 1)

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train for 1 epoch
model.fit(x, y, epochs=1, batch_size=32)
```
This script creates and trains a simple neural network using random data — just to make sure TensorFlow’s deep learning functions work properly.

**Run the Script**

Execute the script with Python:

```console
python test_nn.py
```

**Output**

TensorFlow will print training progress, like:
```output
32/32 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - loss: 0.1024
```

This confirms that TensorFlow is working properly on your Arm64 VM.
