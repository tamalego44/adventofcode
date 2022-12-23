#include <stdio.h>
#include <stdlib.h>

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
	char buff[LMAX];
	fp = fopen(filename, "r");
	
	if (fp == NULL) {
		perror("Error reading file");
		exit(1);
	}

	int a;
	int b;
	int c;
	int d;
	int n = 0;
	while (fgets(buff, LMAX, fp)) {
		//printf("%s", buff);
		sscanf(buff, "%d-%d,%d-%d", &a, &b, &c, &d);
		//printf("[%d,%d,%d,%d]\n", a, b, c, d);

		if (a <= c && b >= d) {
			n++;
		}
		else if (a >= c && b <= d) {
			n++;
		}
	}

	printf("Overlapping sections: %d\n", n);
}
