"""Supporting commands for the DeiT-Tiny VGF Learning Path, not ExecuTorch."""

import argparse
import json
import math
import struct
from pathlib import Path


MODEL_ID = "facebook/deit-tiny-patch16-224"
MODEL_REVISION = "b3428f18dcc7b543470d07f14b4a4157815d1880"
DATASET_ID = "timm/oxford-iiit-pet"
DATASET_REVISION = "089695c834a7deb60505b7cc506672db1c31a6aa"
NUM_CLASSES = 37
INPUT_SHAPE = (1, 3, 224, 224)


def validate_labels(metadata):
    if not isinstance(metadata, dict):
        raise ValueError("Expected a JSON object containing breed labels")
    labels = metadata["id2label"]
    if not isinstance(labels, dict) or set(labels) != {
        str(index) for index in range(NUM_CLASSES)
    }:
        raise ValueError("Expected breed labels for class IDs 0 through 36")
    if not all(isinstance(label, str) and label for label in labels.values()):
        raise ValueError("Breed labels must be nonempty strings")
    return labels


def checkpoint(args):
    model_dir = args.work_dir / "deit-tiny-oxford-pet/final_model"
    config = json.loads((model_dir / "config.json").read_text(encoding="utf-8"))
    validate_labels(config)
    source = model_dir / "model.safetensors"
    target = model_dir / "pytorch_model.bin"
    if source.is_file():
        import torch
        from safetensors.torch import load_file

        # Refresh the export copy after retraining, even if an older .bin exists.
        weights = load_file(str(source))
        torch.save(weights, target)
        print(f"Export weights: {target}")
        print(f"Original weights preserved: {source}")
    elif target.is_file() and target.stat().st_size:
        print(f"Using existing export weights: {target}")
    else:
        raise FileNotFoundError(
            f"No model.safetensors or nonempty pytorch_model.bin in {model_dir}. "
            "Run train_deit.py first."
        )
    print(f"Export checkpoint ready: {model_dir}")


def prepare(args):
    if args.sample_index < 0:
        raise ValueError("--sample-index must be zero or greater")
    model_dir = args.work_dir / "deit-tiny-oxford-pet/final_model"
    config = json.loads((model_dir / "config.json").read_text(encoding="utf-8"))
    labels = validate_labels(config)

    from datasets import load_dataset
    from transformers import AutoImageProcessor

    dataset = load_dataset(DATASET_ID, revision=DATASET_REVISION, split="test")
    if args.sample_index >= len(dataset):
        raise ValueError(f"--sample-index must be less than {len(dataset)}")
    sample = dataset[args.sample_index]
    expected_id = int(sample["label"])
    if labels[str(expected_id)] != dataset.features["label"].names[expected_id]:
        raise ValueError(
            "Checkpoint breed labels do not match the Oxford-IIIT Pet dataset"
        )
    image = sample["image"].convert("RGB")
    processor = AutoImageProcessor.from_pretrained(
        MODEL_ID, revision=MODEL_REVISION, use_fast=True
    )
    pixels = processor(image, return_tensors="pt")["pixel_values"].contiguous()
    if tuple(pixels.shape) != INPUT_SHAPE:
        raise ValueError(
            f"Expected input shape {INPUT_SHAPE}, got {tuple(pixels.shape)}"
        )

    image.save(args.work_dir / "input.jpg")
    pixels.detach().cpu().numpy().astype("<f4").tofile(args.work_dir / "input.bin")
    reference = {
        "sample_index": args.sample_index,
        "expected_id": expected_id,
        "id2label": labels,
    }
    (args.work_dir / "reference.json").write_text(
        json.dumps(reference, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Input image: {args.work_dir / 'input.jpg'}")
    print(f"Input tensor ready: {INPUT_SHAPE}")
    print(f"Expected breed: {labels[str(expected_id)]}")


def inspect(args):
    reference_path = args.work_dir / "reference.json"
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    labels = validate_labels(reference)
    expected_id = reference["expected_id"]
    if type(expected_id) is not int or not 0 <= expected_id < NUM_CLASSES:
        raise ValueError(
            "Expected dataset class ID must be an integer from 0 through 36"
        )
    output = (args.work_dir / "prediction-0.bin").read_bytes()
    if len(output) != NUM_CLASSES * 4:
        raise ValueError(
            f"Expected 37 float32 scores (148 bytes), got {len(output)} bytes"
        )
    scores = struct.unpack("<37f", output)
    if not all(math.isfinite(score) for score in scores):
        raise ValueError("Output contains non-finite scores")
    log = (args.work_dir / "runtime.log").read_text(encoding="utf-8", errors="replace")
    for name in ("prediction-0.bin", "runtime.log"):
        if (args.work_dir / name).stat().st_mtime_ns < reference_path.stat().st_mtime_ns:
            raise ValueError(
                f"{name} predates the prepared image. Rerun executor_runner "
                "before inspecting the result."
            )
    for message in ("Entered VGF init", "Model executed successfully"):
        if message not in log:
            raise ValueError(f"Runtime log is missing: {message}")

    predicted_id = max(range(NUM_CLASSES), key=scores.__getitem__)
    print(f"Expected breed: {labels[str(expected_id)]}")
    print(f"VGF prediction: {labels[str(predicted_id)]}")
    print(f"Matches dataset label: {predicted_id == expected_id}")
    print("Output scores: 37 finite values")
    print("VGF execution: confirmed")

    if args.compare_fp32:
        import numpy as np
        import torch
        from transformers import ViTForImageClassification

        pixels = np.fromfile(args.work_dir / "input.bin", dtype="<f4")
        if pixels.size != math.prod(INPUT_SHAPE) or not np.isfinite(pixels).all():
            raise ValueError("Input must contain 150528 finite float32 values")
        model = ViTForImageClassification.from_pretrained(
            args.work_dir / "deit-tiny-oxford-pet/final_model", local_files_only=True
        ).eval()
        with torch.inference_mode():
            logits = model(
                pixel_values=torch.from_numpy(pixels.reshape(INPUT_SHAPE))
            ).logits
            reference_id = logits.argmax(-1).item()
        print(f"FP32 prediction: {labels[str(reference_id)]}")
        print(f"Matches FP32 prediction: {predicted_id == reference_id}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name, handler, help_text in (
        ("checkpoint", checkpoint, "Prepare the trained weights for export"),
        ("prepare", prepare, "Prepare a real pet image for executor_runner"),
        ("inspect", inspect, "Decode the prediction and verify VGF execution"),
    ):
        command = commands.add_parser(name, help=help_text, description=help_text)
        command.add_argument(
            "--work-dir",
            type=Path,
            default=Path("arm_test/deit_vgf"),
            help="Directory containing the trained model and inference artifacts",
        )
        if name == "prepare":
            command.add_argument(
                "--sample-index",
                type=int,
                default=0,
                help="Zero-based index in the dataset test split",
            )
        elif name == "inspect":
            command.add_argument(
                "--compare-fp32",
                action="store_true",
                help="Also run the trained PyTorch model on the same input",
            )
        command.set_defaults(handler=handler)
    args = parser.parse_args()
    try:
        args.handler(args)
    except ImportError as error:
        parser.exit(
            1,
            f"Error: {error}. Activate the environment with the example dependencies.\n",
        )
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()
