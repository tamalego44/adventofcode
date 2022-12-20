#include <stdio.h>
#include <stdlib.h>

#define LMAX 100
#define NMAX 10000

int getMax(int *cals);

int main(int argc, char *argv[]) {
	// Verify proper args were used
	// Usage: ./p<1/2> <filename>
	char *filename;
	if (argc != 2) {
		printf("Improper Syntax. Usage: ./p<1/2> <filename>\n");
		printf("Filename is likely \"sample.txt\" or \"input.txt\"\n");
	}
	else {
		filename = argv[1];
	}

	FILE* fp;
	fp = fopen(filename, "r");
	
	char buff[LMAX];
       	int cals[NMAX] = {0};
	int i = 0;	
	while(fgets(buff, LMAX, fp)){
		//printf("%s", buff);

		if (buff[0] == '\n') {
			i++;
		}
		else {
			cals[i] += atoi(buff);
		}
	}
	
	int top3 = 0;
	for (i=0; i<3; i++) {
		top3 += getMax(cals);
	}

	printf("The highest 3 calories sum to: %d\n", top3);
}

int getMax(int *cals) {
	int max = -1, maxi = -1;
	for (int i=0; cals[i] != 0; i++) {
		if (cals[i] > max) {
			max = cals[i];
			maxi = i;
		}
	}
	cals[maxi] = -1;
	return max;
}
