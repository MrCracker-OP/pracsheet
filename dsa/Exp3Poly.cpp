#include <stdio.h>
#include <stdlib.h>

// Corrected struct naming to 'Node' consistently
typedef struct Node {
    int coefficient;
    int exponent;
    struct Node *next; 
} Node;

// Create a new node for the polynomial
Node *createNode(int coefficient, int exponent){
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL) { // Check for malloc failure
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->coefficient = coefficient;
    newNode->exponent = exponent;
    newNode->next = NULL;
    return newNode;
}

// Insert a node in descending order of exponents
Node *insertNode(Node *head, int coefficient, int exponent){
    Node *newNode = createNode(coefficient, exponent);
    if (head == NULL || exponent > head->exponent){
        newNode->next = head;
        return newNode;
    }

    Node *current = head;
    while (current->next != NULL && current->next->exponent > exponent){
        current = current->next;
    }
    newNode->next = current->next;
    current->next = newNode;
    return head;
}

// Display the polynomial
void displayPolynomial(Node *head) {
    if (head == NULL) {
        printf("0");
        return;
    }
    
    while (head != NULL){
        if (head->exponent == 0) {
            printf("%d", head->coefficient);
        }
        else if (head->exponent == 1) {
            printf("%dx", head->coefficient);
        }
        else {
            printf("%dx^%d", head->coefficient, head->exponent);
        }
        
        if (head->next != NULL && head->next->coefficient > 0){
            printf(" + ");
        }
        head = head->next;
    }
}

// Add two polynomials
Node *addPolynomials(Node *poly1, Node *poly2){
    Node *result = NULL;

    while (poly1 != NULL || poly2 != NULL) {
        if(poly1 != NULL && (poly2 == NULL || poly1->exponent > poly2->exponent)){
            result = insertNode(result, poly1->coefficient, poly1->exponent);
            poly1 = poly1->next;
        }
        else if (poly2 != NULL && (poly1 == NULL || poly2->exponent > poly1->exponent)){
            result = insertNode(result, poly2->coefficient, poly2->exponent);
            poly2 = poly2->next;
        }
        else{
            int sumCoeff = poly1->coefficient + poly2->coefficient;
            if (sumCoeff != 0) {
                result = insertNode(result, sumCoeff, poly1->exponent);
            }
            poly1 = poly1->next;
            poly2 = poly2->next;
        }
    }

    return result;
}

// Free the memory used by the polynomial list
void freePolynomial(Node *head){
    Node *temp;
    while (head != NULL){
        temp = head;
        head = head->next;
        free(temp);
    } 
}

int main(){
    Node *poly1 = NULL, *poly2 = NULL;

    // First polynomial: 3x^4 + 2x^2 + 1
    poly1 = insertNode(poly1, 3, 4);
    poly1 = insertNode(poly1, 2, 2);
    poly1 = insertNode(poly1, 1, 0);

    // Second polynomial: 4x^3 + 3x^1
    poly2 = insertNode(poly2, 4, 3);
    poly2 = insertNode(poly2, 3, 1);

    printf("First Polynomial: ");
    displayPolynomial(poly1);
    printf("\n");

    printf("Second Polynomial: ");
    displayPolynomial(poly2);
    printf("\n");

    printf("Sum of Polynomials: ");
    Node *sum = addPolynomials(poly1, poly2);
    displayPolynomial(sum);
    printf("\n"); // Corrected newline

    // Free memory
    freePolynomial(poly1);
    freePolynomial(poly2);
    freePolynomial(sum);

    return 0;
}
