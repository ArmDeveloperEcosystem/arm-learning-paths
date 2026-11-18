#!/usr/bin/env python3
"""Prepare and verify files offline for the tested E8 A0 HP SWD procedure."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil


APP_START = 0x80000000
APP_END = 0x80580000
HP_ADDRESS = 0x80200000
SECTOR_SIZE = 0x4000


def one_match(pattern, text, label):
    matches = re.findall(pattern, text, re.MULTILINE)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one {label}; found {len(matches)}")
    return matches[0]


def file_info(path, address):
    path = path.resolve(strict=True)
    data = path.read_bytes()
    size = len(data)
    end = address + size
    sector_start = address // SECTOR_SIZE * SECTOR_SIZE
    sector_end = (end + SECTOR_SIZE - 1) // SECTOR_SIZE * SECTOR_SIZE
    if not size or address % 16 or size % 16:
        raise ValueError(f"{path.name}: address and nonzero size must be 16-byte aligned")
    if not APP_START <= sector_start < sector_end <= APP_END:
        raise ValueError(f"{path.name}: programming envelope exceeds E8 application MRAM")
    return {
        "source": str(path),
        "address": hex(address),
        "size": size,
        "end_exclusive": hex(end),
        "sector_start": hex(sector_start),
        "sector_end_exclusive": hex(sector_end),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def prepare(args):
    config = args.config.read_text()
    board_target = one_match(r'^CONFIG_BOARD_TARGET="([^"]+)"$', config, "board target")
    if (board_target != "alif_e8_dk/ae822fa0e5597xx0/rtss_hp"
            or not re.search(r"^CONFIG_SOC_AE822FA0E5597XX0_RTSS_HP=y$", config, re.MULTILINE)):
        raise ValueError("This procedure requires an E8 DK AE822FA0 HP build")
    values = [
        int(one_match(rf"^{key}=(0x[0-9a-fA-F]+|[0-9]+)$", config, key), 0)
        for key in ("CONFIG_FLASH_BASE_ADDRESS", "CONFIG_FLASH_LOAD_OFFSET")
    ]
    address = sum(values)
    if values[0] != APP_START or address != HP_ADDRESS:
        raise ValueError("This procedure requires E8 A0 HP firmware linked at 0x80200000")

    package_map = args.package_map.read_text()
    before_summary, separator, summary = package_map.partition("APP Package Summary:")
    if not separator:
        raise ValueError("Missing vendor APP Package Summary")
    user_section = before_summary.split("User managed MRAM locations", 1)
    if len(user_section) != 2:
        raise ValueError("Missing user-managed image section")
    user_section = user_section[1].split("APP Package Start Address", 1)[0]
    row = one_match(
        r"^(0x[0-9a-fA-F]+)\s+(0x[0-9a-fA-F]+)\s+([0-9]+)\s+(\S+)\s+(.+?)\s*$",
        user_section,
        "user-managed image",
    )
    image_address, hex_size, decimal_size, signing, filename = row
    if signing != "signed" or filename != args.firmware.name:
        raise ValueError("Firmware basename must match the sole signed user-managed image")
    if int(image_address, 0) != address or int(hex_size, 0) != int(decimal_size):
        raise ValueError("User-managed image address or size disagrees with the build/map")

    package_address = int(one_match(
        r"^\s*- APP Package Start Address:\s*(0x[0-9a-fA-F]+)\s*$",
        summary, "package start address",
    ), 0)
    package_size = int(one_match(
        r"^\s*- APP Package total size:\s*([0-9]+) bytes\s*$",
        summary, "package size",
    ))
    firmware = file_info(args.firmware, address)
    package = file_info(args.package, package_address)
    if firmware["size"] != int(decimal_size) or package["size"] != package_size:
        raise ValueError("Actual staged file sizes disagree with the vendor map")
    if int(package["end_exclusive"], 0) != APP_END:
        raise ValueError("Signed package must end exactly at 0x80580000")
    if int(firmware["sector_end_exclusive"], 0) > int(package["sector_start"], 0):
        raise ValueError("Firmware and package programming envelopes overlap")
    if args.firmware.suffix != ".bin" or args.firmware.name.casefold() in {
        "apptocpackage.bin", "firmware-readback.bin", "package-readback.bin"
    }:
        raise ValueError("Firmware must be a .bin image with a non-reserved basename")

    if args.app_config:
        hp = json.loads(args.app_config.read_text())["HP_APP"]
        if (hp.get("disabled", False) or hp.get("signed") is not True
                or hp.get("binary") != filename or hp.get("cpu_id") != "M55_HP"
                or int(hp.get("mramAddress", "0"), 0) != address
                or hp.get("flags") != ["boot"]):
            raise ValueError("HP_APP configuration disagrees with this MRAM boot procedure")

    output = args.output_dir.resolve()
    for path in (output, args.firmware.resolve(), args.package.resolve()):
        if any(character in str(path) for character in ('"', '\r', '\n')):
            raise ValueError("J-Link paths cannot contain quotes or newlines")
    if output.exists() and any(output.iterdir()):
        raise ValueError("Output directory must be new or empty; preserve previous evidence")
    output.mkdir(parents=True, exist_ok=True)
    for name, record, snapshot_name in (
        ("firmware", firmware, filename), ("package", package, "AppTocPackage.bin")
    ):
        snapshot = output / snapshot_name
        shutil.copyfile(record["source"], snapshot)
        if hashlib.sha256(snapshot.read_bytes()).hexdigest() != record["sha256"]:
            raise ValueError(f"{name} changed while preparing its snapshot; start again")
        record["file"] = str(snapshot)
        record["readback"] = str(output / f"{name}-readback.bin")
    shutil.copyfile(args.config, output / "build.config")
    shutil.copyfile(args.package_map, output / "app-package-map.txt")
    if args.app_config:
        shutil.copyfile(args.app_config, output / "app-config.json")

    records = (firmware, package)
    (output / "01-program.jlink").write_text("H\nSleep 1000\n" + "".join(
        f'LoadFile "{item["file"]}" {item["address"]} noreset\n' for item in records
    ) + "Exit\n")
    (output / "02-readback-fresh-process.jlink").write_text("H\n" + "".join(
        f'SaveBin "{item["readback"]}" {item["address"]} {hex(item["size"])}\n'
        for item in records
    ) + "Exit\n")
    (output / "03-reset-probe-only.jlink").write_text(
        "R0\nSleep 200\nR1\nSleep 2500\nExit\n"
    )
    manifest = {
        "schema_version": 2,
        "device": "AE822FA0E5597LS0_M55_HP",
        "image_boot_device": "AE822FA0E5597LS0_M55_HP",
        "programming_core": args.programming_core,
        "programming_device": f"AE822FA0E5597LS0_M55_{args.programming_core}",
        "board_target": board_target,
        "interface": "SWD",
        "speed_khz": 4000,
        "application_mram": {"start": hex(APP_START), "end_exclusive": hex(APP_END)},
        "observed_sector_size": SECTOR_SIZE,
        "firmware": firmware,
        "package": package,
        "procedure": [
            f"Run 01 in a named {args.programming_core} connection; close Commander afterwards.",
            f"Run 02 in a NEW named {args.programming_core} connection with no preceding downloads; close it.",
            "Run offline verify and require both physical readbacks to match.",
            "Run 03 in a NEW probe-only process with AutoConnect 0; never connect a CPU there.",
            "Open a NEW named HP connection after the pin pulse to check actual boot.",
        ],
        "scope": "Offline range/name/hash checks; vendor-generated signatures are not authenticated here.",
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Prepared {output / 'manifest.json'}; no debugger was launched")


def verify(args):
    manifest = json.loads(args.manifest.read_text())
    results = {}
    for name in ("firmware", "package"):
        item = manifest[name]
        for path in (Path(item["file"]), Path(item["readback"])):
            data = path.read_bytes()
            if len(data) != item["size"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
                raise ValueError(f"{name}: size/SHA-256 mismatch in {path}")
        results[name] = {"readback": item["readback"], "sha256": item["sha256"], "match": True}
    print(json.dumps(results, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    setup = commands.add_parser("prepare", help="Validate inputs and emit command fragments offline")
    for flag in ("config", "firmware", "package", "package-map", "output-dir"):
        setup.add_argument(f"--{flag}", type=Path, required=True)
    setup.add_argument("--app-config", type=Path, help="Optional matching vendor HP_APP JSON")
    setup.add_argument(
        "--programming-core", choices=("HP", "HE"), default="HP",
        help="Core used for MRAM debug access; the signed application still boots HP",
    )
    check = commands.add_parser("verify", help="Compare fresh target readbacks with prepared hashes")
    check.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            prepare(args)
        else:
            verify(args)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
