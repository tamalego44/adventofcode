#include <stdio.h>
#include <stdlib.h>
#include "llist.h"

void printList(struct llist *list) {
    // If no elements print empty list
    if (list->size == 0) {
        printf("[]\n");
        return;
    }
    // Otherwise there is at least one element

    printf("[");
    struct node *p;
    for (p = list->head; p->next != list->head; p=p->next) {
        printf("%d, ", p->data);
    }
    printf("%d]\n", p->data);
}

struct llist* newList() {
    struct llist *l = (struct llist*) malloc(sizeof(struct llist));
    l->size = 0;
    l->head = NULL;
    return l;
}

void insertList(struct llist *list, int key, int data) {
    struct node *link = (struct node*) malloc(sizeof(struct node));

    link->data = data;
    link->key = key;

    if (list->head == NULL) {
        link->next = link;
        link->prev = link;
        list->head = link;
    }
    else {
        link->next = list->head;
        link->prev = list->head->prev;
        list->head->prev->next = link;
        list->head->prev = link;
    }
    list->size++;
}

void mixList(struct llist *list, int key) {
    struct node *link = list->head;
    while (link->key != key) {
        link = link->next;
    }
    printf("%d\n", link->data);

    // Now link should point to the proper node to mix
    if (link->data > 0) {
        for (int i=0; i<link->data; i++) {
            link->prev->next=link->next;
            link->next->prev=link->prev;
            struct node *new = link->next->next;
            link->next->next=link;
            link->prev=link->next;
            link->next=new;
            new->prev=link;
        }
    } else if (link->data < 0) {
        for (int i=0; i<-(link->data); i++) {
            link->next->prev=link->prev;
            link->prev->next=link->next;
            struct node *new = link->prev->prev;
            link->prev->prev=link;
            link->next=link->prev;
            link->prev=new;
            new->next=link;
        }
    }
}

int nAfterZeroList(struct llist *list, int n) {
    struct node *link = list->head;
    while (link->data != 0) {
        link = link->next;
    }

    for (int i=0; i < n; i++) {
        link = link->next;
    }

    printf("%d\n", link->data);
    return link->data;
}