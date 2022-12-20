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
	
	int map[LMAX] = {0};	
	int score = 0;
	while (fgets(buff, LMAX, fp)) {
		//printf("%s", buff);
		//printf("%d\n", (int)strlen(buff)-1);
		int l = (int) strlen(buff) - 1;
		for (int i=0; i < l/2; i++) {
			//printf("%c\n", buff[i]);
			map[calcPriority(buff[i])] += 1;
		}
		for (int i=l/2; i< l; i++) {
			if (map[calcPriority(buff[i])] != 0) {
				score += calcPriority(buff[i]);
				//printf("%d\n", calcPriority(buff[i]));
				break;
			}
		}
		memset(map, 0, LMAX*sizeof(int));
	}
	printf("Total Priority: %d\n", score);
}
