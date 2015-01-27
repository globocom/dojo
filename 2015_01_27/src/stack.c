#include <stdlib.h>
#include "stack.h"

struct stack* create_stack(void)
{
    struct stack *s = malloc(sizeof (struct stack));
    s->length = 0;
    s->top = NULL;

    return s;
}

int push(struct stack* s, int v)
{
    struct node *n = malloc(sizeof (struct node));
    if (!n) {
        return 1;
    }
    n->value = v;
    n->next = s->top;

    s->top = n;
    s->length++;

    return 0;
}

int pop(struct stack *s, int *value)
{
    if (s->top) {
        *value = s->top->value;
        
        struct node *top = s->top;
        
        s->top = s->top->next;
        s->length--;

        free(top);

        return 0;
    }

    return 1;
}

void destroy(struct stack *s)
{
    while (s->top) {
        struct node *top = s->top;
        s->top = s->top->next;
        free(top);
    };

    free(s);
}
