---
# User change
title: "Migrating applications to Arm servers"

weight: 2

layout: "learningpathall"


---

You can migrate applications to the Arm architecture and benefit from improved price performance.

This Learning Path provides a general overview of application migration to Arm servers. Specific migration examples are not covered, but technical guidance is provided which is useful for developers.

## Development machine

The first step in application migration is to setup a Linux development machine. Most of the time this an Arm based instance from a cloud service provider, but it can be any kind of virtual machine such as [Multipass](/install-guides/multipass/). You can use a development machine to explore and experiment with application dependencies. 

Assuming a Linux machine is available, analyze and make a list of what is needed to migrate a particular application to an Arm server.

Identify and create a list of development tools. 

Common development tools are:

- Programming languages for applications
- Build tools and languages used in build and run scripts
- Container tools
- Performance analysis tools

Other requirements could be a Linux Desktop to run graphical applications. 

Remember that all software needs to be available for the Arm architecture. While most applications in the Linux ecosystem run on Arm, keep an eye out for exceptions.

## Migration challenges

With a general idea of what is needed on the development machine, look into application dependencies in more detail. 

Common software dependencies include:
- Operating systems: most Linux distributions run on Arm, but not all. Older versions of Linux distributions may not be available on Arm. 
- Libraries: look for libraries that are not part of the operating system and are installed separately from the Linux package manager.
- Runtimes and frameworks: analyze packages used in Python and Javascript to make sure they available.
- Container dependencies: container applications rely on other containers. Many container images support multiple architectures, but some may not support Arm.
- Development tools: check that all tools are available on Arm, especially any proprietary software tools.

Start by making a list of dependencies and confirm they are available for the Arm architecture. Also, check for any dependence on cloud services used by an application.

For open source projects, search for Arm in the GitHub issues list and look at the project history. There is often a question and answer about Arm support.

Applications typically fall into three categories as shown on the table below. 

| Difficulty | Applications | Notes |
| -----------|--------------|---------|
| Easy       | Interpreted languages and Jit compilers (Python, Java, PHP, Node.js) | Use multi-arch container images and popular Linux distributions |
| More difficult | Compiled languages (C/C++, Go, Rust) | Recompile on an Arm development machine or cross-compile applications |
| Not possible | Something significant is not available on Arm | A language, runtime, or operating system which is not available on Arm |

While most software is available on Arm, you may come across dependencies which are not possible to run on Arm. 

## Tips

Things to be aware of when migrating applications.

### Interpreted and Containerized applications

- Python: make sure to use a newer pip
- Java: try [Amazon Corretto](https://aws.amazon.com/corretto) or use Java 11. Make sure to look for x86_64 shared objects in JARs. [Graviton getting started](https://github.com/aws/aws-graviton-getting-started/blob/main/java.md) has good tips.
- Containers: may need to rebuild some containers for the Arm architecture. Use the docker manifest command to see if Arm support is included in the image.

### Compiled applications

- C/C++: Look for intrinsics and use libraries for migration
- Go: Use a recent version, 1.18 and newer has many performance improvements for Arm

Newer software can make a big performance impact. 

## Example scenarios

Here are a number of real-world migration scenarios. They cover migrations ranging from easy to difficult. 

| Application migration | Migration results |
|-----------------------|--------------------|
|Node.js application    | Just works! nothing special for Arm and you may not even notice it is running on Arm|
|C++ application has some x86_64 intrinsics | [Migrate to NEON](/learning-paths/server-and-cloud/intrinsics/) using sse2neon or SIMDe|
|Pandoc (documentation tool) has a filter not available on Arm|Rebuild dependency library from source (and ask maintainers for Arm support)|
|Encryption in a Java app is slow | Use  -XX:+UnlockDiagnosticVMOptions -XX:+UseAESCTRIntrinsics flags to improve Arm crypto performance|
|Dependent container not available for Arm|Build the container yourself (and ask the maintainers for Arm support)|
Benchmark results are mediocre on Arm|Rebuild C++ components with newer compiler and enable [Large System Extensions](/learning-paths/server-and-cloud/lse/)|

## Summary

Arm servers enable the best price performance for many applications. The majority of software is available now to make it possible to migrate applications to Arm. 

Continue to get more guidance on a variety of migration topics. 



