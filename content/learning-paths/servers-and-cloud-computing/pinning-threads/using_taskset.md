---
title: Using Taskset
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Python Script

Now that we have a basic program that utilizes all the available CPU cores, we will interleave this with a single-threaded program sensitive to variations in execution. This could be to simulate, for example, a log ingesting process or a single-threaded consumer that needs to keep a steady pace. 

Check that you have Python installed.

```bash
python3 --version
```

You should see the version of Python. If not, please install Python using the [online instructions](https://www.python.org/downloads/).

```output
Python 3.12.3
```

Next, create a virtual environment. This allows you to install packages without interfering with system packages.

```bash
python3 -m venv venv
source venv/bin/activate
pip install matplotlib
```

Create a file named `single_threaded_python_script.py` and update the permissions with the commands below.

```bash
touch single_threaded_python_script.py
chmod 755 single_threaded_python_script.py
```

Paste in the follow Python script into `single_threaded_python_script.py`. 

```python
#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt
import matplotlib
import sys

def timer(func):
    def foo(*args,**kwargs):
        with open("data.txt", "a") as f:
            start = time.perf_counter()
            ans = func(*args,**kwargs)
            end = time.perf_counter()
            duration = end - start
            # print(f"Function {func.__name__} took {(duration*1000):4f} milliseconds")
            f.write((str(duration*1000)) + ", ")
        return ans
    return foo

@timer
def bar(x:int)->float:
    """Random function that is time sensitive"""
    res = 0.0
    for i in range(0,x*100):
        res += (float(i) / 9.0) + (42.0 + float(i))

    return res

def plot_csv_values_from_txt(path: str, *, title: str | None = None, show_markers: bool = False) -> None:
    """
    Reads a .txt file containing comma-separated numeric values (with optional whitespace/newlines)
    and plots them as a simple chart.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split on commas, trim whitespace, ignore empty tokens (handles trailing comma)
    tokens = [t.strip() for t in text.replace("\n", " ").split(",")]
    values = [float(t) for t in tokens if t]

    plt.figure()
    x = range(len(values))
    if show_markers:
        plt.plot(x, values, marker="o", linestyle="-")
    else:
        plt.plot(x, values)

    plt.xlabel("Sample Number")
    plt.ylabel("Time / milliseconds")
    if title:
        plt.title(title)
    plt.tight_layout()
    plt.grid()
    plt.show()
    if (sys.argv[1] == "exclusive"):
        plt.savefig("Exclusive.jpg")
    elif (sys.argv[1] == "shared"):
        plt.savefig("Shared.jpg")
    elif (sys.argv[1] == "free"):
        plt.savefig("Free.jpg")

def main():

    for i in range(0,10000):
        bar(50)
    if (sys.argv[1] == "exclusive"):
        plot_csv_values_from_txt(path="data.txt",title="Exclusively Pinned")
    elif (sys.argv[1] == "shared"):
        plot_csv_values_from_txt(path="data.txt", title="Shared")
    elif (sys.argv[1] == "free"):
        plot_csv_values_from_txt(path="data.txt", title="Free")
    return 0

if __name__ == "__main__":
    main()
```

The Python script above repeatedly measures the time to execute an arbitrary function, `bar` and writes it to a file `data.txt`. It then generates a time-series graph of the time to illustrate and compare the effects of pinning threads under different scenarios. 


### Using Taskset to Pin Threads

We will explore 3 different scenarios. One where we let the operating system allocate to any of 4 cores, another scenario where we pin the single-threaded process to an individual core but our program `prog` is free to run on any core, and a final scenario where the single-threaded script has exclusive access to a single core. We will observe the tradeoff in execution time for both programs running simulatenously. 

Create 3 bash scripts with the following command.

```bash
touch free-script.sh exclusive.sh shared-pinned.sh
chmod 755 free-script.sh exclusive.sh shared-pinned.sh
```
Paste in the script below to the corresponding files. 

#### Free

```bash
#!/bin/bash

set -euo pipefail

rm -f ./data.txt
taskset --cpu-list 0-3 ./single_threaded_python_script.py free & # time-critical python script
taskset --cpu-list 0-3 ./prog

wait
```

#### Shared-Pinned

```bash
#!/bin/bash

set -euo pipefail

rm -f ./data.txt
taskset --cpu-list 0 ./single_threaded_python_script.py shared & # time-critical python script
taskset --cpu-list 0-3 ./prog

wait
```

#### Exclusive Access

```bash
#!/bin/bash

set -euo pipefail

rm -f ./data.txt
taskset --cpu-list 0 ./single_threaded_python_script.py exclusive & # time-critical python script
taskset --cpu-list 1-3 ./prog

wait
```

```bash
./free-script.sh
./shared-pinned.sh
./exclusive.sh
```

The terminal output is the execution time under the 3 corresponding scenarios. Additionally, the Python script will generate 3 files, `Free.jpg`, `Exclusive.jpg` and `Shared.jpg`. 

As the terminal output below shows, the `free.sh` script, where the Linux scheduler performs assigns threads to cores without restriction, calculated `prog` the quickest at 5.8s. The slowest calculation is where the Python script has exclusive access to cpu 0. This is to be expected as we have constrained `prog` to fewer cores.  

```output
Answer = 3.14159        5 iterations took 5838 milliseconds
Answer = 3.14159        5 iterations took 5946 milliseconds
Answer = 3.14159        5 iterations took 5971 milliseconds
```

However, this is a tradeoff between the performance of the Python script. Looking at `free.jpg`, we have periodic zones of high latency (3.5ms) that likely coincide when there is contention between the `prog` and the Python script. 

![free](./free.jpg)

When, pinning the Python script to a core 0 with `prog` free to use any cores we also observe this behaviour.

![shared](./pinned_shared.jpg)

Finally, when the Python script has exclusive access to core 0, we observe more consistent time around 0.49ms as the script is not contending with any other demanding processes.

![exclusive](./exclusive.jpg)

There are multiple additional factors the influence why we this exact profile, including the Linux scheduler algorithm and their associated parameters as well as the priority of the process. We will not go into said factors as it is out of scope for this learning path. If you'd like to learn more, please look into the Linux scheduler and priority setting via the [nice](https://man7.org/linux/man-pages/man2/nice.2.html) utility.