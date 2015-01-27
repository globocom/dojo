#ifndef STACK_H
#define STACK_H

struct node {
    struct node* next;
    int value;
};

struct stack {
    struct node* top;
    int length;
};

struct stack* create_stack(void);
int push(struct stack*, int);
int pop(struct stack*, int *);
void destroy(struct stack *);

#endif
