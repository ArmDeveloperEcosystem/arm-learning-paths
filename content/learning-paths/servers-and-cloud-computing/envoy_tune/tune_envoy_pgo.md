---
title: "Tune Envoy by PGO"
weight: 3
layout: "learningpathall"
---

###  Envoy Deployment Tuning by PGO

PGO (Profile-Guided Optimization) allows your compiler to better optimize code for how it actually runs. Applying this to Envoy can result in a 10% enhancement in performance. 

Use the information below as general guidance on tuning Envoy by PGO.

### LLVM/Clang build  

When building Envoy by default using Bazel and LLVM/Clang, we recommend using the latest compiler version. It is advisable to build LLVM/Clang from the most recent [source code](https://github.com/envoyproxy/envoy) for optimal results. Refer to the [LLVM Documentation](https://llvm.org/docs/UserGuides.html) and [Clang Documentation](https://llvm.org/docs/UserGuides.html) for specific build details.

### Building Envoy with PGO

First, you should have at least LLVM, Clang, and compiler-rt checked out locally.

Next, at a high level, you’re going to need to do the following:
```console
	1.Build Envoy using the Clang you built above, but with instrumentation

	2.Use the instrumented Envoy to generate profiles, which consists of two steps:

		Running the instrumented Envoy on tasks that represent how users will use it.

		Using a tool to convert the “raw” profiles generated above into a single, final PGO profile.

	3.Build a final release Envoy using the profile collected from your benchmark
```
 
In more detailed steps:

1. Build envoy with instrumentation
```console
bazel build -c opt --copt="-fprofile-generate=/path/to/stage2/profiles" --cxxopt="-fprofile-generate=/path/to/stage2/profiles" --linkopt="-fprofile-generate=/path/to/stage2/profiles"  envoy --jobs=$(nproc)
```
2. Generate profiles:
Run the envoy built by the step 1 with the target test cases, when the test fininshed, run the following command to kill the envoy services.
```console
sudo pkill -2 envoy
```
You should now have a few *.profraw files in /path/to/stage2/profiles/. You need to merge these using llvm-profdata (even if you only have one! The profile merge transforms profraw into actual profile data, as well). This can be done with the following command:
```console
/path/to/clang/llvm-profdata merge -output=/path/to/output/profdata.prof /path/to/stage2/profiles/*.profraw.
```

3.Build a final Envoy release

Now, build your final, PGO-optimized Envoy. To do this,you can run the following command:
```console
bazel build -c opt --copt="-fprofile-use=/path/to/output/profdata.prof" --cxxopt="-fprofile-use=/path/to/output/profdata.prof" --linkopt="-fprofile-use=/path/to/output/profdata.prof" envoy.stripped --jobs=$(nproc) 
```

### LLVM/Clang PGO Documentation

More options for LLVM/Clang PGO can see in [profile-guided-optimization](https://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization)
