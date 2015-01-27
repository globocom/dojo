#include <stdlib.h>
#include <check.h>
#include "../src/stack.h"

struct stack *stack;

void setup(void)
{
    stack = create_stack();
}

void teardown(void)
{
    destroy(stack);
}

START_TEST(test_create_stack)
{
    ck_assert(stack);
    ck_assert_int_eq(stack->length, 0);
    ck_assert_ptr_eq(stack->top, NULL);
}
END_TEST

START_TEST(test_push_one_element)
{
    ck_assert(!push(stack, 5));
    ck_assert_int_eq(stack->length, 1);
    ck_assert_int_eq(stack->top->value, 5);
}
END_TEST

START_TEST(test_push_two_elements)
{
    ck_assert(!push(stack, 8));
    ck_assert(!push(stack, 3));

    ck_assert_int_eq(stack->length, 2);
    ck_assert_int_eq(stack->top->value, 3);
    ck_assert_int_eq(stack->top->next->value, 8);
}
END_TEST

START_TEST(test_pop)
{
    int value;
    ck_assert(!push(stack, 3));

    ck_assert_int_eq(pop(stack, &value), 0);
    ck_assert_int_eq(stack->length, 0);
    ck_assert_ptr_eq(stack->top, NULL);
    ck_assert_int_eq(value, 3);
}
END_TEST

START_TEST(test_pop_empty_stack)
{
    int value;

    ck_assert_int_eq(pop(stack, &value), 1);
}
END_TEST

START_TEST(test_destroy)
{
    struct stack *s = create_stack();
    push(s, 10);
    push(s, 12);
    push(s, 4);
    destroy(s);
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
    tcase_add_test(tc_core, test_push_one_element);
    tcase_add_test(tc_core, test_push_two_elements);
    tcase_add_test(tc_core, test_pop);
    tcase_add_test(tc_core, test_pop_empty_stack);
    tcase_add_test(tc_core, test_destroy);

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
