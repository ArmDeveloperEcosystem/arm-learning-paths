---
title: (Optional) Export PyTorch model to ExecuTorch format
weight: 5
layout: learningpathall
---

## Overview

This section exports an MNIST PyTorch model to ExecuTorch `.pte` format for the Arm Ethos-U85 NPU on the Alif Ensemble E8 DevKit.


{{% notice Note %}}
If you are using the provided `.pte` file, you can skip this section.
{{% /notice %}}

The Docker container is used for this step. Files written to `/home/developer/output` in the container appear on your host machine in `~/mnist_alif/executorch-alif/output`.


## Start your container

Ensure you are inside your container and load up the Executorch environment:

```bash
# Inside Docker container
source ~/executorch-venv/bin/activate
source $ET_HOME/setup_arm_env.sh
```

Verify the tools:
```bash
vela --version
python3 -c "from executorch.exir import to_edge; print('ExecuTorch OK')"
```

## Download the model files

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

<!-- {{% notice Note %}}
The model input is a normalized float32 tensor with shape [1, 1, 28, 28]. The output is 10 logits, one for each digit from 0 to 9.
{{% /notice %}} -->

## Add calibration input

The model is exported with int8 quantization, so the compiler needs a representative MNIST input during export. This input is not the image that runs on the board. It is only used to set quantization ranges when generating the `.pte` file.
```bash
curl -L -o /home/developer/output/sample_one.pt https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/sample_one.pt
```

Verify the calibration input:
```bash
python3 - << 'EOF'
import torch
x = torch.load("/home/developer/output/sample_one.pt", map_location="cpu")
print(x.shape)
print(x.dtype)
EOF
```
Expected output:
```output
torch.Size([1, 1, 28, 28])
torch.float32
```

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
Use full paths such as `/home/developer/models/mnist_model.py`. Do not use `~` in the export command.
{{% /notice %}}

Verify the exported file:

```bash
ls -lh /home/developer/output/mnist_ethos_u85.pte
```

## Build ExecuTorch static libraries

The firmware links against ExecuTorch runtime libraries. Build the bare-metal Cortex-M libraries inside the container:

```bash
cd $ET_HOME
source ~/executorch-venv/bin/activate
rm -rf arm_test/cmake-out
bash backends/arm/scripts/build_executorch.sh
```

This step can take several minutes.

When the build finishes, list the generated static libraries:

```bash
find arm_test/cmake-out -type f -name "*.a" | sort
```

You should see libraries including:

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

Because `/home/developer/output` is mounted from your host machine, `et_bundle.tar.gz` is now available on your host at:

```text
~/mnist_alif/executorch-alif/output/et_bundle.tar.gz
```