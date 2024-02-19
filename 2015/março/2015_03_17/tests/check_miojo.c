#include <stdlib.h>
#include <check.h>
#include <limits.h>
#include "../src/miojo.h"

void setup(void)
{
}

void teardown(void)
{
}

START_TEST(test_no_turns)
{
    ck_assert_int_eq(calc_time(3, 4, 7), 7);
}
END_TEST

START_TEST(test_one_turn)
{
    ck_assert_int_eq(calc_time(3, 5, 7), 10);
}
END_TEST

START_TEST(test_two_turns)
{
    ck_assert_int_eq(calc_time(3, 10, 9), 30);
}
END_TEST

START_TEST(test_fail)
{
    ck_assert_int_eq(calc_time(3, 4, 6), -1);
}
END_TEST

START_TEST(test_three_turns)
{
    ck_assert_int_eq(calc_time(3, 2, 9), 9);
}
END_TEST

START_TEST(test_one_turn_again)
{
    ck_assert_int_eq(calc_time(3, 3, 9), 3);
}
END_TEST

START_TEST(test_fail_one)
{
    ck_assert_int_eq(calc_time(1, 3, 9), -1);
}
END_TEST

START_TEST(test_three_turns_eight)
{
    ck_assert_int_eq(calc_time(8, 5, 7), 15);
}
END_TEST

START_TEST(test_four_turns_eight)
{
    ck_assert_int_eq(calc_time(1, 5, 7), 15);
}
END_TEST

START_TEST(test_overflow)
{
  ck_assert_int_eq(calc_time(899, INT_MAX/2, INT_MAX-10), -2);
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
    tcase_add_test(tc_core, test_three_turns);
    tcase_add_test(tc_core, test_one_turn_again);
    tcase_add_test(tc_core, test_fail_one);
    tcase_add_test(tc_core, test_three_turns_eight);
    tcase_add_test(tc_core, test_four_turns_eight);
    tcase_add_test(tc_core, test_overflow);

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
