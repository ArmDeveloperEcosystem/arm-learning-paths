---
title: Laying the foundations
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section you will setup the structure for the Matrix processing library. 
At the end, you will be able to build the library and an application that uses the library on
all supported platforms: macOS, Linux, and Windows.

## Before you begin

You will need the following tools, make sure they are available on your development platform:

- A C++ compiler with C++17 support. Any recent version of Clang or the GNU compiler
  (gcc) will work.
- [CMake](/install-guides/cmake/) build tool
- A build system: [GNU Make](https://www.gnu.org/software/make/) or
  [Ninja](https://ninja-build.org/)
- A documentation generator: [Doxygen](https://www.doxygen.nl/)
- An IDE ([Visual Studio Code](https://code.visualstudio.com/) is a popular
  choice) or a text editor ([Vim](https://www.vim.org/), [GNU
  EMacs](https://www.gnu.org/software/emacs/), [Sublime
  Text](https://www.sublimetext.com/) are popular choices).

## About configuring vs. building

When developing software, two separate but linked aspects must be
considered: 
- How to configure the project 
- How to build the source code

The first aspect is about configuring the project, which covers:
- The platform itself (Windows, macOS, Linux): each platform has specific
  requirements and usage.
- Discovering what is available on the platform. For example, `libpng` might
  be required by the project to process images in the PNG format, and it may or may not
  be available on the platform. Alternatively, it might be available, but not with a
  suitable configuration for the project needs. You may need to 
  maintain a custom version of required dependencies. 
- Selecting project features: in some cases, projects might offer some degree of
  configuration, for example to disable support for PNG format images when a
  user knows that a feature will never be used. This is done to avoid bloating the
  application with never used code and functionality.

The second aspect is about building the project, which covers:
- Compiling the human readable source code to produce binaries (executables and
  libraries) that can be run. This involves invoking tools
  like compilers and linkers.
- Managing dependencies: this ensures the different parts of the project are built
  in the proper order, and that when a rebuild is necessary (because a file has
  changed for example), only the required parts of the project are re-built. It
  is an important optimization to save build time, especially for developers as
  they spend most of their time in an edit-compile-run loop.

These two aspects are so common that tools are available to ease development and
cover all situations and platforms. The tool used for this project is 
CMake. CMake is available on all platforms and used by
numerous projects, from very small projects to large 
projects like [LLVM](https://www.llvm.org) or [Qt](https://www.qt.io/).

## Directory structure

Organizing the files in a project is important because it allows you to:

- Easily navigate and find information for new people as well as experienced
  developers
- Organize the information for the tools, such as compilers and linkers
- Organize the information of what will be exported or installed and what is
  only relevant for building the project
- Accommodate for future growth: over time, features will be added to the
  project, which usually translates to more source files. Having the proper
  directory structure in place will help to keep the project tidy

The directory structure of this project is:

```TXT
Matrix/
├── build/
├── include/
│   └── Matrix/
├── lib/
│   └── Matrix/
└── src/
```

It's a common practice, and CMake recommends it, to build projects outside of
the source tree as this provides several advantages:

- Keeps clutter out of the source tree, which is often under version control
- Provides an easy way to remove the build artifacts (object files, libraries,
  executables, libraries)
- Allows several build trees to co-exist at the same time, to have for example
  debug and optimized builds, or builds with different configuration options

In this case, the project will be built in the `build/` directory.

{{% notice Note%}}
If the project is under version control, then the `build/` directory can be
ignored because the contents can always be regenerated. If you are using `git`,
the way to configure `git` to ignore the `build/` directory is to add it to a
`.gitignore` file. Other revision control systems have a similar way to ignore
files and directories.
{{% /notice %}}

You will also note that the Matrix library headers are located in a `Matrix/`
directory. It is highly probable that some of the header files (`Matrix.h` for
example) will collide with some other file for some users. In order to be sure
that compilers pick the right files, all the headers are placed in a `Matrix/`
directory, effectively giving some form of namespace to the include file look-up
by the tools.

The source code for the Matrix library will live in `lib/Matrix` and the
applications' source code will be located in `src/`.

## Add a demo application

There is nothing like creating the canonical `Hello, World!` application. 

Use your favorite text editor or IDE to
create the file `src/howdy.cpp` and add the following content to it:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-1/src/howdy.cpp" >}}

## Setup CMake

CMake reads a file named `CMakeLists.txt` to get the project description
and all of its instructions.

At the top of your project, create file `CMakeLists.txt` and add the following
content to it with your text editor:

```TXT
cmake_minimum_required(VERSION 3.5)

project(Matrix LANGUAGES CXX)

add_executable(howdy src/howdy.cpp)
```

The `cmake_minimum_required` command at the first line tells CMake that the
project wants it to be at least version 3.5. This is a very old version because
your Matrix project is not using any new commands or options from CMake.
`cmake_minimum_required` is required, as it helps diagnose version
mismatches.

The second command, `project` is also required by CMake: it gives a name
(`Matrix`) to the project and specifies which language is used (C++).

The last command, `add_executable` instructs CMake to build an executable named
`howdy` from source file `src/howdy.cpp`.

From this minimalistic project description, you are ready to configure
and build your Matrix project.

## Configure and build the application

At this stage, your project contains the following directories and files:

```TXT
Matrix/
├── CMakeLists.txt
├── include/
│   └── Matrix/
├── lib/
│   └── Matrix/
└── src/
    └── howdy.cpp
```

Copy and paste the command below to configure your project, using `clang++` as the
C++ compiler, `Ninja` as the build system, `build` as the out-of-tree build
directory, and the current directory (`.`) as the project source directory:

```BASH { output_lines = "2-10" }
CXX=clang++ cmake -G Ninja -B build -S .
-- The CXX compiler identification is AppleClang 15.0.0.15000100
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /opt/homebrew/opt/ccache/libexec/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done (0.9s)
-- Generating done (0.0s)
-- Build files have been written to: .../chapter-1/build
```

To use the default build system, Unix Makefiles, you can just the `-G Ninja` above.

Now that your project is configured, build it with:

```BASH { output_lines = "3" }
cd build/
ninja
[2/2] Linking CXX executable howdy
```

Execute the `howdy` application with:

```BASH { output_lines = "2" }
./howdy
Hello, World !
```

Depending on your platform, the application may be named slightly differently,
On Windows it would be `howdy.exe`, so to execute it you would instead
have to type:

```BASH { output_lines = "2" }
.\howdy.exe
Hello, World !
```

{{% notice Note%}}
You can remove the `build` directory at any point without any fear of losing
important data, as you can always recreate those files with the above configure
and build steps.
{{% /notice %}}

## Add the Matrix library foundations

You will now add the Matrix library foundations: a header file, source code,
build instructions, and another example program using the library to check
everything is working.

The simplest function you can add at this stage is one that will return the
library version.

Add the `Matrix.h` header file, declaring the `Version` object
and the `getVersion` function and save the file as `include/Matrix/Matrix.h`:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-1/include/Matrix/Matrix.h" >}}

With those declarations in place, create and add the following lines to
`lib/Matrix/Matrix.cpp` to provide an implementation to `getVersion`:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-1/lib/Matrix/Matrix.cpp" >}}

Now, you can create a program that will make use of the
``getVersion`` function. Use your editor to save the code below as `src/getVersion.cpp`:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-1/src/getVersion.cpp" >}}

Finally, add the instructions below in the top-level `CMakeLists.txt`
to build the Matrix library, with `add_library`, and instruct CMake where the
Matrix library header files can be found with `target_include_directories` (and
specify along the way that C++17 is to be used for the Matrix library with
`target_compile_features`), and eventually compile our `src/getVersion.cpp` file
and link it to the Matrix library with `add_executable` and
`target_link_library` to produce the `matrix-getVersion` executable:

{{< include-code TXT "content/learning-paths/cross-platform/matrix/projects/chapter-1/CMakeLists.txt" >}}

Now build and run the program with:

```BASH { output_lines = "2-3,5" }
ninja
[6/6] Linking CXX executable matrix-getVersion

./matrix-getVersion
Using Matrix version: 0.1.0
```

Congratulations, you have constructed a library and a program to test it. 

## What have you achieved so far ?

At this stage, your Matrix project has the following directory structure:
slightly different on Windows or Linux):

```TXT
Matrix/
├── CMakeLists.txt
├── build/
│   ├── CMakeCache.txt
│   ...
│   ├── howdy*             <- The howdy executable program
│   ├── libMatrix.a        <- The Matrix library
│   └── matrix-getVersion* <- The getVersion executable program
├── include/
│   └── Matrix/
│       └── Matrix.h
├── lib/
│   └── Matrix/
│       └── Matrix.cpp
└── src/
    ├── getVersion.cpp
    └── howdy.cpp
```

You can download the [archive](/artifacts/matrix/chapter-1.tar.xz) of the
project in its current state to experiment locally on your machine.

You have created the foundation for developing and evolving your Matrix
library in a platform agnostic way, meaning it can be easily developed and used
on macOS, Linux, and Windows. This was done *almost* effortlessly thanks to
CMake, which shields developers from all the platform specific details like how
to invoke the compiler, build libraries, and link with those libraries on each of
those platforms.

On top of hiding the platform specific details, CMake also does not force a
development environment onto project developers as you can use your favorite editor or IDE. 
For example, Visual Studio Code can work seamlessly with CMake thanks to some plugins, and CMake can
generate project files for several popular IDEs, such as Xcode, Sublime Text, Eclipse,
CodeBlocks, and CodeLite. You can run `cmake --help` to get a
list of supported *generators* (in CMake terminology) for your platform.
