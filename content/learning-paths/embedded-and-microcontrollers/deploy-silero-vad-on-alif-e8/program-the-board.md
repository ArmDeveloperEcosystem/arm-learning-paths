---
title: Program the Silero firmware on the E8 HP core
description: Preserve the boot configuration, sign the embedded-model firmware, and independently verify its MRAM installation.
weight: 6
layout: learningpathall
---

## Use the E8 A0 SWD programming procedure

Each firmware contains its PTE; the validation configuration also embeds the recording. Install two MRAM payloads through J-Link SWD: the selected HP firmware and its signed Alif application table-of-contents package (AToC). No external OSPI model transfer is needed. Program and check `validation` first, then repeat this procedure for `live`.

This procedure targets **E8 A0 `AE822FA0E5597LS0`** with its display attached. Keep the validation and live firmware identities, signed packages, readbacks, and logs separate. Other silicon revisions require separate validation.

Close other debugger sessions. With board power disconnected, verify **SW3 JLOB=EN** and select **SW4 UART4** for the HP console, then connect **PRG USB** using a data-capable cable. SW4 selects the UART bridge; SWD does not require SEUART. Use SEUART only for Security Toolkit ISP operations. See the [official Alif DK-E8 User Guide](https://alifsemi.com/download/AUGD0023).

## Select the configuration and evidence directory

The build lesson initially selects `validation`. Preserve that selection and create its evidence directory:

```bash
: "${SILERO_MODE:?Select validation or live from the build/validation lesson}"
: "${SILERO_BUILD:?Select the matching firmware build directory}"
export SILERO_RUN_DIR="$SILERO_OUTPUT/$SILERO_MODE"
mkdir -p "$SILERO_RUN_DIR"
```

After the 79-value comparison passes, repeat the programming steps with `SILERO_MODE=live`, `SILERO_BUILD="$SILERO_LIVE_BUILD"`, and `SILERO_RUN_DIR="$SILERO_OUTPUT/live"`. Create that directory before proceeding. Both modes require their own signed package and fresh readbacks. The helper refuses to overwrite an existing prepared run; use a new evidence directory for later rebuilds.

## Select the J-Link probe

List probes and select the intended board's numeric serial number, separate from its `/dev/cu.usbmodem...` UART path:

```bash
export JLINK_EXECUTABLE="${JLINK_EXECUTABLE:-$JLINK_COMMANDER}"
printf 'ShowEmuList USB\nExit\n' > "$SILERO_RUN_DIR/list-probes.jlink"
"$JLINK_EXECUTABLE" -AutoConnect 0 -NoGui 1 \
  -CommandFile "$SILERO_RUN_DIR/list-probes.jlink"
export JLINK_SERIAL=REPLACE_WITH_YOUR_PROBE_SERIAL
cat > "$SILERO_RUN_DIR/jlink-selected" <<'SH'
#!/bin/sh
case "$JLINK_SERIAL" in
  ''|*[!0-9]*) echo 'Set the numeric JLINK_SERIAL' >&2; exit 2;;
esac
exec "$JLINK_EXECUTABLE" -USB "$JLINK_SERIAL" "$@"
SH
chmod +x "$SILERO_RUN_DIR/jlink-selected"
export JLINK_COMMANDER="$SILERO_RUN_DIR/jlink-selected"
```

Keep these exported variables active. `JLINK_EXECUTABLE` must name the actual SEGGER binary, never the wrapper. Select the serial again when changing boards.

Check that HP can read application MRAM:

```bash
export ALIF_MRAM_CORE=HP
export ALIF_MRAM_DEVICE=AE822FA0E5597LS0_M55_HP
printf 'H\nMem32 0x80000000 4\nG\nExit\n' \
  > "$SILERO_RUN_DIR/check-mram-access.jlink"
"$JLINK_COMMANDER" -Device "$ALIF_MRAM_DEVICE" -If SWD -Speed 4000 \
  -AutoConnect 1 -NoGui 1 -ExitOnError 1 \
  -CommandFile "$SILERO_RUN_DIR/check-mram-access.jlink"
```

If HP reports no AHB ROM and cannot connect, set `ALIF_MRAM_CORE=HE` and `ALIF_MRAM_DEVICE=AE822FA0E5597LS0_M55_HE`, then rerun this access check. Use that fallback only if a fresh HE connection reads MRAM successfully. This debug route has also been exercised on E8 A0; the image still targets and boots HP. Keep `ALIF_DEVICE=AE822FA0E5597LS0_M55_HP`. Stop if neither core is readable.

## Back up application MRAM

Before downloading, save the application-MRAM region `[0x80000000, 0x80580000)` in a fresh process:

```bash
(
set -e
test ! -e "$SILERO_RUN_DIR/application-mram-before.bin"
cat > "$SILERO_RUN_DIR/backup-mram.jlink" <<EOF
H
SaveBin "$SILERO_RUN_DIR/application-mram-before.bin" 0x80000000 0x580000
G
Exit
EOF
"$JLINK_COMMANDER" -Device "$ALIF_MRAM_DEVICE" -If SWD -Speed 4000 \
  -AutoConnect 1 -NoGui 1 -ExitOnError 1 \
  -CommandFile "$SILERO_RUN_DIR/backup-mram.jlink"
python - <<'PY'
from pathlib import Path
import os
backup = Path(os.environ["SILERO_RUN_DIR"]) / "application-mram-before.bin"
assert backup.stat().st_size == 0x580000, "Incomplete application-MRAM backup"
PY
shasum -a 256 "$SILERO_RUN_DIR/application-mram-before.bin"
)
```

Retain the backup and hash. Use a new output workspace for another board instead of overwriting evidence. Stop on a failed debug connection or incomplete read. This procedure assumes debug access is already provisioned; it does not replace Security Enclave firmware or system MRAM.

## Stage and sign the aligned firmware

Download the [MRAM preparation helper](../prepare_mram_programming.py) to `$ALIF_WORK`. Check its SHA256 using `shasum -a 256`; require:

```output
3aab6ca07ae2249609bcfc342c4aa2d17560d3fe99441f6cab2fef8c5bdd5614
```

Use the known working application JSON for this A0 board as `ALIF_APP_CONFIG`. The standard template is `build/config/app-cpu-stubs.json`; use it only after confirming its device configuration and companion images match the board. Preserve all AP/HE entries, signing settings, clocks, and referenced binaries. Create a separate HP configuration and stage the firmware before signing:

```bash
export MRAM_HELPER="$ALIF_WORK/prepare_mram_programming.py"
export ALIF_APP_CONFIG="${ALIF_APP_CONFIG:-$ALIF_SE_TOOLS_DIR/build/config/app-cpu-stubs.json}"
test -s "$ALIF_APP_CONFIG"
test -x "$ALIF_SE_TOOLS_DIR/app-gen-toc"
tar -czf "$SILERO_RUN_DIR/setools-config-before-silero.tar.gz" \
  -C "$ALIF_SE_TOOLS_DIR" build/config
python - <<'PY'
from pathlib import Path
import json
import os

build = Path(os.environ["SILERO_BUILD"]) / "zephyr"
tools = Path(os.environ["ALIF_SE_TOOLS_DIR"])
output = Path(os.environ["SILERO_RUN_DIR"])
values = dict(
    line.split("=", 1)
    for line in (build / ".config").read_text().splitlines()
    if line.startswith("CONFIG_") and "=" in line
)
assert values.get("CONFIG_RTSS_HP") == "y", "Build must target HP"
mode = os.environ["SILERO_MODE"]
assert mode in ("validation", "live"), "Select validation or live"
assert (values.get("CONFIG_SILERO_LIVE_AUDIO") == "y") == (mode == "live"), \
    "Selected mode does not match the built firmware"
address = int(values["CONFIG_FLASH_BASE_ADDRESS"], 0) + int(
    values["CONFIG_FLASH_LOAD_OFFSET"], 0
)
assert address == 0x80200000, f"Unexpected HP firmware address: {address:#x}"
configuration = json.loads(Path(os.environ["ALIF_APP_CONFIG"]).read_text())
hp = configuration["HP_APP"]
assert hp["cpu_id"] == "M55_HP" and hp.get("signed") is True
hp.update(disabled=False, binary="silero-vad-hp.bin", mramAddress=hex(address))
hp["flags"] = ["boot"]
hp.pop("loadAddress", None)
image = (build / "zephyr.bin").read_bytes()
padding = (-len(image)) % 16
(tools / "build/images" / hp["binary"]).write_bytes(image + bytes(padding))
(output / "silero-vad-hp.json").write_text(json.dumps(configuration, indent=4) + "\n")
print(f"Firmware: {len(image)} bytes + {padding} zero padding bytes at {address:#x}")
PY
```

The two source builds have different identities:

| Configuration | Raw binary | Zero padding | Staged binary SHA256 |
| --- | --- | --- | --- |
| Validation | 846,396 bytes | 4 bytes | `1af2578fbb100d1c18a1a30371b49e27c984a7b712309cc1f06ff398bf1d4a73` |
| Live | 690,312 bytes | 8 bytes | `e594f0f853e04cd795a4aaa10ceb71c4f5d23335dd226a09510dc4eaf307e31e` |

The live staged image is 690,320 bytes. The command computes padding for your build before signing. Build paths and metadata can change later hashes; record your own raw and staged identities. Never pad or modify an image after signing.

Review the generated JSON. Only its HP entry should differ from the known working template. It must use `M55_HP`, `silero-vad-hp.bin`, MRAM address `0x80200000`, and the `boot` flag. Changing this JSON cannot relocate linked firmware.

Generate the signed package and snapshot the exact staged firmware, package, and map:

```bash
unset MRAM_RUN
cp "$SILERO_RUN_DIR/silero-vad-hp.json" \
  "$ALIF_SE_TOOLS_DIR/build/config/silero-vad-hp.json" &&
(
cd "$ALIF_SE_TOOLS_DIR" || exit
set -o pipefail
./app-gen-toc -f build/config/silero-vad-hp.json \
  2>&1 | tee "$SILERO_RUN_DIR/silero-gen-toc.log"
) &&
python "$MRAM_HELPER" prepare \
  --config "$SILERO_BUILD/zephyr/.config" \
  --firmware "$ALIF_SE_TOOLS_DIR/build/images/silero-vad-hp.bin" \
  --package "$ALIF_SE_TOOLS_DIR/build/AppTocPackage.bin" \
  --package-map "$ALIF_SE_TOOLS_DIR/build/app-package-map.txt" \
  --app-config "$SILERO_RUN_DIR/silero-vad-hp.json" \
  --programming-core "$ALIF_MRAM_CORE" \
  --output-dir "$SILERO_RUN_DIR/mram-silero" &&
export MRAM_RUN="$SILERO_RUN_DIR/mram-silero"
```

Require successful generation and helper checks before continuing. The output directory must be new or empty. Review its `manifest.json` and package map: the helper derives the AToC package address and size from **APP Package Summary**, requires 16-byte alignment, and bounds both payloads and their 16 KiB programming envelopes below `0x80580000` without overlap. It accepts the tested single signed HP-image layout; stop if your package differs.

The AToC header address is inside the package and is not its load address. Companion images, configuration, and certificates are included in the package. `AppTocPackage.bin.sign` is ISP transport authentication, not a third SWD payload. The helper checks layout and bytes; it does not authenticate signatures.

## Program and independently read back both payloads

Each invocation below starts a separate process. The first downloads with `noreset`; the second reads the physical ranges with no preceding downloads, so it cannot reuse the earlier process's flash-download cache:

```bash
(
set -e
test -n "${MRAM_RUN:-}"
device=$(python -c 'import json,sys; print(json.load(open(sys.argv[1]))["programming_device"])' \
  "$MRAM_RUN/manifest.json")
for script in 01-program.jlink 02-readback-fresh-process.jlink; do
  "$JLINK_COMMANDER" -Device "$device" -If SWD -Speed 4000 \
    -AutoConnect 1 -NoGui 1 -ExitOnError 1 \
    -CommandFile "$MRAM_RUN/$script"
done
python "$MRAM_HELPER" verify --manifest "$MRAM_RUN/manifest.json"
)
```

Require both fresh readbacks to match their prepared sizes and SHA256 hashes. This verifies those two payloads; it does not compare the rest of MRAM with the backup. A successful install still needs a completed application run.

## Capture UART4 before reset-pin boot

Use UART4 at **115200 baud, 8N1**. If changing SW4, disconnect board power first, select UART4, then reconnect PRG USB. In a second terminal, activate the same environment and set the capture location:

```bash
source "$HOME/silero-alif-e8/.venv/bin/activate"
export SILERO_OUTPUT="$HOME/silero-alif-e8/model-and-builds"
export SILERO_MODE=validation
export SILERO_RUN_DIR="$SILERO_OUTPUT/$SILERO_MODE"
python -m serial.tools.list_ports
export ALIF_CONSOLE=/dev/cu.replace-with-your-application-uart
python -u -m serial.tools.miniterm "$ALIF_CONSOLE" 115200 --raw \
  2>&1 | tee "$SILERO_RUN_DIR/alif-silero.log"
```

Adjust those paths if you chose another workspace, and set `SILERO_MODE=live` in this capture terminal when programming live mode. Each configuration writes its own `alif-silero.log`. With capture running, return to the original programming terminal and boot using a **probe-only** process:

```bash
"$JLINK_COMMANDER" -AutoConnect 0 -NoGui 1 -ExitOnError 1 \
  -CommandFile "$MRAM_RUN/03-reset-probe-only.jlink"
```

That script pulses `R0`, waits 200 ms, sets `R1`, and waits 2,500 ms. It must not connect a CPU or issue generic `r`: the reset-pin pulse lets the Security Enclave boot the newly signed package. See [SEGGER Commander commands](https://kb.segger.com/J-Link_Commander).

For validation, wait for all 79 `PROB` lines and `Model executed successfully.`; the display then replays cached results. For live mode, require the microphone startup message and advancing `LIVE frame=...` diagnostics while speaking and pausing. Live mode has no final completion message. Exit the capture terminal with **Ctrl+]** after the checks in the validation lesson. Keep one reset per log, retain all display/capture/delegate faults, and use a fresh log before another reset. SW4 can remain on UART4 for later SWD programming; return it to SEUART only for SETOOLS ISP.

## What you've accomplished

You have preserved the boot configuration, installed the embedded-model HP firmware through SWD, independently verified both MRAM payloads, and captured a fresh application run. Next, compare the validation image's 79 probabilities with the host reference, then repeat this procedure with live mode and check the microphone pipeline.
