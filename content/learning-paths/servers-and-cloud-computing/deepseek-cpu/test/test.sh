#!/bin/bash

################################################################################
# DeepSeek-CPU Learning Path - Technical Accuracy Test Script
################################################################################
#
# This script executes all bash/console commands from the Learning Path to
# verify technical accuracy and identify issues.
#
# Source: content/learning-paths/servers-and-cloud-computing/deepseek-cpu/
#
# Requirements:
#   - Arm-based server with Ubuntu 24.04 LTS
#   - At least 64 cores and 512GB RAM
#   - At least 400GB disk storage
#   - Internet connectivity for downloads
#
# Usage:
#   ./test.sh [options]
#
# Options:
#   --skip-download    Skip model download (assumes model already downloaded)
#   --skip-inference   Skip running inference test
#   --cleanup          Clean up test artifacts after completion
#   --verbose          Enable verbose output
#
################################################################################

set -e  # Exit on error
set -u  # Exit on undefined variable

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK_DIR="${SCRIPT_DIR}/.."
TEST_LOG="${SCRIPT_DIR}/test_results.log"
SKIP_DOWNLOAD=false
SKIP_INFERENCE=false
CLEANUP=false
VERBOSE=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

################################################################################
# Helper Functions
################################################################################

log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $*" | tee -a "$TEST_LOG"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $*" | tee -a "$TEST_LOG"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $*" | tee -a "$TEST_LOG"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $*" | tee -a "$TEST_LOG"
}

check_command() {
    if command -v "$1" &> /dev/null; then
        log_success "$1 is available"
        return 0
    else
        log_error "$1 is not available"
        return 1
    fi
}

check_system_requirements() {
    log "Checking system requirements..."
    
    # Check OS
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        log "OS: $NAME $VERSION"
        if [[ "$VERSION_ID" != "24.04" ]]; then
            log_warning "Expected Ubuntu 24.04, found $VERSION_ID"
        fi
    fi
    
    # Check architecture
    ARCH=$(uname -m)
    log "Architecture: $ARCH"
    if [[ "$ARCH" != "aarch64" ]]; then
        log_warning "Expected aarch64 architecture, found $ARCH"
    fi
    
    # Check CPU cores
    CORES=$(nproc)
    log "CPU Cores: $CORES"
    if [ "$CORES" -lt 64 ]; then
        log_warning "Recommended: 64+ cores, found $CORES cores"
    fi
    
    # Check RAM
    TOTAL_RAM_KB=$(grep MemTotal /proc/meminfo | awk '{print $2}')
    TOTAL_RAM_GB=$((TOTAL_RAM_KB / 1024 / 1024))
    log "Total RAM: ${TOTAL_RAM_GB}GB"
    if [ "$TOTAL_RAM_GB" -lt 512 ]; then
        log_warning "Recommended: 512GB+ RAM, found ${TOTAL_RAM_GB}GB"
    fi
    
    # Check disk space
    DISK_AVAIL_GB=$(df -BG . | tail -1 | awk '{print $4}' | sed 's/G//')
    log "Available disk space: ${DISK_AVAIL_GB}GB"
    if [ "$DISK_AVAIL_GB" -lt 400 ]; then
        log_warning "Recommended: 400GB+ free space, found ${DISK_AVAIL_GB}GB"
    fi
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --skip-download)
                SKIP_DOWNLOAD=true
                shift
                ;;
            --skip-inference)
                SKIP_INFERENCE=true
                shift
                ;;
            --cleanup)
                CLEANUP=true
                shift
                ;;
            --verbose)
                VERBOSE=true
                set -x
                shift
                ;;
            --help)
                grep "^#" "$0" | grep -v "^#!/" | sed 's/^# //'
                exit 0
                ;;
            *)
                log_error "Unknown option: $1"
                exit 1
                ;;
        esac
    done
}

################################################################################
# Test Sections (Following Learning Path Order)
################################################################################

