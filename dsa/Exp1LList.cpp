#include <stdio.h>
#include <stdlib.h>

// Define the structure for a node
struct node {
    int data;
    struct node* next;
};

struct node* head = NULL;

// Function to create a new node
struct node* createnode(int data) {
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = data;
    newnode->next = NULL;
    return newnode;
}

// Insert at the beginning
void insertatbeg() {
    int data;
    printf("Enter data: ");
    scanf("%d", &data);
    struct node* newnode = createnode(data);
    newnode->next = head;
    head = newnode;
    printf("Inserted at the beginning.\n");
}

// Insert at the end
void insertatend() {
    int data;
    printf("Enter data: ");
    scanf("%d", &data);
    struct node* newnode = createnode(data);

    if (head == NULL) {
        head = newnode;
    } else {
        struct node* temp = head;
        while (temp->next != NULL) temp = temp->next;
        temp->next = newnode;
    }
    printf("Inserted at end.\n");
}

// Insert at a specific position
void insertatpos() {
    int data, pos;
    printf("Enter data: ");
    scanf("%d", &data);
    printf("Enter position: ");
    scanf("%d", &pos);

    if (pos == 1) {
        insertatbeg();
        return;
    }

    struct node* newnode = createnode(data);
    struct node* temp = head;

    for (int i = 1; i < pos - 1 && temp != NULL; i++) temp = temp->next;

    if (temp == NULL) {
        printf("Invalid position.\n");
        free(newnode);
    } else {
        newnode->next = temp->next;
        temp->next = newnode;
        printf("Inserted at position %d.\n", pos);
    }
}

// Delete at the beginning
void deleteatbeg() {
    if (head == NULL) {
        printf("List is empty.\n");
    } else {
        struct node* temp = head;
        head = head->next;
        free(temp);
        printf("Deleted from beginning.\n");
    }
}

// Delete at the end
void deleteatend() {
    if (head == NULL) {
        printf("List is empty.\n");
    } else if (head->next == NULL) {
        free(head);
        head = NULL;
        printf("Deleted from end.\n");
    } else {
        struct node* temp = head;
        while (temp->next->next != NULL) temp = temp->next;
        free(temp->next);
        temp->next = NULL;
        printf("Deleted from end.\n");
    }
}

// Display the linked list
void traverse() {
    if (head == NULL) {
        printf("List is empty.\n");
    } else {
        struct node* temp = head;
        printf("List: ");
        while (temp != NULL) {
            printf("%d -> ", temp->data);
            temp = temp->next;
        }
        printf("NULL\n");
    }
}

// Main menu for the program
int main() {
    int choice;
    while (1) {
        printf("\nMenu:\n");
        printf("1) Insert at beginning\n");
        printf("2) Insert at end\n");
        printf("3) Insert at position\n");
        printf("4) Delete at beginning\n");
        printf("5) Delete at end\n");
        printf("6) Show list\n");
        printf("7) Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: insertatbeg(); break;
            case 2: insertatend(); break;
            case 3: insertatpos(); break;
            case 4: deleteatbeg(); break;
            case 5: deleteatend(); break;
            case 6: traverse(); break;
            case 7: exit(0);
            default: printf("Invalid choice. Try again.\n");
        }
    }
    return 0;
}
