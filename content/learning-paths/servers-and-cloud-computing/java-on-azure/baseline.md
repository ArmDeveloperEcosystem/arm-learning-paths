---
title: Java Baseline Testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Construct an HTTP response in Java

Before benchmarking with JMH, compile and run a small Java program on your Cobalt 200 VM. The program constructs an HTTP response string in memory and prints it. It does not start a server or perform network I/O.

The single elapsed-time measurement includes JVM startup effects such as class initialization and JIT compilation. Use it to check that the code runs, then use JMH in the next section for warmed-up measurements.

Using a file editor of your choice, create a file named `HttpSingleRequestTest.java`, and add the content below to it:

```java
public class HttpSingleRequestTest {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        String response = generateHttpResponse("Tomcat baseline test on Arm64");
        long endTime = System.nanoTime();
        double durationInMicros = (endTime - startTime) / 1_000.0;
        System.out.println("Response Generated:\n" + response);
        System.out.printf("Response generation took %.2f microseconds.%n", durationInMicros);
    }
    private static String generateHttpResponse(String body) {
        return "HTTP/1.1 200 OK\r\n" +
               "Content-Type: text/plain\r\n" +
               "Content-Length: " + body.length() + "\r\n\r\n" +
               body;
    }
}
```
## Compile and run the Java program

Compile the program and run it with modest heap sizes and the G1 garbage collector:

```console
javac HttpSingleRequestTest.java
java -Xms128m -Xmx256m -XX:+UseG1GC HttpSingleRequestTest
```

## JVM flags explained

- **-Xms128m** - sets the initial heap size to 128 MB
- **-Xmx256m** - sets the maximum heap size to 256 MB
- **-XX:+UseG1GC** - enables the G1 garbage collector designed for low pause times

## Sample output

If the program runs successfully, you should see output similar to the following:

```output
Response Generated:
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 29

Tomcat baseline test on Arm64
Response generation took 6780.65 microseconds.
```

## Interpret the result

The response should contain `HTTP/1.1 200 OK`, a text content type, and the sample body. The content length is valid for this ASCII-only example. For arbitrary text, HTTP content length must reflect the encoded byte count.

The printed time is a single measurement during a fresh JVM run. It varies with class loading, compilation, CPU load, and other activity, and does not measure HTTP server latency or steady-state Java performance. Continue to JMH to measure repeated response construction with warmup.
