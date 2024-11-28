#include <stdio.h>
#include <conio.h>  // Turbo C uses <conio.h> for `getch`
#include <stdlib.h> // For malloc and free

// Structure for a binary tree
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Create a new Node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Insert a new Node into the BST
struct Node* insert(struct Node* root, int data) {
    if (root == NULL) 
        return createNode(data);
    if (data < root->data)
        root->left = insert(root->left, data);
    else if (data > root->data)
        root->right = insert(root->right, data);
    return root;
}

// Search for a value in the BST
struct Node* search(struct Node* root, int key) {
    if (root == NULL || root->data == key) 
        return root;
    if (key < root->data)
        return search(root->left, key);
    return search(root->right, key);
}

// In-order traversal
void inOrder(struct Node* root) {
    if (root != NULL) {
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}

// Pre-order traversal
void preOrder(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}

// Post-order traversal
void postOrder(struct Node* root) {
    if (root != NULL) {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }
}

// Find the minimum value node
struct Node* findMin(struct Node* node) {
    while (node != NULL && node->left != NULL)
        node = node->left;
    return node;
}

// Delete a node from the BST
struct Node* deleteNode(struct Node* root, int data) {
    struct Node* temp; // Declare variable at the start of the function

    if (root == NULL) 
        return root;
    if (data < root->data)
        root->left = deleteNode(root->left, data);
    else if (data > root->data)
        root->right = deleteNode(root->right, data);
    else {
        if (root->left == NULL) {
            temp = root->right; // No re-declaration here
            free(root);
            return temp;
        }
        if (root->right == NULL) {
            temp = root->left; // No re-declaration here
            free(root);
            return temp;
        }
        temp = findMin(root->right); // No re-declaration here
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

void main() {
    struct Node* root = NULL;
    struct Node* searchResult;  // Declare all variables at the start
    int key;

    // Insert nodes into the BST
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    clrscr(); // Clear screen (Turbo C specific)

    // Traversals
    printf("In-Order: ");
    inOrder(root);
    printf("\n");

    printf("Pre-Order: ");
    preOrder(root);
    printf("\n");

    printf("Post-Order: ");
    postOrder(root);
    printf("\n");

    // Search
    key = 40;  // Initialize the variable after declaration
    searchResult = search(root, key);  // Use pre-declared variable
    printf("Node %d %s in the tree.\n", key, searchResult ? "found" : "not found");

    // Deletion
    printf("Deleting node 20\n");
    root = deleteNode(root, 20);
    printf("In-Order after deletion: ");
    inOrder(root);
    printf("\n");

    getch(); // Wait for keypress (Turbo C specific)
}

