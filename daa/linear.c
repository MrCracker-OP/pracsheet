#include<stdio.h>

int main(){
    int a[100], n, key, i;

    printf("How many numbers? ");
    scanf("%d", &n);

    printf("Enter numbers:\n");
    for(i=0; i < n; i++)
    scanf("%d", &a[i]);

    printf("Search for?");
    scanf("%d", &key);

    for(i=0; i < n; i++) {
        if(a[i] == key) {
            printf("Found at %d\n", i);
            return 0;
        }
    }

    printf("Not found\n");
    return 0;
}