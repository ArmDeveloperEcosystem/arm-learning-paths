---
title: "Run the application and compare execution times"

weight: 3

layout: "learningpathall"
---

## Objective
In this section, you will change the build configuration of the application and then launch it using various settings to compare the computation times.

## Building and running an application
To prepare an application for ARM64 and x64 builds, proceed as follows:

1. Click the Any CPU drop-down and select Configuration Manager...:

![fig8](Figures/08.png)

2. In the Configuration Manager, click New... from the Active Solution Platform drop-down:

![fig9](Figures/09.png)

3. In the New Solution Platform window, select ARM64, and click the OK button.

![fig10](Figures/10.png)

4. Similarly, create the x64 solution platform.

To build and run the application. Select the solution platform (like x64), and then click Arm64.Desktop.WPF button:

![fig11](Figures/11.png)

When the application launches, type the execution count value (e.g., 2000), and click the "Run calculations" button. The application will display the column with the label denoting the computation time. Repeat this for other execution counts: 4000, 6000, 8000, and 10000. Your results should look like the following figure.

![fig12](Figures/12.png)

Now, relaunch the application for the ARM64 solution platform, and observe the computation times:

![fig13](Figures/13.png)

On average, we achieved about a 30% reduction in computation times.

## Summary
In this learning path, we created the Windows Presentation Foundation. The application was performing a computationally intensive operation: the multiply-add operation on two vectors. This operation served as a benchmark to measure and compare the performance between the two architectures: x64 and Arm64. 

Upon running the application with various execution counts on both configurations, we systematically recorded the computation times. The exercise illuminated a noteworthy performance gain—on average, a 30% reduction in computation times—when the application ran on the Arm64 architecture compared to the x64 architecture. This significant improvement highlights the advantage of tailoring applications to specific hardware architectures, in this case, demonstrating the enhanced performance capabilities of Arm64 architecture-based devices for demanding computational tasks.
