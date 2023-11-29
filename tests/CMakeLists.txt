# Some basic tests to check if the library works
set(TEST_NAME "udsp_test")
add_executable(udsp_test udsp_test/udsp_test.c)
target_link_libraries(udsp_test udsp)

add_test(NAME ${TEST_NAME} COMMAND udsp_test)
