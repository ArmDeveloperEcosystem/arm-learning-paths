---
title: Example Application
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example Application.

Copy and paste the following Java snippet into a file called `HeapUsageExample.java`. This contrived code example allocates 1 million string objects to fill up the heap. We can use this example to easily observe the effects of different GC tuning parameters.

```java
public class HeapUsageExample {
    public static void main(String[] args) {
        System.out.println("Starting the application...");

        try {
            // Create a large number of objects to quickly use up the heap
            for (int i = 0; i < 1000000; i++) {
                String[] array = new String[1000];
                for (int j = 0; j < array.length; j++) {
                    array[j] = "Object " + j;
                }
            }
        } catch (OutOfMemoryError e) {
            System.err.println("OutOfMemoryError caught: " + e.getMessage());
        }

        System.out.println("Application finished.");
    }
}
```

### Enable GC logging

To observe the what the GC is doing, one option is to enabling logging whilst the JVM is running. To enable this, we need to pass in some command-line arguments. The `gc` option logs the GC information we are interested. The `filecount` option creates a rolling log to prevent uncontrolled growth of logs with the drawback that historical logs may be rewritten and lost. Run the following command from the terminal. 

```bash
java -Xms512m -Xmx1024m -XX:+UseSerialGC -Xlog:gc:file=gc.log:tags,uptime,time,level:filecount=10,filesize=16m HeapUsageExample.java
```

> **_PLEASE NOTE:_** This command will work with JDK 11 onwards (to be checked)

The `-Xms512m` and `-Xmx1024` options create a minimum and maximum heap size of 512 MiB and 1GiB respectively. This is simply so we do not have to wait for too long to see activity within the GC. Additionally, we force the JVM to use the serial garbage collector with the `-XX:+UseSerialGC` flag. 

You will now see logs, named `gc.log.*` within the same directory. Viewing the contents you will see the following.

```output
[2024-11-08T15:04:54.304+0000][0.713s][info][gc          ] GC(2) Pause Young (Allocation Failure) 139M->3M(494M) 3.627ms
...
[2024-11-08T15:04:54.350+0000][0.759s][info][gc          ] GC(3) Pause Young (Allocation Failure) 139M->3M(494M) 3.699ms
```

From these logs we can see how often the Young garbage collection is occuring, by how much of the Young segment is reduced and how long it takes. The results below will vary on your own system. 

- Frequency ~= Every 0.14s 
- Pause duration ~= 3.6ms
- Reduction size ~= 139MB -> 3M

This logging method has the benefit of being verbose but at the tradeoff of clarity. Furthermore, this method clearly isn't suitable for a running process which makes debugging a live environment slightly more challenging. 

### Use jstat to observe real-time GC statistics

The following java code snippet is a long-running example that prints out a random integer and double precision floating point number 4 times a second. Copy the example below and paste into a file called `WhileLoopExample.java`.

```java
import java.util.Random;

public class GenerateRandom {

    public static void main(String[] args) {
        Random rand = new Random();

        while (true) {
            // Generate random integer in range 0 to 999
            int rand_int1 = rand.nextInt(1000);

            // Print random integer
            System.out.println("Random Integers: " + rand_int1);

            // Generate random double
            double rand_dub1 = rand.nextDouble();

            // Print random double
            System.out.println("Random Doubles: " + rand_dub1);

            // Sleep for 1 second (1000 milliseconds)
            try {
                Thread.sleep(250);
            } catch (InterruptedException e) {
                System.err.println("Thread interrupted: " + e.getMessage());
            }
        }
    }
}
```

Run the following command and open up a separate terminal session. Start the Java program with the command below. This will use the default parameters for the garbage collection. 

```bash
java WhileLoopExample.java
```
On the other terminal session, we use the `jstat` command to print out the JVM statistics specifically related to the GC using the `-gcutil` flag. 

```bash
jstat -gcutil $(pgrep java) 1000
```


You will obserse an output like the following:

```output
  S0     S1     E      O      M     CCS    YGC     YGCT     FGC    FGCT     CGC    CGCT       GCT   
     -      -  33.33   0.00      -      -      0     0.000     0     0.000     0     0.000     0.000
     -      -  33.33   0.00      -      -      0     0.000     0     0.000     0     0.000     0.000
     -      -  33.33   0.00      -      -      0     0.000     0     0.000     0     0.000     0.000
```

The columns of interest are:
- **E (Eden Space Utilization)**: The percentage of the Eden space that is currently used. High utilization indicates frequent allocations and can trigger minor GCs.
- **O (Old Generation Utilization)**: The percentage of the Old (Tenured) generation that is currently used. High utilization can lead to Full GCs, which are more expensive.
- **YGCT (Young Generation GC Time)**: The total time (in seconds) spent in Young Generation (minor) GC events. High values indicate frequent minor GCs, which can impact performance.
- **FGCT (Full GC Time)**: The total time (in seconds) spent in Full GC events. High values indicate frequent Full GCs, which can significantly impact performance.
- **GCT (Total GC Time)**: The total time (in seconds) spent in all GC events (Young, Full, and Concurrent). This provides an overall view of the time spent in GC, helping to assess the impact on application performance.


