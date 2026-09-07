#!/usr/bin/env python3

import argparse
from pathlib import Path

from huggingface_hub import snapshot_download

from adapter_contract import model_directory


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-id", required=True, help="Hugging Face model repository ID")
    args = parser.parse_args()

    destination = model_directory(args.repo_id)
    print(f"Downloading {args.repo_id} to {destination} ...")
    snapshot_path = Path(snapshot_download(repo_id=args.repo_id, local_dir=destination))

    print(f"Model directory: {snapshot_path.resolve()}")


if __name__ == "__main__":
    main()
