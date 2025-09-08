#!/usr/bin/env bash

source $(dirname $BASH_SOURCE[0])/config.sh

for chapter in $CHAPTERS; do

  # Configure
  echo
  echo "======================================="
  echo $(basename $chapter)
  echo "======================================="

  if [ ! -d $chapter/$BUILD_DIR ]; then
    echo '$' CXX=clang++ cmake \
      -DCMAKE_BUILD_TYPE:STRING=Debug \
      -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON \
      -G Ninja -B $chapter/$BUILD_DIR -S $chapter
    CXX=clang++ cmake \
      -DCMAKE_BUILD_TYPE:STRING=Debug \
      -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON \
      -G Ninja -B $chapter/$BUILD_DIR -S $chapter
  fi

  # Build
  cmake --build $chapter/$BUILD_DIR

done
