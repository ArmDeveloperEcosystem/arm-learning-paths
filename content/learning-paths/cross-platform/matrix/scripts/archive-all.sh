#!/usr/bin/env bash

source $(dirname $BASH_SOURCE[0])/config.sh

# Start from a clean build directory.
$(dirname $BASH_SOURCE[0])/clean-all.sh

mkdir -p $ARTIFACTS_DIR/matrix

for chapter in $CHAPTERS; do

  pushd $(dirname $chapter) &> /dev/null

  project=$(basename $chapter)
  echo "Archiving $project to $ARTIFACTS_DIR/matrix/$project.tar.gz"
  tar --create --auto-compress --file=$ARTIFACTS_DIR/matrix/$project.tar.xz --options xz:compression-level=9 --exclude $project/.git/ --exclude $project/.vscode/ $project

  popd &> /dev/null

done
