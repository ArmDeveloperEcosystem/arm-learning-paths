---
title: BOLT with Multiple Systems
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BOLT with Multiple Systems

Steps to optimise executable with BOLT using multiple systems. In this example we are using 2 systems, an Arm Linux target system and a Linux build system for running BOLT.

### Collect Perf Samples

This is performed on the Arm target system.

Record samples while running executable

```bash { target="ubuntu:latest" }
perf record -e cycles:u -o perf.data -- ./executable
```

Copy `perf.data` amd `executable` to the build system using `scp`. You will need to replace `BUILD-SYSTEM` & `/path/to/bolt/work-area` with the build system hostname & work area path respectively.

```bash { target="ubuntu:latest" }
scp perf.data BUILD-SYSTEM:/path/to/bolt/work-area
scp executable BUILD-SYSTEM:/path/to/bolt/work-area
```

### Convert Profile and Generate Optimised Executable

This is performed on the build system.

Verify that `perf.data` and `executable` have been copied.

```bash { target="ubuntu:latest" }
ls
```

```output
drwxrwxr-x  2 username username    4096 Nov 28 12:43 ./
drwxrwxr-x 14 username username    4096 Nov 28 11:09 ../
-rwxrwxr-x  1 username username   32712 Nov 28 11:10 executable*
-rw-------  1 username username  407112 Nov 28 11:10 perf.data
```

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata -nl ./executable
llvm-bolt ./executable -o ./new_executable -data perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

This will generate the new executable and it will need to be copied back to the target system so it can be run.

### Run New Executable

This is run from the target system

Copy `new_executable` to the target system. You will need to replace `BUILD-SYSTEM` & `/path/to/bolt/work-area/new_executable` with the build system hostname & path to new_executable respectively.

```bash { target="ubuntu:latest" }
scp BUILD-SYSTEM:/path/to/bolt/work-area/new_executable .
```

Verify that `new_executable` has been copied.

```bash { target="ubuntu:latest" }
ls
```

```output
drwxrwxr-x  2 username username    4096 Nov 28 12:43 ./
drwxrwxr-x 14 username username    4096 Nov 28 11:09 ../
-rwxrwxr-x  1 username username   32712 Nov 28 11:10 executable*
-rwxrwxr-x  1 username username 6304960 Nov 28 12:43 new_executable*
-rw-------  1 username username  407112 Nov 28 11:10 perf.data
```

Run the new executable

```bash { target="ubuntu:latest" }
./new_executable
```
