#!/usr/bin/env python3
"""Parse XNNPACK verbose log (xnntrace.log) to microkernel counts and metadata.

Input: a single run verbose trace produced by executor_runner with XNN logging.
Output CSV columns:
  model_id,kernel_name,category,count,dtype,xnn_op,variant,ukernel_shape,arch_chain,has_sme,has_sme2

Notes:
- XNN logs include lines like:
  Using binary microkernel 'xnn_f32_vadd_ukernel__neon_u8'
- Kernel naming schema (approx.):
  xnn_<dtype>_<op>_<variant?>_ukernel_<shape?>__<arch>_<microarch...>
  We extract components to aid backend/microarch attribution (e.g., SME/SME2).
"""

import argparse
import csv
import re
from pathlib import Path
from collections import Counter
from typing import Dict


LINE_RE = re.compile(r"Using\s+(?P<cat>\w+)\s+microkernel\s+'(?P<kernel>[^']+)'", re.IGNORECASE)


def parse_kernel_name(name: str) -> Dict[str, str]:
    # Example: xnn_f32_igemm_minmax_ukernel_4x8__aarch64_neonfma_cortex_a75
    out = {
        "dtype": "",
        "xnn_op": "",
        "variant": "",
        "ukernel_shape": "",
        "arch_chain": "",
        "has_sme": "0",
        "has_sme2": "0",
    }
    if not name:
        return out
    base = name
    arch = ""
    if "__" in name:
        base, arch = name.split("__", 1)
        out["arch_chain"] = arch
        s = arch.lower()
        if "sme2" in s:
            out["has_sme2"] = "1"
        if "sme" in s:
            out["has_sme"] = "1"
    parts = base.split("_")
    # Expect: xnn, dtype, op, variant?, ukernel, shape?
    if len(parts) >= 3:
        out["dtype"] = parts[1]
        out["xnn_op"] = parts[2]
    if "ukernel" in parts:
        uk_idx = parts.index("ukernel")
        # variant is what's between op and ukernel if present
        if uk_idx - 1 >= 3:
            out["variant"] = parts[3]
        # shape after ukernel if present
        if uk_idx + 1 < len(parts):
            out["ukernel_shape"] = parts[uk_idx + 1]
    return out


def parse_xnntrace(path: Path, model_id: str):
    counts = Counter()
    categories = {}
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = LINE_RE.search(line)
            if not m:
                continue
            kernel = m.group("kernel").strip()
            cat = m.group("cat").lower()
            # normalize some category aliases
            if cat in {"transposec", "transpose"}:
                cat = "transpose"
            counts[kernel] += 1
            categories[kernel] = cat
    rows = []
    for kernel, cnt in counts.most_common():
        meta = parse_kernel_name(kernel)
        rows.append({
            "model_id": model_id,
            "kernel_name": kernel,
            "category": categories.get(kernel, "unknown"),
            "count": cnt,
            **meta,
        })
    return rows


def write_csv(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "model_id",
                "kernel_name",
                "category",
                "count",
                "dtype",
                "xnn_op",
                "variant",
                "ukernel_shape",
                "arch_chain",
                "has_sme",
                "has_sme2",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main():
    ap = argparse.ArgumentParser(description="Convert xnntrace.log to microkernel counts CSV")
    ap.add_argument("--xnntrace", required=True, help="Path to xnntrace.log")
    ap.add_argument("--out", required=True, help="Output CSV path")
    ap.add_argument("--model-id", help="Optional model identifier to embed in output; defaults to file stem")
    args = ap.parse_args()

    model_id = args.model_id or Path(args.xnntrace).stem
    rows = parse_xnntrace(Path(args.xnntrace), model_id)
    write_csv(Path(args.out), rows)
    print(f"Wrote {len(rows)} kernel rows to {args.out}")


if __name__ == "__main__":
    main()
