#include <stdio.h>
#include <stdlib.h>
#include "llist.h"

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
	
	//int dec_key = 811589153;	
	struct llist *l = newList();
	int i = 0;
	while (fgets(buff, LMAX, fp)) {
		insertList(l, i, atoi(buff));
		i++;
	}
	//printList(l);
	
	for (int j = 0; j < i; j++) {
		mixList(l, j);
		//printList(l);
	}

	int score = 0;
	score += nAfterZeroList(l, 1000);
	score += nAfterZeroList(l, 2000);
	score += nAfterZeroList(l, 3000);

	printf("Coordinate Sum: %d\n", score);
}
