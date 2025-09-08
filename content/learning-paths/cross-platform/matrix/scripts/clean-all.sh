#!/usr/bin/env bash

source $(dirname $BASH_SOURCE[0])/config.sh

for chapter in $CHAPTERS; do

  for D in $BUILD_DIR .cache; do
    if [ -d $chapter/$D ]; then
      rm -Rf $chapter/$D
    fi
  done

done
