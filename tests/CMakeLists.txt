# Some basic tests to check if the library works
set(TEST_NAME "udsp_test")
add_executable(udsp_test udsp_test/udsp_test.c)
target_link_libraries(udsp_test udsp)

set_tests_properties(udsp_test PROPERTIES 
    TIMEOUT 10
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/tests"
)

add_test(NAME ${TEST_NAME} COMMAND udsp_test)
