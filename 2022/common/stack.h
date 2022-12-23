#ifndef STACK_H_
#define STACK_H_

#define STACKMAX 1000

struct stack {
	char list[STACKMAX];
	int size;
};

struct stack* stack_new();
char stack_pop(struct stack *s);
void stack_push(struct stack *s, char c);
char stack_peek(struct stack *s);
void stack_print(struct stack *s);
void stack_free(struct stack *s);

#endif
