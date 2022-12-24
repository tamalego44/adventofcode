#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "funcs.h"

#define LMAX 1000
#define NMAX 10000

void print_map(int map[][LMAX], int w, int h) {
	for (int j=0; j<h; j++) {
		for (int i=0; i<w; i++) {
			printf("%d", map[j][i]);
		}
		printf("\n");
	}
}

int scenic_score(int map[][LMAX], int w, int h, int x, int y) {
	
	int s1 = 0;
	for (int i=x-1; i >= 0; i--) {
		s1++;
		if (map[y][i] >= map[y][x]) {
			break;
		}
	}

	int s2 = 0;
	for (int i=x+1; i < w; i++) {
		s2++;
		if (map[y][i] >= map[y][x]) {
			break;
		}
	}

	int s3 = 0;
	for (int i=y-1; i >= 0; i--) {
		s3++;
		if (map[i][x] >= map[y][x]) {
			break;
		}
	}

	int s4 = 0;
	for (int i=y+1; i < h; i++) {
		s4++;
		if (map[i][x] >= map[y][x]) {
			break;
		}
	}

	return s1 * s2 * s3 * s4;

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

	int map[LMAX][LMAX];
	memset(map, 0, sizeof(int)*LMAX*LMAX);
	int w = 0;
	int h = 0;
	while (fgets(buff, LMAX, fp)) {
		w = strlen(buff) - 1;
		for(int i=0; i < w; i++) {
			map[h][i] = buff[i] - '0';
		}
		h++;
	}
	printf("%d, %d\n", w, h);
	print_map(map, w, h);

	int score = 0;

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			score = MAX(score, scenic_score(map, w, h, j, i));
		}
	}

	printf("Highest Scenic Score: %d\n", score);
}
