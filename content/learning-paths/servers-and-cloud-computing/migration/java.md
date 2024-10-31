---
# User change
title: "Migrating Java applications"

weight: 4

layout: "learningpathall"

---

# Java on Arm Neoverse processors

Java is a general-purpose, high-level programming language used in a wide variety of applications.

Java code is typically compiled to bytecode that runs on a Java virtual machine (JVM) making it portable across computer architectures.

There are many ways to install Java on Arm Linux distributions. Refer to the [Java install guide](/install-guides/java/) for information about how to install Java.

# How can I increase Java performance on Arm? 

Java runs well on Arm, but there are some things to investigate to make sure you are getting the best performance. 

## Which JVM flags impact performance?

The JVM includes a number of flags which are available to tune performance and aid in debugging. Some of the flags are general purpose and some are Arm architecture specific. 

To print the final values of the flags after the JVM has been initialized run:

```console
java -XX:+PrintFlagsFinal -version
```

Use the output from the above command to see the current values before making any changes.

For example, to check the value of `CICompilerCount` run:

```console
java -XX:+PrintFlagsFinal -version | grep CICompilerCount
```

The value of the flag is printed:

```output
  intx CICompilerCount = 3     {product} {ergonomic}
```

### Flags to review

The `-XX:-TieredCompilation -XX:ReservedCodeCacheSize -XX:InitialCodeCacheSize` flags provide significant performance improvement for some applications. 

The `-XX:-TieredCompilation` flag turns off intermediate compilation tiers. This may help  long-running, predictable applications especially when the warmup period doesn't significantly impact overall performance.

You can increase the code cache sizes using the `-XX:ReservedCodeCacheSize` and `-XX:InitialCodeCacheSize` flags. Increasing them may improve performance. You can also decrease them in a memory constrained environment. 

The `-XX:CICompilerCount` flag specifies the number of compiler threads for the just-in-time (JIT) compiler. This can be useful to tune performance on multi-core systems. 

The `-XX:CompilationMode` flag instructs the JIT compiler to to use highest optimization level (`high-only`) or the quick optimization level (`quick-only`). 

The best way to determine optimal values for your application is to test your application with different values. 

### Architecture flags

There are flags that are specific to the Arm architecture and indicate if a particular hardware feature is used. You can see all the flags by running:

```console
java -XX:+PrintFlagsFinal -version | grep ARCH
```

The output is similar to:

```output
bool AvoidUnalignedAccesses                   = false                                {ARCH product} {default}
intx BlockZeroingLowLimit                     = 256                                  {ARCH product} {default}
bool NearCpool                                = true                                 {ARCH product} {default}
 int SoftwarePrefetchHintDistance             = 192                                  {ARCH product} {default}
bool TraceTraps                               = false                                {ARCH product} {default}
bool UseBlockZeroing                          = true                                 {ARCH product} {default}
cstr UseBranchProtection                      = none                                 {ARCH product} {default}
bool UseCRC32                                 = true                                 {ARCH product} {default}
bool UseCryptoPmullForCRC32                   = false                                {ARCH product} {default}
bool UseLSE                                   = true                                 {ARCH product} {default}
bool UseNeon                                  = false                                {ARCH product} {default}
bool UseSIMDForArrayEquals                    = true                                 {ARCH product} {default}
bool UseSIMDForBigIntegerShiftIntrinsics      = true                                 {ARCH product} {default}
bool UseSIMDForMemoryOps                      = false                                {ARCH product} {default}
uint UseSVE                                   = 0                                    {ARCH product} {default}
bool UseSimpleArrayEquals                     = false                                {ARCH product} {default}
```

Depending on your application, you may want to investigate the vector processing flags for SIMD, NEON, SVE, and CRC. 

