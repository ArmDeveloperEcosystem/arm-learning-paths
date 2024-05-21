# Set the minimum CMake version we require. In our case, it is intentionnally
# very old as we are not making use of recent CMake features.
cmake_minimum_required(VERSION 3.5)

# Give a name to our project ('Matrix') and inform CMake about the language used.
project(Matrix LANGUAGES CXX)

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
