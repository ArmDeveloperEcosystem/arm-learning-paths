#!/usr/bin/env python3
"""
Export helper for profiling workflows (kept intentionally minimal).

This is based on ExecuTorch's upstream XNNPACK export flow (see
`executorch/examples/xnnpack/aot_compiler.py`), with a small addition:

- We patch ExecuTorch's model registry at runtime so models registered under
  `model_profiling/models/` can be exported without editing ExecuTorch sources.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import logging
import os
import sys
from pathlib import Path
from typing import Iterable, List, Optional

import torch

# Repo + ExecuTorch discovery (no hard dependency on PYTHONPATH).
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_EXECUTORCH_OVERRIDE = (
    os.environ.get("EXECUTORCH_REPO")
    or os.environ.get("EXECUTORCH_PATH")
    or os.environ.get("EXECUTORCH_DIR_OVERRIDE")
)
EXECUTORCH_DIR = (
    Path(_EXECUTORCH_OVERRIDE).expanduser().resolve()
    if _EXECUTORCH_OVERRIDE
    else REPO_ROOT / "executorch"
)

sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(EXECUTORCH_DIR))

from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.exir import EdgeCompileConfig, ExecutorchBackendConfig, to_edge_transform_and_lower
from executorch.extension.export_util.utils import save_pte_program
from model_profiling.models import patch_executorch_model_registry

patch_executorch_model_registry()

from executorch.examples.models import MODEL_NAME_TO_MODEL
from executorch.examples.models.model_factory import EagerModelFactory

# Import quantization utilities if available
try:
    from executorch.examples.xnnpack import MODEL_NAME_TO_OPTIONS
    from executorch.examples.xnnpack.quantization.utils import quantize
    QUANTIZATION_AVAILABLE = True
except ImportError:
    QUANTIZATION_AVAILABLE = False
    MODEL_NAME_TO_OPTIONS = None


logger = logging.getLogger("export")


def _to_jsonable_list(seq) -> List:
    out = []
    for x in seq:
        try:
            out.append(int(x))
        except Exception:
            out.append(str(x))
    return out


def _tensor_meta_from_val(val) -> Optional[dict]:
    if val is None:
        return None
    if hasattr(val, "shape") and hasattr(val, "dtype"):
        meta = {"shape": _to_jsonable_list(list(val.shape)), "dtype": str(val.dtype)}
        if hasattr(val, "stride"):
            try:
                meta["stride"] = _to_jsonable_list(list(val.stride()))
            except Exception:
                meta["stride"] = str(val.stride())
        if hasattr(val, "requires_grad"):
            meta["requires_grad"] = bool(val.requires_grad)
        if hasattr(val, "is_quantized"):
            try:
                meta["is_quantized"] = bool(val.is_quantized)
            except Exception:
                meta["is_quantized"] = False
        return meta
    return None


def _save_graph_json(ep, example_inputs, graph_path: Path, model_name: str):
    graph = ep.graph if hasattr(ep, "graph") else ep.graph_module.graph
    sample_inputs = []
    for inp in example_inputs:
        if isinstance(inp, torch.Tensor):
            sample_inputs.append(_to_jsonable_list(list(inp.shape)))
        elif isinstance(inp, (list, tuple)):
            sample_inputs.append(
                [_to_jsonable_list(list(x.shape)) if isinstance(x, torch.Tensor) else str(type(x)) for x in inp]
            )
        elif isinstance(inp, dict):
            sample_inputs.append(
                {k: (_to_jsonable_list(list(v.shape)) if isinstance(v, torch.Tensor) else str(type(v))) for k, v in inp.items()}
            )
        else:
            sample_inputs.append(str(type(inp)))

    nodes = []
    for idx, node in enumerate(graph.nodes):
        meta = getattr(node, "meta", {}) or {}
        tensor_meta = None
        val = meta.get("val", None)
        if tensor_meta is None:
            tensor_meta = _tensor_meta_from_val(val)
        if tensor_meta is None:
            tensor_meta = _tensor_meta_from_val(meta.get("tensor_meta", None))

        node_info = {
            "index": idx,
            "name": node.name,
            "op": node.op,
            "target": str(node.target) if node.target else None,
            "args": [str(arg) for arg in node.args],
            "kwargs": {str(k): str(v) for k, v in node.kwargs.items()},
        }
        if meta:
            node_info["meta_keys"] = list(meta.keys())
        if tensor_meta:
            node_info["tensor_meta"] = tensor_meta
        nodes.append(node_info)

    graph_data = {
        "model_info": {"type": model_name, "sample_input_shapes": sample_inputs},
        "graph_info": {"num_nodes": len(nodes), "graph_type": str(type(graph))},
        "nodes": nodes,
    }
    graph_path.parent.mkdir(parents=True, exist_ok=True)
    with open(graph_path, "w") as f:
        json.dump(graph_data, f, indent=2)


@contextlib.contextmanager
def _inside_executorch_repo():
    cwd = Path.cwd()
    if cwd.name == "executorch":
        yield
        return
    os.chdir(EXECUTORCH_DIR)
    try:
        yield
    finally:
        os.chdir(cwd)


def export_model(args) -> Path:
    if args.model not in MODEL_NAME_TO_MODEL:
        raise ValueError(
            f"Unknown model '{args.model}'. Available: {list(MODEL_NAME_TO_MODEL.keys())}"
        )

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    with _inside_executorch_repo():
        model, example_inputs, example_kwarg_inputs, _ = EagerModelFactory.create_model(
            *MODEL_NAME_TO_MODEL[args.model]
        )
    example_kwarg_inputs = example_kwarg_inputs or {}

    model = model.eval()

    dtype = torch.float16 if args.dtype == "fp16" else torch.float32
    model = model.to(dtype=dtype)
    example_inputs = tuple(
        t.to(dtype=dtype) if isinstance(t, torch.Tensor) else t for t in example_inputs
    )

    ep = torch.export.export(model, example_inputs, kwargs=example_kwarg_inputs, strict=False)
    
    # Apply quantization if requested
    if args.quantize:
        if not QUANTIZATION_AVAILABLE:
            raise RuntimeError(
                "Quantization is not available. Make sure you're using an ExecuTorch environment "
                "with quantization support (e.g., PR 16533 environment)."
            )
        if args.model not in MODEL_NAME_TO_OPTIONS:
            raise RuntimeError(
                f"Model '{args.model}' is not in MODEL_NAME_TO_OPTIONS. "
                f"Available models: {list(MODEL_NAME_TO_OPTIONS.keys())}"
            )
        if args.backend != "xnnpack":
            raise NotImplementedError(
                "Quantization is only supported with xnnpack backend"
            )
        
        logger.info("Quantizing model...")
        quant_type = MODEL_NAME_TO_OPTIONS[args.model].quantization
        model = ep.module()
        model = quantize(model, example_inputs, quant_type)
        # Re-export after quantization
        ep = torch.export.export(model, example_inputs, kwargs=example_kwarg_inputs, strict=False)

    edge = to_edge_transform_and_lower(
        ep,
        partitioner=[XnnpackPartitioner()] if args.backend == "xnnpack" else [],
        compile_config=EdgeCompileConfig(
            _check_ir_validity=False if args.quantize else True,
            _skip_dim_order=True,
        ),
    )
    exec_prog = edge.to_executorch(
        config=ExecutorchBackendConfig(extract_delegate_segments=False)
    )

    # Use "q8" tag for quantized models, otherwise use dtype
    if args.quantize:
        pte_stem = f"{args.model}_{args.backend}_q8"
    else:
        pte_stem = f"{args.model}_{args.backend}_{args.dtype}"
    
    save_pte_program(exec_prog, pte_stem, str(outdir))
    if args.save_graph:
        graph_path = outdir / "graph.json"
        _save_graph_json(ep, example_inputs, graph_path, args.model)
    pte_file = outdir / f"{pte_stem}.pte"
    logger.info("Export complete: %s", pte_file)
    return pte_file


def parse_args(argv: Iterable[str]):
    parser = argparse.ArgumentParser(description="ExecuTorch export helper (minimal)")
    parser.add_argument("--model", required=True, help="Model name (e.g., squeeze_sam)")
    parser.add_argument("--backend", choices=["xnnpack", "portable"], default="xnnpack")
    parser.add_argument("--dtype", choices=["fp32", "fp16"], default="fp16")
    parser.add_argument(
        "--quantize",
        action="store_true",
        help="Produce an 8-bit quantized model (INT8). Requires xnnpack backend and quantization support."
    )
    parser.add_argument("--outdir", required=True, help="Directory to store export artifacts")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--save-graph", action="store_true", help="Emit graph.json alongside PTE")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None):
    args = parse_args(argv if argv is not None else sys.argv[1:])
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(message)s")
    export_model(args)


if __name__ == "__main__":
    main()
