---
title: Testing your work
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this chapter, after an introduction to testing, you will add unit testing
with a first test to your Matrix library code base.

## About unit testing

It's common practice when developing software to do so with unit tests. While it
might appear to be unnecessary in the beginning, tests are bringing significant
advantages:

- confidence for the developer, when adding new functionality, or when porting
  to a new platform / target
- confidence for the users
- catch regressions
- show how to use the library in practice
- welcome new comers to the project, as this allows them to check their patches
  and make sure they did not inadvertently broke the codebase.
- ...

You'll notice that setting up the testing comes almost first in this learning
path, and in any case before the actual library development !

Many unit testing frameworks exist in general, and C++ is not short of them as
you can notice in this [wikipedia
article](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#C++) that
attempts to enumerate them. There is no need to reinvent the wheel, this
learning path uses [GoogleTest](https://github.com/google/googletest) as an
example.

## Setup GoogleTest

You could rely on the platform to provide an installation of GoogleTest --- and
ask your library developers to install it by themselves. This feels like an
unnecessary step though. As testing is a corner stone of your Matrix library
development, GoogleTest should be installed automatically as a dependency in the
build tree of your project. One great point with
[GoogleTest](https://github.com/google/googletest) is that it provides a
seamless integration with CMake, so let's set it up for your project !

Adding external dependencies is easily done with CMake. This is done with a
separate `CMakeLists.txt` file, placed in directory `external/`. This file is in
charge of all our external dependencies. It will be used by our main
`CMakeLists.txt`.

Create `external/CMakeLists.txt` with the following content:

{{< include-code TXT "content/learning-paths/cross-platform/matrix/projects/chapter-2/external/CMakeLists.txt" >}}

A new CMake thing that appears here is CMake variables. They start with the `$`
character and have a name in between curly braces. CMake variable can be set by
the CMake itself, or by the user, and they can be modified or used. In your
case, variable `${EXTERNAL_PROJECT_CMAKE_ARGS}` is set with the options that we
want to pass to CMake for installing the external dependencies:

- `${CMAKE_CXX_COMPILER}`: the C++ compiler used by CMake
- `${CMAKE_BUILD_TYPE}`: the type of build used by CMake (`Release`, `Debug`,
  ...)
- `${CMAKE_INSTALL_PREFIX}`: where CMake will install the project

The project code base is now looking like:

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

We now only have to use that new `CMakeLists.txt` in our top level CMake file.
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

`${CMAKE_GENERATOR}` is what CMake will use to perform the build, usually GNU's
Make or Ninja, but it can be an IDE specific project file as well (XCode, ...).
`${CMAKE_SOURCE_DIR}` is the path to the top level directory of your project
(where the main `CMakeLists.txt` is located) and `${CMAKE_BINARY_DIR}` is the
build directory.

At configuration time, CMake will download, build and install googletest and
make it available to your project thru the use of `find_package`.

If you now build your code base, CMake will notice it has been updated and will
perform all necessary steps. The transcript belows shows that besides our own
executable, CMake has configured, build and installed googletest.

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

Now that googletest is available, you will add your very first test !

In order to keep the project tidy, all tests will go inside a `tests/`
directory. One file , `tests/main.cpp`, will contain the top level part of the
testing. As a project may contain a lot of tests, it's good to split them across
several files inside `tests/`.

Create the top-level test in `tests/main.cpp` and paste the following into it:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-2/tests/main.cpp" >}}

Create `tests/Version.cpp` and add the `getVersion` unit test into it:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-2/tests/Version.cpp" >}}

This test does nothing more than invoking `getVersion` and checking that the
`major`, `minor` and `patch` level match the expected values.

The last step to do is to instruct CMake that about the tests. All tests will
linked together in a single `matrix-test` executable (linking with the Matrix
library and googletest), and you will add a convenience `check` target so the
tests can be run easily. Add the following at the bottom of the top-level
`CMakeLists.txt`:

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

Yay, your first ever unit test of our Matrix library passes ! Congratulations !

## What have you achieved so far ?

Your code base is now looking like:

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
project in its current state to experiment locally on your machine.

CMake allowed to use googletest as an external project very easily. Adding unit
tests as you go is now very simple.

You have put in place the unit testing environment for your Matrix library and
added a unit test. The infrastructure is now in place for eventually
implementing the core of our Matrix processing library.
