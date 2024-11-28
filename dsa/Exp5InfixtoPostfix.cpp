#include <stdio.h>
#include<ctype.h> // For isalnum
#define MAX 100

char stack[MAX];
int top = -1;

//Function to push an element into the stack
void push(char c){
    if (top == MAX -1){
        printf("Stack Overflow!\n");
    }else{
        stack[++top]=c;
    }
}

// Function to pop an element into the stack
char pop(){
    if(top==-1){
        printf("Stack underflow!\n");
        return '\0';
    }else{
        return stack[top--];
    }
}

// Function to get the precedence of operators
int precedence(char c){
    if(c == '^') return 3;
    else if (c == '*' || c == '/') return 2;
    else if (c == '+' || c == '-') return 1; 
    else return 0;
}

// Function to convert infix to postfix
void infixtoPostfix(char infix[]){
    char postfix[MAX];
    int i = 0,j = 0;

    while (infix[i] != '\0'){
        char c = infix[i];

        // If character is an operand , add it to the result
        if (isalnum(c)){
            postfix[j++] = c;
        }
        // If character is '(' , add it to the result
        else if (c == '('){
            push(c);
        }
        // If character is ')',pop untit '(' is found
        else if (c == ')'){
            while(top != -1 && stack[top] != '('){
                postfix[j++] = pop();
            }
            pop();// Remove '(' from the stack
        }
        // If character is an operator
        else{
            while(top != -1 && precedence(c) <= precedence(stack[top])){
                postfix[j++] = pop();
            }
            push(c);
        }
        i++;
    }

    //Pop all remaining opeators from the stack
    while(top != -1){
        postfix[j++] = pop();
    }

    postfix[j] = '\0'; // NULL - terminate the postfic string

    printf("Postfix Expression: %s\n", postfix);
}

// Main function
int main(){
    char infix[MAX];

    printf("Enter an infix expression: ");
    scanf("%s", infix);

    infixtoPostfix(infix);

    return 0;
}
