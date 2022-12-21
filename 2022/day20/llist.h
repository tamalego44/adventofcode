#ifndef LLIST_H_
#define LLIST_H_

struct node {
    int key;
    int data;
    struct node *prev;
    struct node *next;
};

struct llist {
    struct node *head;
    int size;
}

void printList(struct llist *list);
struct llist* newList();
void insertList(struct llist *list, int key, int data);
void mixList(struct llist *list, int key);
int nAfterZeroList(struct llist *list, int n);

#endif