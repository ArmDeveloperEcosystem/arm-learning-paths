---
title: Test the library
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Learn about unit testing

It's common practice when developing software to create unit tests. While it
might appear unnecessary in the beginning, tests provide significant
advantages:

- Confidence for developers, when adding new functionality, or when porting
  to a new platform 
- Confidence for the users that the quality is good
- Ability to catch regressions
- Show how to use the library in practice
- Welcome new people to the project, as this allows them to check their patches
  and make sure they did not inadvertently brake anything

You'll notice that setting up testing comes before the actual library code development.

Many unit testing frameworks exist in general, and C++ is not short of them as
you can notice in this [wikipedia
article](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#C++). 
This project uses [GoogleTest](https://github.com/google/googletest) as the testing framework.

## Setup GoogleTest

You could rely on the operating system platform to provide GoogleTest, then 
ask developers to install it on each computer they use, but this feels like an
unnecessary step. 

As testing is a corner stone of your Matrix library
development, GoogleTest should be installed automatically as a dependency in the
build tree of your project. 

One great feature of GoogleTest is that it provides a seamless integration with CMake. 

Adding external dependencies is easily done with CMake. This is done with a
separate `CMakeLists.txt` file, placed in the `external/` directory. This file covers
all external dependencies. It will be used by the main
`CMakeLists.txt`.

Create the file `external/CMakeLists.txt` with the following content:

{{< include-code TXT "content/learning-paths/cross-platform/matrix/projects/chapter-2/external/CMakeLists.txt" >}}

You may notice a new new CMake feature, variables. Variables start with the `$`
character and have a name in between curly braces. A CMake variable can be set by
the CMake itself, or by the user, and they can be modified or used. 

In this case, the variable `${EXTERNAL_PROJECT_CMAKE_ARGS}` is set with the options to 
pass to CMake for installing the external dependencies:

- `${CMAKE_CXX_COMPILER}`: the C++ compiler used by CMake
- `${CMAKE_BUILD_TYPE}`: the type of build used by CMake (`Release`, `Debug`,
  ...)
- `${CMAKE_INSTALL_PREFIX}`: where CMake will install the project

The project now looks like this:

```TXT
Matrix/
├── CMakeLists.txt
├── build/
│   ...
├── external/
│   └── CMakeLists.txt
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

Next, you need to use the new `CMakeLists.txt` in the top level CMake file.

Add the following lines after the Matrix project declaration in the top-level
`CMakeLists.txt`:

```TXT
# ===================================================================
# Download, configure, build and install locally our external dependencies.
# This is done once, at configuration time.
# -------------------------------------------------------------------

# Build CMake command line so that it will use the same CMake configuration than
# the one we have been invoked with (generator, compiler, build type, build directory)
set(EXTERNAL_PROJECT_CMAKE_ARGS
      -G ${CMAKE_GENERATOR}
      -DCMAKE_CXX_COMPILER:PATH=${CMAKE_CXX_COMPILER}
      -DCMAKE_BUILD_TYPE:STRING=${CMAKE_BUILD_TYPE}
      -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_BINARY_DIR})

# Download and configure our external dependencies
execute_process(
  COMMAND ${CMAKE_COMMAND}
      -S ${CMAKE_SOURCE_DIR}/external
      -B ${CMAKE_BINARY_DIR}/external
      ${EXTERNAL_PROJECT_CMAKE_ARGS}
)

# Build our external dependencies.
execute_process(
  COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR}/external
)
# Install our external dependencies.
execute_process(
  COMMAND ${CMAKE_COMMAND} --install ${CMAKE_BINARY_DIR}/external
)

# Import googletest package information (library names, paths, dependencies, ...)
set(GTest_DIR "${CMAKE_BINARY_DIR}/lib/cmake/GTest"
    CACHE PATH "Path to the googletest package configuration files")
