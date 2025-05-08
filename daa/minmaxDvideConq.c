#include <stdio.h>

void maxminDC(int a[], int i, int j, int *max, int *min) {
    int mid, max1, min1;
    
    // Base case when there's only one element
    if (i == j) {
        *max = a[i];
        *min = a[i];
        return;
    }

    // Base case when there are two elements
    if (i == j - 1) {
        if (a[i] < a[j]) {
            *max = a[j];
            *min = a[i];
        } else {
            *max = a[i];
            *min = a[j];
        }
        return;
    }

    // Divide the array into two halves
    mid = (i + j) / 2;
    
    // Recursive calls for both halves
    maxminDC(a, i, mid, max, min);
    maxminDC(a, mid + 1, j, &max1, &min1);

    // Compare and update the overall max and min
    if (*max < max1) {
        *max = max1;
    }
    if (*min > min1) {
        *min = min1;
    }
}

int main() {
    int arr[30];
    int i, n, max, min;

    // Get the size of the array and the elements
    printf("Enter size of an array: ");
    scanf("%d", &n);

    printf("\nEnter array elements: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Initialize max and min before calling maxminDC
    max = arr[0];
    min = arr[0];

    // Call the divide and conquer function
    maxminDC(arr, 0, n - 1, &max, &min);

    // Print the result
    printf("Maximum: %d\n", max);
    printf("Minimum: %d\n", min);

    return 0;
}
