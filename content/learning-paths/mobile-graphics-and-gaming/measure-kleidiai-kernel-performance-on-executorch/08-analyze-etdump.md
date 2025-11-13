---
title: Analyzing ETRecord and ETDump
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the final step, we create an Inspector instance by providing the paths to the generated ETDump and ETRecord. 
The Inspector analyzes the runtime data from the ETDump file and maps it to the corresponding operators in the Edge Dialect Graph.


To visualize all runtime events in a tabular format, simply call:

```python 

import os
import sys
from executorch.devtools.inspector import Inspector

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <model_pte>")
    sys.exit(1)

pte_file = sys.argv[1]

base = os.path.splitext(pte_file)[0]

etrecord = f"{base}.etrecord"
etdump = f"{base}.etdump"
csvfile = f"{base}.csv"

ins = Inspector(etrecord=etrecord, etdump_path=etdump)
ins.print_data_tabular(include_delegate_debug_data=True, include_units=False)

with open(csvfile, "w", encoding="utf-8") as f:
    ins.save_data_to_tsv(f)

```

Next, you can examine the generated CSV file to view the execution time information for each node in the model.

Below is an example showing the runtime data corresponding to the Fully Connected node.


| event_block_name | event_name                     | p10 (ms)              | p50 (ms)              | p90 (ms)              | avg (ms)              | min (ms)              | max (ms)              | op_types                  | is_delegated_op | delegate_backend_name |
|-----------------|--------------------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|--------------------------|----------------|---------------------|
| Default         | Method::init                   | 33.277046            | 33.277046            | 33.277046            | 33.277046            | 33.277046            | 33.277046            | []                       | FALSE          |                     |
| Default         | Program::load_method           | 33.300006            | 33.300006            | 33.300006            | 33.300006            | 33.300006            | 33.300006            | []                       | FALSE          |                     |
| Execute         | Fully Connected (NC, F32) GEMM #1 | 0.0160000000000196   | 0.0180000000000007   | 0.0190000000000055   | 0.0187449000000005   | 0.0149999999999864   | 4.244                | []                       | TRUE           | XnnpackBackend      |
| Execute         | DELEGATE_CALL                  | 0.04136              | 0.04464              | 0.04792              | 0.046082053          | 0.03372              | 4.390585             | ['aten.linear.default']  | FALSE          | XnnpackBackend      |
| Execute         | Method::execute                | 0.04848              | 0.0525595            | 0.05756              | 0.0540658046         | 0.03944              | 4.404385             | []                       | FALSE          |                     |


You can experiment with different models and matrix sizes to obtain various performance results.
