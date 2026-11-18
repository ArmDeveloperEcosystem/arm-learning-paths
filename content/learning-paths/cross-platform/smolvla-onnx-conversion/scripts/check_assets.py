#!/usr/bin/env python3
"""Verify the pinned model, source, and environment used by the Learning Path."""

from __future__ import annotations

import argparse
from importlib import metadata
import json
from pathlib import Path
import subprocess
import sys

from workspace import configure_workspace


EXPECTED = {
    "lerobot": "30da8e687a6dfc617fcd94afc367ac7071c376ce",
    "model_repo": "HuggingFaceVLA/smolvla_libero",
    "model_revision": "6721902bc4d61e50a3bfdb11dfb4cb626f05d102",
    "base_model_repo": "HuggingFaceTB/SmolVLM2-500M-Instruct",
    "base_model_revision": "7b375e1b73b11138ff12fe22c8f2822d8fe03467",
}

EXPECTED_PACKAGES = {
    "torch": "2.11.0+cpu",
    "torchvision": "0.26.0+cpu",
    "torchao": "0.18.0",
    "transformers": "5.5.4",
    "onnx": "1.22.0",
    "onnxruntime": "1.29.0",
}

POLICY_FILES = (
    "config.json",
    "model.safetensors",
    "policy_preprocessor.json",
    "policy_preprocessor_step_5_normalizer_processor.safetensors",
    "policy_postprocessor.json",
    "policy_postprocessor_step_1_unnormalizer_processor.safetensors",
)
BASE_MODEL_FILES = ("config.json", "model.safetensors", "tokenizer.json")


def verify_snapshot(root: Path, files: tuple[str, ...], revision: str) -> None:
    """Verify required snapshot files and their Hugging Face revisions."""

    for relative in files:
        asset = root / relative
        metadata_file = root / ".cache/huggingface/download" / f"{relative}.metadata"
        if not asset.is_file():
            raise FileNotFoundError(f"Missing public asset: {asset}")
        if not metadata_file.is_file():
            raise FileNotFoundError(f"Missing Hugging Face metadata: {metadata_file}")
        lines = metadata_file.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != revision:
            raise RuntimeError(f"Unexpected Hugging Face revision for {asset}")


def verify_environment(work_root: Path) -> None:
    """Verify the Python version, pinned packages, and environment manifest."""

    if sys.version_info[:2] != (3, 12):
        raise RuntimeError("Python 3.12 is required")
    environment = work_root / "environment.freeze.txt"
    if not environment.is_file():
        raise FileNotFoundError(f"Missing environment manifest: {environment}")

    for package, expected in EXPECTED_PACKAGES.items():
        actual = metadata.version(package)
        if actual != expected:
            raise RuntimeError(f"Unexpected {package} version: {actual}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-root", type=Path)
    args = parser.parse_args()
    work_root = configure_workspace(args.work_root)

    revisions_path = work_root / "revisions.json"
    revisions = json.loads(revisions_path.read_text(encoding="utf-8"))
    if revisions != EXPECTED:
        raise RuntimeError(f"Revision manifest does not match the Learning Path: {revisions_path}")

    actual_lerobot = subprocess.check_output(
        ["git", "-C", str(work_root / "lerobot"), "rev-parse", "HEAD"],
        text=True,
    ).strip()
    if actual_lerobot != EXPECTED["lerobot"]:
        raise RuntimeError(f"Unexpected LeRobot revision: {actual_lerobot}")
    lerobot_status = subprocess.check_output(
        ["git", "-C", str(work_root / "lerobot"), "status", "--porcelain"],
        text=True,
    ).strip()
    if lerobot_status:
        raise RuntimeError("LeRobot worktree has local changes")

    verify_snapshot(
        work_root / "artifacts/smolvla_libero",
        POLICY_FILES,
        EXPECTED["model_revision"],
    )
    verify_snapshot(
        work_root / "artifacts/smolvlm_base",
        BASE_MODEL_FILES,
        EXPECTED["base_model_revision"],
    )
    verify_environment(work_root)

    print("PASS: public policy, base model, LeRobot source, and environment are ready")


if __name__ == "__main__":
    main()
