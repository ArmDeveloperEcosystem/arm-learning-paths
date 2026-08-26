#!/usr/bin/env python3
"""Quantize constant ONNX linear weights with TorchAO INT4 for Arm CPUs."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import tempfile

import numpy as np
import onnx
import torch
import torchao
from onnx import AttributeProto, TensorProto, helper, numpy_helper
from torchao.quantization import (
    IntxWeightOnlyConfig,
    MappingType,
    PerGroup,
    quantize_,
)


GROUP_SIZE = 32
ACCURACY_LEVEL = 4


class Names:
    def __init__(self, graph: onnx.GraphProto) -> None:
        self.used = {item.name for item in graph.initializer}
        self.used.update(item.name for item in (*graph.input, *graph.output, *graph.value_info))
        self.used.update(
            value
            for node in graph.node
            for value in (*node.input, *node.output)
            if value
        )

    def make(self, base: str) -> str:
        candidate = base
        index = 1
        while candidate in self.used:
            candidate = f"{base}_{index}"
            index += 1
        self.used.add(candidate)
        return candidate


def resolve_initializer(
    name: str,
    initializers: dict[str, onnx.TensorProto],
    producers: dict[str, onnx.NodeProto],
) -> str | None:
    seen: set[str] = set()
    while name not in initializers:
        if name in seen:
            raise ValueError("Identity cycle found while resolving a weight")
        seen.add(name)
        producer = producers.get(name)
        if producer is None or producer.op_type != "Identity" or len(producer.input) != 1:
            return None
        name = producer.input[0]
    return name


def gemm_attributes(node: onnx.NodeProto) -> dict[str, object]:
    return {item.name: helper.get_attribute_value(item) for item in node.attribute}


def eligible_weight(
    node: onnx.NodeProto,
    initializers: dict[str, onnx.TensorProto],
    producers: dict[str, onnx.NodeProto],
) -> tuple[str, bool] | None:
    transpose = False
    if node.op_type == "MatMul" and len(node.input) >= 2:
        pass
    elif node.op_type == "Gemm" and len(node.input) >= 2:
        attrs = gemm_attributes(node)
        if (
            int(attrs.get("transA", 0)) != 0
            or int(attrs.get("transB", 0)) != 1
            or float(attrs.get("alpha", 1.0)) != 1.0
            or float(attrs.get("beta", 1.0)) != 1.0
        ):
            return None
        transpose = True
    else:
        return None

    name = resolve_initializer(node.input[1], initializers, producers)
    if name is None:
        return None
    tensor = initializers[name]
    if len(tensor.dims) != 2 or tensor.data_type != TensorProto.FLOAT:
        return None
    return name, transpose


def pack_nibbles(values: np.ndarray, pad_value: int) -> np.ndarray:
    if values.shape[-1] % 2:
        padding = [(0, 0)] * (values.ndim - 1) + [(0, 1)]
        values = np.pad(values, padding, constant_values=pad_value)
    values = np.asarray(values, dtype=np.uint8)
    return values[..., 0::2] | (values[..., 1::2] << np.uint8(4))


def torchao_qparams(weight: np.ndarray, config: IntxWeightOnlyConfig):
    """Return ORT-packed qdata, scales, zero points, and K."""
    k, n = weight.shape
    linear = torch.nn.Linear(k, n, bias=False, device="meta")
    linear_weight = torch.from_numpy(np.ascontiguousarray(weight.T)).clone()
    linear.weight = torch.nn.Parameter(linear_weight, requires_grad=False)
    quantize_(linear, config)

    qweight = linear.weight
    qdata = qweight.qdata.detach().cpu().numpy().astype(np.int16)
    scales = qweight.scale.detach().cpu().numpy().astype(np.float32)
    zero_points = qweight.zero_point.detach().cpu().numpy().astype(np.int16)
    if qdata.min() < -8 or qdata.max() > 7 or zero_points.min() < -8 or zero_points.max() > 7:
        raise ValueError("TorchAO produced values outside the signed INT4 range")

    blocks = k // GROUP_SIZE
    packed = pack_nibbles((qdata + 8).astype(np.uint8), pad_value=0).reshape(
        n, blocks, GROUP_SIZE // 2
    )
    packed_zp = pack_nibbles(
        (zero_points + 8).astype(np.uint8), pad_value=8
    )
    if scales.shape != (n, blocks) or packed_zp.shape != (n, (blocks + 1) // 2):
        raise ValueError("Unexpected TorchAO group-wise parameter shape")
    return packed, np.ascontiguousarray(scales), np.ascontiguousarray(packed_zp), k


def nested_uses(graph: onnx.GraphProto) -> set[str]:
    used = {item.name for item in graph.output}
    for node in graph.node:
        used.update(value for value in node.input if value)
        for attr in node.attribute:
            if attr.type == AttributeProto.GRAPH:
                used.update(nested_uses(attr.g))
            elif attr.type == AttributeProto.GRAPHS:
                for child in attr.graphs:
                    used.update(nested_uses(child))
    return used


def clean_graph(graph: onnx.GraphProto, original_initializers: set[str]) -> None:
    while True:
        used = nested_uses(graph)
        kept = [
            node
            for node in graph.node
            if not (
                node.op_type == "Identity"
                and all(output not in used for output in node.output)
            )
        ]
        if len(kept) == len(graph.node):
            break
        del graph.node[:]
        graph.node.extend(kept)

    used = nested_uses(graph)
    kept_initializers = [item for item in graph.initializer if item.name in used]
    del graph.initializer[:]
    graph.initializer.extend(kept_initializers)
    kept_inputs = [
        item
        for item in graph.input
        if item.name not in original_initializers or item.name in used
    ]
    del graph.input[:]
    graph.input.extend(kept_inputs)


def convert(model: onnx.ModelProto, config: IntxWeightOnlyConfig) -> dict[str, int]:
    graph = model.graph
    names = Names(graph)
    initializers = {item.name: item for item in graph.initializer}
    original_initializers = set(initializers)
    producers = {output: node for node in graph.node for output in node.output if output}
    cache: dict[tuple[str, bool], tuple[str, str, str, int, int]] = {}
    new_initializers: list[onnx.TensorProto] = []
    new_nodes: list[onnx.NodeProto] = []
    converted_matmul = converted_gemm = 0

    def quantized_weight(name: str, transpose: bool):
        key = (name, transpose)
        if key in cache:
            return cache[key]
        source = np.asarray(numpy_helper.to_array(initializers[name]), dtype=np.float32)
        weight = np.ascontiguousarray(source.T if transpose else source)
        k = weight.shape[0]
        if k % GROUP_SIZE:
            raise ValueError(
                f"Eligible weight {name!r} has K={k}; K must be divisible by {GROUP_SIZE}"
            )
        packed, scales, zero_points, k = torchao_qparams(weight, config)
        suffix = "__transposed" if transpose else ""
        packed_name = names.make(name + suffix + "__torchao_int4")
        scales_name = names.make(name + suffix + "__torchao_scales")
        zp_name = names.make(name + suffix + "__torchao_zero_points")
        new_initializers.extend(
            (
                numpy_helper.from_array(packed, packed_name),
                numpy_helper.from_array(scales, scales_name),
                numpy_helper.from_array(zero_points, zp_name),
            )
        )
        cache[key] = (packed_name, scales_name, zp_name, k, weight.shape[1])
        return cache[key]

    for node in graph.node:
        spec = eligible_weight(node, initializers, producers)
        if spec is None:
            new_nodes.append(node)
            continue
        weight_name, transpose = spec
        packed, scales, zero_points, k, n = quantized_weight(weight_name, transpose)
        output = node.output[0]
        has_bias = node.op_type == "Gemm" and len(node.input) >= 3 and bool(node.input[2])
        matmul_output = names.make(output + "__torchao_matmul") if has_bias else output
        new_nodes.append(
            helper.make_node(
                "MatMulNBits",
                [node.input[0], packed, scales, zero_points],
                [matmul_output],
                name=names.make((node.name or output) + "__TorchAO_INT4"),
                domain="com.microsoft",
                K=k,
                N=n,
                bits=4,
                block_size=GROUP_SIZE,
                accuracy_level=ACCURACY_LEVEL,
            )
        )
        if has_bias:
            new_nodes.append(
                helper.make_node(
                    "Add",
                    [matmul_output, node.input[2]],
                    [output],
                    name=names.make((node.name or output) + "/BiasAdd"),
                )
            )
        if node.op_type == "MatMul":
            converted_matmul += 1
        else:
            converted_gemm += 1

    if not converted_matmul and not converted_gemm:
        raise ValueError("The model has no eligible FP32 MatMul or standard Gemm weights")
    del graph.node[:]
    graph.node.extend(new_nodes)
    graph.initializer.extend(new_initializers)
    clean_graph(graph, original_initializers)

    final_initializers = {item.name: item for item in graph.initializer}
    final_producers = {output: node for node in graph.node for output in node.output if output}
    missed = sum(
        eligible_weight(node, final_initializers, final_producers) is not None
        for node in graph.node
    )
    if missed:
        raise RuntimeError(f"Conversion left {missed} eligible FP32 linear nodes")
    return {
        "matmul": converted_matmul,
        "gemm": converted_gemm,
        "weights": len(cache),
        "fp32_matmul": sum(node.op_type == "MatMul" for node in graph.node),
        "fp32_gemm": sum(node.op_type == "Gemm" for node in graph.node),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="FP32 ONNX model")
    parser.add_argument(
        "--output", type=Path, required=True, help="new single-file INT4 ONNX model"
    )
    args = parser.parse_args()

    source = args.input.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite {output.name}")
    if torchao.__version__.split("+")[0].split(".")[:2] != ["0", "18"]:
        raise RuntimeError(f"This converter requires TorchAO 0.18, found {torchao.__version__}")

    config = IntxWeightOnlyConfig(
        weight_dtype=torch.int4,
        granularity=PerGroup(GROUP_SIZE),
        mapping_type=MappingType.ASYMMETRIC,
    )
    model = onnx.load(source, load_external_data=True)
    stats = convert(model, config)
    microsoft_imports = [
        item for item in model.opset_import if item.domain == "com.microsoft"
    ]
    if microsoft_imports:
        microsoft_imports[0].version = 1
        for duplicate in microsoft_imports[1:]:
            model.opset_import.remove(duplicate)
    else:
        model.opset_import.append(helper.make_opsetid("com.microsoft", 1))
    onnx.external_data_helper.convert_model_from_external_data(model)
    if any(onnx.external_data_helper.uses_external_data(item) for item in model.graph.initializer):
        raise RuntimeError("Failed to embed all output tensors")

    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=output.parent, prefix=f".{output.name}.", suffix=".onnx"
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        onnx.save_model(model, temporary, save_as_external_data=False)
        onnx.checker.check_model(str(temporary), full_check=False)
        if output.exists():
            raise FileExistsError(f"Refusing to overwrite {output.name}")
        temporary.chmod(0o644)
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    print(
        f"Converted {stats['matmul']} MatMul and {stats['gemm']} Gemm nodes "
        f"using {stats['weights']} TorchAO INT4 weights."
    )
    print(
        f"Kept {stats['fp32_matmul']} dynamic/unsupported MatMul and "
        f"{stats['fp32_gemm']} Gemm nodes in FP32."
    )
    print(f"Wrote one ONNX file ({output.stat().st_size / (1024 * 1024):.1f} MiB): {output.name}")


if __name__ == "__main__":
    main()
