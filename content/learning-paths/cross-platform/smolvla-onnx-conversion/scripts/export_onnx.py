#!/usr/bin/env python3
"""Export a public two-camera SmolVLA checkpoint and validate ONNX Runtime."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import gc
import json
import math
import os
from pathlib import Path
import platform
import shutil
import tempfile
from typing import Sequence

import numpy as np
import torch
from torch import Tensor, nn
from torch.nn import functional as F

from workspace import configure_workspace, load_smolvla_policy


WORK_ROOT = configure_workspace()


INPUT_NAMES = (
    "camera1",
    "camera2",
    "lang_tokens",
    "lang_attention_mask",
    "state",
    "noise",
)
EXPECTED_ACTION_DIM = 7
EXPECTED_DENOISING_STEPS = 10

_ORIGINAL_TORCH_CUMSUM = torch.cumsum
_ORIGINAL_TORCH_FULL = torch.full


@contextmanager
def fresh_directory(destination: Path):
    """Build a directory beside its destination, then publish it in one rename."""

    destination = destination.resolve()
    if os.path.lexists(destination):
        raise FileExistsError(f"Refusing to overwrite {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(
        tempfile.mkdtemp(
            prefix=f".{destination.name}.tmp-", dir=str(destination.parent)
        )
    )
    try:
        yield staging
        if os.path.lexists(destination):
            raise FileExistsError(f"Destination appeared during the run: {destination}")
        staging.rename(destination)
    except BaseException:
        if os.path.lexists(staging):
            shutil.rmtree(staging)
        raise


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def validate_array(
    name: str,
    value: np.ndarray,
    *,
    shape: Sequence[int] | None = None,
    dtype: np.dtype | type | None = None,
) -> None:
    if shape is not None and tuple(value.shape) != tuple(shape):
        raise ValueError(f"{name} has shape {value.shape}; expected {tuple(shape)}")
    if dtype is not None and value.dtype != np.dtype(dtype):
        raise TypeError(f"{name} has dtype {value.dtype}; expected {np.dtype(dtype)}")
    if np.issubdtype(value.dtype, np.number) and not np.isfinite(value).all():
        raise ValueError(f"{name} contains a non-finite value")


def policy_dimensions(policy: nn.Module) -> dict[str, int]:
    state_feature = policy.config.robot_state_feature
    action_feature = policy.config.action_feature
    if state_feature is None or len(state_feature.shape) != 1:
        raise ValueError("The checkpoint must define one robot-state feature")
    if action_feature is None or len(action_feature.shape) != 1:
        raise ValueError("The checkpoint must define one action feature")
    dimensions = {
        "state_dim": int(state_feature.shape[0]),
        "action_dim": int(action_feature.shape[0]),
        "action_chunk_size": int(policy.model.config.chunk_size),
        "latent_action_dim": int(policy.model.config.max_action_dim),
        "denoising_steps": int(policy.model.config.num_steps),
    }
    if dimensions["action_dim"] != EXPECTED_ACTION_DIM:
        raise ValueError(
            f"This Learning Path requires {EXPECTED_ACTION_DIM} action channels"
        )
    if dimensions["denoising_steps"] != EXPECTED_DENOISING_STEPS:
        raise ValueError(
            f"This Learning Path requires {EXPECTED_DENOISING_STEPS} denoising steps"
        )
    return dimensions


def install_exportable_rope() -> None:
    """Replace SmolVLA's in-place RoPE implementation with an ONNX-safe form."""

    import lerobot.policies.smolvla.smolvlm_with_expert as expert_module

    def apply_rope(x: Tensor, positions: Tensor, max_wavelength: float = 10_000) -> Tensor:
        half = x.shape[-1] // 2
        source_dtype = x.dtype
        source = x.to(torch.float32)
        exponents = (2.0 / x.shape[-1]) * torch.arange(
            half, dtype=torch.float32, device=x.device
        )
        timescale = max_wavelength**exponents
        radians = positions[..., None].to(torch.float32) / timescale[None, None, :]
        radians = radians[..., None, :]
        first, second = source.split(half, dim=-1)
        result = torch.cat(
            [
                first * torch.cos(radians) - second * torch.sin(radians),
                second * torch.cos(radians) + first * torch.sin(radians),
            ],
            dim=-1,
        )
        return result.to(source_dtype)

    expert_module.apply_rope = apply_rope


