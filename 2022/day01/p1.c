#include <stdio.h>

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
	
}
