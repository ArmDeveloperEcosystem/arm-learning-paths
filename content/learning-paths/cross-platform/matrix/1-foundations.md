---
title: Laying the foundations
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## How do I get started on setting up my development platform?

To begin, make sure you have the following tools available on your development platform:

- A C++ compiler with C++17 support. Clang or the GNU compiler (gcc) both work.
- [CMake](/install-guides/cmake/) build tool.
- A build system. You can use [GNU Make](https://www.gnu.org/software/make/) or
  [Ninja](https://ninja-build.org/).
- A documentation generator. You can use [Doxygen](https://www.doxygen.nl/).

On a Ubuntu machine, they can be installed with:

```BASH
sudo apt-get install build-essential clang ninja-build cmake doxygen -y
```

In addition to these tools, you also need an IDE (Integrated Development
Environment).

[Visual Studio Code](https://code.visualstudio.com/) is a popular
choice, and you can install it by following these
[instructions](https://code.visualstudio.com/docs/setup/linux). Alternatively,
you can use a text editor like [Vim](https://www.vim.org/), [GNU
Emacs](https://www.gnu.org/software/emacs/), or [Sublime
Text](https://www.sublimetext.com/), which are also popular and they all
support extensions that make C++ development easy.


## What are the differences between configuring the project and building the code?

When developing software, there are two separate, but linked, stages:

- Configuring the project.
- Building the source code.

**Configuring the project** includes making decisions and preparatory work around:
- Selecting a platform, such as Windows, macOS, or Linux - each platform has its own specific
  requirements and usage.
- Discovering what is available on the platform - for example, `libpng` might be
  required by the project to process images in PNG format, but it might not be available on the platform. Alternatively, it might be available, but not with a suitable configuration for the project requirements. You may need to maintain a customized version of required dependencies.
- Selecting project features - in some cases, projects might offer some degree of configuration, for example, disabling support for a feature that will never be used. This is done to avoid bloating the application with never-used code and functionality.


**Building the source code** includes:
- Compiling the human-readable source code to produce binaries (executables and
  libraries) that can be run. This involves invoking tools like compilers and linkers.
- Managing dependencies - this ensures that the different parts of the project are built
  in the correct order, and that when a rebuild is necessary, such as when a file changes, only the required parts of the project are rebuilt. It is an important optimization to save build time, especially for developers who spend most of their time in an edit-compile-run loop.

These two considerations are fundamental to the process of getting set up. Accordingly, tools are available to ease development and
cover a wide variety of situations and platforms. The tool used for this project is
**CMake**. CMake is available on all platforms and used by
numerous projects, from very small projects to large
projects like [LLVM](https://www.llvm.org) or [Qt](https://www.qt.io/).

## Directory structure

Organizing the files in a project is important because it allows you to:

- Easily navigate the structure and find information.  
- Organize information for the tools, such as compilers and linkers.
- Make a distinction between information that is exported or installed, and what is
  only relevant for building the project.
- Accommodate for future growth - over time, features are added to the
  project, which usually translates to more source files. Having an organized
  directory structure improves the efficiency of the project.

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

CMake recommends that you build projects outside of the source tree for the following reasons:

- Reduces clutter in the source tree, which is often under version control.
- Provides an easy way to remove the build artifacts, such as object files, libraries, and executables.
- Allows several build trees to co-exist. For example, to have debug and optimized builds, or builds with differing configuration options.

In this case, the project is built in the `build/` directory.

{{% notice Note%}}
If the project is under version control, then the `build/` directory can be
ignored as the contents can always be regenerated. If you are using `git`,
the way to configure `git` to ignore the `build/` directory is to add it to a
`.gitignore` file. Other revision control systems have a similar way to ignore
files and directories.
{{% /notice %}}

You will also note that the Matrix library headers are located in a `Matrix/`
directory. It is highly probable that some of the header files (`Matrix.h` for
example) will collide with some other file for some users. In order to be sure
that compilers pick the right files, all the headers are placed in a `Matrix/`
directory, effectively providing some form of namespace to the include file look-up
by the tools.

The source code for the Matrix library will live in `lib/Matrix` and the
applications' source code will be located in `src/`.

## Add a demo application

There is nothing like creating the canonical `Hello, World!` application!

Use your favorite text editor or IDE to
create the file `src/howdy.cpp` and add the following content:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-1/src/howdy.cpp" >}}

## Setup CMake

CMake reads a file named `CMakeLists.txt` to get the project description
and all of its instructions.

At the top of your project, create file `CMakeLists.txt` and add the following
content to it, using your text editor:

```TXT
cmake_minimum_required(VERSION 3.5)

project(Matrix LANGUAGES CXX)

add_executable(howdy src/howdy.cpp)
```

The `cmake_minimum_required` command at the first line tells CMake that the
project requires at least version 3.5. This is an old version because
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

To use the default build system, Unix Makefiles, you can just omit the `-G Ninja`
from the command line.

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

Depending on your platform, the application might be named slightly differently.
On Windows, it would be `howdy.exe`, so to execute it you would instead
have to type:

```BASH { output_lines = "2" }
.\howdy.exe
Hello, World !
```

{{% notice Note%}}
You can remove the `build` directory at any point without any fear of losing
important data, as you can always recreate those files with the configure-and-build steps described above.
{{% /notice %}}

## Add the Matrix library foundations

You will now add the Matrix library foundations: a header file, source code,
build instructions, and another example program using the library to check that
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

Finally, add the instructions below in the top-level `CMakeLists.txt`:

{{< include-code TXT "content/learning-paths/cross-platform/matrix/projects/chapter-1/CMakeLists.txt" >}}

The `add_library` instructs CMake how to build the Matrix library. The
`target_include_directories` specifies where the Matrix library header is located, and the `target_compile_features` specifies that C++17 is the version
of the C++ language that is used by the Matrix library. The `matrix-getVersion`
executable is compiled from the `src/getVersion.cpp` source file with the
`add_executable` command and has to be linked with our Matrix library with the
`target_link_library` command.

Now build the program with:

```BASH { output_lines = "2" }
ninja
[6/6] Linking CXX executable matrix-getVersion
```

and run it with:

```BASH { output_lines = "2" }
./matrix-getVersion
Using Matrix version: 0.1.0
```

Congratulations, you have constructed a library and a program to test it!

## What have you achieved so far ?

At this stage, your Matrix project has the following directory structure, which is slightly different depending on whether it is Windows or Linux:

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

You have created the foundation for developing and evolving your Matrix
library in a platform-agnostic way, meaning that it can be easily developed and used
on macOS, Linux, and Windows. This was done *almost* effortlessly thanks to
CMake, which shields developers from all the platform-specific details such as how
to invoke the compiler, build libraries, and link with those libraries on each of
those platforms.

In addition to concealing the platform-specific details, CMake also does not restrict project developers to one specific development environment. You can use your favorite editor or IDE.
For example, Visual Studio Code can work seamlessly with CMake with plugins, and CMake can
generate project files for several popular IDEs, such as Xcode, Sublime Text, Eclipse,
CodeBlocks, and CodeLite. You can run `cmake --help` to get a
list of supported *generators* (in CMake terminology) for your platform.
