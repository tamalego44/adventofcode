#ifndef LLIST_H_
#define LLIST_H_

struct node {
    int key;
    long long int data;
    struct node *prev;
    struct node *next;
};

struct llist {
    struct node *head;
    long long int size;
};

void printList(struct llist *list);
struct llist* newList();
void insertList(struct llist *list, int key, long long int data);
void mixList(struct llist *list, int key);
long long int nAfterZeroList(struct llist *list, int n);

#endif
