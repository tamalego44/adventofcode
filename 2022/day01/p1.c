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
	
	int max = 0;
	for (i=0; cals[i] != 0; i++) {
		if (cals[i] > max) {
			max = cals[i];
		}
	}
	printf("Highest Calories: %d\n", max);

}
