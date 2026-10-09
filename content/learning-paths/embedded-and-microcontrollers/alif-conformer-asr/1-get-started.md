---
title: Get started with Conformer ASR and MLEK
description: Review the ASR flow, clone the Arm MLEK repository, and generate the ExecuTorch Conformer model resources used by the FVP application.
weight: 2

layout: "learningpathall"
---

## What is automatic speech recognition?

Automatic speech recognition (ASR) converts speech audio into text. The application you will run reads fixed 16 kHz audio, converts the samples into Mel spectrogram features, runs a Conformer model, and decodes the output tokens into text.

[Conformer](https://github.com/sooftware/conformer/) is a transformer-based neural network architecture used for speech tasks. It combines attention layers, which help the model use context from different parts of an utterance, with convolution layers, which help capture local audio patterns.

The Conformer model in this flow does not take raw audio directly. The preprocessing code creates an 80-bin Mel spectrogram using a 512-sample window and 160-sample hop. The postprocessing code then removes repeated tokens and maps token IDs to text using the SentencePiece vocabulary.

The [SentencePiece vocabulary](https://github.com/google/sentencepiece/blob/master/README.md#what-is-sentencepiece) is the token list used by the decoder. The model outputs token IDs, not finished words, and the vocabulary maps each ID to a text piece such as a letter, word fragment, or word-start marker.

## The ML Evaluation Kit

The Machine Learning Evaluation Kit (MLEK) is a set of embedded machine learning examples, build scripts, model resources, and deployment flows for Arm-based microcontroller systems. In this section, you will review the ASR and MLEK flow, clone the Arm MLEK repository, initialize submodules, and run the ExecuTorch resource setup script that prepares the Conformer model assets.

Ethos-U85 is an Arm NPU for accelerating neural networks in high-performance microcontroller designs, and is a primary target for the MLEK. Conformer is a good fit for this target because ASR depends on both local sound patterns and longer-range speech context. In this flow, the model is exported as an ExecuTorch `.pte` file using the Ethos-U ExecuTorch backend, so supported operations can run on the Ethos-U85 NPU instead of only on the Cortex-M CPU.

Before using the physical Alif E8 AppKit, you will run the ASR application on the [Corstone-320 Fixed Virtual Platform (FVP)](https://support.arm.com/documentation/109760/0000/SSE-320-FVP). An FVP is a software model of an Arm system that can run the same baremetal firmware you later port and deploy to hardware. Corstone-320 includes an Ethos-U85 target, so you can prototype and debug the model, runtime, and application flow before porting the application to the Alif board.

## Prepare your development host

{{% notice Important %}}
Use Linux on an x86_64 or aarch64 host, or use an **Apple Silicon Mac** running macOS 15 or later. 

The commands have not been validated on native Windows. WSL with USB passthrough can work with the E8 AppKit, but that configuration is outside the scope of this Learning Path.
{{% /notice %}}

MLEK requires Python 3.10, 3.11, or 3.12. Install the host packages for your operating system. The macOS commands assume you have already installed [Homebrew](https://brew.sh/).

{{< tabpane code=true >}}
  {{< tab header="Ubuntu Linux" language="bash">}}
sudo apt update
sudo apt install -y \
  build-essential \
  git \
  ninja-build \
  python3 \
  python3-dev \
  python3-pip \
  python3-venv \
  unzip \
  curl \
  libsndfile1
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
xcode-select --install
brew install git python@3.12 libsndfile
alias python3=/opt/homebrew/bin/python3.12
  {{< /tab >}}
{{< /tabpane >}}

Install the `arm-none-eabi` distribution of the [Arm GNU Toolchain](/install-guides/gcc/arm-gnu/). The compiler must be version 13.2.1 or later for Cortex-M85; Arm GNU Toolchain 14.2.Rel1 is the version used by the pinned MLEK Docker environment.

Verify the host and toolchain:

```bash
python3 --version
make --version
arm-none-eabi-gcc --version
```

## Clone the Arm MLEK repository

Clone the Arm ML Embedded Evaluation Kit repository:

```bash
cd "$HOME"
git clone https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit.git
cd ml-embedded-evaluation-kit
git checkout f2f6247a672794ecf9df0216d14c3a5c324537dd
git submodule update --init --recursive
```

## Set up ExecuTorch resources

Run the setup script with ExecuTorch enabled. Selecting only the `asr` use case avoids generating resources for unrelated MLEK examples.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu Linux" language="bash">}}
python3 set_up_default_resources.py \
  --parallel "$(nproc)" \
  --ml-frameworks executorch \
  --use-case asr
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
python3 set_up_default_resources.py \
  --parallel "$(sysctl -n hw.logicalcpu)" \
  --ml-frameworks executorch \
  --use-case asr
  {{< /tab >}}
{{< /tabpane >}}

The first run creates a Python environment and downloads the pinned model and framework dependencies. It can take several minutes.

Confirm that MLEK generated the `.pte` models and that the vocabulary is present:

```bash
find resources_downloaded/asr -name '*.pte' -print
ls -lh resources/asr/labels/librispeech_sp.pieces
```

## How are the ExecuTorch .pte files generated?

The setup script is a wrapper around the MLEK resource pipeline. For the ASR use case, it does three jobs:

1. Creates a Python virtual environment in `resources_downloaded/env`.
2. Downloads the Conformer checkpoint into `resources_downloaded/asr/`.
3. Runs the ASR lowering script to create ExecuTorch `.pte` files for the configured targets.

The ASR resource entry in `resources/use_case_resources.json` tells MLEK which checkpoint to download and which lowering script to run.

The `requirements.txt` file installs the Conformer Python package used by the generator. The generator then recreates the model architecture, loads the trained FP32 weights, and switches the model to inference mode:

```python
model = Conformer(
    num_classes=129,
    input_dim=NUM_MELS,
    encoder_dim=144,
    num_encoder_layers=16,
    num_attention_heads=4,
    # Other hyperparameters omitted.
)

checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=True)
model.load_state_dict(checkpoint["model"])
model.eval()
```

The script creates example inputs with the same shape expected by the embedded application: one tensor for Mel spectrogram features, and one tensor for the input length:

```python
example_inputs = (
    torch.rand(1, CHUNK_SIZE, NUM_MELS),
    torch.tensor([CHUNK_SIZE], dtype=torch.int32),
)
```

Next, PyTorch exports the model with `torch.export`. This produces an exported program that ExecuTorch can lower:

```python
exported_program = export(
    load_model(checkpoint_path), example_inputs, strict=True
)
graph_module = exported_program.module(check_guards=False)
```

For Ethos-U targets, the script prepares the graph for post-training quantization using the ExecuTorch Arm backend's `EthosUQuantizer`. It calibrates the graph by running the model over the WAV files in `resources/asr/samples/`, using the same log Mel spectrogram preprocessing as the application:

```python
quantizer = EthosUQuantizer(compile_spec)
quantizer.set_global(get_symmetric_quantization_config(is_per_channel=True))

quantized_graph_module = prepare_pt2e(graph_module, quantizer)
for sample in list(audio_samples_dir.glob("*.wav")):
    audio_tensor = preprocess_audio(sample)
    quantized_graph_module(audio_tensor, chunk_tensor)

quantized_graph_module = convert_pt2e(quantized_graph_module)
```

After calibration and conversion, the generator exports the quantized graph again and creates an Ethos-U partitioner. The partitioner marks the parts of the graph that can be delegated to the Ethos-U backend:

```python
partitioner = EthosUPartitioner(compile_spec)
exported_program = export(quantized_graph_module, example_inputs, strict=True)
```

Finally, ExecuTorch lowers the exported program to the edge form, applies the Ethos-U partitioner, converts the result to an ExecuTorch program, and writes the `.pte` file:

```python
edge_program_manager = to_edge_transform_and_lower(
    exported_program,
    partitioner=[partitioner],
    compile_config=EdgeCompileConfig(_check_ir_validity=False),
)

save_pte_program(
    edge_program_manager.to_executorch(
        config=ExecutorchBackendConfig(extract_delegate_segments=False)
    ),
    str(output),
)
```

- The `.pte` model file contains the ExecuTorch program that runs the Conformer network.
- The `.pieces` vocabulary file contains the text tokens used to decode the model output.

At runtime, the application converts audio into Mel spectrogram features, runs the `.pte` model, and then uses the vocabulary file to turn model output IDs into text.

The vocab file is a line-by-line token list. During postprocessing, the decoder uses the model output value as an index into this list.

Each entry is a piece of text. Some pieces are single letters, some are word fragments, and some represent common words or word starts. SentencePiece uses the `▁` marker to represent a word boundary, so `▁the` means the token starts a new word.

## What you have accomplished and what is next

You have reviewed how the Conformer ASR application fits into MLEK, cloned the Arm MLEK repository, and generated the ExecuTorch `.pte` model and vocabulary resources used by the FVP application.

Next, you will build and run the ASR application on the Corstone-320 FVP.
