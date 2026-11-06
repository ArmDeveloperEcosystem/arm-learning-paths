---
title: Program the Silero firmware on the E8 HP core
description: Generate an application image configuration and program the firmware, embedded model, and audio into E8 MRAM.
weight: 6
layout: learningpathall
---

## Check the firmware and programming connection

The firmware contains both the PTE and validation audio. Program the single `zephyr.bin` produced by the previous lesson into MRAM. Rebuild and reprogram that firmware whenever you change the model or embedded recording.

Connect the board's **PRG USB** port with a data-capable cable. For programming, leave **SW4 on SEUART** and close any terminal using the Security Toolkit's serial port. Use the Security Toolkit configured for your E8 silicon revision, with the device configuration and boot images already established in the setup lesson.

Check the paths from your active shell:

```bash
test -s "$SILERO_BUILD/zephyr/zephyr.bin"
test -s "$SILERO_BUILD/zephyr/zephyr.elf"
test -x "$ALIF_SE_TOOLS_DIR/app-gen-toc"
test -x "$ALIF_SE_TOOLS_DIR/app-write-mram"
```

The pinned HP board configuration places the Zephyr application at **`0x80200000`**: MRAM base `0x80000000` plus flash load offset `0x200000`. This is the Zephyr HP partition used here. The address must agree with your generated build configuration and linker layout.

## Preserve the existing boot configuration

The Security Toolkit generates an application table of contents (AToC) from a JSON configuration. Start with the configuration already used by your working E8 boot setup. Keep its device configuration, AP images, HE images, signing options, and clock settings. This lesson changes only the HP application entry.

The standard Zephyr runner uses `build/config/app-cpu-stubs.json` as its template. Use that file only after confirming that its device configuration and companion images match your E8. If your working setup uses a different application configuration, set `ALIF_APP_CONFIG` to that file instead.

Save a copy of the toolkit configuration and stage the new binary under a distinct name:

```bash
export ALIF_APP_CONFIG="$ALIF_SE_TOOLS_DIR/build/config/app-cpu-stubs.json"

test -s "$ALIF_APP_CONFIG"
tar -czf "$SILERO_OUTPUT/setools-config-before-silero.tar.gz" \
  -C "$ALIF_SE_TOOLS_DIR" build/config
cp "$SILERO_BUILD/zephyr/zephyr.bin" \
  "$ALIF_SE_TOOLS_DIR/build/images/silero-vad-hp.bin"
```

The next command reads that template, checks the build's HP flash address, and writes a separate application configuration. It leaves the original template unchanged:

```bash
python - "$SILERO_BUILD/zephyr/.config" "$ALIF_APP_CONFIG" \
  "$SILERO_OUTPUT/silero-vad-hp.json" <<'PY'
from pathlib import Path
import json
import sys

build_config, template, destination = map(Path, sys.argv[1:])
values = dict(
    line.split("=", 1)
    for line in build_config.read_text().splitlines()
    if line.startswith("CONFIG_") and "=" in line
)
assert values.get("CONFIG_RTSS_HP") == "y", "Build must target the HP core"
address = int(values["CONFIG_FLASH_BASE_ADDRESS"], 0) + int(
    values["CONFIG_FLASH_LOAD_OFFSET"], 0
)
assert address == 0x80200000, f"Unexpected HP flash address: {address:#x}"

configuration = json.loads(template.read_text())
hp = configuration["HP_APP"]
assert hp["cpu_id"] == "M55_HP", "Template must contain the HP application"
hp["disabled"] = False
hp["binary"] = "silero-vad-hp.bin"
hp["mramAddress"] = hex(address)
hp["flags"] = ["boot"]
hp.pop("loadAddress", None)
destination.write_text(json.dumps(configuration, indent=4) + "\n")
print(json.dumps(hp, indent=2))
PY
```

Review the printed HP entry. It must select `M55_HP`, name `silero-vad-hp.bin`, use `mramAddress` of `0x80200000`, and contain the `boot` flag. MRAM execution uses `mramAddress`; the template's SRAM `loadAddress` and `load` flag must be absent from this entry.

Review the complete new JSON before generating images. Its other entries should match the known working template, and every referenced binary must remain available in the toolkit's `build/images` directory. Keep the existing Security Enclave table of contents (SETOC) and device clock configuration; this application update does not require replacing them.

## Generate and program the application image

Run the toolkit from its installation directory so it finds its configuration and image files:

```bash
cd "$ALIF_SE_TOOLS_DIR"
./app-gen-toc -f "$SILERO_OUTPUT/silero-vad-hp.json"
./app-write-mram -p
cd "$EXECUTORCH_ROOT"
```

Select the E8's SEUART programming port when prompted. Require successful image generation and MRAM programming with no device-revision, image, authentication, or serial-port errors. Programming success establishes that the image was transferred; the next lesson checks model execution and output agreement.

## Capture the application console

The pinned E8 HP device tree selects **UART4 at 115200 baud, 8N1** for the Zephyr console. The E8 DevKit routes its onboard USB-to-UART bridge between SEUART, UART2, and UART4 using SW4. It uses the same PRG USB connection for programming and application logging; no separate serial adapter is needed.

After programming completes, disconnect board power, move **SW4 from SEUART to UART4**, and reconnect PRG USB. Rediscover the host serial device, then set `ALIF_CONSOLE` to that device. PySerial is installed by the Zephyr requirements; use its terminal to capture one run:

```bash
python -m serial.tools.list_ports
export ALIF_CONSOLE=/dev/cu.replace-with-your-application-uart
python -u -m serial.tools.miniterm "$ALIF_CONSOLE" 115200 --raw \
  2>&1 | tee "$SILERO_OUTPUT/alif-silero.log"
```

Start capture first, then press the board’s **RESET** button to begin a fresh run. Wait for all probability lines and `Model executed successfully.` before exiting the terminal with **Ctrl+]**. Keep one run per log file. If the application reports an error or the console remains silent, preserve that log and diagnose the failed stage before retrying the probability comparison.

Before any later programming operation, close the terminal, disconnect board power, return **SW4 to SEUART**, and reconnect PRG USB. SETOOLS cannot communicate with the Secure Enclave while the bridge is routed to UART4.

## What you've accomplished

After completing these steps, you have programmed the HP firmware with its embedded model and audio while retaining the E8's other boot-image and device settings. You have also captured a complete application run for validation.

Next, compare its 79 speech probabilities with the matching quantized host reference.
