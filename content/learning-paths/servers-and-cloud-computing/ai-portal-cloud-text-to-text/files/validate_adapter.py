#!/usr/bin/env python3

import argparse
import inspect
import re
from pathlib import Path

from adapter_contract import TextGenerationAdapter, resolve_model_directory


PLACEHOLDER_PATTERN = re.compile(
    r"<(?:MODEL|RUNTIME|PLACEHOLDER|TODO)[A-Z0-9_-]*>"
)


def normalized_runtime(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def main() -> None:
    parser = argparse.ArgumentParser()
    model_source = parser.add_mutually_exclusive_group(required=True)
    model_source.add_argument("--model-id")
    model_source.add_argument("--model-dir")
    parser.add_argument("--runtime")
    args = parser.parse_args()

    model_dir = resolve_model_directory(args.model_id, args.model_dir).resolve()
    errors = []
    script_dir = Path(__file__).resolve().parent
    model_adapter_path = script_dir / "model_adapter.py"

    try:
        from model_adapter import ModelAdapter
    except Exception as error:
        ModelAdapter = None
        errors.append(f"Unable to import model_adapter.py: {error}")

    if ModelAdapter is not None:
        if not issubclass(ModelAdapter, TextGenerationAdapter):
            errors.append("ModelAdapter must inherit TextGenerationAdapter")
        if inspect.isabstract(ModelAdapter):
            errors.append("ModelAdapter does not implement every adapter method")

    try:
        adapter_source = model_adapter_path.read_text(encoding="utf-8")
    except OSError as error:
        errors.append(f"Unable to read model_adapter.py: {error}")
    else:
        if PLACEHOLDER_PATTERN.search(adapter_source):
            errors.append("model_adapter.py contains an unresolved placeholder")

    requirements_path = script_dir / "runtime-requirements.txt"
    if not requirements_path.is_file() or not requirements_path.read_text().strip():
        errors.append("runtime-requirements.txt is missing or empty")

    adapter = None
    if not errors and ModelAdapter is not None:
        adapter = ModelAdapter(model_dir, "auto", 1)
        try:
            adapter.validate_model_directory()
        except (OSError, TypeError, ValueError) as error:
            errors.append(str(error))
        if args.runtime and normalized_runtime(args.runtime) != normalized_runtime(
            adapter.runtime_name
        ):
            errors.append(
                f"Requested runtime '{args.runtime}' does not match "
                f"adapter runtime '{adapter.runtime_name}'"
            )

    if errors:
        print("Adapter validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Adapter validation passed")
    print(f"Runtime: {adapter.runtime_name}")
    print(f"Interaction mode: {adapter.interaction_mode}")
    print("Model directory contains the files required by the adapter")


if __name__ == "__main__":
    main()
