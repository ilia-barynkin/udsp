#!/usr/bin/sh

rm -rf build
mkdir build
cd build
cmake ./..
make -j$(nproc)
make run_tests

# This is an ad-hoc solution to check if the library works
# without messing with the CMake / setuptools hell
# TODO: replace it with a less barbaric solution

mkdir functests
cp ./lib/libudsp.so ./functests
cp -r ../py_bindings/*.py ./functests
mkdir ./functests/data
cp ../tests/weight/weight.csv ./functests/weight.csv
cp -r ../tests/**/*.py ./functests
cd functests
python target.py

cd ../..
