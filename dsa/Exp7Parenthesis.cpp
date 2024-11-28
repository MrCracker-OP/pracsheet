#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 100

// Stack implementation
char stack[MAX];
int top = -1;

//Push function
void push(char ch){
    if(top < MAX -1){
        stack[++top] = ch;
    }
}

// Pop function
char pop(){
    if(top >= -1){
        return stack[top--];
    }
    return '\0';
}

//Function to check matching brakets
int isMatchingPair(char open,char close){
    return (open == '(' && close == ')') ||
           (open == '{' && close == '}') ||
           (open == '[' && close == ']');
}

// Function to check if the expression is balanced
int isBalanced(char* expr){
    for(int i = 0; i < strlen(expr); i++){
        char ch = expr[i];
        if (ch == '(' || ch == '{' || ch == '['){
            push(ch);
        }else if(ch == ')' || ch == '}' || ch == ']'){
            if(top == -1 || !isMatchingPair(pop(),ch)){
                return 0;
            }
        }
    }
    return (top == -1);
}

int main(){
    char expr[MAX];
    printf("Enter an expression: ");
    scanf("%s",expr);

    if(isBalanced(expr)){
        printf("The expression is balances.\n");
    }else{
        printf("The expression is not balanced.\n");

    }
    return 0;
}