---
title: Load test sample
weight: 8
layout: learningpathall
---

## Overview

This section converts a handwritten digit image into a C header that the firmware can include at build time.

The MNIST model expects one grayscale 28 x 28 image. The script in this section resizes the image, converts it to grayscale, scales pixel values to the range 0 to 127, and writes the result to `input_mnist.h`.

## Set up Python image tools

Create a Python virtual environment for image preprocessing:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
cd ~/mnist_alif
python3 -m venv venv_image_prep
source venv_image_prep/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy pillow
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
cd ~\mnist_alif
py -m venv venv_image_prep
.\venv_image_prep\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy pillow
  {{< /tab >}}
{{< /tabpane >}}

## Save your image

Create a directory for the input image and preprocessing script:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
mkdir -p ~/mnist_alif/image
cd ~/mnist_alif/image
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
New-Item -ItemType Directory -Force -Path ~\mnist_alif\image
cd ~\mnist_alif\image
  {{< /tab >}}
{{< /tabpane >}}

Place a PNG or JPEG image of a handwritten digit in this directory and name it:

```text
mnist_image.jpg
```

{{% notice Note %}}
Use a simple, centered, high-contrast digit image. The script supports black-on-white and white-on-black images, and automatically converts black-on-white images to MNIST-style white-on-black format.


Feel free to use any of the images within this dataset: https://huggingface.co/datasets/ylecun/mnist.
{{% /notice %}}

## Download the preprocessing script

Download `prepare_mnist_image.py` into the image directory:

```bash
cd ~/mnist_alif/image
curl -o prepare_mnist_image.py https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/prepare_mnist_image.py
```

The script converts the image to 28 x 28 grayscale pixels, scales each pixel into the int8 range used by the firmware input, then writes the values as a C array:
```python
pixels = np.clip(np.rint(pixels * 127.0 / 255.0), 0, 127).astype(np.int8)
flat = pixels.reshape(-1)
```
The generated header will contain a total of 784 values, one for each pixel in the 28 x 28 input image.

## Generate the input header

Run the preprocessing script:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
cd ~/mnist_alif/image
python prepare_mnist_image.py mnist_image.jpg --output input_mnist.h
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
cd ~\mnist_alif\image
python .\prepare_mnist_image.py .\mnist_image.jpg --output .\input_mnist.h
  {{< /tab >}}
{{< /tabpane >}}

Verify the generated file:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
ls -lh input_mnist.h
head -n 8 input_mnist.h
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
Get-Item .\input_mnist.h
Get-Content .\input_mnist.h -TotalCount 8
  {{< /tab >}}
{{< /tabpane >}}

Open `input_mnist.h` and look at the generated `input_mnist` array. This is the numeric pixel data that `main.cpp` passes into the ExecuTorch runner.

## Copy the header into the firmware project

Copy `input_mnist.h` into the application assets directory:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
cp ~/mnist_alif/image/input_mnist.h ~/mnist_alif/alif_vscode-template/mnist_executorch/assets/
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
Copy-Item "$HOME\mnist_alif\image\input_mnist.h" "$HOME\mnist_alif\alif_vscode-template\mnist_executorch\assets\"
  {{< /tab >}}
{{< /tabpane >}}

Verify that both firmware assets are present:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
ls -lh ~/mnist_alif/alif_vscode-template/mnist_executorch/assets/
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
Get-ChildItem "$HOME\mnist_alif\alif_vscode-template\mnist_executorch\assets"
  {{< /tab >}}
{{< /tabpane >}}

You should see:

```output
input_mnist.h
mnist_model_data.h
```

## Summary

You converted a test digit image into `input_mnist.h` and copied it into the firmware project. The next section builds and flashes the application to the Alif Ensemble E8 DevKit.

