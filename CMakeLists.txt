cmake_minimum_required(VERSION 3.10)
project(udsp C)

set(SOURCES
    src/udsp.c
)

include_directories(src)
add_library(udsp STATIC ${SOURCES})

# Removing C stdlib dependency
set(CMAKE_C_STANDARD_LIBRARIES "")

set_target_properties(udsp PROPERTIES OUTPUT_NAME 
    udsp
)
set_target_properties(udsp PROPERTIES LIBRARY_OUTPUT_DIRECTORY 
    ${CMAKE_BINARY_DIR}/lib
)
set_target_properties(udsp PROPERTIES ARCHIVE_OUTPUT_DIRECTORY 
    ${CMAKE_BINARY_DIR}/archive
)
set_target_properties(udsp PROPERTIES RUNTIME_OUTPUT_DIRECTORY 
    ${CMAKE_BINARY_DIR}/runtime
)