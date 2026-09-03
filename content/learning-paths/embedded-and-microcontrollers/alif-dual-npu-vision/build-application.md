---
title: Build the dual-NPU application
description: Configure the Zephyr overlays and build the firmware and model payload for the E8 high-performance core.
weight: 4
layout: "learningpathall"
---

The sample includes compiled PTE models for Ethos-U55 and Ethos-U85. It also includes a startup image that verifies both inference pipelines before the application starts the live camera.

## Define the build inputs

From the west workspace root, activate the Python environment and define the sample paths:

```bash
cd $HOME/alif-dual-npu
source .venv/bin/activate
APP=$PWD/sdk-alif/samples/modules/executorch/dual_npu_vision
OD=$PWD/sdk-alif/samples/modules/tflite-micro/alif_object_detection
MODULES=$(west list -f '{abspath}' | grep -v '/modules/lib/executorch$' | paste -sd';' -)
MODULES="$MODULES;$PWD/modules/lib/executorch;$PWD/modules/ethos-u-core-driver-src"
```

The overlay order matters. The final `isp_route.overlay` file disables the CPI memory endpoint and routes camera frames exclusively through the ISP.

## Build the firmware

Run the complete build command:

```bash
west build \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  -d build-dual-npu-vision \
  "$APP" --pristine -- \
  -DZEPHYR_MODULES="$MODULES" \
  -DPYTHON_EXECUTABLE="$PWD/.venv-executorch/bin/python" \
  -DPython3_EXECUTABLE="$PWD/.venv-executorch/bin/python" \
  -DCMSIS_NN_LOCAL_PATH="$PWD/modules/cmsis-nn-src" \
  -DDTC_OVERLAY_FILE="$APP/boards/dual_npu_e8.overlay;$OD/boards/alif_e8_dk_ae822fa0e5597xx0_rtss_hp.overlay;$OD/serial_camera.overlay;$OD/serial_camera_mt9m114.overlay;$OD/serial_camera_isp.overlay;$OD/serial_camera_mt9m114_isp.overlay;$APP/isp_route.overlay" \
  -DOVERLAY_CONFIG="$APP/vision.conf"
```

A successful build ends with messages showing that Zephyr linked the ELF file and generated the binary.

Confirm that the three expected outputs exist:

```bash
ls -lh build-dual-npu-vision/zephyr/zephyr.bin \
  build-dual-npu-vision/zephyr/zephyr.elf \
  build-dual-npu-vision/model_assets.bin
```

The files have these roles:

| File | Purpose |
| --- | --- |
| `zephyr.bin` | Cortex-M55 Zephyr application |
| `zephyr.elf` | Symbols and debug information |
| `model_assets.bin` | U85 PTE, U55 PTE, startup image, and ImageNet labels |

The checked-in PTE files let you build this Learning Path without regenerating models. The original artifacts were generated on a Linux development host, but the model inputs are public and do not depend on that host.

Create a directory for the source weights:

```bash
cd $HOME/alif-dual-npu
mkdir -p model-weights
```

Download the trained [SSD-Slim int8 model](https://github.com/emza-vs/ModelZoo/blob/59fcdb2aab865a8a8d93a9d419b3c5490a5508e4/Models/Object_detection/SSD/ssd_slim_120x160x1_v1_int8.tflite) and the official [torchvision MobileNetV2 checkpoint](https://download.pytorch.org/models/mobilenet_v2-7ebf99e0.pth). The SSD URL is pinned to the commit that added the model:

```bash
curl -L \
  https://raw.githubusercontent.com/emza-vs/ModelZoo/59fcdb2aab865a8a8d93a9d419b3c5490a5508e4/Models/Object_detection/SSD/ssd_slim_120x160x1_v1_int8.tflite \
  -o model-weights/ssd_slim_120x160x1_v1_int8.tflite
curl -L \
  https://download.pytorch.org/models/mobilenet_v2-7ebf99e0.pth \
  -o model-weights/mobilenet_v2-7ebf99e0.pth
```

Verify both downloads before using them:

```bash
echo "64fcc31aa517798d0e798551418c85bc0a5ed03a75c45c4e47fc7ee41e5ea51f  model-weights/ssd_slim_120x160x1_v1_int8.tflite" | shasum -a 256 -c -
echo "7ebf99e03e254b273379b23edca7ec0da9f48273b23a332b93c1c99d49e86e8f  model-weights/mobilenet_v2-7ebf99e0.pth" | shasum -a 256 -c -
```

The SSD source repository does not publish a PyTorch checkpoint. Install TensorFlow in the ExecuTorch Python environment, then use the sample's importer to convert the trained, quantized constants into the common PyTorch checkpoint:

```bash
.venv-executorch/bin/python -m pip install tensorflow==2.20.0
.venv-executorch/bin/python \
  "$APP/tools/import_ssd_slim_tflite.py" \
  --source model-weights/ssd_slim_120x160x1_v1_int8.tflite \
  --output model-weights/ssd_slim_common.pth
```

Generate both PTE files with the Alif Vela configuration included in the SDK:

```bash
"$APP/tools/generate_pte_models.sh" \
  "$PWD/sdk-alif/samples/modules/executorch/ensemble_vela.ini" \
  "$PWD/model-weights/ssd_slim_common.pth" \
  "$PWD/model-weights/mobilenet_v2-7ebf99e0.pth"
```

The script emits `comparable_ssd_slim_u55.pte` and `mobilenet_v2_imagenet_u85.pte` in the sample's `models` directory. The export uses PT2E quantization, deterministic representative inputs, the ExecuTorch Ethos-U partitioner, and Vela. Both programs expose int8 tensors and require complete delegation, with no Cortex-M fallback operators. The SSD checkpoint is produced by the supplied offline weight-import tool. Both deployed files are native ExecuTorch PTE programs.
