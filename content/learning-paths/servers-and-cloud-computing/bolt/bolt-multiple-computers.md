---
title: BOLT with Multiple Computers
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BOLT with Multiple Computers

Steps to optimise executable with BOLT using multeple computers. In this example we are using 2 computers, Arm Computer is a Arm Linux computer and BOLT Computer is a Linux Computer.

### Collect Perf Samples

This is performed on the Arm Computer.

Record samples while running executable

```bash { target="ubuntu:latest" }
perf record -e cycles:u -o perf.data -- ./executable
```

Copy `perf.data` amd `executable` to the BOLT Computer using `scp`. You will need to replace `BOLT-COMPUTER` & `/path/to/bolt/work-area` with BOLT Computer hostname & work area path respectively.

```bash { target="ubuntu:latest" }
scp perf.data BOLT-COMPUTER:/path/to/bolt/work-area
scp executable BOLT-COMPUTER:/path/to/bolt/work-area
```

### Convert Profile and Generate Optimised Executable

This is performed on the BOLT Computer.

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
perf2bolt -p perf.data -o perf.fdata ./executable -nl
llvm-bolt ./executable -o ./new_executable -data perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

This will generate the new executable and it will need to be copied back to the Arm Computer so it can be run.

### Run New Executable

This is run from the Arm Computer

Copy `new_executable` to the Arm Computer. You will need to replace `BOLT-COMPUTER` & `/path/to/bolt/work-area/new_executable` with BOLT Computer hostname & path to new_executable respectively.

```bash { target="ubuntu:latest" }
scp BOLT-COMPUTER:/path/to/bolt/work-area/new_executable .
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
