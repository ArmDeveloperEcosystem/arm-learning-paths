---
title: Program the external model and final firmware
description: Program and verify the model in external OSPI flash, then install the matching live camera application.
weight: 6
layout: learningpathall
---

## Program OSPI through the board-side writer

The final live model is stored separately from firmware in external OSPI flash. The generic J-Link flash loader failed when programming this 13,293,120-byte artifact, so this lesson uses the board-side flash writer that completed the transfer.

The writer is a small Zephyr application that writes OSPI through the board's flash driver. J-Link stages 64 KiB chunks in RAM; the writer validates each chunk's CRC, writes it, then reads flash back and compares bytes.

This chapter writes the model region beginning at external OSPI offset zero, mapped at `0xC0000000`, and replaces the application firmware. Use the E8 and memory layout described here, and retain any existing data you need from that region before programming.

## Build and flash the recovery writer

Download the [OSPI writer source](../ospi-writer.zip), save it as `$ALIF_WORK/ospi-writer.zip`, and extract it once:

```bash
unzip "$ALIF_WORK/ospi-writer.zip" -d "$ALIF_WORK"
export RECOVERY_SOURCE="$ALIF_WORK/ospi-writer"
```

With the prepared workspace active, build the writer using the pinned OSPI overlay:

```bash
west build \
  -d "$MOBILE_SAM_OUTPUT/build-ospi-writer" \
  -p always \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  "$RECOVERY_SOURCE" -- \
  -DEXTRA_DTC_OVERLAY_FILE="$SDK_ALIF/snippets/ospi-flash/e8_ospi1.overlay"

west flash -d "$MOBILE_SAM_OUTPUT/build-ospi-writer" \
  --runner alif_flash -- \
  --device "$ALIF_DEVICE" \
  --commander "$JLINK_COMMANDER"
```

Let the writer boot. Its mailbox at `0x20080000` should contain magic `4F535049`, protocol version `00000001`, and ready status `52454144`. The transfer staging buffer begins at `0x20081000`. These addresses belong to this recovery firmware; they are not model addresses and must not be reused with an unrelated running application.

The script checks the mailbox before transferring. If it is unavailable, establish that the writer firmware is running before retrying.

## Check the host script requirements

The supplied script reads `JLINK_COMMANDER` from your environment, targets the E8 HP device selected earlier, and uses `/usr/bin/python3` for CRC32 calculation. Its J-Link path is the only change from the script used for the reference deployment. Confirm that the configured executable and system Python are available before transferring. This engineering utility is specific to this E8 memory layout.

## Transfer and verify the model

Close other J-Link sessions and run a normal first transfer, including erase:

```bash
expect "$RECOVERY_SOURCE/flash_model.expect" \
  "$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.bin"
```

For the validated 13,293,120-byte artifact, the output is:

```output
Model programmed and verified: 13293120 bytes
```

Your freshly exported file may have a different size. Require successful completion for the full file, with no writer CRC, flash-readback, mailbox, or timeout error. The script rounds erase length to 4 KiB sectors, then sends and verifies chunks of up to 64 KiB.

The script supports `--skip-erase` for recovery after a confirmed completed erase. Use the normal command above for a fresh transfer. An interrupted write needs its erase/write state understood before any resume attempt.

## Install the live application

After model programming completes, flash the live application built with that same PTE and metadata:

```bash
west flash -d "$MOBILE_SAM_OUTPUT/build-mobilesam-live" \
  --runner alif_flash -- \
  --device "$ALIF_DEVICE" \
  --commander "$JLINK_COMMANDER"
```

Power-cycle the board, retaining SW4 on SEUART, and continue to live validation.

The writer replaces the running OSPI-consuming application before modifying model storage. The earlier direct-J-Link approach used a separately flashed idle `hello_world` for the same controller-ownership reason. Do not write model flash while the live application is still reading or executing through its OSPI mapping.

When only firmware changes and the PTE is unchanged, the external model does not need reprogramming. When the PTE changes, program its complete new contents and rebuild firmware with its matching metadata and size.

## What you've accomplished

You have programmed and verified the complete model separately from the matching application firmware. Next, verify that camera capture, model execution, and mask rendering all advance on the board.
