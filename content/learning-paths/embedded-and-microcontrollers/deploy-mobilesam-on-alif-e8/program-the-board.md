---
title: Program the external model and final firmware
description: Preserve the E8 boot configuration, verify the model in OSPI flash, and install its matching live-camera firmware.
weight: 6
layout: learningpathall
---

## Use the tested A0 programming route

This lesson uses J-Link SWD to install two MRAM payloads: the HP firmware and its signed Alif application table-of-contents package (AToC). The board-side writer then programs the separate model in external OSPI flash at `0xC0000000`.

Writer installation, fresh MRAM readback, reset-pin boot, and the complete public-model transfer were exercised on the original E8 A0 board. A replacement A0 board also passed writer installation and fresh readback through its HE debug connection, then booted the HP writer. The default camera-and-UART firmware passed fresh payload readbacks and two independent reset-pin runtime checks; the validation lesson gives their scope. This procedure targets an HP image for `AE822FA0E5597LS0`; other silicon revisions need separate validation.

Retain data you need from application MRAM and the model's OSPI region before replacing them. Close other debugger sessions. SW4 selects the UART bridge, not SWD: use UART4 for the HP console or SEUART for SETOOLS ISP. Installed SETOOLS rejects `Interface=jtag`, and the pinned `west flash` runner uses ISP; neither command selects the SWD procedure below.

## Build the writer and download the preparation helper

Download the [OSPI writer source](../ospi-writer.zip) and [MRAM preparation helper](../prepare_mram_programming.py), saving both in `$ALIF_WORK`. Check the helper's SHA256 with `shasum -a 256`; it must be:

```output
3aab6ca07ae2249609bcfc342c4aa2d17560d3fe99441f6cab2fef8c5bdd5614
```

```bash
unzip "$ALIF_WORK/ospi-writer.zip" -d "$ALIF_WORK"
export RECOVERY_SOURCE="$ALIF_WORK/ospi-writer"
export MRAM_HELPER="$ALIF_WORK/prepare_mram_programming.py"
west build \
  -d "$MOBILE_SAM_OUTPUT/build-ospi-writer" \
  -p always \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  "$RECOVERY_SOURCE" -- \
  -DEXTRA_DTC_OVERLAY_FILE="$SDK_ALIF/snippets/ospi-flash/e8_ospi1.overlay"
```

The writer stages 64 KiB chunks in RAM, checks their CRC, writes OSPI through the board's flash driver, then reads flash back and compares bytes. The generic J-Link OSPI loader failed with the original large live model, so use this writer for model transfer.

## Select the probe and back up application MRAM

List attached probes, then replace the serial placeholder with your intended board's numeric J-Link serial number. This is not the `/dev/cu.usbmodem...` UART path. The executable wrapper passes that serial to every J-Link invocation, including the writer's Expect script:

```bash
export JLINK_EXECUTABLE="${JLINK_EXECUTABLE:-$JLINK_COMMANDER}"
printf 'ShowEmuList USB\nExit\n' > "$MOBILE_SAM_OUTPUT/list-probes.jlink"
"$JLINK_EXECUTABLE" -AutoConnect 0 -NoGui 1 \
  -CommandFile "$MOBILE_SAM_OUTPUT/list-probes.jlink"
export JLINK_SERIAL=REPLACE_WITH_YOUR_PROBE_SERIAL
cat > "$MOBILE_SAM_OUTPUT/jlink-selected" <<'SH'
#!/bin/sh
case "$JLINK_SERIAL" in
  ''|*[!0-9]*) echo 'Set the numeric JLINK_SERIAL' >&2; exit 2;;
esac
exec "$JLINK_EXECUTABLE" -USB "$JLINK_SERIAL" "$@"
SH
chmod +x "$MOBILE_SAM_OUTPUT/jlink-selected"
export JLINK_COMMANDER="$MOBILE_SAM_OUTPUT/jlink-selected"
```

Keep the wrapper and its exported variables active for the rest of this Learning Path. `JLINK_EXECUTABLE` must name the actual SEGGER binary, never the wrapper. After switching boards, select that board's serial again. The writer script hardcodes the tested A0 HP device; changing `ALIF_DEVICE` does not retarget this writer script.

