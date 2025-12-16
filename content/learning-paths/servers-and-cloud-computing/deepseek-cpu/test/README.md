# DeepSeek-CPU Learning Path - Test Suite

This directory contains testing and maintenance resources for the DeepSeek-CPU Learning Path.

## Files

### summary.txt
A comprehensive technical accuracy review document that identifies:
- Current status of OS versions, software dependencies, and external resources
- Potential issues that need investigation
- Recommendations for keeping the Learning Path up to date
- Regular maintenance schedule suggestions

**Review Date:** December 16, 2025

### test.sh
An automated test script that executes all commands from the Learning Path to verify technical accuracy.

## Using the Test Script

### Prerequisites

To run the complete test suite, you need:
- An Arm-based server (e.g., AWS Graviton4 r8g.24xlarge)
- Ubuntu 24.04 LTS
- At least 64 CPU cores
- At least 512GB RAM
- At least 400GB free disk storage
- Internet connectivity for downloads

### Basic Usage

Run the full test suite:
```bash
cd /path/to/deepseek-cpu/test
./test.sh
```

### Test Options

The script supports several options to customize testing:

**Skip model download** (use if model is already downloaded):
```bash
./test.sh --skip-download
```

**Skip inference tests** (faster, doesn't run the model):
```bash
./test.sh --skip-inference
```

**Clean up artifacts after testing**:
```bash
./test.sh --cleanup
```

**Enable verbose output**:
```bash
./test.sh --verbose
```

**Combine multiple options**:
```bash
./test.sh --skip-download --skip-inference --cleanup
```

**View help**:
```bash
./test.sh --help
```

### Test Output

The script produces several output files in the test directory:

- `test_results.log` - Complete log of all test operations
- `inference_output.txt` - Output from running the LLM inference
- `server_output.txt` - Output from the llama-server
- `curl_output.json` - API response from curl test
- `python_output.txt` - Output from Python API test
- `curl-test.sh` - Generated curl test script
- `python-test.py` - Generated Python test script

### What the Test Script Validates

The script tests all major sections of the Learning Path:

1. **System Requirements**: Checks OS version, CPU cores, RAM, disk space
2. **Dependencies**: Installs and verifies build tools (gcc, cmake, etc.)
3. **llama.cpp Build**: Clones and compiles llama.cpp with Arm optimizations
4. **Model Download**: Downloads DeepSeek-R1 model from Hugging Face
5. **Inference Test**: Runs the chatbot and validates output
6. **API Server**: Tests both curl and Python API access methods

### Expected Runtime

**Full test** (including model download):
- Time: 2-4 hours (depending on network speed)
- Disk usage: ~354GB for model
- Cost: Significant (running large Arm instance)

**Quick test** (skip download and inference):
- Time: 10-15 minutes
- Disk usage: Minimal
- Cost: Lower

### Troubleshooting

**Model download fails:**
- Check internet connectivity
- Verify Hugging Face is accessible
- Ensure sufficient disk space
- Try manual download using huggingface-cli

**Build fails:**
- Verify all dependencies are installed
- Check gcc/cmake versions
- Ensure sufficient memory for compilation

**Inference fails or runs out of memory:**
- Verify instance has 512GB+ RAM
- Check model files are complete
- Try reducing thread count (-t flag)

**Server won't start:**
- Check port 8080 is available
- Verify model path is correct
- Review server_output.txt for errors

## Maintenance Schedule

Based on the technical review, we recommend:

### Quarterly (Every 3 Months)
- Run this test script on a Graviton4 instance
- Verify model is still available from Hugging Face
- Check for llama.cpp updates
- Test all external links
- Review Python package versions

### Annual
- Re-evaluate OS version (Ubuntu LTS)
- Update hardware recommendations
- Refresh performance benchmarks
- Check for new DeepSeek model releases

### Ad-hoc
- When llama.cpp releases major updates
- When users report issues
- When external links break
- When DeepSeek releases new models

## Integration with CI/CD

This test script can be integrated into automated testing pipelines:

```bash
# Example GitHub Actions workflow
- name: Test Learning Path
  run: |
    cd content/learning-paths/servers-and-cloud-computing/deepseek-cpu/test
    ./test.sh --skip-inference --verbose
```

For full testing including inference, consider:
- Running on dedicated Arm hardware
- Caching model downloads between runs
- Setting appropriate timeouts
- Monitoring resource usage

## Contributing

When updating the Learning Path:

1. Review `summary.txt` for known issues
2. Update the main markdown files
3. Run `test.sh` to verify changes
4. Update `summary.txt` if findings change
5. Update test script if new commands are added

## Support

For issues with:
- **The Learning Path content**: Create an issue in the repository
- **DeepSeek model**: Check DeepSeek-AI GitHub and Hugging Face
- **llama.cpp**: Check llama.cpp GitHub repository
- **This test suite**: Review test_results.log for details

## License

This test suite follows the same license as the main repository.
