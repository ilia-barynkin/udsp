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
cp ../tests/weight/inmove1.xlsm ./functests/data/inmove1.xlsm
cp ../tests/weight/weight.csv ./functests/data/weight.csv
cp ../tests/dist/dist.xlsx ./functests/data/dist.xlsx
cp ../tests/dist/dist.csv ./functests/data/dist.csv
cp -r ../tests/**/*.py ./functests
cd functests

cd ../..
