---
title: Java Baseline Testing 
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Deploy a Java application with a Tomcat-like operation 
Apache Tomcat is a widely used Java web application server. Technically, it is a Servlet container, responsible for executing Java servlets and supporting technologies like:

  * JSP (JavaServer Pages): Java-based templates for dynamic web content.
  * RESTful APIs: Lightweight endpoints for modern microservices.

In production, frameworks like Tomcat introduce additional complexity (request parsing, thread management, I/O handling). Before layering those components, it's useful to measure how efficiently raw Java executes simple request/response logic on Azure Cobalt 100 Arm-based instances.

In this section, you will run a minimal Tomcat-like simulation. It won't launch a real server, but instead it:
  * Constructs a basic HTTP response string in memory.
  * Measures the time taken to build that response, acting as a microbenchmark.
  * Provides a baseline for raw string and I/O handling performance in Java.

Using a file editor of your choice create a file named `HttpSingleRequestTest.java`, and add the content below to it:

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
Compile and Run Java program :

```console
javac HttpSingleRequestTest.java
java -Xms128m -Xmx256m -XX:+UseG1GC HttpSingleRequestTest
```

- -Xms128m  sets the initial heap size for the Java Virtual Machine to 128 MB. 
- -Xmx256m sets the maximum heap size for the JVM to 256 MB. 
- -XX:+UseG1GC enables the G1 Garbage Collector (Garbage First GC), designed for low pause times and better performance in large heaps.

You should output similar to:
```output
java -Xms128m -Xmx256m -XX:+UseG1GC HttpSingleRequestTest
Response Generated:
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 29

Tomcat baseline test on Arm64
Response generation took 12901.53 microseconds.
```
Output breakdown:

Generated Response: The program generates a fake HTTP 200 OK response with headers and a custom body string.
Timing Result: The program prints how long it took (in microseconds) to build that response.
In this example, it took ~12,901 µs (~12.9 ms). Your result will vary depending on CPU load, JVM warm-up, and environment.

This provides you with a baseline measurement of how Java handles simple string operations and memory allocation on Cobalt 100 (Arm64) instances.
It serves as a lightweight proxy for Tomcat-style request handling before adding the full complexity of a servlet container.
