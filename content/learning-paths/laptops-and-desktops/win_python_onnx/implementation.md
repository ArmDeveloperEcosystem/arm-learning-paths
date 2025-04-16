---
# User change
title: "Using ONNX Runtime"

weight: 3

layout: "learningpathall"
---

## Objective
Next, you will implement Python code that accomplishes the following tasks:
* Downloads a pre-trained ONNX model specifically trained on the MNIST dataset, along with the MNIST dataset itself, which is widely used for benchmarking machine learning models.
* Executes predictions (inference) using the pre-trained ONNX model on test images containing handwritten digits from the MNIST dataset.
* Evaluates and measures the performance of the inference process, providing insights into the efficiency and speed of the neural network model on your specific system architecture.

This practical demonstration will illustrate the end-to-end workflow of deploying and evaluating ONNX-formatted machine learning models.

## Implementation

### Model
Create a file named main.py. At the beginning of this file, include the following import statements: 
 
```Python
import onnxruntime as ort
import numpy as np
import matplotlib.pyplot as plt
import wget, time, os, urllib
import torchvision
import torchvision.transforms as transforms
```

These statements import the necessary Python libraries:
* onnxruntime - enables running inference with ONNX models.
* numpy - facilitates numerical computations and handling of arrays.
* matplotlib - used for visualizing results such as classification outputs.
* wget, urllib, and os - provide utilities for downloading files and interacting with the file system.
* torchvision - allows easy access to datasets like MNIST.

Next, add the following function immediately below the import statements in your main.py file: 

```Python
def download_model(model_name):
    if not os.path.exists(model_name):
        base_url = 'https://github.com/dawidborycki/ONNX.WoA/raw/refs/heads/main/models/'
        url = urllib.parse.urljoin(base_url, model_name)
        wget.download(url)
```

This function, download_model, accepts one parameter, model_name. It first checks whether a file with this name already exists in your local directory. If the file does not exist, it downloads the specified ONNX model file from the given GitHub repository URL. This automated check ensures that you won't repeatedly download the model unnecessarily. 

### Inference
Next, you will implement a Python function to perform neural inference. Add the following code to your main.py file below the previously defined download_model function:

```Python
def onnx_predict(onnx_session, input_name, output_name,  
    test_images, test_labels, image_index, show_results): 
  
    test_image = np.expand_dims(test_images[image_index], [0,1]) 
  
    onnx_pred = onnx_session.run([output_name], {input_name: test_image.astype('float32')}) 
  
    predicted_label = np.argmax(np.array(onnx_pred)) 
    actual_label = test_labels[image_index] 
  
    if show_results: 
        plt.figure() 
        plt.xticks([]) 
        plt.yticks([])  
        plt.imshow(test_images[image_index], cmap=plt.cm.binary) 
         
        plt.title('Actual: %s, predicted: %s'  
            % (actual_label, predicted_label), fontsize=22)
        plt.show() 
     
    return predicted_label, actual_label 
```

The onnx_predict function prepares a single test image from the dataset by reshaping it to match the input shape expected by the ONNX model, which is (1, 1, 28, 28). This reshaping is achieved using NumPy's expand_dims function. Next, the function performs inference using the ONNX runtime (onnx_session.run). The inference results are probabilities (scores) for each digit class, and the function uses np.argmax to select the digit class with the highest probability, returning it as the predicted label. Optionally, the function visually displays the image along with its actual and predicted labels.

### Performance measurements
Next, add the following performance-measuring function below onnx_predict in your main.py file:

```Python
def measure_performance(onnx_session, input_name, output_name,  
    test_images, test_labels, execution_count): 
  
    start = time.time()     
  
    image_indices = np.random.randint(0, test_images.shape[0] - 1, execution_count) 
     
    for i in range(1, execution_count): 
        onnx_predict(onnx_session, input_name, output_name,  
            test_images, test_labels, image_indices[i], False) 
     
    computation_time = time.time() - start 
     
    print('Computation time: %.3f ms' % (computation_time*1000)) 
```

This measure_performance function assesses the inference speed by repeatedly invoking the onnx_predict function. It measures the total computation time (in milliseconds) required for the specified number of inference executions (execution_count) and outputs this measurement to the console.

### Putting Everything Together
Finally, integrate all previously defined functions by adding these statements at the bottom of your main.py file:
```Python
if __name__ == "__main__":
    # Download and prepare the model
    model_name = 'mnist-12.onnx'
    download_model(model_name)

    # Set up ONNX inference session
    onnx_session = ort.InferenceSession(model_name)

    input_name = onnx_session.get_inputs()[0].name
    output_name = onnx_session.get_outputs()[0].name

    # Load the MNIST dataset using torchvision
    transform = transforms.Compose([transforms.ToTensor()])
    mnist_dataset = torchvision.datasets.MNIST(root='./data', train=False,
                                               download=True, transform=transform)

    test_images = mnist_dataset.data.numpy()
    test_labels = mnist_dataset.targets.numpy()

    # Normalize images
    test_images = test_images / 255.0

    # Perform a single prediction and display the result
    image_index = np.random.randint(0, test_images.shape[0] - 1)
    onnx_predict(onnx_session, input_name, output_name,  
                 test_images, test_labels, image_index, True)

    # Measure inference performance
    measure_performance(onnx_session, input_name, output_name,  
                        test_images, test_labels, execution_count=1000)
```

This script first initializes an ONNX inference session with the downloaded model (mnist-12.onnx). It then retrieves the model's input and output details, loads the MNIST dataset for testing, runs a sample inference showing visual results, and finally measures the performance of the inference operation over multiple runs.

## Summary
In this section, you implemented Python code to download a pre-trained ONNX model and the MNIST dataset, perform inference to recognize handwritten digits, and measure inference performance. In the next step, you will install all required dependencies and run the code.