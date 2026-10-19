---
title: Build and run ASR on a Corstone-320 FVP
description: Build the Arm MLEK Conformer ASR application and run it on a Corstone-320 FVP to validate the model, runtime, and file-based audio path.
weight: 3

layout: "learningpathall"
---

## Understand the FVP ASR application

You'll build the Arm Machine Learning Evaluation Kit (MLEK) `asr` application and run it on the Corstone-320 Fixed Virtual Platform (FVP). The application checks the following before you move to the Alif E8 AppKit:

- Conformer model
- ExecuTorch runtime
- Audio preprocessing
- Token decoding

The FVP application runs the same core automatic speech recognition (ASR) stages used later on the E8 AppKit:

1. Read 16 kHz audio samples from the built-in sample set.
2. Convert the samples into Mel spectrogram features.
3. Run the Conformer model through ExecuTorch and the Ethos-U85 delegate.
4. Decode the output token scores with the SentencePiece vocabulary.
5. Print the decoded text to the FVP console.

On the FVP, the audio comes from WAV files compiled into the application. The result is printed over a simulated UART.

On the E8 AppKit, the audio comes from an onboard pulse-density modulation (PDM) microphone. An external Octal Serial Peripheral Interface (OSPI) flash stores the model, and an external screen displays the output.

Besides these distinctions, the Conformer model format, preprocessing, inference, and token decoding stages all stay the same.

## Build the FVP ASR application

Activate the Python environment created by the setup script:

```bash
source resources_downloaded/env/bin/activate
```

Configure the application with the MLEK `mps4-320-gcc` preset:

```bash
cmake -B build_fvp_asr \
  --preset mps4-320-gcc \
  -DML_FRAMEWORK=executorch \
  -DUSE_CASE_BUILD=asr \
  -DETHOS_U_NPU_TIMING_ADAPTER_ENABLED=OFF
```

The preset selects the following configuration:

- MPS4 Corstone-320 platform
- Cortex-M85 CPU
- Ethos-U85 with 256 MACs
- Dedicated SRAM memory mode
- GNU bare-metal toolchain

Disabling the timing adapter prepares this build for the functional fast-mode FVP run.

Build only the ASR target:

```bash
cmake --build build_fvp_asr --target mlek_asr --parallel
```

The output is similar to:

```output
build_fvp_asr/bin/mlek_asr.axf
```

An `.axf` file is the linked executable, in ELF format. It contains compiled code and data, their memory locations, and potentially debugging information. An FVP can load an appropriate `.axf` file directly.

## Install and verify the Corstone-320 FVP

The MLEK resource setup script doesn't install the Corstone-320 FVP. Install the FVP before you run the built `mlek_asr.axf` application.

For macOS, ensure that [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/) is installed before continuing. On macOS, you'll also activate the free MDK Community license for evaluation and non-commercial use.

{{< tabpane code=true >}}
  {{< tab header="Linux x86_64" language="bash">}}
cd "$HOME"
curl -LO https://developer.arm.com/-/cdn-downloads/permalink/FVPs-Corstone-IoT/Corstone-320/FVP_Corstone_SSE-320_11.27_25_Linux64.tgz
tar -xf FVP_Corstone_SSE-320_11.27_25_Linux64.tgz
./FVP_Corstone_SSE-320.sh \
  --i-agree-to-the-contained-eula \
  --no-interactive
export PATH="$HOME/FVP_Corstone_SSE-320/models/Linux64_GCC-9.3:$PATH"
source "$HOME/FVP_Corstone_SSE-320/scripts/runtime.sh"
unset PYTHONHOME
FVP_Corstone_SSE-320 --version
  {{< /tab >}}
  {{< tab header="Linux aarch64" language="bash">}}
cd "$HOME"
curl -LO https://developer.arm.com/-/cdn-downloads/permalink/FVPs-Corstone-IoT/Corstone-320/FVP_Corstone_SSE-320_11.27_25_Linux64_armv8l.tgz
tar -xf FVP_Corstone_SSE-320_11.27_25_Linux64_armv8l.tgz
./FVP_Corstone_SSE-320.sh \
  --i-agree-to-the-contained-eula \
  --no-interactive
export PATH="$HOME/FVP_Corstone_SSE-320/models/Linux64_armv8l_GCC-9.3:$PATH"
source "$HOME/FVP_Corstone_SSE-320/scripts/runtime.sh"
unset PYTHONHOME
FVP_Corstone_SSE-320 --version
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
docker info

cd "$HOME"
git clone https://github.com/Arm-Examples/FVPs-on-Mac.git
cd FVPs-on-Mac
git checkout 1458860a85bb702080276542ace78f72cba660b6
mkdir -p "$HOME/.armlm"
./build.sh

