---
title: Tosa Extraction
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Conversion Method
we will cover how to convert model from base python code to a .pte with a chosen backend from executorch and then directly below we shall show the steps to do that 



## Extracting the TOSA buffers

For conversion via the executorch tosa backend we are going to import the tosa spec and then convert the model as seen below 

{insert sample code}
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


This will become clearer in the next section. you will see 2 files in the "Executorch models" folder one is the tosa operators with the .tosa extension on the end and the other is the .vgf that exposes the vgf backend. the .vgf becomes important later 