test_section_1_install_dependencies() {
    log "========================================================================"
    log "Section 1: Install build dependencies"
    log "========================================================================"
    
    log "Updating package lists..."
    sudo apt update
    
    log "Installing make and cmake..."
    sudo apt install make cmake -y
    
    log "Installing gcc and g++..."
    sudo apt install gcc g++ -y
    sudo apt install build-essential -y
    
    # Verify installations
    check_command gcc
    check_command g++
    check_command cmake
    check_command make
    
    # Check versions
    log "gcc version: $(gcc --version | head -n1)"
    log "g++ version: $(g++ --version | head -n1)"
    log "cmake version: $(cmake --version | head -n1)"
    
    log_success "Dependencies installed successfully"
}

test_section_2_build_llama_cpp() {
    log "========================================================================"
    log "Section 2: Clone and build llama.cpp"
    log "========================================================================"
    
    cd "$WORK_DIR"
    
    # Clone if not exists
    if [ ! -d "llama.cpp" ]; then
        log "Cloning llama.cpp repository..."
        git clone https://github.com/ggerganov/llama.cpp
    else
        log "llama.cpp directory already exists, using existing clone"
    fi
    
    cd llama.cpp
    
    # Record commit for reproducibility
    COMMIT_HASH=$(git rev-parse HEAD)
    log "Building llama.cpp at commit: $COMMIT_HASH"
    
    log "Creating build directory..."
    mkdir -p build
    cd build
    
    log "Running cmake with Arm optimizations..."
    cmake .. -DCMAKE_CXX_FLAGS="-mcpu=native" -DCMAKE_C_FLAGS="-mcpu=native"
    
    log "Building llama.cpp (this may take several minutes)..."
    cmake --build . --config Release -v -j $(nproc)
    
    log "Checking build artifacts..."
    cd bin
    if [ -f "./llama-cli" ]; then
        log_success "llama-cli built successfully"
    else
        log_error "llama-cli binary not found"
        return 1
    fi
    
    if [ -f "./llama-server" ]; then
        log_success "llama-server built successfully"
    else
        log_error "llama-server binary not found"
        return 1
    fi
    
    log "Testing llama-cli help output..."
    ./llama-cli -h > /dev/null 2>&1 && log_success "llama-cli help command works" || log_error "llama-cli help command failed"
    
    log_success "llama.cpp built successfully"
}

test_section_3_setup_huggingface() {
    log "========================================================================"
    log "Section 3: Set up Hugging Face and download model"
    log "========================================================================"
    
    cd "$WORK_DIR"
    
    log "Installing Python dependencies..."
    sudo apt install python-is-python3 python3-pip python3-venv -y
    
    log "Creating Python virtual environment..."
    if [ ! -d "venv" ]; then
        python -m venv venv
    fi
    
    log "Activating virtual environment..."
    source venv/bin/activate
    
    log "Installing huggingface_hub..."
    pip install huggingface_hub
    
    # Verify installation
    if pip show huggingface_hub > /dev/null 2>&1; then
        VERSION=$(pip show huggingface_hub | grep Version | awk '{print $2}')
        log_success "huggingface_hub installed (version: $VERSION)"
    else
        log_error "huggingface_hub installation failed"
        return 1
    fi
    
    if [ "$SKIP_DOWNLOAD" = false ]; then
        log "Downloading DeepSeek-R1 model (this will take a long time and use ~354GB)..."
        log_warning "Model download can take hours depending on connection speed"
        
        # Download with error handling
        if huggingface-cli download bartowski/DeepSeek-R1-GGUF \
            --include "*DeepSeek-R1-Q4_0*" \
            --local-dir DeepSeek-R1-Q4_0; then
            log_success "Model downloaded successfully"
        else
            log_error "Model download failed"
            return 1
        fi
        
        # Verify model files
        MODEL_PATH="DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0-00001-of-00010.gguf"
        if [ -f "$MODEL_PATH" ]; then
            log_success "Model file found: $MODEL_PATH"
            MODEL_SIZE=$(du -h "$MODEL_PATH" | cut -f1)
            log "Model file size: $MODEL_SIZE"
        else
            log_error "Model file not found: $MODEL_PATH"
            log "Available files in DeepSeek-R1-Q4_0:"
            find DeepSeek-R1-Q4_0 -type f 2>/dev/null || log "Directory not found"
            return 1
        fi
    else
        log "Skipping model download (--skip-download specified)"
    fi
    
    log_success "Hugging Face setup completed"
}

