#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "funcs.h"

#define LMAX 100
#define NMAX 1000

struct point {
	int x;
	int y;
};

struct point* newPoint(int x, int y) {
	struct point *p = malloc(sizeof(struct point));
	p->x = x;
	p->y = y;

	return p;
}

void fixTail(struct point *h, struct point *t) {
	int dx = h->x > t->x ? h->x - t->x : t->x - h->x;
	int dy = h->y > t->y ? h->y - t->y : t->y - h->y;
	int ddx = dx == 0 ? 0 : (h->x - t->x) / dx;
	int ddy = dy == 0 ? 0 : (h->y - t->y) / dy;

	if (dx == 0 && dy > 1) {
		t->y += ddy;
	}
	else if (dy == 0 && dx > 1) {
		t->x += ddx;
	}
	else if (dx > 1 || dy > 1) {
		t->x += ddx;
		t->y += ddy;
	}
}

void fixTails(int n, struct point *knots[]) {
	for (int i = 1; i < n; i++) {
		fixTail(knots[i-1], knots[i]);
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
	int n = 10;
	
	struct point *knots[n];
	for (int i = 0; i < n; i++) {
		knots[i] = newPoint(500, 500);
		// Where knots[0] is the head
	}

	while (fgets(buff, LMAX, fp)) {
		printf("%s", buff);
		char dir;
		int dist;
		sscanf(buff, "%c %d", &dir, &dist);
		
		for (int i = 0; i < dist; i++) {
			switch (dir) {
				case 'U':
					knots[0]->y++;
					break;
				case 'D':
					knots[0]->y--;
					break;
				case 'R':
					knots[0]->x++;
					break;
				case 'L':
					knots[0]->x--;
					break;
			}
			fixTails(n, knots);
			//map[hx][hy] = 1;
			map[knots[9]->x][knots[9]->y] = 1;
		}

	}
	
	int count = countMap(map);
	printf("Total spaces: %d\n", count);
}
