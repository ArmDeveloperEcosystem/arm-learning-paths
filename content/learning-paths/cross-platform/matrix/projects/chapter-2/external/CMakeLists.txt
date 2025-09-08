cmake_minimum_required(VERSION 3.6)

project(external LANGUAGES CXX)

# Get the functionality to configure, build and install external project
# from CMake module 'ExternalProject'.
include(ExternalProject)

# Use the same compiler, build type and instalation directory than those
# from our caller.
set(EXTERNAL_PROJECT_CMAKE_ARGS
      -DCMAKE_CXX_COMPILER:PATH=${CMAKE_CXX_COMPILER}
      -DCMAKE_BUILD_TYPE:STRING=${CMAKE_BUILD_TYPE}
      -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_INSTALL_PREFIX})

# Add 'googletext' as an external project, that will be cloned with git,
# from the official googletest repository, at version v1.14.
# We ask for a shallow clone, which is a clone with only the revision
# we are interested in rather than googletest's full history ---
# this makes the clone much faster (less data traffic), and uses much
# less disk space ; furthermore, as we are not developping googletest
# but just merely using it, we don't need thre full history. It will be
# built and installed with our build configuration passed with CMAKE_ARGS.
ExternalProject_Add(googletest
    PREFIX "external"
    GIT_REPOSITORY "https://github.com/google/googletest"
    GIT_TAG "v1.14.0"
    GIT_SHALLOW TRUE
    CMAKE_ARGS ${EXTERNAL_PROJECT_CMAKE_ARGS}
)
