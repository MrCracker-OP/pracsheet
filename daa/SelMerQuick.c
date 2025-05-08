#include <stdio.h>

#define MAX 20

void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min = i;
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[min])
                min = j;
        int temp = a[i];
        a[i] = a[min];
        a[min] = temp;
    }
}

void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i], j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}

void merge(int a[], int l, int m, int h) {
    int temp[MAX], i = l, j = m + 1, k = l;
    while (i <= m && j <= h) {
        if (a[i] < a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while (i <= m) temp[k++] = a[i++];
    while (j <= h) temp[k++] = a[j++];
    for (i = l; i <= h; i++) a[i] = temp[i];
}

void mergeSort(int a[], int l, int h) {
    if (l < h) {
        int m = (l + h) / 2;
        mergeSort(a, l, m);
        mergeSort(a, m + 1, h);
        merge(a, l, m, h);
    }
}

int partition(int a[], int l, int h) {
    int pivot = a[l], i = l, j = h;
    while (i < j) {
        while (i < j && a[j] >= pivot) j--;
        while (i < j && a[i] <= pivot) i++;
        if (i < j) {
            int temp = a[i]; a[i] = a[j]; a[j] = temp;
        }
    }
    a[l] = a[i];
    a[i] = pivot;
    return i;
}

void quickSort(int a[], int l, int h) {
    if (l < h) {
        int p = partition(a, l, h);
        quickSort(a, l, p - 1);
        quickSort(a, p + 1, h);
    }
}

void printArray(int a[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main() {
    int a[MAX], b[MAX], n;

    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter elements: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    // Selection Sort
    for (int i = 0; i < n; i++) b[i] = a[i];
    selectionSort(b, n);
    printf("Selection Sort: ");
    printArray(b, n);

    // Insertion Sort
    for (int i = 0; i < n; i++) b[i] = a[i];
    insertionSort(b, n);
    printf("Insertion Sort: ");
    printArray(b, n);

    // Quick Sort
    for (int i = 0; i < n; i++) b[i] = a[i];
    quickSort(b, 0, n - 1);
    printf("Quick Sort: ");
    printArray(b, n);

    // Merge Sort
    for (int i = 0; i < n; i++) b[i] = a[i];
    mergeSort(b, 0, n - 1);
    printf("Merge Sort: ");
    printArray(b, n);

    return 0;
}