test_section_4_run_chatbot() {
    log "========================================================================"
    log "Section 4: Run DeepSeek-R1 Chatbot"
    log "========================================================================"
    
    if [ "$SKIP_INFERENCE" = true ]; then
        log "Skipping inference test (--skip-inference specified)"
        return 0
    fi
    
    cd "$WORK_DIR/llama.cpp/build/bin"
    
    MODEL_PATH="../../../DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0-00001-of-00010.gguf"
    
    if [ ! -f "$MODEL_PATH" ]; then
        log_error "Model file not found: $MODEL_PATH"
        log "Cannot run inference without model"
        return 1
    fi
    
    log "Running inference with DeepSeek-R1 model..."
    log_warning "This will take several minutes and use significant resources"
    
    # Run with timeout to prevent hanging
    timeout 600 ./llama-cli \
        -m "$MODEL_PATH" \
        -no-cnv \
        --temp 0.6 \
        -t 64 \
        --prompt "<|User|>Building a visually appealing website can be done in ten simple steps:<｜Assistant｜>" \
        -n 512 \
        > "${SCRIPT_DIR}/inference_output.txt" 2>&1 || {
            log_error "Inference failed or timed out"
            return 1
        }
    
    log "Checking inference output..."
    if grep -q "llama_perf_context_print" "${SCRIPT_DIR}/inference_output.txt"; then
        log_success "Inference completed successfully"
        
        # Extract performance metrics
        log "Performance metrics:"
        grep "llama_perf" "${SCRIPT_DIR}/inference_output.txt" | while read -r line; do
            log "  $line"
        done
        
        # Check for Arm optimizations
        if grep -q "MATMUL_INT8 = 1" "${SCRIPT_DIR}/inference_output.txt"; then
            log_success "Arm MATMUL_INT8 optimization detected"
        fi
        
        if grep -q "SVE = 1" "${SCRIPT_DIR}/inference_output.txt"; then
            log_success "Arm SVE optimization detected"
        fi
    else
        log_error "Inference output appears incomplete"
        return 1
    fi
    
    log_success "Chatbot test completed"
}

test_section_5_api_server() {
    log "========================================================================"
    log "Section 5: Test API Server"
    log "========================================================================"
    
    if [ "$SKIP_INFERENCE" = true ]; then
        log "Skipping API server test (--skip-inference specified)"
        return 0
    fi
    
    cd "$WORK_DIR"
    
    log "Installing jq..."
    sudo apt install jq -y
    
    MODEL_PATH="DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0-00001-of-00010.gguf"
    
    if [ ! -f "$MODEL_PATH" ]; then
        log_error "Model file not found: $MODEL_PATH"
        return 1
    fi
    
    log "Starting llama-server in background..."
    cd llama.cpp/build/bin
    ./llama-server -m "../../../$MODEL_PATH" --port 8080 > "${SCRIPT_DIR}/server_output.txt" 2>&1 &
    SERVER_PID=$!
    
    log "Server PID: $SERVER_PID"
    log "Waiting for server to start..."
    sleep 30
    
    # Check if server is running
    if ! ps -p $SERVER_PID > /dev/null; then
        log_error "Server failed to start"
        cat "${SCRIPT_DIR}/server_output.txt"
        return 1
    fi
    
    log "Testing curl API call..."
    cd "$WORK_DIR"
    
    cat > "${SCRIPT_DIR}/curl-test.sh" << 'EOF'
curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json" -d '{
    "model": "any-model",
    "messages": [
      {
        "role": "system",
        "content": "You are a coding assistant, skilled in programming."
      },
      {
        "role": "user",
        "content": "Write a hello world program in C++."
      }
    ]
  }' 2>/dev/null | jq -C
