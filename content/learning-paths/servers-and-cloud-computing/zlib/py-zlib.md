---
layout: learningpathall
title: Improve python application performance using Cloudflare zlib
weight: 3
---

## Install necessary software packages

* Make sure `python3` is available when `python` is run. 

```bash
sudo apt install python-is-python3 -y
```

## Detailed Steps

The previous section explained how to build the Cloudflare `zlib` which includes the use of `crc32` instructions to improve performance on data compression. 

Use a Python example and measure the performance difference with `zlib-cloudflare`.

Use a text editor to copy and save the code below in a file named `zip.py`

```python { file_name="zip.py" }
import gzip

size = 16384

with open('largefile', 'rb') as f_in:
    with gzip.open('largefile.gz', 'wb') as f_out:
        while (data := f_in.read(size)):
            f_out.write(data)

f_out.close()
```

## Create a large file to compress

The above Python code will read a file named `largefile` and write a compressed version as `largefile.gz`

To create the input file, use the `dd` command.

```bash
dd if=/dev/zero of=largefile count=1M bs=1024
```

## Run the example using the default zlib

Run with the default `zlib` and time the execution.

```bash
time python ./zip.py
```

Make a note of how many seconds the program took. 

## Run the example again with zlib-cloudflare

This time, use `LD_PRELOAD` to change to `zlib-cloudflare` instead and check the performance difference. 

Adjust the path to `libz.so` as needed. 

```bash
time LD_PRELOAD=/usr/local/lib/libz.so python ./zip.py
```

Notice the time saved using `zlib-cloudflare`.

The next section introduces how to use Linux `perf` to profile applications and look for `zlib` activity.
