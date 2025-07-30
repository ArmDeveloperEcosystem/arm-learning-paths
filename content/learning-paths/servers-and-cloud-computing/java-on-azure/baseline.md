---
title: Java Baseline Testing 
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Deploy a Java application with Tomcat-like operation 
Apache Tomcat is a Java-based web application server (technically, a Servlet container) that executes Java web applications. It's widely used to host Java servlets, JSP (JavaServer Pages), 
and RESTful APIs written in Java. 

The below Java class simulates the generation of a basic HTTP response and measures the time taken to construct it, mimicking a lightweight Tomcat-like operation. It measures how long it 
takes to build the response string, helping evaluate raw Java execution efficiency before deploying heavier frameworks like Tomcat.

Create a file named `HttpSingleRequestTest.java`, and add the below content to it:

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

You should see an output similar to:
```output

Response Generated:
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 29

Tomcat baseline test on Arm64
Response generation took 22125.79 microseconds.
```
Output summary:

- The program generated a fake HTTP 200 OK response with a custom message.
- It then measured and printed the time taken to generate that response (22125.79 microseconds).
- This serves as a basic baseline performance test of string formatting and memory handling on the JVM running on an Azure Arm64 instance.
