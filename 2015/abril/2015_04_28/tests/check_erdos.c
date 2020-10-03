#include <stdlib.h>
#include <check.h>
#include "../src/erdos.h"

void setup(void)
{
}

void teardown(void)
{
}

START_TEST(test_must_return_empty_list)
{
    struct publication publications;
    struct person p;
    p.name = "Erdos";
    publications.people = NULL;
    publications.people = g_list_append(publications.people, &p);
    ck_assert_ptr_eq(erdos(&publications, 1), NULL);
}
END_TEST

START_TEST(test_one_person)
{
    struct publication publications;
    struct person p1;
    p1.name = "Erdos";
    struct person p2;
    p2.name = "Rafael";
    publications.people = NULL;
    publications.people = g_list_append(publications.people, &p2);
    publications.people = g_list_append(publications.people, &p1);
    GList *result = erdos(&publications, 1);

    struct person *p3 = g_list_first(result)->data;
    ck_assert_str_eq(p3->name, "Rafael");
    ck_assert_int_eq(p3->weight, 1);
}
END_TEST

START_TEST(test_three_people)
{
    struct publication publications[2];
    struct person p1;
    p1.name = "Erdos";
    struct person p2;
    p2.name = "Rafael";
    struct person p3;
    p3.name = "Isaac";
    publications[0].people = NULL;
    publications[0].people = g_list_append(publications[0].people, &p2);
    publications[0].people = g_list_append(publications[0].people, &p1);
    publications[1].people = NULL;
    publications[1].people = g_list_append(publications[1].people, &p2);
    publications[1].people = g_list_append(publications[1].people, &p3);
    GList *result = erdos(publications, 2);

    struct person *rafael = g_list_nth(result, 0)->data;
    ck_assert_str_eq(rafael->name, "Rafael");
    ck_assert_int_eq(rafael->weight, 1);

    struct person *isaac = g_list_nth(result, 1)->data;
    ck_assert_str_eq(isaac->name, "Isaac");
    ck_assert_int_eq(isaac->weight, 2);
}
END_TEST

Suite* stack_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Erdos");
    tc_core = tcase_create("Core Functions");
    tcase_add_checked_fixture(tc_core, setup, teardown);
    tcase_add_test(tc_core, test_must_return_empty_list);
    tcase_add_test(tc_core, test_one_person);
    tcase_add_test(tc_core, test_three_people);


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
