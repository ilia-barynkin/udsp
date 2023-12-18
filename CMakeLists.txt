cmake_minimum_required(VERSION 3.10)
project(udsp C)

find_package(Python REQUIRED COMPONENTS Interpreter Development)

# Define source files
set(source_files
    src/stat.c
    src/convolve.c
    src/running_stat.c
    src/filters.c
)

find_path(PYTHON_INCLUDE_DIR NAMES Python.h PATH_SUFFIXES python3.11)
include_directories(src ${PYTHON_INCLUDE_DIR})

# Create shared library
add_library(udsp SHARED ${source_files})
target_link_libraries(udsp ${PYTHON_LIBRARIES} m)

# Set output properties
set_target_properties(udsp PROPERTIES
    OUTPUT_NAME udsp
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/archive
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/runtime
)

# Enable testing
enable_testing()

# Add tests directory
add_subdirectory(tests)
