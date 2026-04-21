---
title: More Conversions and simulations
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## VGF for NGP: other methods

in order to have the model ready for NGP we need to get the model as in the vgf file format for the purposes of this conversion we are going to take a step back and use our original model file we made and run the model converter: 

{insert code and commands}

    # code to convert the .tosa of a model to a .vgf

    tosa_path = pathlib.Path("./executorch_model/model.tosa")
    vgf_path = pathlib.Path("./executorch_model/model.vgf")

    subprocess.run(
        [
            "model_converter",
            "--input",str(tosa_path),
            "--output",str(vgf_path),
        ],
        check=True,
    )

now that we have our vgf model we can begin to test our model on certain simulations and prepare it for our pipeline. 
you will notice that we already have a .vgf file that we made earlier this is simply to show that we can take a exposed tosa operators/buffers and run the converter to get a .vgf 


## a more sublime approach?

We can lower to vgf via our own executorch vgf backend which can be seen below, this method also exposes the tosa operators but in all formats not just a specified format

Be sure to modify this code in your own testing as it is purely sample code: 


    model = some example model
    
    ep = torch.export.export(model, example_inputs) # export your model ready to be passed into the executorch api

    # VGF lowering
    compile_spec = VgfCompileSpec()    
    compile_spec.dump_intermediate_artifacts_to("executorch_model")   # default FP compile spec
    partitioner = VgfPartitioner(compile_spec)

    edge_pm = to_edge_transform_and_lower(
        ep,
        partitioner=[partitioner],
        compile_config=EdgeCompileConfig(_check_ir_validity=False),
    )

    et_pm = edge_pm.to_executorch(
        config=ExecutorchBackendConfig(extract_delegate_segments=False)
    )

    # Save .pte
    out_name = "sample_vgf.pte"
    save_pte_program(et_pm, out_name)
    print("Wrote:", os.path.abspath(out_name))

    graph_module = ep.module(check_guards=False)
    _ = graph_module.print_readable()

## Back to model explorer

Now with your new .vgf file and .pte go back to the model explorer and have a look at both models. you'll start to see how the actual model file is built and structured 


## Building the run time

in order to run theVKML we need to build the run time below is the cmake command to do that: 
    
    %%bash
    # Ensure the vulkan environment variables and MLSDK components are available on $PATH
    
    source arm-scratch/setup_path.sh

    # Compiled programs will appear in the executorch/cmake-out directory we create here.
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

{Code + commands to run vkml}
    
    import subprocess
    # Setup paths
    et_dir = os.path.join(cwd_dir) # needs mods 
    et_dir = os.path.abspath(et_dir)
    script_dir = os.path.join(et_dir, "backends", "arm", "scripts")

    args = f"--model={pte_path}"
    subprocess.run(os.path.join(script_dir, "run_vkml.sh") + " " + args, shell=True, cwd=et_dir) # modify to run on add sigmoid 