docker run --rm \
  --mount "type=bind,src=${HOME},dst=${HOME}" \
  --env "HOME=${HOME}" \
  --env "ARMLM_CACHED_LICENSES_LOCATION=${HOME}/.armlm" \
  fvp:11.27.31 \
  /opt/avh-fvp/bin/arm_license_management_utilities/armlm activate \
  --server https://mdk-preview.keil.arm.com \
  --product KEMDK-COM0

export PATH="$HOME/FVPs-on-Mac/bin:$PATH"
FVP_Corstone_SSE-320 --version
  {{< /tab >}}
{{< /tabpane >}}

The `PATH` setting and the Linux `runtime.sh` environment apply only to the current terminal. Add the appropriate settings to your shell startup file if you need to open a new terminal later.

## Run the application on the FVP

Return to the Arm MLEK repository root:

```bash
cd "$HOME/ml-embedded-evaluation-kit"
```

The generated model targets an Ethos-U85 with 256 MACs, so the FVP must use the matching `num_macs=256` setting. Run headlessly and enable the NPU functional fast mode:

{{% notice Note %}}
Fast mode is for checking application behavior. Performance and cycle figures reported by this run aren't meaningful. A timing-accurate run needs to keep the timing adapter enabled and omit `--fast`, and can take more than one hour.
{{% /notice %}}

```bash
FVP_Corstone_SSE-320 \
  -a "$PWD/build_fvp_asr/bin/mlek_asr.axf" \
  -C mps4_board.subsystem.ethosu.num_macs=256 \
  -C mps4_board.subsystem.ethosu.extra_args="--fast" \
  -C mps4_board.visualisation.disable-visualisation=1 \
  -C vis_hdlcd.disable_visualisation=1 \
  -C mps4_board.telnetterminal0.start_telnet=0 \
  -C mps4_board.uart0.out_file='-' \
  -C mps4_board.uart0.unbuffered_output=1 \
  -C mps4_board.uart0.shutdown_on_eot=1
```

A successful run identifies the sample and prints decoded text similar to:

```output
INFO - Using sample audio: another_door.wav
INFO - Decoded output: and he walked immediately out of the apartment by another door
```

The application uses audio samples compiled into the firmware at build time. By default, the `asr` use case reads WAV files from `resources/asr/samples/`.

## Use a custom audio sample

To test a known phrase, place one or more 16 kHz WAV files in a directory and set `asr_FILE_PATH` when configuring the build:

```bash
mkdir -p /tmp/asr_wavs
cp my_clip.wav /tmp/asr_wavs/

cmake -B build_fvp_asr \
  --preset mps4-320-gcc \
  -DML_FRAMEWORK=executorch \
  -DUSE_CASE_BUILD=asr \
  -DETHOS_U_NPU_TIMING_ADAPTER_ENABLED=OFF \
  -Dasr_FILE_PATH=/tmp/asr_wavs/

cmake --build build_fvp_asr --target mlek_asr --parallel
```

The CMake configure step converts the WAV files into generated C/C++ files and compiles them into the firmware.

Run the `FVP_Corstone_SSE-320` command from earlier again. The output should now identify your custom audio file:

```output
INFO - Using sample audio: my_clip.wav
INFO - Decoded output: <recognized text>
```

## Troubleshoot issues with the FVP ASR application

To troubleshoot issues with the FVP ASR application, consider the following guidance:

- If macOS reports that it can't find a compatible `executorch` or `tosa-tools` distribution, confirm that the host is Apple silicon. Ensure that the host is running macOS 15 or later and using Python 3.10 through 3.12.
- If the macOS FVP reports a license error, confirm that `~/.armlm` contains the active license cache. Repeat the activation step or use the entitlement for your organization.
- If Docker can't access the `.axf` file, confirm that the MLEK repository is under your home directory. Run the command from the repository root.
- If Linux can't find the FVP or its Python runtime, repeat the `PATH` export and source `FVP_Corstone_SSE-320/scripts/runtime.sh` in the current terminal.
- If inference appears to stall, confirm that the build used `ETHOS_U_NPU_TIMING_ADAPTER_ENABLED=OFF` and that the FVP command includes `extra_args="--fast"`.

## What you've accomplished and what's next

You've built the Arm MLEK Conformer ASR application and run it on the Corstone-320 FVP. Deactivate your environment before moving on.

Next, you'll clone the separate Alif MLEK repository and prepare the equivalent Conformer resources in its layout. You'll then compare the board-specific application with the FVP application.