def install_exportable_attention(policy: nn.Module) -> None:
    """Use exportable eager attention in the vision encoder."""

    for module in policy.modules():
        config = getattr(module, "config", None)
        if (
            config is not None
            and getattr(config, "model_type", None) == "smolvlm_vision"
            and hasattr(config, "_attn_implementation")
        ):
            config._attn_implementation = "eager"


def static_trace_length(value: object) -> object:
    """Convert a traced scalar shape to a constant for this fixed-shape graph."""

    if isinstance(value, Tensor) and value.ndim == 0:
        return int(value.detach().cpu())
    return value


def install_exportable_masking() -> None:
    """Handle Transformers 5.5 scalar shape tensors in the legacy exporter."""

    import transformers.masking_utils as masking_utils

    original_sdpa_mask = masking_utils.sdpa_mask

    def exportable_sdpa_mask(*args, **kwargs):
        positional = list(args)
        if len(positional) > 1:
            positional[1] = static_trace_length(positional[1])
        elif "q_length" in kwargs:
            kwargs["q_length"] = static_trace_length(kwargs["q_length"])
        if len(positional) > 2:
            positional[2] = static_trace_length(positional[2])
        elif "kv_length" in kwargs:
            kwargs["kv_length"] = static_trace_length(kwargs["kv_length"])
        return original_sdpa_mask(*positional, **kwargs)

    masking_utils.sdpa_mask = exportable_sdpa_mask


def boolean_safe_cumsum(input_tensor: Tensor, *args, **kwargs) -> Tensor:
    """Preserve PyTorch bool cumsum semantics with an ONNX-valid integer input."""

    if input_tensor.dtype == torch.bool:
        input_tensor = input_tensor.to(torch.int64)
    return _ORIGINAL_TORCH_CUMSUM(input_tensor, *args, **kwargs)


def install_exportable_cumsum() -> None:
    """Make boolean cumulative sums legal for ONNX Runtime."""

    torch.cumsum = boolean_safe_cumsum


def dtype_stable_full(size, fill_value, *args, **kwargs) -> Tensor:
    """Make PyTorch's integer fill-value dtype inference explicit for ONNX."""

    if "dtype" not in kwargs and type(fill_value) is int:
        kwargs["dtype"] = torch.int64
    return _ORIGINAL_TORCH_FULL(size, fill_value, *args, **kwargs)


def install_exportable_full() -> None:
    """Prevent legacy ONNX ScatterND from mixing float and integer tensors."""

    torch.full = dtype_stable_full


def exportable_sinusoidal_embedding(
    time: Tensor,
    dimension: int,
    min_period: float,
    max_period: float,
    device: torch.device | str = "cpu",
) -> Tensor:
    """Compute SmolVLA timestep features in ONNX Runtime-supported FP32."""

    if dimension % 2 != 0:
        raise ValueError(f"dimension ({dimension}) must be divisible by 2")
    if time.ndim != 1:
        raise ValueError("The time tensor is expected to have shape (batch_size,)")
    fraction = torch.linspace(
        0.0,
        1.0,
        dimension // 2,
        dtype=torch.float32,
        device=device,
    )
    period = min_period * (max_period / min_period) ** fraction
    sin_input = (1.0 / period * 2 * math.pi)[None, :] * time.to(torch.float32)[:, None]
    return torch.cat([torch.sin(sin_input), torch.cos(sin_input)], dim=1)


def install_exportable_timestep_embedding() -> None:
    """Avoid unsupported double-precision Sin/Cos kernels in ONNX Runtime CPU."""

    import lerobot.policies.smolvla.modeling_smolvla as smolvla_module

    smolvla_module.create_sinusoidal_pos_embedding = exportable_sinusoidal_embedding


