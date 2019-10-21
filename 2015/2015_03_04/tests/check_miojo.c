#include <stdlib.h>
#include <check.h>
#include "../src/miojo.h"

void setup(void)
{
}

void teardown(void)
{
}

START_TEST(test_no_turns)
{
    ck_assert_int_eq(calc_time(4, 7), 7);
}
END_TEST

START_TEST(test_one_turn)
{
    ck_assert_int_eq(calc_time(5, 7), 10);
}
END_TEST

START_TEST(test_two_turns)
{
    ck_assert_int_eq(calc_time(10, 9), 30);
}
END_TEST

START_TEST(test_fail)
{
    ck_assert_int_eq(calc_time(4, 6), -1);
}
END_TEST

Suite* stack_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Miojo");
    tc_core = tcase_create("Core Functions");
    tcase_add_checked_fixture(tc_core, setup, teardown);
    tcase_add_test(tc_core, test_no_turns);
    tcase_add_test(tc_core, test_one_turn);
    tcase_add_test(tc_core, test_two_turns);
    tcase_add_test(tc_core, test_fail);


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
    //srunner_set_fork_status(sr, CK_NOFORK);

    srunner_run_all(sr, CK_NORMAL);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}
