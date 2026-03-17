---
# User change
title: "Build ExecuTorch models for Ethos-U65"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

On the FRDM i.MX 93, you deploy ExecuTorch as two cooperating artifacts:

|Component|Role in Deployment|What It Contains|Why It's Required|
|---------|------------------|----------------|-----------------|
|**`.pte file`**  (e.g., `mobilenetv2_u65.pte`)|The model itself, exported from ExecuTorch|Serialized and quantized operator graph + weights + metadata|Provides the neural network to be executed|
|**`executor_runner`**  (binary [ELF](https://www.netbsd.org/docs/elf.html) file)|The runtime program that runs the .pte file|C++ application that loads the .pte, prepares buffers, and calls the NPU or CPU backend|Provides the execution engine and hardware access logic|

<style>
.ascii-diagram {
  font-size: 12px; /* Or smaller, like 10px */
  line-height: 1.2;
  font-family: monospace;
  white-space: pre-wrap;
  overflow-x: auto;
}
</style>
<center>
<br>
<pre class="ascii-diagram">
┌───────────────────────────────────────────────────┐
│                                                   │
│                Host Development                   │
│         (e.g., Linux or macOS+Docker)             │
│                                                   │
│  [Model export / compilation with ExecuTorch]     │
│                                                   │
│     ┌───────────────────┐        ┌───────────┐    │
│     │                   │        │           │    │
│     │  executor_runner  │        │  .pte     │    │
│     │  (ELF binary)     │        │ (model)   │    │
│     │                   │        │           │    │
│     └───────────┬───────┘        └─────┬─────┘    │
│                 │                      │          │
└─────────────────┼──────────────────────┼──────────┘
       │ SCP/serial transfer  │
       │                      │
       ▼                      ▼
┌───────────────────────────────────────────────────┐
│                                                   │
│            NXP i.MX93 Embedded Board              │
│                                                   │
│                                                   │
│  ┌───────────────────────────────────────────┐    │
│  │   executor_runner (runtime binary)        │    │
│  │                                           │    │
│  │    ┌───────────────────────────────┐      │    │
│  │    │ Load .pte (model)             │      │    │
│  │    └───────────────┬───────────────┘      │    │
│  │                    │                      │    │
│  │                    ▼                      │    │
│  │    ┌───────────────────────────────┐      │    │
│  │    │ Initialize hardware (CPU/NPU) │      │    │
│  │    └───────────────┬───────────────┘      │    │
│  │                    │                      │    │
│  │                    ▼                      │    │
│  │    ┌───────────────────────────────┐      │    │
│  │    │ Perform inference             │      │    │
│  │    └───────────────┬───────────────┘      │    │
│  │                    │                      │    │
│  │                    ▼                      │    │
│  │    ┌───────────────────────────────┐      │    │
│  │    │ Output results                │      │    │
│  │    └───────────────────────────────┘      │    │
│  └───────────────────────────────────────────┘    │
│                                                   │
└───────────────────────────────────────────────────┘
</pre>
<i>ExecuTorch runtime deployment to an embedded system</i>
</center>

## Build the ExecuTorch .pte for Ethos-U65

This section shows you how to build `.pte` files for the Ethos-U65 NPU.
You compile two models:

- A simple add model to validate the toolchain and U65 compile spec
- MobileNet V2 to demonstrate a realistic workload and confirm NPU operator coverage

The `.pte` file is the handoff point between “host build time” and “device run time”. In the later deployment steps, Linux is responsible for loading firmware, and the Cortex-M33 firmware is responsible for loading and executing the `.pte` using the Ethos-U delegate.

### Compile a simple add model

This script creates a basic addition model, quantizes it, and compiles it for the Ethos-U65. Use this to verify that your environment is correctly configured.

1. Create the compilation script:

   ```bash
   cat > compile_u65.py << 'EOF'
   import torch
   from torch.export import export
   from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_pt2e
   from executorch.backends.arm.ethosu import EthosUCompileSpec, EthosUPartitioner
   from executorch.backends.arm.quantizer import EthosUQuantizer, get_symmetric_quantization_config
   from executorch.exir import to_edge_transform_and_lower

   class SimpleAdd(torch.nn.Module):
       def forward(self, x, y):
           return x + y

   model = SimpleAdd().eval()
   example_inputs = (torch.ones(1, 1, 1, 1), torch.ones(1, 1, 1, 1))

   print("[1/5] Exporting...")
   exported_program = export(model, example_inputs)

   print("[2/5] Creating U65 spec...")
   compile_spec = EthosUCompileSpec(
       target="ethos-u65-256",
       system_config="Ethos_U65_High_End",
       memory_mode="Shared_Sram",
   )

   print("[3/5] Quantizing...")
   quantizer = EthosUQuantizer(compile_spec)
   quantizer.set_global(get_symmetric_quantization_config())
   prepared = prepare_pt2e(exported_program.graph_module, quantizer)
   prepared(*example_inputs)
   quantized = convert_pt2e(prepared)

   print("[4/5] Lowering to U65...")
   quantized_program = export(quantized, example_inputs)
   edge = to_edge_transform_and_lower(quantized_program, partitioner=[EthosUPartitioner(compile_spec)])
   pte = edge.to_executorch()

   print("[5/5] Saving...")
   with open("model_u65.pte", "wb") as f:
       f.write(pte.buffer)
   print(f"SUCCESS: model_u65.pte ({len(pte.buffer)/1024:.1f} KB)")
   EOF
   ```

2. Run the compilation:

   ```bash
   python3 compile_u65.py
   ```

   If successful, you see output similar to:

   ```output
   [1/5] Exporting...
   [2/5] Creating U65 spec...
   [3/5] Quantizing...
   [4/5] Lowering to U65...
   [5/5] SUCCESS! Saved: model_u65.pte
   File size: 3.9 KB
   ```

### Compile MobileNet V2

This script compiles the [MobileNet V2](https://pytorch.org/hub/pytorch_vision_mobilenet_v2/) computer vision model for the Ethos-U65. MobileNet V2 is a convolutional neural network (CNN) used for image classification and object detection.

{{% notice Note %}}
MobileNet V2 uses `export_for_training()` instead of `export()` because it contains batch normalization layers that must be traced in training mode before quantization can fuse them. The simple add model above has no such layers, so `export()` is sufficient.
{{% /notice %}}

1. Create the MobileNet V2 compilation script:

   ```bash
   cat > compile_mv2_u65.py << 'EOF'
   import torch
   from torch.export import export, export_for_training
   from torchvision.models import mobilenet_v2, MobileNet_V2_Weights
   from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_pt2e
   from executorch.backends.arm.ethosu import EthosUCompileSpec, EthosUPartitioner
   from executorch.backends.arm.quantizer import EthosUQuantizer, get_symmetric_quantization_config
   from executorch.exir import to_edge_transform_and_lower

   print("[1/5] Loading MobileNetV2...")
   model = mobilenet_v2(weights=MobileNet_V2_Weights.IMAGENET1K_V1).eval()
   example_inputs = (torch.randn(1, 3, 224, 224),)

   print("[2/5] Exporting...")
   exported_program = export_for_training(model, example_inputs).module()

   print("[3/5] Quantizing for U65...")
   compile_spec = EthosUCompileSpec(
       target="ethos-u65-256",
       system_config="Ethos_U65_High_End",
       memory_mode="Shared_Sram",
   )
   quantizer = EthosUQuantizer(compile_spec)
   quantizer.set_global(get_symmetric_quantization_config())
   prepared = prepare_pt2e(exported_program, quantizer)
   prepared(*example_inputs)
   quantized = convert_pt2e(prepared)

   print("[4/5] Lowering to U65...")
   quantized_program = export(quantized, example_inputs)
   edge = to_edge_transform_and_lower(quantized_program, partitioner=[EthosUPartitioner(compile_spec)])
   pte = edge.to_executorch()

   print("[5/5] Saving...")
   with open("mobilenetv2_u65.pte", "wb") as f:
       f.write(pte.buffer)
   print(f"SUCCESS: mobilenetv2_u65.pte ({len(pte.buffer)/1024/1024:.2f} MB)")
   EOF
   ```

2. Run the compilation:

   ```bash
   python3 compile_mv2_u65.py
   ```

    If successful, you see the Vela compiler summary indicating 100% NPU utilization. This is an important bring-up signal because it shows the graph was lowered onto the Ethos-U path rather than falling back to CPU execution.

   ```output
   Network summary for out
   Accelerator configuration               Ethos_U65_256
   System configuration                    Ethos_U65_High_End
   Memory mode                             Shared_Sram

   CPU operators = 0 (0.0%)
   NPU operators = 117 (100.0%)

   Neural network macs                     300838272 MACs/batch
   SUCCESS: mobilenetv2_u65.pte (3.34 MB)
   ```

3. Verify that the `.pte` file was generated:

   ```bash
   ls -la mobilenetv2_u65.pte
   ```

### Copy models to the SD card

The `executor_runner` firmware loads `.pte` models from a fixed DDR address (`0xC0000000`). The model must be written to DDR before Linux boots, using U-Boot.

1. Copy the `.pte` files out of the Docker container:

   ```bash
   docker cp <container-id>:/root/executorch/model_u65.pte .
   docker cp <container-id>:/root/executorch/mobilenetv2_u65.pte .
   ```

   Replace `<container-id>` with your Docker container ID.

2. Write the `.pte` files to the first partition of the SD card so U-Boot can load them:

{{< tabpane code=false >}}
{{< tab header="Linux" >}}
sudo mount /dev/sdX1 /mnt
sudo cp model_u65.pte mobilenetv2_u65.pte /mnt/
sudo umount /mnt
{{< /tab >}}
{{< tab header="macOS" >}}
cp model_u65.pte mobilenetv2_u65.pte /Volumes/<SD_CARD_NAME>/
{{< /tab >}}
{{< /tabpane >}}

{{% notice Parameter placeholders %}}
For the commands above:
- Replace `/dev/sdX1` with your SD card's first partition.
- Replace `<SD_CARD_NAME>` with the mounted volume name.
{{% /notice %}}

## What you've learned and what's next

In this section you've:

- Compiled a simple add model to verify the Ethos-U65 toolchain setup
- Built a MobileNet V2 `.pte` file with 100% NPU operator coverage
- Staged the models on your SD card for deployment

With both `.pte` files ready, you can now build the Cortex-M33 `executor_runner` firmware that will load and execute them.

