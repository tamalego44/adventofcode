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
	
	long long int dec_key = 811589153;	
	struct llist *l = newList();
	int i = 0;
	while (fgets(buff, LMAX, fp)) {
		insertList(l, i, (((long long int) atoi(buff)) * dec_key));
		i++;
	}
	//printList(l);
	//printf("%lld\n", l->size);

	for (int k = 0; k < 10; k++) {
		for (int j = 0; j < i; j++) {
			mixList(l, j);
			//printList(l);
		}
		//printList(l);
	}

	long long int score = 0;
	score += nAfterZeroList(l, 1000);
	//printf("%lld", nAfterZeroList(l, 1000));
	score += nAfterZeroList(l, 2000);
	score += nAfterZeroList(l, 3000);

	printf("Coordinate Sum: %lld\n", score);
}
