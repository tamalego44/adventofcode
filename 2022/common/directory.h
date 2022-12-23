#ifndef DIRECTORY_H_
#define DIRECTORY_H_

#define NMAX 10000

struct file {
	char name[100];
	int size;
};

struct dir {
	char name[100];
	struct dir *out;
	struct dir *dir_contents[NMAX];
	struct file *file_contents[NMAX];
	int ndirs;
	int nfiles;
};

struct dir* dir_root();
struct dir* dir_new(struct dir *od, char *name);
struct file* file_new(char *name, int size);
struct dir* dir_subdir(struct dir *d, char *name);
struct file* dir_subfile(struct dir *d, char *name, int size);
void dir_print(struct dir *d, int depth);
int dir_size(struct dir *d);
int dir_sum(struct dir *d, int max);
int dir_smallest(struct dir *d, int min);
#endif
