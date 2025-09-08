# Set the minimum CMake version we require. In our case, it is intentionnally
# very old as we are not making use of recent CMake features.
cmake_minimum_required(VERSION 3.5)

# Give a name to our project ('Matrix') and inform CMake about the language used.
project(Matrix LANGUAGES CXX)

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

# Add 'howdy', a standalone executable with no dependency to any library that
# has to be built from the sources in 'src/howdy.cpp'.
add_executable(howdy src/howdy.cpp)

# Add our 'Matrix' library, that is built as a static library, from source file
# 'lib/Matrix/Matrix.cpp'. CMake is instruction that C++17 is used, and that
# the library headers can be found in ${CMAKE_SOURCE_DIR}/include.
add_library(Matrix STATIC lib/Matrix/Matrix.cpp)
target_compile_features(Matrix PUBLIC cxx_std_17)
target_include_directories(Matrix
  PUBLIC ${CMAKE_SOURCE_DIR}/include)

# Add 'matrix-getVersion', an executable that depends on the Matrix library,
# that has to be built from source file 'src/getVersion.cpp'.
add_executable(matrix-getVersion src/getVersion.cpp)
target_link_libraries(matrix-getVersion Matrix)

# ===================================================================
# Testing
# -------------------------------------------------------------------
add_executable(matrix-test tests/main.cpp tests/Version.cpp)
target_link_libraries(matrix-test GTest::gtest Matrix)
add_custom_target(check
   COMMAND matrix-test --gtest_color=yes --gtest_output=xml:matrix-test.xml
)
