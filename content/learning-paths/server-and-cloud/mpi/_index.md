---
title: Get started with parallel application development

description: Learning path for building and running parallel applications on Arm and tips to debug and optimize them.

minutes_to_complete: 30   

who_is_this_for: This is an advanced topic for HPC software developers writing MPI applications.

learning_objectives: 
    - Debug and fix a parallel application
    - Profile and optimize your code
    - Use optimized routines for common math operations

prerequisites:
    - General knowledge about distributed parallelism (MPI)
    - A C and Fortran compiler. Tested ![c_compiler](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/badges/gcc.svg) ![f_compiler](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/badges/gfortran.svg)
    - MPI framework. Tested ![openmpi](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/badges/openmpi.svg)
    - BLAS library. Tested ![blas](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/badges/blas.svg)
    - Python with NumPy, SciPy and MPI4Py. Tested ![python](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/badges/python.svg) ![numpy](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/badges/numpy.svg) ![scipy](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/badges/scipy.svg) ![mpi4py](https://raw.githubusercontent.com/armflorentlebeau/arm_hpc_tools_trial/master/.github/badges/mpi4py.svg)

author_primary: Florent Lebeau

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - C
    - Fortran
    - Python
    - GCC
    - Armclang
    - Arm Forge
    - gdb

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
