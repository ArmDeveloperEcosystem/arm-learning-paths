---
# User change
title: "Build ExecuTorch"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

For a full tutorial on building ExecuTorch please see learning path [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/).

## Install ExecuTorch

1. Upgrade pip and install build tools:

   ```bash
   pip install --upgrade pip setuptools wheel
   ```

2. Build and install the `executorch` pip package:

   ```bash
   ./install_executorch.sh
   ```

## Build troubleshooting

If the `install_executorch.sh` script fails, manually install the dependencies using the following commands:

```bash
pip install torch torchvision
pip install --no-build-isolation .
pip install --no-build-isolation third-party/ao
```

## Set up the Arm toolchain

Initialize the Arm-specific environment and accept the EULA:

1. Run the setup script:

   ```bash
   ./examples/arm/setup.sh --i-agree-to-the-contained-eula
   ```

2. Source the environment variables:

   ```bash
   source ./examples/arm/arm-scratch/setup_path.sh
   ```

## Apply the Ethos-U65 patch

As of this writing, ExecuTorch does not officially support the Ethos-U65. You must patch the `compile_spec.py` file to enable U65 compilation targets within the build system.

1. Create and apply the patch by running the following command block:

   ```bash
   cat > /tmp/patch_u65.py << 'PATCH'
   import os

   # Locate the file within the virtual environment
   filepath = "/root/executorch/.venv/lib/python3.12/site-packages/executorch/backends/arm/ethosu/compile_spec.py"

   with open(filepath, 'r') as f:
       content = f.read()

   # 1. Inject U65 Configuration Support
   old_code = '        elif "ethos-u85" in target_lower:'
   new_code = '''        elif "ethos-u65" in target_lower:
               self.tosa_spec = TosaSpecification.create_from_string("TOSA-1.0+INT")
               default_system_config = "Ethos_U65_High_End"
               default_memory_mode = "Shared_Sram"
           elif "ethos-u85" in target_lower:'''

   content = content.replace(old_code, new_code)

   # 2. Inject U65 Compile Spec Builder Logic
   old_check = '''        if "u55" in target_lower:
               return CompileSpecBuilder(
                   TosaSpecification.create_from_string("TOSA-0.80+BI+u55")
               )
           if "u85" in self.target:'''

   new_check = '''        if "u55" in target_lower:
               return CompileSpecBuilder(
                   TosaSpecification.create_from_string("TOSA-0.80+BI+u55")
               )
           if "u65" in target_lower:
               return CompileSpecBuilder(
                   TosaSpecification.create_from_string("TOSA-1.0+INT")
               )
           if "u85" in self.target:'''

   content = content.replace(old_check, new_check)

   with open(filepath, 'w') as f:
       f.write(content)

   print(f"Patched {filepath}! U65 support added.")
   PATCH

   python3 /tmp/patch_u65.py
   ```

2. Verify the patch by running:

   ```bash
   python3 -c "from executorch.backends.arm.ethosu import EthosUCompileSpec; EthosUCompileSpec(target='ethos-u65-256'); print('U65 OK')"
   ```

   If successful, you see the output `U65 OK`.

## Additional troubleshooting

1. Allocate at least 4 GB of swap space:

   ```bash
   fallocate -l 4G /swapfile
   chmod 600 /swapfile
   mkswap /swapfile
   swapon /swapfile
   ```

   Deallocate the swap space after you complete this learning path (optional):

   ```bash
   swapoff /swapfile
   rm /swapfile
   ```

   {{% notice macOS %}}

   Increase the "Swap" space in Docker settings to 4 GB: 
   ![Increase the swap space in Docker settings to 4 GB alt-text#center](./increase-swap-space-to-4-gb.jpg "Increase the swap space in Docker settings to 4 GB")

   {{% /notice %}}

2. Kill the `buck2` process if it hangs:

   ```bash 
   ps aux | grep buck
   pkill -f buck
   ```

3. Clean the build environment and reinitialize all submodules:

   ```bash
   ./install_executorch.sh --clean
   git submodule sync
   git submodule update --init --recursive
   ```

4. Try `install_executorch.sh` again:

   ```bash
   ./install_executorch.sh
   ```