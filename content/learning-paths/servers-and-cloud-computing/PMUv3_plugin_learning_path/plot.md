---
title: Plot, visualize, and analyze the results
weight: 5                      # _index.md always has weight of 1 to order correctly

### FIXED, DO NOT MODIFY
layout: "learningpathall"       
---

## Visualize the results

A Python program is available to help you plot, visualize, and analyze the results collected with the PMUv3 plugin.

You need `python3` and a number of Python packages.

If you are running on Ubuntu, install the following packages:

```console
sudo apt install python-is-python3 python3-pip python3-venv -y
```

Create and activate a Python virtual environment:

```console
python3 -m venv venv
source venv/bin/activate
```

Next, use Pip to install the required packages:

```console
pip install pandas pyyaml matplotlib PyPDF2
```

Download the Python application code to plot and analyze results:

```console
git clone https://github.com/GayathriNarayana19/Performance_Analysis_Backend.git
```

Copy the code below into a file named `config.yaml` in your `test/` directory which contains your CSV files:

```yaml
base_dirs:
  - path: '.'
    output_file: 'metrics.csv'
output_dir: './test_plotting/'
base_filename: 'bundle{}.csv'
num_bundles: 15
scenarios:
  - "test1: section1"
title: 'Section1'

#########DO NOT MODIFY BELOW THIS LINE##########
kpi_metrics:
  - - ['L1_I-cache_MPKI', ['L1I_CACHE_REFILL', 'INST_RETIRED']]
    - ['I-side_page_table_MPKI', ['ITLB_WALK', 'INST_RETIRED']]
    - ['L2_cache_MPKI', ['L2D_CACHE_REFILL', 'INST_RETIRED']]
    - ['Branch_MPKI', ['BR_MIS_PRED_RETIRED', 'INST_RETIRED']]
    - ['D-side_page_table_MPKI', ['DTLB_WALK', 'INST_RETIRED']]
    - ['L1_D-cache_MPKI', ['L1D_CACHE_REFILL', 'INST_RETIRED']]
    - ['LLC_cache_MPKI', ['LL_CACHE_MISS_RD', 'INST_RETIRED']]
  - - ['L1_data_TLB_read_miss_rate', ['L1D_TLB_REFILL_RD', 'L1D_TLB_RD']]
    - ['L2_TLB_miss_rate', ['L2D_TLB_REFILL', 'L2D_TLB']]
    - ['L2_TLB_write_miss_rate', ['L2D_TLB_REFILL_WR', 'L2D_TLB_WR']]
    - ['L2_TLB_read_miss_rate', ['L2D_TLB_REFILL_RD', 'L2D_TLB_RD']]
    - ['L1_data_TLB_miss_rate', ['L1D_TLB_REFILL', 'L1D_TLB']]
    - ['L1_instruction_TLB_miss_rate', ['L1I_TLB_REFILL', 'L1I_TLB']]
    - ['L1_data_TLB_write_miss_rate', ['L1D_TLB_REFILL_WR', 'L1D_TLB_WR']]
  - - ['L1_D-cache_read_miss_rate', ['L1D_CACHE_REFILL_RD', 'L1D_CACHE_RD']]
    - ['L1_D-cache_write_miss_rate', ['L1D_CACHE_REFILL_WR', 'L1D_CACHE_WR']]
    - ['L1_D-cache_miss_rate', ['L1D_CACHE_REFILL', 'L1D_CACHE']]
    - ['L1_I-cache_miss_rate', ['L1I_CACHE_REFILL', 'L1I_CACHE']]
    - ['L2_cache_miss_rate', ['L2D_CACHE_REFILL', 'L2D_CACHE']]
    - ['L1_D-cache_rate_of_cache_misses_in_L1_and_L2', ['L1D_CACHE_REFILL_OUTER', 'L1D_CACHE_REFILL']]
  - - ['Front_end_stall_rate', ['STALL_FRONTEND', 'CPU_CYCLES']]
    - ['Back_end_stall_rate', ['STALL_BACKEND', 'CPU_CYCLES']]
  - - ['Speculatively_executed_IPC', ['INST_SPEC', 'CPU_CYCLES']]
    - ['Architecturally_executed_IPC', ['INST_RETIRED', 'CPU_CYCLES']]
  - - ['VFP_instruction_rate_per_instructions', ['VFP_SPEC', 'INST_SPEC']]
    - ['DMB_rate_per_instructions', ['DMB_SPEC', 'INST_SPEC']]
    - ['DP_instruction_rate_per_instructions', ['DP_SPEC', 'INST_SPEC']]
    - ['ISB_rate_per_instructions', ['ISB_SPEC', 'INST_SPEC']]
    - ['CRYPTO_instruction_rate_per_instructions', ['CRYPTO_SPEC', 'INST_SPEC']]
    - ['PC_WRITE_instruction_rate_per_instructions', ['PC_WRITE_SPEC', 'INST_SPEC']]
    - ['SIMD_instruction_rate_per_instructions', ['ASE_SPEC', 'INST_SPEC']]
    - ['BR_IMMED_instruction_rate_per_instructions', ['BR_IMMED_SPEC', 'INST_SPEC']]
    - ['ST_instruction_rate_per_instructions', ['ST_SPEC', 'INST_SPEC']]
    - ['BR_RETURN_instruction_rate_per_instructions', ['BR_RETURN_SPEC', 'INST_SPEC']]
    - ['DSB_rate_per_instructions', ['DSB_SPEC', 'INST_SPEC']]
    - ['LD_instruction_rate_per_instructions', ['LD_SPEC', 'INST_SPEC']]
    - ['BR_INDIRECT_instruction_rate_per_instructions', ['BR_INDIRECT_SPEC', 'INST_SPEC']]
    - ['Exception_rate_per_instructions', ['EXC_TAKEN', 'INST_RETIRED']]

kpi_file_groups:
  - ["bundle11.csv", "bundle12.csv"]
  - ["bundle0.csv", "bundle1.csv", "bundle7.csv", "bundle10.csv"]
  - ["bundle5.csv", "bundle6.csv", "bundle13.csv"]
  - ["bundle4.csv"]
  - ["bundle8.csv"]
  - ["bundle8.csv", "bundle9.csv", "bundle14.csv"]
```

Run the Python application to create the performance plots as follows:

```console
python3 Performance_Analysis_Backend/PMUv3_Backend/pmuv3_plotting.py -config config.yaml
```

Look in the `test_plotting/` directory for a CSV file and the PDF files with the results.

The next section explains how to instrument multiple sections of code. 
