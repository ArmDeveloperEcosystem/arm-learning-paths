---
title: More Conversions and simulations
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## VGF for NGP: other methods

in order to have the model ready for NGP we need to get the model as in the vgf file format for the purposes of this conversion we are going to take a step back and use our original model file we made and run the model converter: 


    # code to convert the .tosa of a model to a .vgf

    tosa_path = pathlib.Path("./executorch-model/model.tosa")
    vgf_path = pathlib.Path("./executorch-model/model.vgf")

    subprocess.run(
        [
            "model_converter",
            "--input",str(tosa_path),
            "--output",str(vgf_path),
        ],
        check=True,
    )

Now that we have a .vgf file we have prepared the model for Neural technology such as plugging it into a vulkan app. 

Below is a more sublime approach and a worked example of emulating the model on the VKML 

What is important however is to have a look at the generated .vgf on the model explorer to see the differences between our exposed tosa delegation. 


## a more sublime approach?

We can lower to vgf via our own ExecuTorch vgf backend which can be seen below, this method also exposes the tosa operators but in all formats not just a specified format

Be sure to modify this code in your own testing as it is purely sample code: 

    from executorch.backends.arm.vgf import VgfCompileSpec, VgfPartitioner
    from executorch.exir import (
        EdgeCompileConfig,
        ExecutorchBackendConfig,
        to_edge_transform_and_lower,
    )
    from executorch.extension.export_util.utils import save_pte_program
    import os
    import torch

    os.makedirs("executorch-model", exist_ok=True)


    # VGF lowering
    compile_spec = VgfCompileSpec()    
    compile_spec.dump_intermediate_artifacts_to("executorch-model")   # default FP compile spec
    partitioner = VgfPartitioner(compile_spec)

    edge_pm = to_edge_transform_and_lower(
        exported_model,
        partitioner=[partitioner],
        compile_config=EdgeCompileConfig(_check_ir_validity=False),
    )

    et_pm = edge_pm.to_executorch(
        config=ExecutorchBackendConfig(extract_delegate_segments=False)
    )

    # Save .pte
    cwd_dir = os.getcwd()
    pte_base_name = "as-vgf"
    out_name = pte_base_name + ".pte"
    save_pte_program(et_pm, out_name)
    print("Wrote:", os.path.abspath(out_name))
    pte_path = os.path.join(cwd_dir, out_name)

    graph_module = exported_model.module(check_guards=False)
    _ = graph_module.print_readable() # for visibility 

## Back to model explorer

Now with your new .vgf file and .pte go back to the model explorer and have a look at both models. you'll start to see how the actual model file is built and structured. 

Run a comparison with our pathway that we have taken in the rest of this learning pathway but bear in mind why we have extracted the tosa flatbuffers before 

to continue with the steps below  you will need to run the above code with the add sigmoid model as the VKML takes in a .pte 


# Extensions - not necessary for preparation but good to have a look at for functionality. 

Please note that to run this extension path that you should use the code snippet directly above tomake a .pte

## Building the run time

in order to run the VKML we need to build the run time below is the cmake command to do that: 
    
    %%bash
    # Ensure the vulkan environment variables and MLSDK components are available on $PATH
    source repo/executorch/examples/arm/arm-scratch/setup_path.sh
    cd repo/executorch/examples/arm

    # Compiled programs will appear in the executorch/cmake-out directory we create here.
    # Build example executor runner application to examples/arm/vgf_minimal_example
    cmake \
    -DCMAKE_INSTALL_PREFIX=cmake-out \
    -DCMAKE_BUILD_TYPE=Debug \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_NAMED_DATA_MAP=ON \
    -DEXECUTORCH_BUILD_EXTENSION_FLAT_TENSOR=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_XNNPACK=OFF \
    -DEXECUTORCH_BUILD_VULKAN=ON \
    -DEXECUTORCH_BUILD_VGF=ON \
    -DEXECUTORCH_ENABLE_LOGGING=ON \
    -DPYTHON_EXECUTABLE=python \
    -B../../cmake-out-vkml ../..

    cmake --build ../../cmake-out-vkml --target executor_runner




## VKML run

we will now run our model on the VKML to see it's speed and correctness. The default inputs are a set of 1's so we should expect a result close to 2

this set of commands assumes your current setup for base is in the executorch repo: 

note that we can only run the VKML on .pte so if you wish to use it then you stick to the executorch flow above 

    import subprocess

    cwd_dir = os.getcwd()

    # Setup paths
    et_dir = os.path.join(cwd_dir)

    script_dir = os.path.join(et_dir, "repo", "executorch" ,"backends", "arm", "scripts")
    et_dir = os.path.join(et_dir, "repo" , "executorch")

    args = f"--model={pte_path}"
    subprocess.run(os.path.join(script_dir, "run_vkml.sh") + " " + args, shell=True, cwd=et_dir)


    
    In our output we can see: 

    outputX 0: tensor(sizes = [1,1,1,1], [0.880797])

    this final output value of 0.88797 is a presigmoid value of 2 whic is what we expect

 