Start with HP for MRAM access. Check that the selected core can read application MRAM before preparing or programming any payload:

```bash
export ALIF_MRAM_CORE=HP
export ALIF_MRAM_DEVICE=AE822FA0E5597LS0_M55_HP
printf 'H\nMem32 0x80000000 4\nG\nExit\n' \
  > "$MOBILE_SAM_OUTPUT/check-mram-access.jlink"
"$JLINK_COMMANDER" -Device "$ALIF_MRAM_DEVICE" -If SWD -Speed 4000 \
  -AutoConnect 1 -NoGui 1 -ExitOnError 1 \
  -CommandFile "$MOBILE_SAM_OUTPUT/check-mram-access.jlink"
```

If HP reports no AHB ROM and cannot connect, try the tested HE fallback by setting `ALIF_MRAM_CORE=HE` and `ALIF_MRAM_DEVICE=AE822FA0E5597LS0_M55_HE`, then rerun the access check. Continue only if that fresh HE connection reads MRAM successfully. Keep `ALIF_DEVICE=AE822FA0E5597LS0_M55_HP`: the signed image and writer boot on HP regardless of which core provides MRAM access. Stop if neither core is readable.

Before the first download, save the A0 application-MRAM region `[0x80000000, 0x80580000)` in a fresh process:

```bash
(
set -e
test ! -e "$MOBILE_SAM_OUTPUT/application-mram-before.bin"
cat > "$MOBILE_SAM_OUTPUT/backup-mram.jlink" <<EOF
H
SaveBin "$MOBILE_SAM_OUTPUT/application-mram-before.bin" 0x80000000 0x580000
G
Exit
EOF
"$JLINK_COMMANDER" -Device "$ALIF_MRAM_DEVICE" -If SWD -Speed 4000 \
  -AutoConnect 1 -NoGui 1 -ExitOnError 1 \
  -CommandFile "$MOBILE_SAM_OUTPUT/backup-mram.jlink"
python - <<'PY'
from pathlib import Path
import os
backup = Path(os.environ["MOBILE_SAM_OUTPUT"]) / "application-mram-before.bin"
assert backup.stat().st_size == 0x580000, "Incomplete application-MRAM backup"
PY
shasum -a 256 "$MOBILE_SAM_OUTPUT/application-mram-before.bin"
)
```

Retain the backup and hash; use a new output workspace rather than overwrite it. Stop if the selected debug connection or read fails; this route assumes debug access is provisioned for the board. It does not update Security Enclave firmware or system MRAM.

## Preserve the boot configuration and sign the staged images

Use `ALIF_APP_CONFIG` as the known working template for this A0 board. Preserve its device configuration, AP and HE images, signing keys/options, clocks, and companion binaries. Back it up before creating separate writer and live configurations:

```bash
test -x "$ALIF_SE_TOOLS_DIR/app-gen-toc"
test -s "$ALIF_APP_CONFIG"
tar -czf "$MOBILE_SAM_OUTPUT/setools-config-before-mobilesam.tar.gz" \
  -C "$ALIF_SE_TOOLS_DIR" build/config
python - <<'PY'
from pathlib import Path
import json
import os

output = Path(os.environ["MOBILE_SAM_OUTPUT"])
tools = Path(os.environ["ALIF_SE_TOOLS_DIR"])
template = Path(os.environ["ALIF_APP_CONFIG"])
for name, build_name in (
    ("ospi-writer-hp", "build-ospi-writer"),
    ("mobilesam-live-hp", "build-mobilesam-live"),
):
    build = output / build_name / "zephyr"
    values = dict(
        line.split("=", 1)
        for line in (build / ".config").read_text().splitlines()
        if line.startswith("CONFIG_") and "=" in line
    )
    assert values.get("CONFIG_RTSS_HP") == "y", "Build must target HP"
    address = int(values["CONFIG_FLASH_BASE_ADDRESS"], 0) + int(
        values["CONFIG_FLASH_LOAD_OFFSET"], 0
    )
    assert address == 0x80200000, f"Unexpected HP firmware address: {address:#x}"
    configuration = json.loads(template.read_text())
    hp = configuration["HP_APP"]
    assert hp["cpu_id"] == "M55_HP" and hp.get("signed") is True
    hp.update(disabled=False, binary=f"{name}.bin", mramAddress=hex(address))
    hp["flags"] = ["boot"]
    hp.pop("loadAddress", None)
    image = (build / "zephyr.bin").read_bytes()
    padding = (-len(image)) % 16
    (tools / "build/images" / hp["binary"]).write_bytes(image + bytes(padding))
    (output / f"{name}.json").write_text(json.dumps(configuration, indent=4) + "\n")
    print(f"{name}: {len(image)} bytes + {padding} padding bytes at {address:#x}")
PY
```

