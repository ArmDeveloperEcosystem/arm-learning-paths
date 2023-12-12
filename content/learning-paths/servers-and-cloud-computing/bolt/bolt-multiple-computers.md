---
title: BOLT with multiple systems
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BOLT with multiple systems

If you want to use an Arm Linux target system and a different build system, the process is outlined below. 

### Collect Perf samples

The Perf data is collected on the Arm target system.

Record samples while running your application. Substitute the actual name of your application for `executable`:

```bash { target="ubuntu:latest" }
perf record -e cycles:u -o perf.data -- ./executable
```

Copy `perf.data` and `executable` to the build system using `scp`. You will need to replace `BUILD-SYSTEM` and `/path/to/bolt/work-area` with the build system hostname and work area path respectively for your setup.

```bash { target="ubuntu:latest" }
scp perf.data BUILD-SYSTEM:/path/to/bolt/work-area
scp executable BUILD-SYSTEM:/path/to/bolt/work-area
```

### Convert the profile data and generate the optimized executable

On the build system, verify that `perf.data` and `executable` have been copied.

List the directory contents:

```bash { target="ubuntu:latest" }
ls
```

You should see `executable` and `perf.data` in your directory. 

```output
drwxrwxr-x  2 username username    4096 Nov 28 12:43 ./
drwxrwxr-x 14 username username    4096 Nov 28 11:09 ../
-rwxrwxr-x  1 username username   32712 Nov 28 11:10 executable*
-rw-------  1 username username  407112 Nov 28 11:10 perf.data
```

Run the command below to convert the profile data:

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata -nl ./executable
llvm-bolt ./executable -o ./new_executable -data perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

This will generate the new executable. You will need to be copied back to the target system so it can be run.

### Run the new executable

This is run from the target system

Copy `new_executable` to the target system. You will need to replace `BUILD-SYSTEM` and `/path/to/bolt/work-area/new_executable` with the build system hostname and path to new_executable respectively.

```bash { target="ubuntu:latest" }
scp BUILD-SYSTEM:/path/to/bolt/work-area/new_executable .
```

Verify that `new_executable` has been copied.

List the directory contents:

```bash { target="ubuntu:latest" }
ls
```

You should see the `new_executable` in the current directory:

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

With a separate build and target system you can use SSH to copy files back and forth and work with BOLT.