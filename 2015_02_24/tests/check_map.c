#include <stdlib.h>
#include <check.h>
#include "../src/map.h"

struct map* my_map;

void setup(void)
{
}

void teardown(void)
{
  destroy_map(my_map);
}

START_TEST(test_new_map)
{
    my_map = new_map(3);
    ck_assert_int_eq(my_map->size, 3);
    ck_assert_int_eq(my_map->lop, 0);
}
END_TEST

START_TEST(test_set_value)
{
    my_map = new_map(3);
    set_value(my_map, 4, 7);
    int value = get_value(my_map, 4);
    ck_assert_int_eq(value, 7);
}
END_TEST

START_TEST(test_reset_value)
{
    my_map = new_map(3);
    set_value(my_map, 4, 7);
    set_value(my_map, 4, 3);
    int value = get_value(my_map, 4);
    ck_assert_int_eq(value, 3);
}
END_TEST

START_TEST(test_set_too_many_values)
{
    my_map = new_map(2);

    set_value(my_map, 1, 2);
    ck_assert_int_eq(my_map->lop, 0);
    ck_assert_int_eq(get_value(my_map, 1), 2);

    set_value(my_map, 2, 3);
    ck_assert_int_eq(my_map->lop, 0);
    ck_assert_int_eq(get_value(my_map, 2), 3);

    set_value(my_map, 3, 4);
    ck_assert_int_eq(my_map->lop, 1);
}
END_TEST

START_TEST(test_get_unknown_key)
{
    my_map = new_map(2);
    ck_assert_int_eq(get_value(my_map, 1), 0);
    ck_assert_int_eq(my_map->lop, 1);
}
END_TEST

START_TEST(test_successful_get_after_error)
{
    my_map = new_map(1);
    set_value(my_map, 10, 20);
    ck_assert_int_eq(get_value(my_map, 1), 0);
    ck_assert_int_eq(my_map->lop, 1);
    ck_assert_int_eq(get_value(my_map, 10), 20);
    ck_assert_int_eq(my_map->lop, 0);
}
END_TEST

Suite* stack_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Map");
    tc_core = tcase_create("Core Functions");
    tcase_add_checked_fixture(tc_core, setup, teardown);
    tcase_add_test(tc_core, test_new_map);
    tcase_add_test(tc_core, test_set_value);
    tcase_add_test(tc_core, test_reset_value);
    tcase_add_test(tc_core, test_set_too_many_values);
    tcase_add_test(tc_core, test_get_unknown_key);
    tcase_add_test(tc_core, test_successful_get_after_error);

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
    srunner_set_fork_status(sr, CK_NOFORK);

    srunner_run_all(sr, CK_NORMAL);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}
