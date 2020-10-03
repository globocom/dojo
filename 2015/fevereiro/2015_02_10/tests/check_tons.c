#include <stdlib.h>
#include <check.h>
#include "../src/tons.h"

void setup(void)
{
}

void teardown(void)
{
}

START_TEST(test_c_c)
{
    int ret = pertence_escala("C", "C");
    ck_assert_int_eq(ret, 1);
}
END_TEST

START_TEST(test_c_d)
{
    int ret = pertence_escala("C", "D");
    ck_assert_int_eq(ret, 1);
}
END_TEST

START_TEST(test_c_e)
{
    int ret = pertence_escala("C", "E");
    ck_assert_int_eq(ret, 1);
}
END_TEST

START_TEST(test_c_cs)
{
    int ret = pertence_escala("C", "C#");
    ck_assert_int_eq(ret, 0);
}
END_TEST

START_TEST(test_d_as)
{
    int ret = pertence_escala("D", "A#");
    ck_assert_int_eq(ret, 0);
}
END_TEST


START_TEST(test_a_fs)
{
    int ret = pertence_escala("A", "F#");
    ck_assert_int_eq(ret, 1);
}
END_TEST

START_TEST(test_a_b)
{
    int ret = pertence_escala("A", "B");
    ck_assert_int_eq(ret, 1);
}
END_TEST

START_TEST(test_b_a)
{
    int ret = pertence_escala("B", "A");
    ck_assert_int_eq(ret, 0);
}
END_TEST

START_TEST(test_a_z)
{
    int ret = pertence_escala("A", "Z");
    ck_assert_int_eq(ret, -1);
}
END_TEST

START_TEST(test_z_z)
{
    int ret = pertence_escala("Z", "Z");
    ck_assert_int_eq(ret, -1);
}
END_TEST

START_TEST(test_d_gb)
{
    int ret = pertence_escala("D", "Gb");
    ck_assert_int_eq(ret, 1);
}
END_TEST

START_TEST(test_d_db)
{
    int ret = pertence_escala("D", "Db");
    ck_assert_int_eq(ret, 1);
}
END_TEST

START_TEST(test_fs_ab)
{
    int ret = pertence_escala("F#", "Ab");
    ck_assert_int_eq(ret, 1);
}
END_TEST


START_TEST(test_db_bb)
{
    int ret = pertence_escala("Db", "Bb");
    ck_assert_int_eq(ret, 1);
}
END_TEST

START_TEST(test_bbb_eh)
{
    int ret = pertence_escala("bbb", "é");
    ck_assert_int_eq(ret, -1);
}
END_TEST

Suite* stack_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Tons");
    tc_core = tcase_create("Core Functions");
    tcase_add_checked_fixture(tc_core, setup, teardown);
    tcase_add_test(tc_core, test_c_c);
    tcase_add_test(tc_core, test_c_d);
    tcase_add_test(tc_core, test_c_e);
    tcase_add_test(tc_core, test_c_cs);
    tcase_add_test(tc_core, test_d_as);
    tcase_add_test(tc_core, test_a_fs);
    tcase_add_test(tc_core, test_a_b);
    tcase_add_test(tc_core, test_b_a);
    tcase_add_test(tc_core, test_a_z);
    tcase_add_test(tc_core, test_z_z);
    tcase_add_test(tc_core, test_d_gb);
    tcase_add_test(tc_core, test_d_db);
    tcase_add_test(tc_core, test_fs_ab);
    tcase_add_test(tc_core, test_db_bb);
    tcase_add_test(tc_core, test_bbb_eh);

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
