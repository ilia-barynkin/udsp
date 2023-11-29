# Some basic tests to check if the library works
set(TEST_NAME "udsp_test")
add_executable(udsp_test udsp_test/udsp_test.c)
target_link_libraries(udsp_test udsp)
add_test(NAME ${TEST_NAME} COMMAND udsp_test)
set_tests_properties(udsp_test PROPERTIES 
    FAIL_REGULAR_EXPRESSION "FAILED"
    TIMEOUT 10
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/tests"
)
# Add a custom target to run tests
add_custom_target(run_tests
    COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/tests"
    COMMENT "Running tests..."
)