class ExportableSmolVLA(nn.Module):
    """Expose the LIBERO policy core with explicit images, state, and noise."""

    def __init__(self, policy: nn.Module, dimensions: dict[str, int]):
        super().__init__()
        self.model = policy.model
        self.state_dim = dimensions["state_dim"]
        self.action_dim = dimensions["action_dim"]
        if len(policy.config.image_features) != 2:
            raise ValueError(
                "This Learning Path expects the two-camera SmolVLA-LIBERO checkpoint"
            )
        if self.model.config.max_state_dim < self.state_dim:
            raise ValueError("The requested state dimension exceeds the model maximum")
        if self.model.config.max_action_dim < self.action_dim:
            raise ValueError("The requested action dimension exceeds the model maximum")

    def forward(
        self,
        camera1: Tensor,
        camera2: Tensor,
        lang_tokens: Tensor,
        lang_attention_mask: Tensor,
        state: Tensor,
        noise: Tensor,
    ) -> Tensor:
        batch_size = state.shape[0]
        image_mask = torch.ones(batch_size, dtype=torch.bool, device=state.device)
        images = [camera1 * 2.0 - 1.0, camera2 * 2.0 - 1.0]
        image_masks = [image_mask, image_mask]
        padded_state = F.pad(state, (0, self.model.config.max_state_dim - self.state_dim))
        actions = self.model.sample_actions(
            images,
            image_masks,
            lang_tokens,
            lang_attention_mask.to(torch.bool),
            padded_state,
            noise=noise,
        )
        return actions[:, :, : self.action_dim]


def make_inputs(
    policy: nn.Module, dimensions: dict[str, int], seed: int
) -> tuple[Tensor, ...]:
    generator = torch.Generator(device="cpu").manual_seed(seed)
    tokenizer = policy.model.vlm_with_expert.processor.tokenizer
    encoded = tokenizer(
        "pick up the black bowl and place it on the plate",
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=48,
    )
    return (
        torch.rand(1, 3, 512, 512, generator=generator),
        torch.rand(1, 3, 512, 512, generator=generator),
        encoded["input_ids"].to(torch.int64),
        encoded["attention_mask"].to(torch.int64),
        torch.randn(
            1,
            dimensions["state_dim"],
            generator=generator,
        ),
        torch.randn(
            1,
            dimensions["action_chunk_size"],
            dimensions["latent_action_dim"],
            generator=generator,
        ),
    )


def save_reference(directory: Path, inputs: Sequence[Tensor]) -> None:
    directory.mkdir(parents=True, exist_ok=False)
    for name, value in zip(INPUT_NAMES, inputs, strict=True):
        np.save(
            directory / f"{name}.npy",
            value.detach().cpu().numpy(),
            allow_pickle=False,
        )


def session_interface(session) -> dict[str, list[dict[str, object]]]:
    def describe(value) -> dict[str, object]:
        return {"name": value.name, "shape": list(value.shape), "type": value.type}

    return {
        "inputs": [describe(value) for value in session.get_inputs()],
        "outputs": [describe(value) for value in session.get_outputs()],
    }


