---
title: "Export a reference model (.pte + .etrecord)"
weight: 6
layout: "learningpathall"
---

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/step04_export.svg"
    alt="Outcome: model exported to .pte and .etrecord"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Outcome: a runnable program and operator metadata for analysis.
  </span>
</p>

## Goal of this step

Export a small model to ExecuTorch so it can be executed by the runners you built. The export step creates:
- a `.pte` program (what `executor_runner` runs), and
- a `.etrecord` file (metadata used to map runtime events back to operator names during analysis).

**Time:** ~1 minute (MobileNet is small)

## Export the reference model

```bash
python scripts/export_model.py \
  --model-name mobilenet_v3_small \
  --out models/mobilenet_v3_small_fp16.pte \
  --dtype fp16
```

{{% notice Note %}}
This learning path uses FP16 to keep iteration fast and to make SME2 effects easy to observe when running on Armv9-class hardware.
{{% /notice %}}

## What you just created

```bash
ls -lh models/mobilenet_v3_small_fp16.*
```

Expected output:
- `mobilenet_v3_small_fp16.pte` (~5 MB): Runnable program
- `mobilenet_v3_small_fp16.pte.etrecord` (~200 KB): Operator metadata for profiling

**Keep these together!** If you move the `.pte`, move the `.etrecord` too.

<details>
  <summary><strong>What the export script is doing</strong> (conceptual)</summary>

```python
from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.exir import to_edge_transform_and_lower

exported = torch.export.export(model, example_inputs, strict=False)
edge = to_edge_transform_and_lower(
    exported, 
    partitioner=[XnnpackPartitioner()],  # Delegates conv/linear to XNNPACK
    generate_etrecord=True                # Critical for operator-level profiling
)
et = edge.to_executorch()

Path("model.pte").write_bytes(et.buffer)
et.get_etrecord().save("model.pte.etrecord")  # Don't skip this!
```
  <p><strong>Why XNNPACK:</strong> it is where the optimized kernels live (including SME2 paths via Arm Kleidi). Delegation coverage shows up later as kernel hints in analysis.</p>
</details>

## Validation

```bash
python scripts/validate_setup.py --model models/mobilenet_v3_small_fp16.pte
```

Expected: Green checkmarks for `.pte` file structure and `.etrecord` presence.

---

**Next:** Run the Mac pipeline and collect traces and metrics.
