#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.h"

#define LMAX 100
#define NMAX 10000

struct stack* stack_new() {
	struct stack *s = malloc(sizeof(struct stack));
	memset(s->list, 0, sizeof(s->list));
	s->size = 0;
	return s;
}

void stack_free(struct stack *s) {
	free(s);
}

void stack_print(struct stack *s) {
	printf("stack_print unimplemented");
}

void stack_push(struct stack *s, char c) {
	s->list[s->size++] = c;
}

char stack_pop(struct stack *s) {
	return s->list[--s->size];
}

char stack_peek(struct stack *s) {
	return s->list[s->size - 1];
}