EOF
    
    chmod +x "${SCRIPT_DIR}/curl-test.sh"
    
    if bash "${SCRIPT_DIR}/curl-test.sh" > "${SCRIPT_DIR}/curl_output.json" 2>&1; then
        log_success "curl API call succeeded"
        
        # Verify JSON response
        if jq -e '.choices[0].message.content' "${SCRIPT_DIR}/curl_output.json" > /dev/null 2>&1; then
            log_success "Valid JSON response received"
        else
            log_error "Invalid JSON response"
        fi
    else
        log_error "curl API call failed"
    fi
    
    log "Testing Python API access..."
    
    # Activate venv
    source venv/bin/activate
    
    log "Installing openai Python package..."
    pip install openai==1.55.3
    
    cat > "${SCRIPT_DIR}/python-test.py" << 'EOF'
from openai import OpenAI

client = OpenAI(
        base_url='http://localhost:8080/v1',
        api_key='no-key'
        )

completion = client.chat.completions.create(
  model="not-used",
  messages=[
    {"role": "system", "content": "You are a coding assistant, skilled in programming."},
    {"role": "user", "content": "Write a hello world program in C++."}
  ],
  stream=True,
)

for chunk in completion:
  print(chunk.choices[0].delta.content or "", end="")
EOF
    
    if timeout 120 python "${SCRIPT_DIR}/python-test.py" > "${SCRIPT_DIR}/python_output.txt" 2>&1; then
        log_success "Python API call succeeded"
    else
        log_error "Python API call failed or timed out"
    fi
    
    log "Stopping server..."
    kill $SERVER_PID 2>/dev/null || true
    wait $SERVER_PID 2>/dev/null || true
    
    log_success "API server tests completed"
}

cleanup_test_artifacts() {
    if [ "$CLEANUP" = false ]; then
        log "Skipping cleanup (use --cleanup to remove test artifacts)"
        return 0
    fi
    
    log "========================================================================"
    log "Cleanup: Removing test artifacts"
    log "========================================================================"
    
    cd "$WORK_DIR"
    
    log "Deactivating virtual environment..."
    deactivate 2>/dev/null || true
    
    log "Removing build artifacts (keeping source)..."
    if [ -d "llama.cpp/build" ]; then
        rm -rf llama.cpp/build
        log "Removed llama.cpp/build"
    fi
    
    log "Removing virtual environments..."
    rm -rf venv pytest 2>/dev/null || true
    
    log "Note: Model files and llama.cpp source code retained"
    log "To fully clean up, manually remove:"
    log "  - DeepSeek-R1-Q4_0/ (model files, ~354GB)"
    log "  - llama.cpp/ (source code)"
    
    log_success "Cleanup completed"
}

################################################################################
# Main Test Execution
################################################################################

main() {
    log "========================================================================"
    log "DeepSeek-CPU Learning Path - Technical Accuracy Test"
    log "========================================================================"
    log "Start time: $(date)"
    log "Working directory: $WORK_DIR"
    log "Test log: $TEST_LOG"
    log ""
    
    parse_args "$@"
    
    # System checks
    check_system_requirements
    log ""
    
    # Run test sections
    test_section_1_install_dependencies
    log ""
    
    test_section_2_build_llama_cpp
    log ""
    
    test_section_3_setup_huggingface
    log ""
    
    test_section_4_run_chatbot
    log ""
    
    test_section_5_api_server
    log ""
    
    # Cleanup if requested
    cleanup_test_artifacts
    log ""
    
    log "========================================================================"
    log "Test completed successfully!"
    log "End time: $(date)"
    log "========================================================================"
    log ""
    log "Test results saved to: $TEST_LOG"
    log "Review the log for any warnings or issues."
}

# Run main function with all arguments
main "$@"
