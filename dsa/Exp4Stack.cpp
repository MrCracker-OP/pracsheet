#include<stdio.h>
#include<stdlib.h>

#define MAX 5// Maximum size of the stack

int stack[MAX];
int top = -1;

// Function to push an element in the stack
void push(){
    int value;
    if(top == MAX -1){
    printf("Stack Overflow!\n");    
    }else{
        printf("Enter the value to push: ");
        scanf("%d\n", &value);
        stack[++top] = value;
        printf("Value pushed: %d\n", value);
    }
}

// Function to pop an element in the stack
void pop(){
    if(top == -1){
        printf("Stack Underflow!\n");
    }else{
        printf("Value popped: %d\n", stack[top--]);
    }
}

// Function to display top element in stack
void peek(){
    if(top == -1){
        printf("Stack is empty!\n");
    }else{
        printf("Top element: %d\n", stack[top]);
    }
}

// Display  all elements in stack
void display(){
    if(top == -1){
        printf("Stack is empty!\n");
    }else{
        printf("Stack elements: ");
         for(int i=0; i<= top; i++){
            printf("%d\n", stack[i]);
         }
         printf("\n");
    }
}

// Function to display the size of the stack
void size(){
    printf("Size of the stack: %d\n", top + 1);
}

// Main function with menu-driven approach
int main(){
    int choice;
    while(1){
        printf("\n--- Stack Menu ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Peek\n");
        printf("4. Display\n");
        printf("5. Size\n");
        printf("6. Exit\n");
        printf("Enter Your Choice: ");
        scanf("%d", &choice);

        switch(choice){
            case 1:
                push();
                break;

            case 2:
                pop();
                break;

            case 3:
                peek();
                break;

            case 4:
                display();
                break;
            
            case 5:
                size();
                break;
            
            case 6:
                exit(0);

            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}