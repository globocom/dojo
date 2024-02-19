#include <stdlib.h>
#include <check.h>
#include <limits.h>
#include "../src/largest_product_grid.h"


void setup(void)
{
}

void teardown(void)
{
}

START_TEST(test_calc_product_line)
{
    int grid_5x5[GRID_SIZE][GRID_SIZE] = {
        {1, 2, 3, 4, 5},
        {5, 9, 2, 1, 7},
        {1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1}
    };
    ck_assert_int_eq(calc_product(grid_5x5), 126);
}
END_TEST

START_TEST(test_calc_product_col)
{
    int grid_5x5[GRID_SIZE][GRID_SIZE] = {
        {1, 2, 3, 4, 5},
        {5, 9, 2, 1, 7},
        {1, 1, 1, 1, 4},
        {1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1}
    };
    ck_assert_int_eq(calc_product(grid_5x5), 140);
}
END_TEST

START_TEST(test_calc_product_diagonal_down)
{
    int grid_5x5[GRID_SIZE][GRID_SIZE] = {
        {1, 2, 3, 4, 5},
        {5, 9, 2, 1, 7},
        {1, 1, 1, 1, 1},
        {1, 7, 1, 1, 1},
        {1, 1, 1, 1, 20}
    };
    ck_assert_int_eq(calc_product(grid_5x5), 180);
}
END_TEST


Suite* stack_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Largest Product in Grid");
    tc_core = tcase_create("Core Functions");
    tcase_add_checked_fixture(tc_core, setup, teardown);
    tcase_add_test(tc_core, test_calc_product_line);
    tcase_add_test(tc_core, test_calc_product_col);
    tcase_add_test(tc_core, test_calc_product_diagonal_down);

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
