---
title: "Tune Envoy by PGO"
weight: 3
layout: "learningpathall"
---

###  Envoy Deployment Tuning by PGO

PGO (Profile-Guided Optimization) allows your compiler to better optimize code for how it actually runs. Applying this to Envoy can result in a 10% enhancement in performance. 

Use the information below as general guidance to tune Envoy by PGO.

### LLVM/Clang build  

When you build Envoy using Bazel and LLVM/Clang, you should use the latest compiler version. For optimal results, it is advisable to build Bazel from the most recent [source code](https://github.com/envoyproxy/envoy). Refer to the [LLVM Documentation](https://llvm.org/docs/UserGuides.html) and [Clang Documentation](https://llvm.org/docs/UserGuides.html) for specific build details.

### Overview of building Envoy with PGO

Here is an overview of the steps that you will need to take to build envoy with PGO:

* Make sure you have LLVM, Clang, and compiler-rt installed locally.
* Build Envoy using the Clang, but with instrumentation.
* Use the instrumented Envoy to generate profiles, which consists of two steps:
	* Running the instrumented Envoy on tasks that represent how users will use it.
	* Using a tool to convert the raw profiles generated from the previous step into a single, final PGO profile.
* Build a final release Envoy using the profile collected from your benchmark.
 
### Detailed steps to build Envoy with PGO

Follow and run the steps below:

1. Build envoy with instrumentation:

```console
bazel build -c opt --copt="-fprofile-generate=/path/to/stage2/profiles" --cxxopt="-fprofile-generate=/path/to/stage2/profiles" --linkopt="-fprofile-generate=/path/to/stage2/profiles"  envoy --jobs=$(nproc)
```
2. Generate profiles:
Run the envoy built by the step 1 with your target test cases. When the test finished, run the following command to kill the envoy services:

```console
sudo pkill -2 envoy
```
You should now have a few *.profraw files in /path/to/stage2/profiles/. You need to merge these using llvm-profdata, even if you only have one file. The profile merge transforms profraw into actual profile data. This can be done with the following command:
```console
/path/to/clang/llvm-profdata merge -output=/path/to/output/profdata.prof /path/to/stage2/profiles/*.profraw.
```

3.Build a final Envoy release

Now, build your final, PGO-optimized Envoy. Run the following command:
```console
bazel build -c opt --copt="-fprofile-use=/path/to/output/profdata.prof" --cxxopt="-fprofile-use=/path/to/output/profdata.prof" --linkopt="-fprofile-use=/path/to/output/profdata.prof" envoy.stripped --jobs=$(nproc) 
```

### LLVM/Clang PGO Documentation

You can view more options for LLVM/Clang PGO in [profile-guided-optimization](https://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization)
