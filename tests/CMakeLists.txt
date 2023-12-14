# Set the test name
set(udsp_test_name "udsp_test")

# Create the udsp_test executable
add_executable(udsp_test udsp_test/udsp_test.c)

find_package(Python REQUIRED COMPONENTS Interpreter Development)

# Link the udsp library
target_link_libraries(udsp_test udsp ${PYTHON_LIBRARIES} m)
find_path(PYTHON_INCLUDE_DIR NAMES Python.h PATH_SUFFIXES python3.11)
include_directories(${PYTHON_INCLUDE_DIR})

# Add the test with the specified name and command
add_test(NAME ${udsp_test_name} COMMAND udsp_test)

# Set properties for the udsp_test
set_tests_properties(udsp_test PROPERTIES 
    FAIL_REGULAR_EXPRESSION "FAILED"
    TIMEOUT 10
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/tests"
)

set(output_file "${CMAKE_BINARY_DIR}/tests/my_test_output.txt")
add_custom_command(TARGET udsp_test POST_BUILD COMMAND ${CMAKE_CTEST_COMMAND} --output-log ${output_file} -R ^my_test$)

# Add a custom target to run tests
add_custom_target(run_tests
    COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/tests"
    COMMENT "Running tests..."
)