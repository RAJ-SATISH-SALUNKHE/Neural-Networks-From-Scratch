#include <stdio.h>
#include <malloc.h>

struct Queue{                                                             // Stores the info about queue element
    int data;
    struct Queue *next;
};

struct Queue *front =  NULL;                                              // Initially NULL because no element in the queue
struct Queue *back = NULL;                                                // Initially NULL because no element in the queue

void Enqueue(int value)
{
    struct Queue * temp = (struct Queue *)malloc(sizeof(struct Queue));   // Create a node/ element at runtime
    temp->data = value;                                                   // Put the value of the node
    temp->next = NULL;                                                    // Initialise the next of this node to NULL
    if(front == NULL){                                                    // If no element was present initially, then assign temp to front
        front = temp;
    }
    if(back != NULL)
    {
        back->next = temp;                                                 // If there is already element present in queue (therefore back is not NULL), then just point back->next to temp, because we enqueue from the back
    }
    back = temp;                                                           // Update the back pointer to temp which is the latest enqeueed node/element
    
    display();
}

void Dequeue()
{
    if(front == NULL)
    {
        printf("Queue is already empty, cannot Dequeue\n");
        return;
    }
    printf("Dequeued element is : %d \n", front->data);
    struct Queue *temp = front;                                             // Create a temp pointer, which points to front
    front = front->next;                                                    // Increment front to front->next
    temp->next = NULL;                                                      // Obvious !!
    free(temp);                                                             // free the temp, because front is alrrady updated, this is dequeing
    display();
}

void display()
{
    if(front == NULL)
    {
        printf("Queue is empty \n");
    }
    struct Queue * temp = front;
    
    while(temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}



void main()
{
    display();
    Enqueue(1);
    Enqueue(2);
    Enqueue(3);
    Enqueue(4);
    Enqueue(5);
    Enqueue(6);
    Enqueue(7);
    Dequeue();
    Dequeue();
    Dequeue();
    Dequeue();
    Dequeue();
    Dequeue();
    Dequeue();
    
}