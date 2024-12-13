---
title: Example Application
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example Application

Using a file editor of your choice, copy the Java snippet below into a file named `HeapUsageExample.java`. 

This code example allocates 1 million string objects to fill up the heap. You can use this example to easily observe the effects of different GC tuning parameters.

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

### Enable Garbage Collector logging

To observe what the Garbage Collector is doing, one option is to enabling logging while the JVM is running. 

To enable this, you need to pass in some command-line arguments. The `gc` option logs the GC information. The `filecount` option creates a rolling log to prevent uncontrolled growth of logs with the drawback that historical logs might be rewritten and lost. 

Run the following command to enable logging with JDK 11 and higher:

```bash
java -Xms512m -Xmx1024m -XX:+UseSerialGC -Xlog:gc:file=gc.log:tags,uptime,time,level:filecount=10,filesize=16m HeapUsageExample.java
```

If you are using JDK8, use the following command instead:

```bash
java -Xms512m -Xmx1024m -XX:+UseSerialGC -Xloggc:gc.log -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation HeapUsageExample.java
```

The `-Xms512m` and `-Xmx1024` options create a minimum and maximum heap size of 512 MiB and 1GiB respectively. This is to avoid waiting too long to see activity within the GC. Additionally, you can force the JVM to use the serial garbage collector with the `-XX:+UseSerialGC` flag. 

You will now see a log file, named `gc.log` created within the same directory. 

Open `gc.log` and the contents should look similar to:

```output
[2024-11-08T15:04:54.304+0000][0.713s][info][gc] GC(2) Pause Young (Allocation Failure) 139M->3M(494M) 3.627ms
...
[2024-11-08T15:04:54.350+0000][0.759s][info][gc] GC(3) Pause Young (Allocation Failure) 139M->3M(494M) 3.699ms
```

These logs provide insights into the frequency, duration, and impact of Young garbage collection events. The results can vary depending on your system.

    - Frequency: ~ every 46 ms
    - Pause duration: ~ 3.6 ms
    - Reduction size: ~ 139 MB (or 3M objects)

This logging method can be quite verbose, and makes it challenging to debug a live running application. 

### Use jstat to observe real-time GC statistics

Using a file editor of your choice, copy the java code below into a file named `WhileLoopExample.java`. 

This java code snippet is a long-running example that prints out a random integer and double precision floating point number four times a second:

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

            // Sleep for 1/4 second (250 milliseconds)
            try {
                Thread.sleep(250);
            } catch (InterruptedException e) {
                System.err.println("Thread interrupted: " + e.getMessage());
            }
        }
    }
}
```

Start the Java program with the command below. This will use the default parameters for the garbage collection:

```bash
java WhileLoopExample.java
```
While the program is running, open another terminal session. 

In the new terminal use the `jstat` command to print out the JVM statistics specifically related to the GC using the `-gcutil` flag:

```bash
jstat -gcutil $(pgrep java) 1000
```

You will observe output like the following until `ctl+c` is pressed:

```output
  S0     S1     E      O      M     CCS    YGC     YGCT    FGC    FGCT    CGC    CGCT     GCT   
  0.00 100.00   6.11   1.81  71.05  73.21      1    0.010     0    0.000     0    0.000    0.010
  0.00 100.00   6.11   1.81  71.05  73.21      1    0.010     0    0.000     0    0.000    0.010
  0.00 100.00   6.11   1.81  71.05  73.21      1    0.010     0    0.000     0    0.000    0.010
...
  0.00 100.00   6.11   1.81  71.05  73.21      1    0.010     0    0.000     0    0.000    0.010
```

The columns of interest are:
- **E (Eden Space Utilization)**: The percentage of the Eden space that is being used. High utilization indicates frequent allocations and can trigger minor GCs.
- **O (Old Generation Utilization)**: The percentage of the Old (Tenured) generation that is being used. High utilization can lead to Full GCs, which are more expensive.
- **YGCT (Young Generation GC Time)**: The total time in seconds spent in Young Generation (minor) GC events. High values indicate frequent minor GCs, which can impact performance.
- **FGCT (Full GC Time)**: The total time in seconds spent in Full GC events. High values indicate frequent Full GCs, which can significantly impact performance.
- **GCT (Total GC Time)**: The total time in seconds spent in all GC events (Young, Full, and Concurrent). This provides an overall view of the time spent in GC, helping to assess the impact on application performance.