find_package(GTest REQUIRED
  CONFIG
  NO_DEFAULT_PATH
  NO_PACKAGE_ROOT_PATH
  NO_SYSTEM_ENVIRONMENT_PATH
)
```

The variable `${CMAKE_GENERATOR}` is what CMake uses to perform the build, usually GNU
Make or Ninja, but it can be an IDE specific project file as well.

The variable `${CMAKE_SOURCE_DIR}` is the path to the top level directory of your project
(where the main `CMakeLists.txt` is located) and `${CMAKE_BINARY_DIR}` is the
build directory.

At configuration time, CMake will download, build and install GoogleTest and
make it available to your project using `find_package`.

Now if you build the project, CMake notices it has been updated and will
perform all necessary steps. 

The output belows shows that besides the
executable, CMake has configured, built, and installed GoogleTest.

Copy and paste the commands to run the build yourself to see the output:

```BASH { output_lines = "3-88" }
cd build
ninja
-- The CXX compiler identification is AppleClang 15.0.0.15000309
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /opt/homebrew/opt/ccache/libexec/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- The CXX compiler identification is AppleClang 15.0.0.15000309
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /opt/homebrew/opt/ccache/libexec/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done (0.3s)
-- Generating done (0.0s)
-- Build files have been written to: .../chapter-2/build/external
[1/8] Creating directories for 'googletest'
[2/8] Performing download step (git clone) for 'googletest'
Cloning into 'googletest'...
HEAD is now at f8d7d77 Bump version to v1.14 in preparation for release
[3/8] Performing update step for 'googletest'
[4/8] No patch step for 'googletest'
[5/8] Performing configure step for 'googletest'
-- The C compiler identification is AppleClang 15.0.0.15000309
-- The CXX compiler identification is AppleClang 15.0.0.15000309
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /opt/homebrew/opt/ccache/libexec/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /opt/homebrew/opt/ccache/libexec/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found Python3: /opt/homebrew/Frameworks/Python.framework/Versions/3.12/bin/python3.12 (found version "3.12.2") found components: Interpreter
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Configuring done (1.4s)
-- Generating done (0.0s)
-- Build files have been written to: .../chapter-2/build/external/external/src/googletest-build
[6/8] Performing build step for 'googletest'
[1/8] Building CXX object googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o
[2/8] Building CXX object googlemock/CMakeFiles/gmock_main.dir/src/gmock_main.cc.o
[3/8] Building CXX object googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
[4/8] Building CXX object googletest/CMakeFiles/gtest.dir/src/gtest-all.cc.o
[5/8] Linking CXX static library lib/libgtest.a
[6/8] Linking CXX static library lib/libgtest_main.a
[7/8] Linking CXX static library lib/libgmock.a
[8/8] Linking CXX static library lib/libgmock_main.a
[7/8] Performing install step for 'googletest'
[0/1] Install the project...
-- Install configuration: "Debug"
-- Installing: .../chapter-2/build/include
-- Installing: .../chapter-2/build/include/gmock
-- Installing: .../chapter-2/build/include/gmock/gmock-matchers.h
...
-- Installing: .../chapter-2/build/include/gmock/gmock.h
-- Installing: .../chapter-2/build/include/gmock/gmock-actions.h
-- Installing: .../chapter-2/build/lib/libgmock.a
-- Installing: .../chapter-2/build/lib/libgmock_main.a
-- Installing: .../chapter-2/build/lib/pkgconfig/gmock.pc
-- Installing: .../chapter-2/build/lib/pkgconfig/gmock_main.pc
-- Installing: .../chapter-2/build/lib/cmake/GTest/GTestTargets.cmake
-- Installing: .../chapter-2/build/lib/cmake/GTest/GTestTargets-debug.cmake
-- Installing: .../chapter-2/build/lib/cmake/GTest/GTestConfigVersion.cmake
-- Installing: .../chapter-2/build/lib/cmake/GTest/GTestConfig.cmake
-- Up-to-date: .../chapter-2/build/include
-- Installing: .../chapter-2/build/include/gtest
-- Installing: .../chapter-2/build/include/gtest/gtest-matchers.h
...
-- Installing: .../chapter-2/build/include/gtest/gtest.h
-- Installing: .../chapter-2/build/include/gtest/gtest-printers.h
-- Installing: .../chapter-2/build/lib/libgtest.a
-- Installing: .../chapter-2/build/lib/libgtest_main.a
-- Installing: .../chapter-2/build/lib/pkgconfig/gtest.pc
-- Installing: .../chapter-2/build/lib/pkgconfig/gtest_main.pc
[8/8] Completed 'googletest'
-- Install configuration: "Debug"
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Configuring done (5.9s)
-- Generating done (0.0s)
-- Build files have been written to: .../chapter-2/build
[6/6] Linking CXX executable matrix-getVersion
```

## Add your first test

Now that GoogleTest is available, you can add the first test.

In order to keep the project clean, all tests go inside a `tests/`
directory. One file, `tests/main.cpp`, contains the top level directions for
testing. 

As a project may contain many tests, it's good to split them across
several files inside the `tests/` directory.

Create the top-level test in `tests/main.cpp` and paste the following code into the file:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-2/tests/main.cpp" >}}

Create `tests/Version.cpp` and add the `getVersion` unit test into the file:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-2/tests/Version.cpp" >}}

This test invokes `getVersion` and checks that the
`major`, `minor` and `patch` level match the expected values.

The last step is to tell CMake about the tests. All tests will
linked together in a single `matrix-test` executable (linking with the Matrix
library and GoogleTest), and you will add a convenience `check` target so the
tests can be run easily. 

Add the following at the bottom of the top-level `CMakeLists.txt`:

```TXT
# ===================================================================
# Testing
# -------------------------------------------------------------------
add_executable(matrix-test tests/main.cpp tests/Version.cpp)
target_link_libraries(matrix-test GTest::gtest Matrix)
add_custom_target(check
   COMMAND matrix-test --gtest_color=yes --gtest_output=xml:matrix-test.xml
)
```

Run the build again and test:

```BASH { output_lines = "3-21" }
cd build
ninja
...
[6/6] Completed 'googletest'
-- Install configuration: "Debug"
-- Configuring done (1.2s)
-- Generating done (0.0s)
-- Build files have been written to: .../chapter-2/build
[3/3] Linking CXX executable matrix-test
$ ninja check
...
[==========] Running 1 test from 1 test suite.
[----------] Global test environment set-up.
[----------] 1 test from Matrix
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 1 test from Matrix (0 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test suite ran. (0 ms total)
[  PASSED  ] 1 test.
```

Congratulations, your first unit test of the Matrix library passes!

## What have you achieved so far?

Your directory structure now looks like this:

```TXT
Matrix/
├── CMakeLists.txt
├── build/
│   ├── howdy*              <- The howdy executable program
...
│   ├── libMatrix.a         <- The Matrix library
│   ├── matrix-getVersion*  <- The getVersion executable program
│   ├── matrix-test*        <- The Matrix library tests executable program
│   └── matrix-test.xml     <- The Matrix test results in XML format>
├── external/
│   └── CMakeLists.txt
├── include/
│   └── Matrix/
│       └── Matrix.h
├── lib/
│   └── Matrix/
│       └── Matrix.cpp
├── src/
│   ├── getVersion.cpp
│   └── howdy.cpp
└── tests/
    ├── Version.cpp
    └── main.cpp
```

You can download the [archive](/artifacts/matrix/chapter-2.tar.xz) of the
project in its current state to experiment on your computer.

CMake makes it easy to use GoogleTest as an external project. Adding unit
tests as you go is now very easy.

You have created the unit testing environment for your Matrix library and
added a test. The infrastructure is now in place to 
implement the core of the Matrix processing library.
