#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include "directory.h"
#include "funcs.h"

#define NMAX 10000

/*
struct dir {
	char *name;
	struct dir *out;
	struct *dir[NMAX] dir_contents;
	struct *file[NMAX] file_contents;
	int ndirs;
	int nfiles;
}

struct file {
	char *name;
	int size;
}
*/

struct dir* dir_root() {
	return dir_new(NULL, "/");
}

struct dir* dir_new(struct dir *od, char *name) {
	struct dir *d = (struct dir*)malloc(sizeof(struct dir));
	memcpy(d->name, name, strlen(name));
	d->out = od;
	memset(d->dir_contents, 0, sizeof(d->dir_contents));
	memset(d->file_contents, 0, sizeof(d->file_contents));
	d->ndirs = 0;
	d->nfiles = 0;
}

struct file* file_new(char *name, int size) {
	struct file *f = (struct file*)malloc(sizeof(struct file));
	memcpy(f->name, name, strlen(name));
	f->size = size;
}

struct dir* dir_subdir(struct dir *d, char *name) {
	for (int i=0; i<d->ndirs; i++) {
		if (strcmp(name, d->dir_contents[i]->name) == 0) {
			return d->dir_contents[i];
		}
	}
	
	// dir not found; create it
	d->dir_contents[d->ndirs] = dir_new(d, name);
	return d->dir_contents[d->ndirs++];
}

struct file* dir_subfile(struct dir *d, char *name, int size) {
	for (int i=0; i<d->nfiles; i++) {
		if (strcmp(name, d->file_contents[i]->name) == 0) {
			printf("%s\n", name);
			return d->file_contents[i];

		}
	}
	
	// file not found; create it
	d->file_contents[d->nfiles] = file_new(name, size);
	return d->file_contents[d->nfiles++];
}

void dir_print(struct dir *d, int depth) {
	for (int i = 0; i < depth*2; i++) {
		printf(" ");
	}
	printf("- %s (dir)\n", d->name);

	for (int i = 0; i < d->ndirs; i++) {
		dir_print(d->dir_contents[i], depth+1);
	}

	for (int i=0; i < d->nfiles; i++) {
		for (int i = 0; i < (depth+1)*2; i++) {
			printf(" ");
		}
		printf("- %s (file, size=%d)\n", d->file_contents[i]->name, d->file_contents[i]->size);
	}
}

int dir_size(struct dir *d) {
	int size = 0;
	for (int i = 0; i < d->ndirs; i++) {
		size += dir_size(d->dir_contents[i]);
	}
	for (int i = 0; i < d->nfiles; i++) {
		size += d->file_contents[i]->size;
	}
	return size;
}

int dir_sum(struct dir *d, int max) {
	int sum = 0;
	int size = dir_size(d);
	for (int i = 0; i < d->ndirs; i++) {
		sum += dir_sum(d->dir_contents[i], max);
	}

	if (size < max) {
		return sum + size;
	}
	else {
		return sum;
	}
}

int dir_smallest(struct dir *d, int min) {
	int smallest = INT_MAX;
	int size = dir_size(d);
	for (int i = 0; i < d->ndirs; i++) {
		smallest = MIN(dir_smallest(d->dir_contents[i], min), smallest);
	}

	if (size > min) {
		return MIN(smallest, size);
	}
	else {
		return smallest;
	}
}