You can try [Process Watch](https://learn.arm.com/learning-paths/servers-and-cloud-computing/processwatch/) to monitor the usage of SIMD and CRC instructions. 

Refer to the [Java documentation](https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html) for more information about the flags.

## Memory and Garbage Collection

The default [JVM ergonomics](https://docs.oracle.com/en/java/javase/21/gctuning/ergonomics.html) can generally be improved upon if you understand your workload well.

Default initial heap size is 1/64th of RAM and default maximum heap size is 1/4th of RAM. If you know your memory requirements, you should set both of these flags to the same value (e.g. `-Xms12g` and `-Xmx12g` for an application that uses at most 12 GB). Setting both flags to the same value will prevent the JVM from having to periodically allocate additional memory. Additionally, for cloud workloads max heap size is often set to 75%-85% of RAM, much higher than the default setting.

If you are deploying in a cloud scenario where you might be deploying the same stack to systems that have varying amounts of RAM, you might want to use `-XX:MaxRAMPercentage` instead of `-Xmx`, so you can specify a percentage of max RAM rather than a fixed max heap size. This setting can also be helpful in containerized workloads.

Garbage collector choice will depend on the workload pattern for which you're optimizing.

* If your workload is a straightforward serial single-core load with no multithreading, the `UseSerialGC` flag should be set to true.
* For multi-core small heap batch jobs (<4GB), the `UseParallelGC` flag should be set to true.
* The G1 garbage collector (`UseG1GC` flag) is better for medium to large heaps (>4GB). This is the most commonly used GC for large parallel workloads, and is the default for high-core environments. If you want to optimize throughput, use this one.
* The ZGC (`UseZGC` flag) has low pause times, which can drastically improve tail latencies. If you want to prioritize response time at a small cost to throughput, use ZGC.
* The Shenandoah GC (`UseShenandoahGC` flag) is still fairly niche. It has ultra low pause times and concurrent evacuation, making it ideal for low-latency applications, at the cost of increased CPU use.

If you'd like to see what the default JVM values are for specific processor counts, you can run

```bash
java -XX:ActiveProcessorCount=[selected processor count] -XX:+PrintFlagsFinal -version
```

Where `[selected processor count]` is the number of processors you want to evaluate the defaults for. You can also use this `-XX:ActiveProcessorCount` if you don't want to set GC and RAM sizes manually, if you know which default configuration you want to force the JVM to use.

## Crypto

AES encryption/decryption has been optimized for Arm, and the optimizations are enabled by default in newer versions of Java.  

You can also look at [Amazon Corretto Crypto Provider (ACCP) 2](https://aws.amazon.com/blogs/security/accelerating-jvm-cryptography-with-amazon-corretto-crypto-provider-2/) to get the best performance on Arm. 

## Stack size

The default stack size for Java threads (ThreadStackSize) is 2 MB on aarch64 compared to 1 MB on x86_64. You can check the default with:

```console
java -XX:+PrintFlagsFinal -version | grep ThreadStackSize
```

The output is:

```output
     intx CompilerThreadStackSize = 2048  {pd product} {default}
     intx ThreadStackSize         = 2048  {pd product} {default}
     intx VMThreadStackSize       = 2048  {pd product} {default}
```

The default can be changed on the command line with either `-XX:ThreadStackSize=<kbytes>` or `-Xss<bytes>`. Note that the first option is in kilobytes and the second is in bytes. 

Usually, there's no need to change the default stack size, because the thread stack will be committed as it grows. 

## Transparent Huge Pages

If Transparent Huge Pages (THP) are set to always, the page size matches the default stack size. In this case, the full stack size is committed to memory. If you have a very high number of threads the memory usage will be large. 

To mitigate this issue, you can either manually change the stack size using the flags or change the THP setting to madvise. 

To view the THP value run:

```console
cat /sys/kernel/mm/transparent_hugepage/enabled
```

If you see the output shows the current value in brackets: 

```output
[always] madvise never
```

You can change to madvise by running:

```console
echo madvise | sudo tee /sys/kernel/mm/transparent_hugepage/enabled
```

Even if you change from always to madvise, the JVM can still use THP for the Java heap and code cache if you use the -XX:+UseTransparentHugePages flag.

## Native code in shared objects

A Java JAR (Java Archive) file is a package file format used to aggregate multiple Java class files, along with associated metadata and resources (like text, images, etc.), into a single file for distribution. 

JAR files can include compiled native code. The Java Native Interface (JNI) is used to interact with native code. For Linux, this means shared libraries (.so files) are included in the JAR. 

Java JARs can include shared-objects that are architecture specific. Some Java libraries check if these shared objects are found and if they are they use a JNI to call to the native library instead of relying on a generic Java implementation of the function. While the code might work, without the JNI the performance can suffer.

A quick way to check if a JAR contains such shared objects is to simply unzip it and check if any of the resulting files are shared-objects and if an aarch64 (arm64) shared-object is missing:

Unzip and search for share objects in the JAR:

```console
unzip foo.jar
find . -name "*.so" -exec file {} \;
```

For each x86-64 ELF file, check there is a corresponding aarch64 ELF file in the binaries. With some common packages (e.g. commons-crypto) we've seen that even though a JAR can be built supporting Arm manually, artifact repositories such as Maven don't have updated versions. To see if a certain artifact version may have Arm support, consult the [Common JARs with native code Table](https://github.com/aws/aws-graviton-getting-started/blob/main/CommonNativeJarsTable.md). 

## Are there other Java on Arm blogs?

Here are a few resources:
- [Improving Java performance on Neoverse N1 systems](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/java-performance-on-neoverse-n1)
- [Arm resources show how to optimize your Java applications for AArch64](https://blogs.oracle.com/javamagazine/post/java-arm-runtime-switches-benchmarks)
- [Unlocking Java Performance on Ampere Altra Family Processors](https://amperecomputing.com/tuning-guides/unlocking-java-performance-tuning-guide)

