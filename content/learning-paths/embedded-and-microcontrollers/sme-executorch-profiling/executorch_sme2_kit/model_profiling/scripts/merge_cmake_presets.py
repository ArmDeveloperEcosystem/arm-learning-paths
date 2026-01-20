#!/usr/bin/env python3
"""
Merge SME2 profiling CMake presets into ExecuTorch's CMakePresets.json.

This script:
1. Reads ExecuTorch's default CMakePresets.json
2. Reads our SME2 profiling presets (from assets/)
3. Merges them, with our presets taking precedence for duplicates
4. Writes the merged result back to ExecuTorch's CMakePresets.json
"""

import json
import sys
from pathlib import Path


def merge_presets(base_presets: list, new_presets: list, preset_type: str) -> list:
    """
    Merge two preset lists, with new_presets taking precedence for duplicates.
    
    Args:
        base_presets: Base preset list (from ExecuTorch)
        new_presets: New preset list (from our assets)
        preset_type: "configurePresets" or "buildPresets" (for error messages)
    
    Returns:
        Merged preset list
    """
    # Create a map of name -> preset for quick lookup
    preset_map = {p["name"]: p for p in base_presets}
    
    # Overwrite/add new presets
    for new_preset in new_presets:
        name = new_preset["name"]
        if name in preset_map:
            print(f"  [merge] Overwriting {preset_type} preset: {name}", file=sys.stderr)
        else:
            print(f"  [merge] Adding {preset_type} preset: {name}", file=sys.stderr)
        preset_map[name] = new_preset
    
    # Return as list, preserving order (base first, then new)
    result = []
    seen = set()
    
    # Add base presets first
    for preset in base_presets:
        name = preset["name"]
        if name not in seen:
            result.append(preset_map[name])
            seen.add(name)
    
    # Add new presets that weren't in base
    for preset in new_presets:
        name = preset["name"]
        if name not in seen:
            result.append(preset_map[name])
            seen.add(name)
    
    return result


def main():
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent.parent  # executorch_sme2_kit/
    executorch_dir = root_dir / "executorch"
    assets_dir = root_dir / "model_profiling" / "assets"
    
    executorch_presets_file = executorch_dir / "CMakePresets.json"
    our_presets_file = assets_dir / "cmake_presets.json"
    
    if not executorch_presets_file.exists():
        print(f"ERROR: ExecuTorch CMakePresets.json not found: {executorch_presets_file}", file=sys.stderr)
        print("  Run setup_repo.sh first to clone ExecuTorch.", file=sys.stderr)
        sys.exit(1)
    
    if not our_presets_file.exists():
        print(f"ERROR: SME2 presets not found: {our_presets_file}", file=sys.stderr)
        sys.exit(1)
    
    # Read base presets
    print(f"[merge] Reading base presets from: {executorch_presets_file}", file=sys.stderr)
    with open(executorch_presets_file, "r") as f:
        base_data = json.load(f)
    
    # Read our presets
    print(f"[merge] Reading SME2 presets from: {our_presets_file}", file=sys.stderr)
    with open(our_presets_file, "r") as f:
        our_data = json.load(f)
    
    # Merge configurePresets
    if "configurePresets" in our_data:
        base_data["configurePresets"] = merge_presets(
            base_data.get("configurePresets", []),
            our_data["configurePresets"],
            "configurePresets"
        )
    
    # Merge buildPresets
    if "buildPresets" in our_data:
        base_data["buildPresets"] = merge_presets(
            base_data.get("buildPresets", []),
            our_data["buildPresets"],
            "buildPresets"
        )
    
    # Write merged result
    print(f"[merge] Writing merged presets to: {executorch_presets_file}", file=sys.stderr)
    with open(executorch_presets_file, "w") as f:
        json.dump(base_data, f, indent=2)
    
    print(f"[merge] ✓ Successfully merged CMake presets", file=sys.stderr)


if __name__ == "__main__":
    main()
