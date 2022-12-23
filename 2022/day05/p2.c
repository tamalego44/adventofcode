#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.h"

#define LMAX 100
#define MAXSZ 100
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
	char buff[LMAX];
	fp = fopen(filename, "r");
	
	if (fp == NULL) {
		perror("Error reading file");
		exit(1);
	}

	int is[MAXSZ] = {0};
	char cs[MAXSZ][MAXSZ];
	memset(cs, 0, sizeof(char) * MAXSZ * MAXSZ);
	struct stack *stacks[MAXSZ];
	int build = 0;
	int nstacks;
	while (fgets(buff, LMAX, fp)) {
		//printf("%s", buff);
		if (build == 0) {
			int l = strlen(buff);
			nstacks = l/4;
			int n;
			int retv = sscanf(buff+4, " %d", &n);

			if (retv == 1) {
				build = 1;
				for (int i=0; i < nstacks; i++) {
					stacks[i] = stack_new();
					for (int j=is[i]-1; j >= 0; j--) {
						stack_push(stacks[i], cs[i][j]);
					}
				}
			}
			else {
				for (int i=0; i < nstacks; i++) {
					char c = 0;
					retv = sscanf(buff+(i*4), "[%c]", &c);

					if (retv > 0) {
						cs[i][is[i]++] = c;
					}
				}
			}
		}
		else {
			int num;
			int from;
			int to;
			int retv = sscanf(buff, "move %d from %d to %d", &num, &from, &to);
			from--;
			to--;

			char standby[MAXSZ] = {0};
			int j = 0;
			if (retv > 0) {
				for (int i=0; i < num; i++) {
					standby[j++] = stack_pop(stacks[from]);
				}
				while (j > 0) {
					stack_push(stacks[to], standby[--j]);
				}	
			}
		}
	}
	for (int i=0; i <nstacks; i++) {
		printf("%c", stack_peek(stacks[i]));
		stack_free(stacks[i]);
	}
	printf("\n");
}
