#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "directory.h"

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
	
	if (fp == NULL) {
		perror("Error reading file");
		exit(1);
	}

	struct dir *root = dir_root();
	struct dir *curr;
	char arg[LMAX];
	while (fgets(buff, LMAX, fp)) {
		memset(arg, 0, sizeof(arg));		
		int retv = sscanf(buff, "$ cd %s", arg);
		if (retv > 0) {
			//printf("%s\n", arg);
			// cd command
			if (strcmp("/", arg) == 0) {
				// cd /
				curr = root;
			}
			else if (strcmp("..", arg) == 0) {
				// cd ..
				curr = curr->out;
			}
			else {
				// cd x
				curr = dir_subdir(curr, arg);
			}
		}
		else {
			int size;
			char name[LMAX];
			retv = sscanf(buff, "%d %s", &size, name);
		       	if (retv == 2) {
				// File
				dir_subfile(curr, name, size);
			}
			else {
				retv = sscanf(buff, "dir %s", name);
				if (retv == 1) {
					dir_subdir(curr, name);
				}
			}
		}
	}

	dir_print(root, 0);

	int total_space = 70000000;
	int current_space = dir_size(root);
	int remaining_space = total_space - current_space;
	int min = 30000000 - remaining_space;
	
	int smallest = dir_smallest(root, min);
	printf("Smallest directory size that fits: %d\n", smallest);
}
