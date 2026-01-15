#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def test_mac_template_has_required_fields() -> None:
    tpl = ROOT / "configs" / "templates" / "mac_template.json"
    data = _load(tpl)
    assert "model" in data
    assert "output_root" in data
    assert isinstance(data.get("experiments"), list) and data["experiments"]
    for exp in data["experiments"]:
        assert "name" in exp and "runner_path" in exp


def test_android_template_has_required_fields() -> None:
    tpl = ROOT / "configs" / "templates" / "android_template.json"
    data = _load(tpl)
    assert "model" in data
    assert "output_root" in data
    assert isinstance(data.get("experiments"), list) and data["experiments"]
    for exp in data["experiments"]:
        assert "name" in exp and "runner_path" in exp


def test_example_config_is_valid_json() -> None:
    for ex in [
        ROOT / "configs" / "examples" / "mac_mobilenet_fp16.json",
        ROOT / "configs" / "examples" / "android_mobilenet_fp16.json",
    ]:
        data = _load(ex)
        assert data["model"].endswith(".pte")


if __name__ == "__main__":
    test_mac_template_has_required_fields()
    test_android_template_has_required_fields()
    test_example_config_is_valid_json()
    print("OK")


