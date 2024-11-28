#include<stdio.h>
#include<stdlib.h>

//Define the structure for a tree node
struct node{
    int item;
    struct node* left;
    struct node* right;
};

//Function to create a new node
struct node* createNode(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->item = value;
    newnode->left = NULL;
    newnode->right = NULL;
    return newnode;
}

// Function to insert a new value into the bst
struct node* insert(struct node* root,int value){
    if(root == NULL)
       return createNode(value);

    if (value < root->item)
        root->left = insert(root->left, value);
    else if(value > root->item)
        root->right = insert(root->right, value);

    return root;
}

// Inorder traversal
void inorder(struct node* root){
    if(root != NULL){
        inorder(root->left);
        printf("%d",root->item);
        inorder(root->right);
    }
}

// Preorder traversal
void preorder(struct node* root) {
    if (root != NULL) {
        printf("%d ", root->item);
        preorder(root->left);
        preorder(root->right);
    }
}

// Postorder traversal
void postorder(struct node* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->item);
    }
}

int main(){
    struct node* root = NULL;

    // Insert values into the tree
    root = insert(root,5);
    insert(root,2);
    insert(root,1);
    insert(root,4);
    insert(root,7);
    insert(root,6);
    insert(root,9);
    
      // Print tree traversals
    printf("Inorder Traversal: ");
    inorder(root);
    printf("\n");

    printf("Preorder Traversal: ");
    preorder(root);
    printf("\n");

    printf("Postorder Traversal: ");
    postorder(root);
    printf("\n");

    return 0;
}

