#include <stdio.h>
#include <malloc.h>

struct Queue{                                       // This structure stores all the information of the Queue
  
  int front;
  int rear;
  int capacity;
  int size;
  int * arr;
    
};


void init(struct Queue * q, int capacity1)           // Initailising the queue
{
    q->front = 0;                                    // front points to the first element of the queue (Not the first element of the array)
    q->rear = -1;                                    // rear points to the last element of the queue (Not the last element of the array)
    q->capacity = capacity1;                         // Max elements which queue can accomodate / size of the array used
    q->arr = (int *)malloc(sizeof(int) * capacity1); //By default malloc has a return datatype of void *, creating an array of int of size = capacity1 at runtime
    q->size = 0;                                     // Initially 0, stores the number of elements in the queue

}




int isFull(struct Queue* q){
    return q->size == q->capacity;  
}

int isEmpty(struct Queue* q){
    return q->size == 0;
}

void enqueue(struct Queue* q, int value)
{
    if (isFull(q)){
        printf("Cannot insert more elements in the Queue, it is already full \n");
        return;
    }
    else{
        q->rear = ((q->rear)+1)%(q->capacity);      // Increment the rear index while enqueuing an element  ( % operation to handle index overflow)
        q->arr[q->rear] = value;                    // Insert element at the rear index
        q->size++;                                  // Increase the size of the queue by 1
    }
    
    displayQueue(q);
}

void dequeue(struct Queue* q)
{
    if (isEmpty(q))
    {
        printf("Queue is already empty, cannot dequeue any element\n");
    }
    else{
        q->front = ((q->front)+1)%(q->capacity);    // Increment the front index by 1 while dequeing an element, because we dequeue from the front
        q->size--;                                  // Decrease the size of the queue by 1 after dequeueing the element
    }
    
    displayQueue(q);
}

void displayQueue(struct Queue* q)
{
    if(isEmpty(q))
    {
        printf("queue is empty\n");
        return;
    }
    int i = q->front;
    int count = q->size;
    
    while(count != 0)
    {
        printf("%d ", q->arr[i]);
        i = (i+1)%q->capacity;
        count -= 1;
    }
    printf("\n");
    return;
}

int getFront(struct Queue *q)
{
    if(isEmpty(q))
    {
        printf("No element in the Queue\n");
        return;
    }
    else
    {
        return q->arr[q->front];
    }
}


void main()
{
    struct Queue q;
    init(&q, 5);
    displayQueue(&q);
    enqueue(&q, 1);
    enqueue(&q, 2);
    enqueue(&q, 5);
    dequeue(&q);
    enqueue(&q, 3);
    enqueue(&q, 6);
    enqueue(&q, 7);
    enqueue(&q, 8);
    dequeue(&q);
    dequeue(&q);
    dequeue(&q);
    printf("the front element is : %d\n", getFront(&q));
    dequeue(&q);
    dequeue(&q);
    
    
    
}