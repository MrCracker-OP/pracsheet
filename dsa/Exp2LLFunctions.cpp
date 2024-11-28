#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
}Node;

// create a new node
Node* createNode(int data){
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Append a node at the end
void append(Node** head, int data){
    Node* newNode = createNode(data);
    if (!*head){
        *head = newNode;
        return;
    }
    Node* temp = *head;
    while (temp->next) temp = temp->next;
    temp->next = newNode;
}

// Print the linked list
void printList(Node* head) {
    while (head) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

// Count nodes in the list
int countNodes(Node* head){
    int count = 0;
    while (head) {
        count++;
        head = head->next;
    }
    return count;
}

// reverse the list
Node* reverseList(Node* head){
    Node* prev = NULL;
    while (head){
        Node* next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev; 
}

// Concatenate two lists
Node* concatenate(Node* list1, Node* list2){
    if(!list1) return list2;
    Node* temp = list1;
    while (temp->next) temp = temp->next;
    temp->next = list2;
    return list1;
}

// Split the list into two halves
void splitList(Node* head, Node** front, Node** back){
    if(!head || !head->next) {
        *front = head;
        *back = NULL;
        return;
    }
    
    Node* slow = head;
    Node* fast = head->next;

    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }

    *front = head;
    *back = slow->next;
    slow->next = NULL;
}

// main function to test the operations
int main(){
    Node* list1 = NULL;
    append(&list1, 1);
    append(&list1, 2);
    append(&list1, 3);
    append(&list1, 4);
    append(&list1, 5);

    printf("List 1: ");
    printList(list1);
    printf("Node count: %d\n", countNodes(list1));

    Node* reversed = reverseList(list1);
    printf("reversed list: ");
    printList(reversed);

    Node* list2 = NULL;
    append(&list2, 6);
    append(&list2, 7);
    Node* concatenated = concatenate(reversed, list2);
    printf("Concatenated List: ");
    printList(concatenated);

    Node* front = NULL;
    Node* back = NULL;
    splitList(concatenated, &front, &back);
    printf("First half after split: ");
    printList(front);
    printf("Second half after split: ");
    printList(back);

    return 0;


}

