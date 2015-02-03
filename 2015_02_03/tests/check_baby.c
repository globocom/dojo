#include <stdlib.h>
#include <check.h>
#include "../src/baby.h"

char *vocabulary[] = {"pa", "ma", "bla", "nhe", NULL};

void setup(void)
{
}

void teardown(void)
{
}

START_TEST(test_pa)
{
    char word[] = "pa";
    ck_assert_int_eq(baby_speak(vocabulary, word), 1);
}
END_TEST



START_TEST(test_papa)
{
    char word[] = "papa";
    ck_assert_int_eq(baby_speak(vocabulary, word), 1);
}
END_TEST


START_TEST(test_papai)
{
    char word[] = "papai";
    ck_assert_int_eq(baby_speak(vocabulary, word), 0);
}
END_TEST

START_TEST(test_blehmapa)
{
    char word[] = "blehmapa";
    ck_assert_int_eq(baby_speak(vocabulary, word), 0);
}
END_TEST

START_TEST(test_mablehmapa)
{
    char word[] = "mablehmapa";
    ck_assert_int_eq(baby_speak(vocabulary, word), 0);
}
END_TEST

START_TEST(test_nheblamapa)
{
    char word[] = "nheblamapa";
    ck_assert_int_eq(baby_speak(vocabulary, word), 1);
}
END_TEST

START_TEST(test_new_vocabulary_papai)
{
    char *vocabulary[] = {"pa", "pai", "ma", "bla", "nhe", NULL};
    char word[] = "papai";
    ck_assert_int_eq(baby_speak(vocabulary, word), 1);
}
END_TEST

START_TEST(test_empty_word)
{
    char word[] = "";
    ck_assert_int_eq(baby_speak(vocabulary, word), 1);
}
END_TEST

START_TEST(test_empty_vocabulary)
{
    char *vocabulary[] = {NULL};
    char word[] = "blapa";
    ck_assert_int_eq(baby_speak(vocabulary, word), 0);
}
END_TEST

START_TEST(test_phrase)
{
    char phrase[] = "papa mama";
    ck_assert_int_eq(baby_speak(vocabulary, phrase), 1);
}
END_TEST

START_TEST(test_phrase_invalid)
{
    char phrase[] = "papa k mama";
    ck_assert_int_eq(baby_speak(vocabulary, phrase), 0);
}
END_TEST

START_TEST(test_crazy_word)
{
    char word[] = "p a";
    ck_assert_int_eq(baby_speak(vocabulary, word), 0);
}
END_TEST

START_TEST(test_crazy_word2)
{
    char word[] = " pa            pa ";
    ck_assert_int_eq(baby_speak(vocabulary, word), 1);
}
END_TEST

START_TEST(test_phrase_with_tab)
{
    char word[] = "papapa\tnhenhemama";
    ck_assert_int_eq(baby_speak(vocabulary, word), 1);
}
END_TEST

START_TEST(test_phrase_with_new_lines)
{
    char word[] = "papapa\nnhenhemama\r";
    ck_assert_int_eq(baby_speak(vocabulary, word), 1);
}
END_TEST

Suite* stack_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Bebe");
    tc_core = tcase_create("Core Functions");
    tcase_add_checked_fixture(tc_core, setup, teardown);
    tcase_add_test(tc_core, test_pa);
    tcase_add_test(tc_core, test_papa);
    tcase_add_test(tc_core, test_papai);
    tcase_add_test(tc_core, test_blehmapa);
    tcase_add_test(tc_core, test_mablehmapa);
    tcase_add_test(tc_core, test_nheblamapa);
    tcase_add_test(tc_core, test_new_vocabulary_papai);
    tcase_add_test(tc_core, test_empty_word);
    tcase_add_test(tc_core, test_empty_vocabulary);
    tcase_add_test(tc_core, test_phrase);
    tcase_add_test(tc_core, test_phrase_invalid);
    tcase_add_test(tc_core, test_crazy_word);
    tcase_add_test(tc_core, test_crazy_word2);
    tcase_add_test(tc_core, test_phrase_with_tab);
    tcase_add_test(tc_core, test_phrase_with_new_lines);

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
