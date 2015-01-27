#include <stdlib.h>
#include <check.h>
#include "../src/stack.h"

void setup(void)
{
}

void teardown(void)
{
}

START_TEST(test_create_stack)
{
}
END_TEST

Suite* stack_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Stack");
    tc_core = tcase_create("Core Functions");
    tcase_add_checked_fixture(tc_core, setup, teardown);
    tcase_add_test(tc_core, test_create_stack);

    suite_add_tcase(s, tc_core);

    return s;
}

int main(void)
{
    int number_failed;
    Suite *s;
    SRunner *sr;

    s = stack_suite();
    sr = srunner_create(s);

    srunner_run_all(sr, CK_NORMAL);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}
