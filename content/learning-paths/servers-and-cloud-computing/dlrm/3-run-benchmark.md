---
title: Run the benchmark
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The final step is to run the actual benchmark.

## Benchmark script

You will now create a script which uses the Docker container to run the benchmark. Create a new file called `run_dlrm_benchmark.sh`. Paste the code below.

```bash
#!/bin/bash

set -ex
yellow="\e[33m"
reset="\e[0m"
data_type=${1:-"int8"}
echo -e "${yellow}Data type chosen for the setup is $data_type${reset}"

# setup environment variables for the dlrm container
data_dir=$HOME/data/
model_dir=$HOME/model/
results_dir=$HOME/results/
dlrm_container="benchmark_dlrm"

# Create results directory
mkdir -p $results_dir/$data_type

###### Run the dlrm container and setup MLPerf #######
# Check if the container exists
echo -e "${yellow}Checking if the container '$dlrm_container' exists...${reset}"
container_exists=$(docker ps -aqf "name=^$dlrm_container$")

if [ -n "$container_exists" ]; then
    echo "${yellow}Container '$dlrm_container' already exists. Will not create a new one. ${reset}"
else
    echo "Creating a new '$dlrm_container' container..."
    docker run -td --shm-size=200G --privileged \
        -v $data_dir:$data_dir \
        -v $model_dir:$model_dir \
        -v $results_dir:$results_dir \
        -e DATA_DIR=$data_dir \
        -e MODEL_DIR=$model_dir \
        -e CONDA_PREFIX=/opt/conda \
        -e NUM_SOCKETS="1" \
        -e CPUS_PER_SOCKET=$(nproc) \
        -e CPUS_PER_PROCESS=$(nproc) \
        -e CPUS_PER_INSTANCE="1" \
        -e CPUS_FOR_LOADGEN="1"  \
        -e BATCH_SIZE="400"  \
        -e PATH=/opt/conda/bin:$PATH \
        --name=$dlrm_container \
        toolsolutions-pytorch:latest
fi

###### Build MLPerf & Dependencies #######
# Copy MLPerf build script to the benchmark_dlrm container
docker cp ~/dlrm_docker_setup/build_mlperf.sh $dlrm_container:$HOME/

# Copy the patches
docker cp ~/dlrm_docker_setup/mlperf_patches $dlrm_container:$HOME/

echo -e "${yellow}Setting up MLPerf benchmarking inside the container...${reset}"
docker exec -it $dlrm_container bash -c ". $HOME/build_mlperf.sh $data_type"

###### Dump the model #######
dumped_fp32_model="dlrm-multihot-pytorch.pt"
int8_model="aarch64_dlrm_int8.pt"
dlrm_test_path="$HOME/inference_results_v4.0/closed/Intel/code/dlrm-v2-99.9/pytorch-cpu-int8"

# Check if FP32 model is already dumped
if [ -f "$HOME/model/$dumped_fp32_model" ]; then
    echo -e "${yellow}File '$dumped_fp32_model' exists. Skipping model dumping step.${reset}"
else
    echo -e "${yellow}File '$dumped_fp32_model' does not exist. Dumping the model weights...${reset}"
    docker cp $HOME/dlrm_docker_setup/requirements.txt $dlrm_container:$HOME
    docker exec -it "$dlrm_container" bash -c "pip install -r requirements.txt ; cd $dlrm_test_path && python python/dump_torch_model.py --model-path=$model_dir/model_weights --dataset-path=$data_dir"
fi

###### Calibrate the model #######
# In the case of INT8, calibrate the model if not already calibrated.
echo -e "${yellow}Checking if INT8 model calibration is required...${reset}"

if [ "$data_type" == "int8" ] && [ ! -f "$HOME/model/$int8_model" ]; then
    echo -e "${yellow}File '$int8_model' does not exist. Running calibration...${reset}"
    # the calibration will create aarch64_dlrm_int8.pt in the $HOME/model directory.
    docker exec -it "$dlrm_container" bash -c "cd $dlrm_test_path && ./run_calibration.sh"
else
    echo -e "${yellow}Calibration step is not needed.${reset}"
fi

###### Run the test #######
# Run the offline test
echo -e "${yellow}Running offline test...${reset}"
docker exec -it "$dlrm_container" bash -c "cd $dlrm_test_path && bash run_main.sh offline $data_type"

# Copy results to the host machine
echo -e "${yellow}Copying results to host...${reset}"
docker exec -it "$dlrm_container" bash -c "cd $dlrm_test_path && cp -r output/pytorch-cpu/dlrm/Offline/performance/run_1/* $results_dir/$data_type/"

# Display the MLPerf summary results
echo -e "${yellow}Displaying MLPerf results...${reset}"
cat $results_dir/$data_type/mlperf_log_summary.txt

```

At a glance, these are the steps it goes through:

- Sets up MLPerf repositories within the container.
- Dumps the model from existing model weights if not already available.
- Calibrates the INT8 model from the dumped model if it has not been previously generated.
- Executes the offline benchmark test, generating terabyte-scale binary data files during the process.

Run the offline test with the `int8` datatype. You can also specify the argument `fp32` to build for the floating point datatype.

```bash
cd $HOME/dlrm_docker_setup
./run_dlrm_benchmark.sh int8
```

## Save output files

You may want to save the final model and data files to run on smaller servers. You can use `scp` to achieve this.

From your long-term storage machine, run the following command. You need to update the parameters before running.

```
scp -i <key-pair> <username>@<ipaddress>:/remote/path/to/file $HOME/model/int8/
```
where `key-pair` is the key-pair used for the larger instance, `username` and `ipaddress` the corresponding access points, and the two paths are the source and destination paths respectively.

Save the following files for long-term storage.

```console
$HOME/model/aarch64_dlrm_int8.pt
$HOME/model/dlrm-multihot-pytorch.pt
$HOME/data/terabyte_processed_test_v2_dense.bin
$HOME/data/terabyte_processed_test_v2_label_sparse.bin
```

To run the INT8 model, an instance with 250 GB of RAM and 500 GB of disk space is enough. For example, the following instance types:

|         CSP           |  Instance type |
| --------------------- | -------------- |
| Google Cloud Platform | c4a-highmem-32 |
| Amazon Web Services   | r8g.8xlarge    |
| Microsoft Azure       | TODO           |

For example, you can re-run the offline `int8` benchmark by cloning the repository to the smaller instance and the following command.

```bash
./run_main.sh offline int8
```

## Understanding the results

As a final step, have a look at the results generated in a text file.
```bash
cat $HOME/results/int8/mlperf_log_summary.txt
```

It should look something like this. Note the ....

```output
================================================
MLPerf Results Summary
================================================
SUT name : PyFastSUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 1434.8 # Each sample tells probability of the user clicking a certain ad. Can be used by Amazon to pick the top 5 ads to recommend to a user
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

