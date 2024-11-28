#include<stdio.h>
#define MAX 10

int front = -1, rear = -1;
int queue[MAX];

//Function to add an element to the queue
void enqueue(int value){
    if(rear == MAX - 1){
        printf("Queue Overflow\n");
        return;
    }
    if(front == -1)
      front = 0;
    rear++;
    queue[rear] = value;
    printf("ENQUEUED: %d\n", value);
}

int dequeue(){
    if(front == -1){
        printf("Queue underflow\n");
        return -1;
    }
    int value = queue[front];
    if(front == rear)
       front = rear - 1;
    else   
       front++;
    return value;

}

void display(){
    if(front == -1){
        printf("Queue is empty\n");
        return;
    }
    printf("Queue: ");
    for(int i = front; i <= rear; i++ ){
        printf("%d", queue[i]);
    }
    printf("\n");
}

void queuesize(){
    if(front == -1){
        printf("Queue is empty\n");
        return;
    }
    printf("Size of the queue: %d\n", rear - front + 1);

}

//Main Function
int main(){
    int choice,value;

    do{
        printf("\nMenu:\n");
        printf("1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Display Queue\n");
        printf("4. Queue Size\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice){
        case 1:
            printf("Enter a value to enqueue: ");
            scanf("%d",&value);
            enqueue(value);
            break;
        case 2:
            value = dequeue();
            if(value != -1)
               printf("Dequeued: %d\n", value);
               break;
        case 3:
            display();
            break;
        case 4:
            queuesize();
            break;
        case 5:
            printf("Exciting...\n");
            break;
        default:
            printf("Invalid choice, try again.\n");
        }

    }while(choice != 5);

    return 0;

}




