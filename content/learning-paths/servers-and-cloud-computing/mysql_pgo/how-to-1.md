---
title: steps to enable MySQL PGO
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction
PGO (Profile-guided optimization) is a compiler optimization technique which uses profiling to improve performance, it can be supported by compilers
like GCC and Clang.

The guidance illustrates how to enable MySQL PGO with GCC compiler.

## Steps to Build MySQL PGO
this is the step to build MySQL with PGO enabled.
1. download mysql-server-8.0.33 and boost_1_77_0:

```
$ git clone https://github.com/mysql/mysql-server
$ cd mysql-server && git checkout mysql-8.0.33 && git submodule update --recursive

$ wget https://boostorg.jfrog.io/artifactory/main/release/1.77.0/source/boost_1_77_0.tar.gz && tar zxf boost_1_77_0.tar.gz
```

2. add "-DFPROFILE_GENERATE=ON" option to cmake, and then build mysql (please don't forget to change DCMAKE_INSTALL_PREFIX and DWITH_BOOST):
```
$ cd mysql-server-8.0.33
$ mkdir build
$ cmake -DCMAKE_C_FLAGS="-g -O3 -march=native -mcpu=native -flto" -DCMAKE_CXX_FLAGS="-g -O3 -mcpu=native -flto" -DCMAKE_INSTALL_PREFIX=/mysql_data/mysql_8.0.33_gcc_11.3.0_profile -DWITH_BOOST=/build/boost_1_77_0 -DFPROFILE_GENERATE=ON ..
$ make -j $(nproc)
$ make install
```

3. start MySQL server installed on /mysql_data/mysql_8.0.33_gcc_11.3.0_profile, run write and read benchmark from client, profile data would be generated under mysql build dir:
```
mysql-server-8.0.33/build-profile-data

```

4. rebuild MySQL with "-DFPROFILE_USE=ON":

```
$ cd mysql-server-8.0.33
$ rm -rf build && mkdir build # make sure it's same build directory as in step 2, or it would fail to find the profile data under build-profile-data
$ cmake -DCMAKE_C_FLAGS="-g -O3 -march=native -mcpu=native -flto" -DCMAKE_CXX_FLAGS="-g -O3 -march=native -mcpu=native -flto" -DCMAKE_INSTALL_PREFIX=/mysql_data/mysql_8.0.33_gcc_11.3.0_pgo  -DWITH_BOOST=/build/boost_1_77_0 -DFPROFILE_USE=ON ..
$ make -j $(nproc)
$ make install
```

5. start MySQL server installed on /mysql_data/mysql_8.0.33_gcc_11.3.0_pgo, run benchmark test and compare the write/read performance with the MySQL server which doesn't enable PGO,
   make sure performance is improved.
