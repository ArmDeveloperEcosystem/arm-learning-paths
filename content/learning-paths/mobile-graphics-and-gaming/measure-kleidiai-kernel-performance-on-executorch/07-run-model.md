---
title: Run model and generate the ETDump
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Copy artifacts to your Arm64 target
From your x86_64 host (where you cross-compiled), copy the runner and exported models to the Arm device:

```bash
scp $WORKSPACE/build-arm64/executor_runner <arm_user>@<arm_host>:~/bench/
scp -r model/ <arm_user>@<arm_host>:~/bench/
```

### Run a model and emit ETDump
Use one of the models you exported earlier (e.g., FP32 linear: linear_model_pf32_gemm.pte).
The flags below tell executor_runner where to write the ETDump and how many times to execute.

```bash 
cd ~/bench
./executor_runner -etdump_path model/linear_model_f32.etdump -model_path model/linear_model_f32.pte -num_executions=1 -cpu_threads 1

```

You can adjust the number of execution threads and the number of times the model is invoked.


You should see output similar to the example below.

```bash
D 00:00:00.015988 executorch:XNNPACKBackend.cpp:57] Creating XNN workspace
D 00:00:00.018719 executorch:XNNPACKBackend.cpp:69] Created XNN workspace: 0xaff21c2323e0
D 00:00:00.027595 executorch:operator_registry.cpp:96] Successfully registered all kernels from shared library: NOT_SUPPORTED
I 00:00:00.035506 executorch:executor_runner.cpp:157] Resetting threadpool with num threads = 1
I 00:00:00.048120 executorch:threadpool.cpp:48] Resetting threadpool to 1 threads.
I 00:00:00.051509 executorch:executor_runner.cpp:218] Model file model/linear_model_f32.pte is loaded.
I 00:00:00.051531 executorch:executor_runner.cpp:227] Using method forward
I 00:00:00.051541 executorch:executor_runner.cpp:278] Setting up planned buffer 0, size 2112.
D 00:00:00.051630 executorch:method.cpp:793] Loading method: forward.
....

D 00:00:00.091432 executorch:XNNExecutor.cpp:236] Resizing output tensor to a new shape
I 00:00:00.091459 executorch:executor_runner.cpp:340] Model executed successfully 1 time(s) in 2.904883 ms.
I 00:00:00.091477 executorch:executor_runner.cpp:349] 1 outputs:
OutputX 0: tensor(sizes=[1, 256], [
  0.0106399, 0.0951964, 1.04854, -0.290168, -0.278126, -0.355151, 0.0583736, -0.431953, -0.0773305, -0.32844,
  ...,
  0.553568, -0.0339369, 0.562088, -1.21021, -0.769254, 0.677771, -0.264338, 1.05453, 0.724467, 0.53182,
])
I 00:00:00.093912 executorch:executor_runner.cpp:125] ETDump written to file 'model/linear_model_f32.etdump'.

```

If the execution is successful, an etdump file will also be generated.

