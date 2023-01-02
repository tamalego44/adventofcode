#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "funcs.h"

#define LMAX 100
#define NMAX 10000

int getSignal(int x, int cycle) {
	if (cycle % 40 == 20 && cycle <= 220) {
		printf("%d\n", x*cycle);
		return x * cycle;
	}
	return 0;
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
	int signal = 0;
	while (fgets(buff, LMAX, fp)) {
		//printf("%s", buff);

		if (strcmp("noop\n", buff) == 0) {
			cycle++;
			signal += getSignal(x, cycle);
			continue;
		}
		
		int d;
		sscanf(buff, "addx %d", &d);

		cycle++;
		signal += getSignal(x, cycle);
		
		x += d;
		cycle++;
		signal += getSignal(x, cycle);	
	}

	printf("Signal Strength: %d\n", signal);
}
