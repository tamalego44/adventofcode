#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LMAX 100
#define NMAX 10000

int calcPriority(char c) {
	int n = c;

	if (65 <= n && n <= 90) {
		n -= 38;
	} else if (97 <= n && n <= 122) {
		n -= 96;
	}
	else {
		return -1;
	}
	
	return n;
}

char reversePriority(int n) {
	if (27 <= n && n <= 52) {
		n+= 38;
	} else if (0 <= n && n <= 26) {
		n += 96;
	}
	else {
		return ' ';
	}

	char c = n;
	return c;
}

void overlap(char *g1, char *g2, char *f, int gl) {
	char map[LMAX] = {0};
	memset(f, 0, gl*sizeof(f[0])); //Overwrite g3
	
	for (int i=0; i < strlen(g1); i++) {
		int n = calcPriority(g1[i]);
		map[n] = 1;
	}
	
	for (int j=0; j < strlen(g2); j++) {
		int n = calcPriority(g2[j]);
		if (map[n] == 1) {
			map[n] = 2;
		}
	}
	
	int i = 0;
	char g3[LMAX] = {0};
	for (int j=0; j < LMAX; j++) {
		if (map[j] == 2) {
			g3[i++] = j;
		}
	}

	for (int j=0; j < i; j++) {
		f[j] = reversePriority((int)g3[j]);
		//printf("%d, %c\n", (int)g3[j], f[j]);
	}
	f[i] = 0;
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
	char b1[LMAX];
	char b2[LMAX];
	char b3[LMAX];
	fp = fopen(filename, "r");
	
	int map[LMAX] = {0};	
	int score = 0;
	while (fgets(b1, LMAX, fp)) {
		//printf("%s", buff);
		//printf("%d\n", (int)strlen(buff)-1);
		fgets(b2, LMAX, fp);
		fgets(b3, LMAX, fp);
		//printf("%s", b1);
		//printf("%s", b2);
		//printf("%s", b3);

		char b4[LMAX];
		char b5[LMAX];
		overlap(b1, b2, b4, LMAX);
		overlap(b3, b4, b5, LMAX);

		//printf("%s\n", b5);
		//printf("=============\n");
		
		score += calcPriority(b5[0]);
	}
	printf("Total Priority: %d\n", score);
}
