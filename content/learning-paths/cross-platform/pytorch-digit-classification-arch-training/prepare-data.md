---
# User change
title: "Prepare the Test Data"

weight: 9

layout: "learningpathall"
---

In this section, you will add the pre-trained model and copy the bitmap image data to the Android project.

## Model

To add the model, create a folder named `assets` in the `app/src/main` folder. 

Copy the pre-trained model, named `model.pth`, to the `assets` folder.  

The model is also available in the [GitHub repository](https://github.com/dawidborycki/Arm.PyTorch.MNIST.Inference.git) if you require it.

## Image data

The data preparation script is shown below: 

```Python
from torchvision import datasets, transforms
from PIL import Image
import os

# Constants
NUM_DIGITS = 10  # Number of unique digits in MNIST (0-9)
EXAMPLES_PER_DIGIT = 2  # Number of examples per digit

# Define the transformation to convert the image to a tensor
transform = transforms.Compose([transforms.ToTensor()])

# Load the MNIST test dataset
test_data = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=transform
)

# Create a directory to save the bitmaps
os.makedirs("mnist_bitmaps", exist_ok=True)

# Dictionary to keep track of collected examples per digit
collected_examples = {digit: 0 for digit in range(NUM_DIGITS)}

# Loop through the dataset and collect the required number of images
for i, (image, label) in enumerate(test_data):
    if collected_examples[label] < EXAMPLES_PER_DIGIT:
        # Convert tensor to PIL image
        pil_image = transforms.ToPILImage()(image)
        # Create the filename with zero-padding
        filename = f"mnist_bitmaps/{label:02d}_{collected_examples[label]:02d}.png"
        # Save the image as PNG
        pil_image.save(filename)
        print(f"Saved: {filename}")

        # Update the count for the current label
        collected_examples[label] += 1

    # Break the loop if all required examples are collected
    if all(count == EXAMPLES_PER_DIGIT for count in collected_examples.values()):
        break
```

This code processes the MNIST test dataset to generate and save bitmap images for digit classification. 

It defines constants for the number of unique digits (0-9) and the number of examples to collect per digit. The dataset is loaded using `torchvision.datasets` with a transformation to convert images to tensors. 

A directory named `mnist_bitmaps` is created to store the images. A dictionary tracks the number of collected examples for each digit. The code iterates through the dataset, converting each image tensor back to a PIL image, and saves two examples of each digit in the format `digit_index_example_index.png`. 

The loop breaks once the specified number of examples per digit is saved, ensuring that exactly 20 images, two per digit, are generated and stored in the specified directory.

{{% notice Note %}}
This data is included in the [GitHub repository](https://github.com/dawidborycki/Arm.PyTorch.MNIST.Inference.git)
{{% /notice %}}

Copy the `mnist_bitmaps` folder to the `assets` folder.

Once you have the `model.pth` and the `mnist_bitmaps` folder in the `assets` folder, continue to the next step to run the Android application. 
