#ifndef QUEUE_H_
#define QUEUE_H_

struct node {
    int data;
    struct node *next;
};

struct queue {
    struct node *head;
    int size;
};

void queuePrint(struct queue *q);
struct queue* newQueue();
void queueEnqueue(struct queue *q, int data);
int queueDequeue(struct queue *q);
int isEmpty(struct queue *q);
#endif