def export_bundle(
    args: argparse.Namespace,
    checkpoint: Path,
    output: Path,
    reference_dir: Path,
) -> None:
    import onnx
    import onnxruntime as ort

    torch.manual_seed(args.seed)
    policy = load_smolvla_policy(checkpoint).to(device="cpu", dtype=torch.float32)
    policy.eval()
    dimensions = policy_dimensions(policy)
    wrapper = ExportableSmolVLA(policy, dimensions).eval()
    inputs = make_inputs(policy, dimensions, args.seed)
    input_arrays = {
        name: np.ascontiguousarray(value.detach().cpu().numpy())
        for name, value in zip(INPUT_NAMES, inputs, strict=True)
    }
    expected_inputs = {
        "camera1": ((1, 3, 512, 512), np.float32),
        "camera2": ((1, 3, 512, 512), np.float32),
        "lang_tokens": ((1, 48), np.int64),
        "lang_attention_mask": ((1, 48), np.int64),
        "state": ((1, dimensions["state_dim"]), np.float32),
        "noise": (
            (
                1,
                dimensions["action_chunk_size"],
                dimensions["latent_action_dim"],
            ),
            np.float32,
        ),
    }
    for name, value in input_arrays.items():
        shape, dtype = expected_inputs[name]
        validate_array(name, value, shape=shape, dtype=dtype)

    action_shape = (1, dimensions["action_chunk_size"], dimensions["action_dim"])
    with torch.inference_mode():
        baseline_output = wrapper(*inputs).detach().cpu().numpy()
    validate_array(
        "unmodified PyTorch actions",
        baseline_output,
        shape=action_shape,
        dtype=np.float32,
    )

    install_exportable_rope()
    install_exportable_masking()
    install_exportable_cumsum()
    install_exportable_full()
    install_exportable_timestep_embedding()
    install_exportable_attention(policy)
    with torch.inference_mode():
        pytorch_output = wrapper(*inputs).detach().cpu().numpy()
    validate_array(
        "export-safe PyTorch actions",
        pytorch_output,
        shape=action_shape,
        dtype=np.float32,
    )
    compatibility_difference = pytorch_output.astype(np.float64) - baseline_output.astype(
        np.float64
    )
    compatibility_passed = bool(
        np.allclose(pytorch_output, baseline_output, atol=args.atol, rtol=args.rtol)
    )
    if not compatibility_passed:
        raise RuntimeError("The export-safe PyTorch path changed checkpoint output")

    with torch.inference_mode():
        torch.onnx.export(
            wrapper,
            inputs,
            str(output),
            input_names=list(INPUT_NAMES),
            output_names=["actions"],
            opset_version=args.opset,
            export_params=True,
            keep_initializers_as_inputs=False,
            external_data=True,
            dynamo=False,
        )
    onnx.checker.check_model(str(output), full_check=False)
    del wrapper, policy
    gc.collect()

    options = ort.SessionOptions()
    options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_BASIC
    session = ort.InferenceSession(
        str(output),
        sess_options=options,
        providers=["CPUExecutionProvider"],
    )
    feeds = input_arrays
    ort_output = session.run(["actions"], feeds)[0]
    validate_array(
        "ONNX Runtime actions", ort_output, shape=action_shape, dtype=np.float32
    )
    difference = ort_output.astype(np.float64) - pytorch_output.astype(np.float64)
    passed = bool(np.allclose(ort_output, pytorch_output, atol=args.atol, rtol=args.rtol))
    save_reference(reference_dir, inputs)

    report = {
        "format": "smolvla-onnx-validation-v3",
        "architecture": platform.machine(),
        "seed": args.seed,
        "opset": args.opset,
        "execution_providers": session.get_providers(),
        "derived_configuration": dimensions,
        "interface": session_interface(session),
        "export_compatibility": {
            "max_absolute_error": float(np.abs(compatibility_difference).max()),
            "mean_absolute_error": float(np.abs(compatibility_difference).mean()),
            "passed": compatibility_passed,
        },
        "max_absolute_error": float(np.abs(difference).max()),
        "mean_absolute_error": float(np.abs(difference).mean()),
        "atol": args.atol,
        "rtol": args.rtol,
        "passed": passed,
        "versions": {
            "python": platform.python_version(),
            "torch": torch.__version__,
            "onnx": onnx.__version__,
            "onnxruntime": ort.__version__,
        },
    }
    report_path = output.parent / "validation.json"
    write_json(report_path, report)
    if not passed:
        raise RuntimeError("ONNX Runtime output did not meet the export tolerances")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reference-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20260813)
    parser.add_argument("--opset", type=int, default=17)
    parser.add_argument("--atol", type=float, default=1.0e-3)
    parser.add_argument("--rtol", type=float, default=1.0e-3)
    args = parser.parse_args()

    if args.opset < 1:
        raise ValueError("--opset must be positive")
    if not np.isfinite(args.atol) or args.atol < 0:
        raise ValueError("--atol must be finite and non-negative")
    if not np.isfinite(args.rtol) or args.rtol < 0:
        raise ValueError("--rtol must be finite and non-negative")

    checkpoint = args.checkpoint.resolve(strict=True)
    expected_checkpoint = (WORK_ROOT / "artifacts/smolvla_libero").resolve(strict=True)
    if checkpoint != expected_checkpoint:
        raise ValueError("--checkpoint must be the prepared workspace artifact")
    final_output = args.output.resolve()
    final_reference = args.reference_dir.resolve()
    final_bundle = final_output.parent
    if final_output.suffix.lower() != ".onnx":
        raise ValueError("--output must use the .onnx suffix")
    if final_output.name == "validation.json":
        raise ValueError("--output collides with validation.json")
    if final_reference.parent != final_bundle:
        raise ValueError("--reference-dir must be inside the ONNX output bundle")
    if final_reference == final_output:
        raise ValueError("--output and --reference-dir must be different paths")
    if final_reference.name == "validation.json":
        raise ValueError("--reference-dir collides with validation.json")

    with fresh_directory(final_bundle) as staging:
        export_bundle(
            args,
            checkpoint,
            staging / final_output.name,
            staging / final_reference.name,
        )
    print(
        f"PASS: ONNX Runtime matches PyTorch within atol={args.atol:g} "
        f"and rtol={args.rtol:g}"
    )


if __name__ == "__main__":
    main()
