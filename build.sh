#!/usr/bin/sh
set -e

rm -rf build
mkdir build
cd build
cmake ./..
make -j$(nproc)
make run_tests
cd ..