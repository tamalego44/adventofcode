#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "funcs.h"

#define LMAX 100
#define NMAX 1000

void fixTail(int hx, int hy, int *tx, int *ty) {
	int dx = hx > *tx ? hx - *tx : *tx - hx;
	int dy = hy > *ty ? hy - *ty : *ty - hy;
	int ddx = dx == 0 ? 0 : (hx - *tx) / dx;
	int ddy = dy == 0 ? 0 : (hy - *ty) / dy;

	if (dx == 0 && dy > 1) {
		*ty += ddy;
	}
	else if (dy == 0 && dx > 1) {
		*tx += ddx;
	}
	else if (dx > 1 || dy > 1) {
		*tx += ddx;
		*ty += ddy;
	}
}

int countMap(uint8_t map[][NMAX]) {
	int count = 0;
	for (int i = 0; i < NMAX; i++) {
		for (int j = 0; j < NMAX; j++) {
			count += map[i][j];
		}
	}
	return count;
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

	uint8_t map[NMAX][NMAX];
	memset(map, 0, sizeof(uint8_t) * NMAX * NMAX);
	int sx = 500;
	int sy = 500;
	int hx = sx;
	int hy = sy;
	int tx = sx;
	int ty = sy;
	int xmax = sx;
	int xmin = sx;
	int ymax = sy;
	int ymin = sy;

	map[hx][hy] = 1;
	while (fgets(buff, LMAX, fp)) {
		printf("%s", buff);
		char dir;
		int dist;
		sscanf(buff, "%c %d", &dir, &dist);
		
		for (int i = 0; i < dist; i++) {
			switch (dir) {
				case 'U':
					hy++;
					break;
				case 'D':
					hy--;
					break;
				case 'R':
					hx++;
					break;
				case 'L':
					hx--;
					break;
			}
			fixTail(hx, hy, &tx, &ty);
			//map[hx][hy] = 1;
			map[tx][ty] = 1;
		}

		xmax = MAX(hx, xmax);
		xmin = MIN(hx, xmin);
		ymax = MAX(hy, ymax);
		ymin = MIN(hy, ymin);
	}
	
	printf("xmax: %d, xmin: %d, ymax: %d, ymin: %d\n", xmax, xmin, ymax, ymin);
	int count = countMap(map);
	printf("Total spaces: %d\n", count);
}
