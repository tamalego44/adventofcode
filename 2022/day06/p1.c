#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

#define LMAX 100
#define NMAX 10000
int main(int argc, char *argv[]) {
	// Verify proper args were used
	// Usage: ./p<1/2> <filename>
	char *filename;
	if (argc != 2) {
		printf("Improper Syntax. Usage: ./p<1/2> <filename>\n");
		printf("Filename is likely \"sample.txt\" or \"input.txt\"\n");
		exit(1);
	}
	else {
		filename = argv[1];
	}

	FILE* fp;
	fp = fopen(filename, "r");
	
	if (fp == NULL) {
		perror("Error reading file");
		exit(1);
	}
	
	struct stack *s = stack_new();
	char c;
	int answer = 0;
	while (fscanf(fp, "%c", &c)) {
		stack_push(s, c);
		answer = stack_check(s, 4);
		if (answer > 0) {
			break;
		}
	}

	if (answer > 0) {
		printf("First index: %d\n", answer);
	}
	else {
		printf("Not found\n");
	}
	stack_free(s);
}
