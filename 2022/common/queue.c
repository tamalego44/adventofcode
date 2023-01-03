#include <stdlib.h>
#include <stdio.h>
#include "queue.h"

void queuePrint(struct queue *q) {
	printf("[");
	struct node *curr;

	for (curr = q->head; curr != NULL; curr = curr->next) {
		printf("%d", curr->data);
		if (curr->next != NULL) {
			printf(", ");
		}
	}
	printf("]\n");
}

struct queue* newQueue() {
	struct queue *q = malloc(sizeof(struct queue));
	q->head = NULL;
	q->size = 0;
}

void queueEnqueue(struct queue *q, int data) {
	struct node *new = malloc(sizeof(struct node));
	new->data = data;
	new->next = NULL;

	if (q->head == NULL) {
		q->head = new;
	}
	else {
		struct node *curr;
		for (curr = q->head; curr->next != NULL; curr = curr->next) {
			continue;
		}
		curr->next = new;
	}
	q->size++;
}

int queueDequeue(struct queue *q) {
	if (q->size < 1) {
		return -1;
	}

	int ret = q->head->data;
	q->head = q->head->next;
	q->size -= 1;

	return ret;
}

int isEmpty(struct queue *q);

int main() {
	struct queue *a = newQueue();

	queuePrint(a);

	queueEnqueue(a, 9);
	queueEnqueue(a, 10);
	queueEnqueue(a, 8);
	queueEnqueue(a, 42);
	queuePrint(a);

	printf("%d\n", queueDequeue(a));
	printf("%d\n", queueDequeue(a));
	printf("%d\n", queueDequeue(a));
	queuePrint(a);

	queueEnqueue(a, 0);
	queuePrint(a);
}
