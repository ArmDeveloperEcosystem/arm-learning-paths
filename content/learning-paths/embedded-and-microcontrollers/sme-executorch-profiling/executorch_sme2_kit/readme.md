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
   # Pipeline automatically runs analysis and generates CSV files
   ```

6. **View results:**
   ```bash
   # Analysis runs automatically during pipeline execution
   # Results include CSV files, pipeline_summary.json/md, and analysis_summary.json
   # Optional: Re-run analysis if needed
   python model_profiling/scripts/analyze_results.py \
     --run-dir out_<model>/runs/mac
   
   # Generate comprehensive markdown report (base report)
   python model_profiling/scripts/generate_report.py \
     --run-dir out_<model>/runs/mac
   
   # For actionable insights: Operator-specific bottleneck analysis
   python model_profiling/tools/analyze_etdump_csv.py \
     --timeline-csv out_<model>/runs/mac/<experiment>/*_all_runs_timeline.csv \
     --compare out_<model>/runs/mac/<experiment_off>/*_all_runs_timeline.csv \
     --name1 "SME2-Off" \
     --name2 "SME2-On" \
     --output-dir out_<model>/runs/mac/ \
     --verbose
   ```
   
   **Note**: The base report shows category-level breakdown. For **actionable insights** (operator-level bottlenecks, portable vs delegated analysis), use `analyze_etdump_csv.py`. See agent skill `07_report_generation.md` for complete workflow.

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

**For EdgeTAM onboarding**: See agent skill `agent_skill_ml_profiling/08_onboard_edgetam.md` for step-by-step instructions.

## Reference

- **Command reference**: See `model_profiling/pipeline_commands.md` for detailed workflow
- **Scripts overview**: See `model_profiling/scripts/readme.md` for script documentation
- **Comprehensive report generation**: See `agent_skill_ml_profiling/07_report_generation.md` for complete workflow including operator-specific bottleneck analysis, portable vs delegated operator identification, and kernel-level insights
- **Learning path**: See the main learning path documentation for context and examples