The writer build is 49,580 bytes; staging adds **four zero bytes before signing**, making 49,584 bytes. The default camera-and-UART build is **171,192 bytes**; staging adds **eight zero bytes**, giving 171,200 bytes with SHA256 `6d782da186b607a815f7b4d3e4bed8dd0bb6bc1d6ca8c1a630fed4120472e25a`. The command computes each build's padding independently. Paths and build metadata can change later hashes; record your own artifacts. Program the staged image described by its package, and never modify an image after signing.

Review both JSON files: only their HP entries should differ from your template. The linked firmware address is `.config`'s MRAM base `0x80000000` plus load offset `0x200000`, giving **`0x80200000`**. Changing JSON alone cannot relocate the firmware.

Define the following reusable preparation function, then prepare the writer package. It invokes SETOOLS only to generate signatures and AToC, then snapshots that exact firmware/package pair:

```bash
prepare_mram_package() {
  local name="$1" build_name="$2"
  local run="$MOBILE_SAM_OUTPUT/mram-$name"
  unset MRAM_RUN
  cp "$MOBILE_SAM_OUTPUT/$name.json" \
    "$ALIF_SE_TOOLS_DIR/build/config/$name.json" || return
  (
    cd "$ALIF_SE_TOOLS_DIR" || return
    set -o pipefail
    ./app-gen-toc -f "build/config/$name.json" \
      2>&1 | tee "$MOBILE_SAM_OUTPUT/$name-gen-toc.log"
  ) || return
  python "$MRAM_HELPER" prepare \
    --config "$MOBILE_SAM_OUTPUT/$build_name/zephyr/.config" \
    --firmware "$ALIF_SE_TOOLS_DIR/build/images/$name.bin" \
    --package "$ALIF_SE_TOOLS_DIR/build/AppTocPackage.bin" \
    --package-map "$ALIF_SE_TOOLS_DIR/build/app-package-map.txt" \
    --app-config "$MOBILE_SAM_OUTPUT/$name.json" \
    --programming-core "$ALIF_MRAM_CORE" \
    --output-dir "$run" || return
  export MRAM_RUN="$run"
}
prepare_mram_package ospi-writer-hp build-ospi-writer
```

Require successful generation and helper checks. Review `$MRAM_RUN/manifest.json` and `app-package-map.txt`. The helper derives the signed package's destination and size from **APP Package Summary**, checks actual sizes and hashes, requires 16-byte alignment, and bounds both payloads and their 16 KiB programming envelopes below system MRAM at `0x80580000` without overlap. It accepts the tested single user-managed signed HP image layout; stop if your package has a different layout.

The tested writer package began at `0x8057c210`, contained 15,856 bytes, and ended at `0x80580000`. These are generated package values, not addresses to copy into another build. The AToC header at `0x8057ff50` is inside the package and is **not** its load address. Companion images, configuration, and certificates are already included in the signed package; `AppTocPackage.bin.sign` is not a third MRAM payload. The helper checks layout and bytes; it does not authenticate vendor signatures.

## Program, independently read back, and boot the writer

Define the programming function below and run it for the prepared writer. Each Commander invocation is a separate process. Downloads use `noreset`; readback occurs in a new named connection to the chosen core with no preceding downloads, so it cannot reuse the earlier process's flash-download cache:

