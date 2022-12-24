#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

int visible(int map[][LMAX], int w, int h, int x, int y) {
	if (x == 0 || x == w || y == 0 || y == h) {
		return 1;
	}

	int v = 1;
	for (int i=x-1; i >= 0; i--) {
		if (map[y][i] >= map[y][x]) {
			v = 0;
		}
	}
	if (v == 1) {
		return 1;
	}

	
	v = 1;
	for (int i=x+1; i < w; i++) {
		if (map[y][i] >= map[y][x]) {
			v = 0;
		}
	}
	if (v == 1) {
		return 1;
	}

	v = 1;
	for (int i=y-1; i >= 0; i--) {
		if (map[i][x] >= map[y][x]) {
			v = 0;
		}
	}
	if (v == 1) {
		return 1;
	}

	v = 1;
	for (int i=y+1; i < h; i++) {
		if (map[i][x] >= map[y][x]) {
			v = 0;
		}
	}
	if (v == 1) {
		return 1;
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

	int count = 0;

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			count += visible(map, w, h, j, i);
		}
	}

	printf("%d trees are visible\n.", count);
}
