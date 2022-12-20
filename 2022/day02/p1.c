#include <stdio.h>
#include <stdlib.h>

int getScore(char a, char b);

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
	fp = fopen(filename, "r");
	
	char buff[10];
	int score = 0;
	char a, b;
	while (fgets(buff, 10, fp)) {
		//printf("%s", buff);
		sscanf(buff, "%c %c", &a, &b);
	       	//printf("a: %c, b: %c", a, b);
		score += getScore(a, b);	
	}	
	
	printf("Total Score: %d\n", score);
}

int getScore(char a, char b) {
	int score = 0;
	if (a == 'A') {
		if (b == 'Y') {
			score += 6;
		} else if (b == 'X') {
			score += 3;
		}
	} else if (a == 'B') {
		if (b == 'Z') {
			score += 6;
		} else if (b == 'Y') {
			score += 3;
		}
	} else {
		if (b == 'X') {
			score += 6;
		} else if (b == 'Z') {
			score += 3;
		}
	}

	switch (b) {
		case 'Z':
			score++;
		case 'Y':
			score++;
		case 'X':
			score++;
		default:
			break;
	}

	return score;
}
