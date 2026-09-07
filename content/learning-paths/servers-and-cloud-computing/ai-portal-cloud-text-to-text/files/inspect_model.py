#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

from adapter_contract import resolve_model_directory


CONFIGURATION_NAMES = {
    "README.md",
    "chat_template.jinja",
    "config.json",
    "config.yaml",
    "genai_config.json",
    "generation_config.json",
    "metadata.yaml",
    "tokenizer_config.json",
}
MAX_CONFIGURATION_BYTES = 64 * 1024


def inspect_model(model_dir: Path, model_id: str | None, runtime: str) -> dict:
    repository_files = []
    configuration_files = {}

    for path in sorted(model_dir.rglob("*")):
        relative_path = path.relative_to(model_dir)
        if not path.is_file() or any(
            part.startswith(".") for part in relative_path.parts
        ):
            continue
        relative_name = relative_path.as_posix()
        size = path.stat().st_size
        repository_files.append({"path": relative_name, "size_bytes": size})

        if path.name in CONFIGURATION_NAMES and size <= MAX_CONFIGURATION_BYTES:
            try:
                configuration_files[relative_name] = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                pass

    return {
        "model_id": model_id,
        "runtime": runtime,
        "repository_files": repository_files,
        "configuration_files": configuration_files,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    model_source = parser.add_mutually_exclusive_group(required=True)
    model_source.add_argument("--model-id")
    model_source.add_argument("--model-dir")
    parser.add_argument("--runtime", required=True)
    parser.add_argument("--output", default="model-summary.json")
    args = parser.parse_args()

    model_dir = resolve_model_directory(args.model_id, args.model_dir).resolve()
    if not model_dir.is_dir():
        raise SystemExit(f"Model directory not found: {model_dir}")

    summary = inspect_model(model_dir, args.model_id, args.runtime)
    output_path = Path(args.output)
    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Model summary: {output_path.resolve()}")
    print(f"Repository files: {len(summary['repository_files'])}")
    print(f"Configuration files: {len(summary['configuration_files'])}")


if __name__ == "__main__":
    main()
