#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "funcs.h"

#define LMAX 100
#define NMAX 10000

void clockPulse(int x, int *cycle) {

	//write pixel if applicable
	if ((x % 40) - 1 <= ((*cycle-1) % 40) && (x % 40) + 1 >= ((*cycle-1) % 40)) {
		printf("#");
	}
	else {
		printf(".");
	}

	*cycle += 1;

	//draw newline if applicable
	if (*cycle % 40 == 1) {
		printf("\n");
	}
	//printf("Cycle: %d\n", *cycle);
}

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

	int cycle = 1;
	int x = 1;
	while (fgets(buff, LMAX, fp)) {
		//printf("%s", buff);

		if (strcmp("noop\n", buff) == 0) {
			clockPulse(x, &cycle);
			continue;
		}
		
		int d;
		sscanf(buff, "addx %d", &d);

		clockPulse(x, &cycle);		
		clockPulse(x, &cycle);	
		x += d;
	}
}
