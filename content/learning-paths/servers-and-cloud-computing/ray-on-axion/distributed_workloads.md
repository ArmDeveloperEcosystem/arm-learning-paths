---
title: Run Distributed Workloads with Ray
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run Distributed Workloads with Ray

This section demonstrates how to execute parallel tasks and distributed training workloads using Ray on Arm.

You will run simple distributed functions and then scale to multi-worker training using Ray.

## Run distributed tasks

Create a Python script to execute parallel tasks:

```bash
vi ray_test.py
```

```python
import ray
ray.init()

@ray.remote
def square(x):
    return x * x

results = ray.get([square.remote(i) for i in range(10)])
print("Results:", results)
```

### Explanation

* `ray.init()` → connects to the running Ray cluster
* `@ray.remote` → converts a function into a distributed task
* `square.remote(i)` → submits tasks asynchronously
* `ray.get()` → collects results from all workers

### Execute the script

```bash
python3 ray_test.py
```

The output is similar to:
```output
Results: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

This confirms parallel execution across CPU cores.

## Run distributed training

Create a script for distributed model training:

```bash
vi ray_train.py
```

```python
import ray
from ray.train.torch import TorchTrainer
from ray.train import ScalingConfig
import torch

def train_func():
    x = torch.randn(100, 10)
    y = torch.randn(100, 1)

    model = torch.nn.Linear(10, 1)
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(5):
        optimizer.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        optimizer.step()
        print(f"Loss: {loss.item()}")

trainer = TorchTrainer(
    train_func,
    scaling_config=ScalingConfig(
        num_workers=2,
        use_gpu=False
    )
)

trainer.fit()
```

### Execute training

```bash
python3 ray_train.py
```

The output is similar to:
```output
(RayTrainWorker pid=5335) Loss: 1.1982450485229492
(RayTrainWorker pid=5335) Loss: 1.158831000328064
(RayTrainWorker pid=5335) Loss: 1.1220906972885132
(RayTrainWorker pid=5335) Loss: 1.088060736656189
(RayTrainWorker pid=5335) Loss: 1.0567599534988403
(RayTrainWorker pid=5336) Loss: 1.4622551202774048 [repeated 5x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
```

This confirms distributed training across multiple workers.

## Explanation

* `TorchTrainer` → handles distributed training execution
* `ScalingConfig(num_workers=2)` → runs training on 2 workers
* Each worker executes training in parallel
* Logs may appear from multiple processes

## Ray Jobs View (Tasks & Training)

![Ray Dashboard Jobs tab showing successful execution of ray_test.py and ray_train.py#center](images/ray-jobs.png "Ray Jobs tab showing distributed tasks and training execution status")

* Each script execution appears as a job
* Status shows **SUCCEEDED**
* Confirms correct distributed execution

## What you've learned and what's next

You have successfully:

* Executed parallel tasks using Ray Core
* Converted functions into distributed workloads
* Performed distributed training using multiple workers
* Observed execution in the Ray dashboard

Next, you will perform hyperparameter tuning, deploy models, and benchmark performance.
