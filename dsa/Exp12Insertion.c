#include <stdio.h>

void insertionsort(int arr[], int n){
    int i, key, j;
    for(i = 0; i < n; i++){
        key = arr[i];
        j = j - 1;

    while(j >= 0 && arr[j] > key){
        arr[j + 1] = arr[j];
        j = j - 1;

    }
    arr[j + 1] = key;
    }
}

int main(){
    int i;
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Unsorted array: ");
    for(i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

    insertionsort(arr, n);
    
    printf("sorted array: ");
    for(i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;

}