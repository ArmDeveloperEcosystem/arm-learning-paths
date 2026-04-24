---
title: Tosa extraction
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why extract TOSA?
When working with the ExecuTorch pipeline it can be really important to **extract and inspect TOSA buffers**. This isn’t just an implementation detail; 

it’s a key step for understanding and debugging how your model is actually being executed.

TOSA (Tensor Operator Set Architecture) acts as an **intermediate representation (IR)** in the pipeline. Your original model (e.g. PyTorch) is first lowered into TOSA before being further compiled into a backend-specific format such as VGF or Ethos-U. By extracting the TOSA buffers, you get a view of the model at a **stable, hardware-agnostic stage** — before backend-specific transformations are applied.

This is useful for several reasons:

- **Debugging correctness**: If the final output is wrong, inspecting TOSA lets we check whether the issue was introduced early (during model conversion) or later (during backend lowering).
- **Understanding operator coverage**: you can see exactly which operations your model was converted into, and whether any were decomposed, approximated, or unsupported.
- **Tracking data transformations**: TOSA buffers show tensor shapes, layouts, and quantisation parameters, helping you verify that data is being handled as expected.
- **Comparing backends**: Since multiple backends (CPU, Vulkan, NPU) all start from TOSA, it provides a common reference point when behaviour differs between them.
- **Performance investigation**: incomplete optimisation can often be spotted at the TOSA level before they propagate into inefficient backend execution.

In short, extracting TOSA buffers gives you a **transparent checkpoint in the pipeline**. It helps you answer the critical question:  

> “Is my model being represented correctly before it gets compiled for hardware?”

For learners moving beyond high-level tools, this step builds the insight needed to confidently debug, optimise, and customise model deployment.



## Extracting the TOSA buffers

For conversion via the executorch tosa backend we are going to import the tosa spec and then convert the model as seen below. Please note that this function is only 1 approach as there are not only floating point representations of these models. 



    from pathlib import Path
    from executorch.exir import to_edge_transform_and_lower, EdgeCompileConfig
    from executorch.backends.arm.tosa import TosaSpecification
    from executorch.backends.arm.tosa.compile_spec import TosaCompileSpec
    from executorch.backends.arm.util._factory import create_partitioner


    BASE_DUMP = Path("tosa-dump")

    def dump_tosa(ep, profile_str: str, label: str):
        BASE_DUMP.mkdir(parents=True, exist_ok=True)

        tosa_spec = TosaSpecification.create_from_string(profile_str)
        compile_spec = TosaCompileSpec(tosa_spec)

        # Force ALL artifacts into the same folder
        compile_spec.dump_intermediate_artifacts_to(str(BASE_DUMP))

        partitioner = create_partitioner(compile_spec)

        _ = to_edge_transform_and_lower(
            ep,
            partitioner=[partitioner],
            compile_config=EdgeCompileConfig(_check_ir_validity=False),
        )

        tosa_files = list(BASE_DUMP.rglob("*.tosa"))

        print(f"\n{label}")
        print(f"  Profile: {profile_str}")
        print(f"  Dump dir: {BASE_DUMP.resolve()}")
        print(f"  Total .tosa files so far: {len(tosa_files)}")

    dump_tosa(exported_model, "TOSA-1.0+FP",
        "AddSigmoidModel (float)")


In the next section we will use this tosa exposure to view the operations inside our model via the "Model-explorer". the file for this exposed backend can be seen in the  


