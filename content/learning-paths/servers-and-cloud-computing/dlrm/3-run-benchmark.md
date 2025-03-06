---
title: Run the benchmark
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The final step is to run the benchmark.

## Download patches

Start by downloading the patches which will be applied during setup.

```bash
wget -r --no-parent https://github.com/ArmDeveloperEcosystem/arm-learning-paths/tree/main/content/learning-paths/servers-and-cloud-computing/dlrm/mlpef_patches $HOME/mlperf_patches
```

## Benchmark script

You will now create a script that automates the setup, configuration, and execution of MLPerf benchmarking for the DLRM (Deep Learning Recommendation Model) inside a Docker container. It simplifies the process by handling dependency installation, model preparation, and benchmarking in a single run. Create a new file called `run_dlrm_benchmark.sh`. Paste the code below.

```bash
#!/bin/bash

set -ex
yellow="\e[33m"
reset="\e[0m"

data_type=${1:-"int8"}

echo -e "${yellow}Data type chosen for the setup is $data_type${reset}"

# Setup directories
data_dir=$HOME/data/
model_dir=$HOME/model/
results_dir=$HOME/results/
dlrm_container="benchmark_dlrm"

mkdir -p $results_dir/$data_type

###### Run the dlrm container and setup MLPerf #######

echo -e "${yellow}Checking if the container '$dlrm_container' exists...${reset}"
container_exists=$(docker ps -aqf "name=^$dlrm_container$")

if [ -n "$container_exists" ]; then
    echo "${yellow}Container '$dlrm_container' already exists.${reset}"
else
    echo "Creating a new '$dlrm_container' container..."
    docker run -td --shm-size=200G --privileged \
        -v $data_dir:$data_dir \
        -v $model_dir:$model_dir \
        -v $results_dir:$results_dir \
        -e DATA_DIR=$data_dir \
        -e MODEL_DIR=$model_dir \
        -e PATH=/opt/conda/bin:$PATH \
        --name=$dlrm_container \
        toolsolutions-pytorch:latest
fi

echo -e "${yellow}Setting up MLPerf inside the container...${reset}"
docker cp $HOME/mlperf_patches $dlrm_container:$HOME/
docker exec -it $dlrm_container bash -c "
    set -ex
    sudo apt update && sudo apt install -y \
        software-properties-common lsb-release scons \
        build-essential libtool autoconf unzip git vim wget \
        numactl cmake gcc-12 g++-12 python3-pip python-is-python3
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12 --slave /usr/bin/g++ g++ /usr/bin/g++-12

    if [ ! -d \"/opt/conda\" ]; then
        wget -O \"$HOME/miniconda.sh\" https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
        chmod +x \"$HOME/miniconda.sh\"
        sudo bash \"$HOME/miniconda.sh\" -b -p /opt/conda
        rm \"$HOME/miniconda.sh\"
    fi
    export PATH=\"/opt/conda/bin:$PATH\"
    /opt/conda/bin/conda install -y python=3.10.12
    /opt/conda/bin/conda install -y -c conda-forge cmake gperftools numpy==1.23.0 ninja pyyaml setuptools

    git clone --recurse-submodules https://github.com/mlcommons/inference.git inference || (cd inference ; git pull)
    cd inference && git submodule update --init --recursive && cd loadgen
    CFLAGS=\"-std=c++14\" python setup.py bdist_wheel
    pip install dist/*.whl

    rm -rf inference_results_v4.0
    git clone https://github.com/mlcommons/inference_results_v4.0.git
    cd inference_results_v4.0 && git checkout ceef1ea

    if [ \"$data_type\" = \"fp32\" ]; then
        git apply $HOME/mlperf_patches/arm_fp32.patch
    else
        git apply $HOME/mlperf_patches/arm_int8.patch
    fi
"

echo -e "${yellow}Checking for dumped FP32 model...${reset}"
dumped_fp32_model="dlrm-multihot-pytorch.pt"
int8_model="aarch64_dlrm_int8.pt"
dlrm_test_path="$HOME/inference_results_v4.0/closed/Intel/code/dlrm-v2-99.9/pytorch-cpu-int8"

if [ ! -f "$HOME/model/$dumped_fp32_model" ]; then
    echo -e "${yellow}Dumping model weights...${reset}"
    docker exec -it "$dlrm_container" bash -c "
        pip install -r --extra-index-url https://download.pytorch.org/whl/nightly/cpu tensordict==0.1.2 torchsnapshot==0.1.0 fbgemm_gpu==2025.1.22+cpu torchrec==1.1.0.dev20250127+cpu
    "
    docker exec -it "$dlrm_container" bash -c "
        cd $dlrm_test_path && python python/dump_torch_model.py --model-path=$model_dir/model_weights --dataset-path=$data_dir
    "
fi

echo -e "${yellow}Checking if INT8 model calibration is required...${reset}"
if [ "$data_type" == "int8" ] && [ ! -f "$HOME/model/$int8_model" ]; then
    echo -e "${yellow}Running INT8 calibration...${reset}"
    docker exec -it "$dlrm_container" bash -c "cd $dlrm_test_path && ./run_calibration.sh"
fi

echo -e "${yellow}Running offline test...${reset}"
docker exec -it "$dlrm_container" bash -c "cd $dlrm_test_path && bash run_main.sh offline $data_type"

echo -e "${yellow}Copying results to host...${reset}"
docker exec -it "$dlrm_container" bash -c "cd $dlrm_test_path && cp -r output/pytorch-cpu/dlrm/Offline/performance/run_1/* $results_dir/$data_type/"

cat $results_dir/$data_type/mlperf_log_summary.txt
```

With the script ready, it's time to run the benchmark:

```bash
./run_dlrm_benchmark.sh
```

## Understanding the results

As a final step, have a look at the results generated in a text file.

The DLRM model optimizes the Click-Through Rate (CTR) prediction. It is a fundamental task in online advertising, recommendation systems, and search engines. Essentially, the model estimates the probability that a user will click on a given ad, product recommendation, or search result. The higher the predicted probability, the more likely the item is to be clicked. In a server context, the goal is to observe a high through-put of these probabilities.

```bash
cat $HOME/results/int8/mlperf_log_summary.txt
```

Your output should contain a `Samples per second`, where each sample tells probability of the user clicking a certain ad.

```output
================================================
MLPerf Results Summary
================================================
SUT name : PyFastSUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 1434.8
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes

================================================
Additional Stats
================================================
Min latency (ns)                : 124022373
Max latency (ns)                : 883187615166
Mean latency (ns)               : 442524059715
50.00 percentile latency (ns)   : 442808926434
90.00 percentile latency (ns)   : 794977004363
95.00 percentile latency (ns)   : 839019402197
97.00 percentile latency (ns)   : 856679847578
99.00 percentile latency (ns)   : 874336993877
99.90 percentile latency (ns)   : 882255616119

================================================
Test Parameters Used
================================================
samples_per_query : 1267200
target_qps : 1920
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 600000
max_duration (ms): 0
min_query_count : 1
max_query_count : 0
qsl_rng_seed : 6023615788873153749
sample_index_rng_seed : 15036839855038426416
schedule_rng_seed : 9933818062894767841
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 204800
```
