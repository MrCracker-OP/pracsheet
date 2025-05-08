#include <stdio.h>

struct Result {
    int min;
    int max;
};

struct Result findMinMax(int a[], int low, int high) {
    struct Result res;
    if (low == high) {
        res.min = res.max = a[low];
    } else {
        int mid = (low + high) / 2;
        struct Result left = findMinMax(a, low, mid);
        struct Result right = findMinMax(a, mid + 1, high);
        res.min = (left.min < right.min) ? left.min : right.min;
        res.max = (left.max > right.max) ? left.max : right.max;
    }
    return res;
}

int main() {
    int a[100], n, i;
    
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    struct Result ans = findMinMax(a, 0, n - 1);
    printf("Min: %d, Max: %d\n", ans.min, ans.max);
    return 0;
}
