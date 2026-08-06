---
title: (Optional) Export PyTorch model to ExecuTorch format
weight: 5
layout: learningpathall
---


## Download the model files

To export an MNIST PyTorch model to ExecuTorch `.pte` format, start by downloading the model files. 

{{% notice Note %}}
If you're using the provided `.pte` file instead, skip the entire model export section and proceed with [Prepare firmware artifacts](/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/).
{{% /notice %}}

From inside your container, create the model and output directories:

```bash
# Create directories (use full paths, not ~)
mkdir -p /home/developer/models
mkdir -p /home/developer/output
```

Download the model script and the training script:

```bash
curl -L -o /home/developer/models/mnist_model.py https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/mnist_model.py
curl -L -o /home/developer/models/train_mnist.py https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/train_mnist.py
```

The model script (`mnist_model.py`) defines a small convolutional network for 28 x 28 grayscale MNIST images. It has two convolution blocks followed by two fully connected layers:
```python
def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        # Fully Connected Layers
        self.fc1 = nn.Linear(32 * 7 * 7, 64)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(64, 10)
```
The convolution layers extract image features such as strokes, edges, and digit shapes. Each output channel from a convolution is called a feature map.

Layer 1 (`fc1`) takes in 32 feature maps of size 7 x 7 each, and reduces those values to 64 features. The final layer (`fc2`) then maps those 64 features to 10 digit scores (0 to 9).

The same file also exposes the objects expected by the ExecuTorch ahead-of-time compiler:
```python
ModelUnderTest = MNISTModel() # PyTorch model to export
ModelInputs = (load_calibration_input(),) 
```

The training script, however, downloads the [MNIST dataset](https://datasetsearch.research.google.com/search?query=mnist&docid=L2cvMTF0ZGh0cHRmMA%3D%3D), normalizes the images, trains the model, and saves the trained weights to `/home/developer/models/mnist_model.pth`.
<!-- {{% notice Note %}}
The model input is a normalized float32 tensor with shape [1, 1, 28, 28]. The output is 10 logits, one for each digit from 0 to 9.
{{% /notice %}} -->

## Add calibration input

The model is exported with int8 quantization, so the compiler needs a representative MNIST input during export. 

This input is not the image that runs on the board. It's used only to set quantization ranges when generating the `.pte` file.

Download the calibration sample:
```bash
curl -L -o /home/developer/output/sample_one.pt https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/sample_one.pt
```

The downloaded sample contains one normalized MNIST-style grayscale image, saved as a PyTorch tensor (`.pt`) with shape `[1, 1, 28, 28]` and type `float32`. 
This allows `mnist_model.py` to load the exact format it needs without any image preprocessing step.

For production-quality quantization, you'd normally calibrate with a larger and more diverse set of representative inputs. To keep the export flow small and reproducible, you'll use one sample for completing the Learning Path.

## Train the model

Run the training script:

```bash
cd /home/developer/models
python3 train_mnist.py --out /home/developer/models/mnist_model.pth --epochs 3
```

The output shows the test accuracy after each epoch:

```output
epoch=1 test_loss=... test_acc=...
epoch=2 test_loss=... test_acc=...
epoch=3 test_loss=... test_acc=...
saved /home/developer/models/mnist_model.pth
```

Verify the checkpoint:

```bash
ls -lh /home/developer/models/mnist_model.pth
```

## Export to ExecuTorch

Export the trained model to `.pte` format for Ethos-U85:

```bash
cd $ET_HOME
MNIST_LOAD_CHECKPOINT=1 python3 -m examples.arm.aot_arm_compiler --model_name=/home/developer/models/mnist_model.py --delegate --quantize --target=ethos-u85-256 --system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Shared_Sram --output=/home/developer/output/mnist_ethos_u85.pte
```
{{% notice Important %}}
Use full paths such as `/home/developer/models/mnist_model.py`. Don't use `~` in the export command.
{{% /notice %}}

The following are the arguments passed in the export command:
- `MNIST_LOAD_CHECKPOINT=1`: loads the trained weights from /home/developer/models/mnist_model.pth.
- `--model_name`: points to the PyTorch model definition.
- `--delegate`: partitions supported operators for execution on the Ethos-U NPU.
- `--quantize`: converts the model for int8 inference.
- `--target=ethos-u85-256`: targets an Ethos-U85 configuration with 256 MACs per cycle.
- `--system_config` and `--memory_mode`: selects the Vela memory configuration used when compiling the NPU command stream.
- `--output`: writes the exported ExecuTorch program.

Vela is Arm’s compiler for Ethos-U NPUs. During export, it prints information about the selected Ethos-U target, memory use, and NPU performance estimates. Review this output to confirm that the model was compiled for the expected `ethos-u85-256` target. 

At the end, you should see confirmation of the saved `.pte` file as follows:

```output
PTE file saved as /home/developer/output/mnist_ethos_u85.pte
```

## Build ExecuTorch static libraries

The firmware links against ExecuTorch runtime libraries. Build the bare-metal Cortex-M libraries inside the container:

```bash
cd $ET_HOME
source ~/executorch-venv/bin/activate
rm -rf arm_test/cmake-out
bash backends/arm/scripts/build_executorch.sh
```

{{% notice Note %}}
This step can take several minutes.
{{% /notice %}}

When the build finishes, list the generated static libraries:

```bash
find arm_test/cmake-out -type f -name "*.a" | sort
```

The output is similar to:

```output
libexecutorch.a
libexecutorch_core.a
libexecutorch_delegate_ethos_u.a
libcortex_m_ops_lib.a
libcmsis-nn.a
```

## Package headers and libraries

Bundle the ExecuTorch headers and libraries into `et_bundle.tar.gz`:

```bash
rm -rf /home/developer/output/et_bundle
mkdir -p /home/developer/output/et_bundle
cp -a arm_test/cmake-out/include /home/developer/output/et_bundle/
cp -a arm_test/cmake-out/lib /home/developer/output/et_bundle/
CMSIS_NN_LIB=$(find arm_test/cmake-out -type f -name "libcmsis-nn.a" | head -n 1)
cp "$CMSIS_NN_LIB" /home/developer/output/et_bundle/lib/
tar -C /home/developer/output -czf /home/developer/output/et_bundle.tar.gz et_bundle
```

Because `/home/developer/output` is mounted from your host machine, `et_bundle.tar.gz` is now available on your host at `~/mnist_alif/executorch-alif/output/et_bundle.tar.gz`.

Exit Docker:

```bash
exit
```

## What you've accomplished and what's next

You've now downloaded and trained the MNIST model and exported an int8 ExecuTorch `.pte` file for the Ethos-U85 NPU. You've also built the bare-metal ExecuTorch libraries and packaged the required headers and libraries into `et_bundle.tar.gz`.

Next, you'll prepare the model and runtime artifacts for the Alif firmware project.
