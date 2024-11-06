---
title: Example Application
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example Application.

Copy and paste the following Java snippet into a file called `short_lived_mem.java`. This code snippet simply indefinitely prints out random integers. 

```java
public class GenerateRandom {

    public static void main(String[] args) {
        Random rand = new Random();

        while (true) {
            // Generate random integers in range 0 to 999
            int rand_int1 = rand.nextInt(1000);
            int rand_int2 = rand.nextInt(1000);

            // Print random integers
            System.out.println("Random Integers: " + rand_int1);
            System.out.println("Random Integers: " + rand_int2);


            // Sleep for 1 second (1000 milliseconds)
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.err.println("Thread interrupted: " + e.getMessage());
            }
        }
    }
}
```
