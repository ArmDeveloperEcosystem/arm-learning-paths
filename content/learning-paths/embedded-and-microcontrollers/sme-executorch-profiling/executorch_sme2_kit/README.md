# SME2 ExecuTorch Profiling Kit

This folder contains the complete, runnable profiling framework. Copy this entire `executorch_sme2_kit/` folder into your workspace to get started.

## Quick Start

1. **Copy this kit folder to your workspace:**
   ```bash
   cp -r executorch_sme2_kit /path/to/your/workspace/executorch_sme2_kit
   cd /path/to/your/workspace/executorch_sme2_kit
   ```

2. **Set up ExecuTorch:**
   ```bash
   bash model_profiling/scripts/setup_repo.sh
   ```

3. **Build runners:**
   ```bash
   bash model_profiling/scripts/build_runners.sh
   ```

4. **Activate venv and export a model:**
   ```bash
   source .venv/bin/activate
   python model_profiling/export/export_model.py \
     --model <model_name> \
     --dtype fp16 \
     --outdir out_<model>/artifacts/
   ```

5. **Create config and run profiling pipeline:**
   ```bash
   # Copy template
   cp model_profiling/configs/templates/mac_template.json \
      model_profiling/configs/my_experiment.json
   # Edit config: set "model" to your .pte path
   # Edit config: set "output_root" to "out_<model>/runs/mac"
   
   python model_profiling/scripts/mac_pipeline.py \
     --config model_profiling/configs/my_experiment.json
   ```

6. **Analyze results:**
   ```bash
   python model_profiling/scripts/analyze_results.py \
     --run-dir out_<model>/runs/mac
   ```

## Structure

- `model_profiling/export/` - Model export script (with registry patching)
- `model_profiling/models/` - Model registry and onboarding scaffolding
- `model_profiling/scripts/` - Pipeline scripts (mac, android, analysis, setup, build)
- `model_profiling/configs/` - Configuration templates and examples
- `out_<model>/artifacts/` - Exported `.pte` files (created during export)
- `out_<model>/runs/` - Profiling results (created during pipeline runs)

**Note**: Replace `<model>` with your actual model name. The `out_<model>/` directories are created automatically when you export and run profiling.

## Adding Your Own Model

See the learning path documentation for detailed onboarding instructions. The key steps:

1. Create `model_profiling/models/<your_model>/` with:
   - `__init__.py` - Registers the model
   - `model.py` - Implements `EagerModelBase`
   - `vendor/` - (optional) vendored upstream code

2. Export using the same `export_model.py` script

3. Run the same pipeline scripts with your exported `.pte`

The pipeline is **model-agnostic** - once you export a `.pte`, everything else stays the same.

## Reference

- **Command reference**: See `model_profiling/pipeline_commands.md` for detailed workflow
- **Scripts overview**: See `model_profiling/scripts/README.md` for script documentation
- **Learning path**: See the main learning path documentation for context and examples
