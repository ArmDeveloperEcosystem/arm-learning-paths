---
layout: learningpathall
title: Improve Python application performance using zlib-ng
weight: 3
---

## Accelerate a Python application that compresses data

In the previous section, you learned how to build `zlib-ng` with Neon SIMD and ARMv8 CRC32 optimizations enabled.

In this section, you will accelerate the performance of an example Python application that compresses a large file and measure the performance difference when using `zlib-ng`.

## Install necessary software packages

Ensure that `python3` is available when you run `python`:

```bash
sudo apt install python-is-python3 -y
```
## Create a large file to compress

Navigate to your home directory before creating the example files:

```bash
cd $HOME
```
The Python file compression application will read an input file named `largefile` and write a compressed version as `largefile.gz`.

To create the input file `largefile`, use the `dd` command.

```bash
dd if=/dev/zero of=largefile count=1M bs=1024
```

## Create an example Python file compression application

To create a Python application for compressing `largefile`, use a text editor to copy and save the code below in a file named `zip.py`.

```python { file_name="zip.py" }
import gzip

size = 16384

with open('largefile', 'rb') as f_in:
    with gzip.open('largefile.gz', 'wb') as f_out:
        while (data := f_in.read(size)):
            f_out.write(data)
```

## Compress the file using the Python application and default zlib

Run `zip.py` with the default `zlib` and time the execution.

```bash
time python zip.py
```

The output is similar to:

```output
real    0m4.662s
user    0m4.544s
sys     0m0.117s
```

Make a note of the `real` time.

## Compress the file again using the Python application and zlib-ng

This time, use `LD_PRELOAD` to switch to `zlib-ng` and measure the performance difference.

Adjust the path to `libz.so.1` as needed.

```bash
time LD_PRELOAD=/usr/local/lib/libz.so.1 python ./zip.py
```

The output is similar to:

```output
real    0m1.759s
user    0m1.654s
sys     0m0.105s
```

Compare the `real` time against the default `zlib` run. 

In this example, `zlib-ng` reduces compression time from 4.6 seconds to 1.8 seconds, roughly a 2.6x improvement — driven by the Neon-accelerated adler32 and inflate chunk copy routines.

## What you've learned and what's next

In this section, you used `zlib-ng` to accelerate the performance of an example Python file compression application. You compared the difference in performance between `zlib` and `zlib-ng`.

In the next section, you will learn how to use Linux `perf` to profile applications and look for `zlib` activity.