```bash
program_prepared_mram() {
  local script device
  test -n "${MRAM_RUN:-}" && test -s "$MRAM_RUN/manifest.json" || return 1
  device=$(python -c 'import json,sys; print(json.load(open(sys.argv[1]))["programming_device"])' \
    "$MRAM_RUN/manifest.json") || return
  for script in 01-program.jlink 02-readback-fresh-process.jlink; do
    "$JLINK_COMMANDER" -Device "$device" -If SWD -Speed 4000 \
      -AutoConnect 1 -NoGui 1 -ExitOnError 1 \
      -CommandFile "$MRAM_RUN/$script" || return
  done
  python "$MRAM_HELPER" verify --manifest "$MRAM_RUN/manifest.json" || return
  "$JLINK_COMMANDER" -AutoConnect 0 -NoGui 1 -ExitOnError 1 \
    -CommandFile "$MRAM_RUN/03-reset-probe-only.jlink"
}
program_prepared_mram
```

Require both fresh readback files to match their prepared size and SHA256. This checks the two payloads; it does not compare the rest of MRAM with your backup.

The final process is **probe-only**: `R0`, 200 ms, `R1`, then 2,500 ms. It must not connect a CPU or issue generic `r`. On the original A0 board, generic `r` reset the HP subsystem and resumed the old image; the reset-pin pulse let the Security Enclave boot the newly signed package. See [SEGGER Commander commands](https://kb.segger.com/J-Link_Commander) for `R0`/`R1` and `LoadFile ... noreset`.

Check the writer in another fresh named HP connection:

```bash
printf 'H\nRegs\nMem32 0x20080000 10\nG\nExit\n' \
  > "$MOBILE_SAM_OUTPUT/check-writer.jlink"
"$JLINK_COMMANDER" -Device "$ALIF_DEVICE" -If SWD -Speed 4000 \
  -AutoConnect 1 -NoGui 1 -ExitOnError 1 \
  -CommandFile "$MOBILE_SAM_OUTPUT/check-writer.jlink"
```

Require mailbox magic `4F535049`, version `00000001`, ready status `52454144`, and zero result before transferring. The mailbox starts at `0x20080000`; its staging buffer starts at `0x20081000`. These addresses belong to this writer. A successful debugger connection alone does not establish readiness.

## Transfer and verify the model

Keep the live application stopped while the writer owns OSPI. The transfer script uses `JLINK_COMMANDER` and `/usr/bin/python3` for CRC32 calculation:

```bash
set -o pipefail
expect "$RECOVERY_SOURCE/flash_model.expect" \
  "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.bin" \
  2>&1 | tee "$MOBILE_SAM_OUTPUT/model-programming.log"
```

The initial erase can be silent for **six minutes or longer**: this model spans 3,252 separate 4 KiB sectors, and progress appears after erase completes. Leave the process running until it reports completion or a specific error. The host polling allowance is at least ten minutes plus J-Link overhead; a silent erase alone is not a timeout.

The public model's successful transfer ends with:

```output
Model programmed and verified: 13317584 bytes
```

Require the complete file size and no CRC, flash-readback, mailbox, or timeout errors. The script then leaves HP halted. Its chunk CRC and board-side flash readback establish model-transfer integrity. Use the normal erase for a fresh transfer; `--skip-erase` is only for recovery after a confirmed completed erase, not an interrupted transfer of unknown state.

## Install the matching live application

Regenerate the live application's own signed package and repeat the same independent readback and reset-pin boot sequence:

```bash
prepare_mram_package mobilesam-live-hp build-mobilesam-live &&
program_prepared_mram
cd "$EXECUTORCH_ROOT"
```

Require helper preparation and both readbacks to pass before accepting the install. Do not reuse the writer's package or addresses for the live firmware. This signs `build-mobilesam-live`, the default build with its dashboard disabled. Check camera capture, inference, and advancing UART frame reports in the next lesson; completed programming does not establish those runtime results.

To capture the console, disconnect power, select **UART4 on SW4**, and reconnect PRG USB. Use 115200 baud, 8N1. Select SEUART again only when using SETOOLS ISP. When only firmware changes and the PTE is unchanged, model flash can be retained. When the PTE changes, program the complete new model and rebuild firmware with its matching metadata and size.

## What you've accomplished

You have preserved the boot configuration, installed the writer through SWD with fresh MRAM readbacks, programmed and verified the model, and installed its matching camera-and-UART firmware. Next, validate advancing capture and inference on the board.
