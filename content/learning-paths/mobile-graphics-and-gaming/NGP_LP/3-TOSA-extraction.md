---
title: Tosa Extraction
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is TOSA and why are we exposing it
TOSA (Tensor Operator Set Architecture) is a standardised intermediate representation for machine learning workloads, designed to provide a consistent and hardware-agnostic description of neural network operations.

In practice, it acts as a bridge between high-level ML frameworks and low-level hardware implementations. Models from frameworks like TensorFlow or PyTorch can be lowered into TOSA, and from there compiled efficiently onto a wide range of targets, including CPUs, GPUs, and dedicated NPUs.

We expose TOSA in this workflow to make that process visible and understandable, it's not a necesary step in the case of using executorch as you will see later.

Rather than treating model deployment as a black box, TOSA highlights:

- The structured sequence of operations that make up the model
- How those operations are standardised and simplified
- Where optimisation and hardware-specific mapping take place





## Extracting the TOSA buffers

For conversion via the executorch tosa backend we are going to import the tosa spec and then convert the model as seen below: 

    
    from pathlib import Path
    BASE_DUMP = Path("Tosa_dump")
    
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


The next section will explore how we visualise the models


