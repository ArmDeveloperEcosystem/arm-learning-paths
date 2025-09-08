readonly LP_DIR=$(realpath $(dirname $BASH_SOURCE[0])/..)
readonly ALP_DIR=$(realpath $LP_DIR/../../../..)
readonly ARTIFACTS_DIR=$ALP_DIR/static/artifacts
readonly CHAPTERS=$(find -s $LP_DIR/projects -type d -name 'chapter-*')
readonly BUILD_DIR="build"
