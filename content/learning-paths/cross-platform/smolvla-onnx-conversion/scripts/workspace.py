#!/usr/bin/env python3
"""Configure caches owned by this standalone Learning Path."""

from __future__ import annotations

import os
from pathlib import Path


def configure_workspace(work_root: Path | None = None) -> Path:
    """Set reproducible cache defaults and return the resolved work root."""

    learning_path_root = Path(__file__).resolve().parent.parent
    if work_root is None:
        work_root = Path(
            os.environ.get("SMOLVLA_LP_WORK_ROOT", learning_path_root / "work")
        )
    work_root = work_root.resolve()
    os.environ.setdefault("HF_HOME", str(work_root / "cache/huggingface"))
    os.environ.setdefault("XDG_CACHE_HOME", str(work_root / "cache/xdg"))
    os.environ.setdefault("TMPDIR", str(work_root / "tmp"))
    return work_root


def base_model_path(work_root: Path | None = None) -> Path:
    """Return the verified local base-model path created by setup.sh."""

    root = configure_workspace(work_root)
    base = root / "artifacts/smolvlm_base"
    required = (base / "config.json", base / "model.safetensors", base / "tokenizer.json")
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing pinned SmolVLM2 base files:\n" + "\n".join(missing))
    return base


def load_smolvla_policy(checkpoint: Path):
    """Load SmolVLA while binding its implicit backbone to the pinned local snapshot."""

    from lerobot.configs.policies import PreTrainedConfig
    from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy

    checkpoint = checkpoint.resolve()
    config = PreTrainedConfig.from_pretrained(checkpoint)
    config.device = "cpu"
    config.vlm_model_name = str(base_model_path())
    return SmolVLAPolicy.from_pretrained(checkpoint, config=config)
