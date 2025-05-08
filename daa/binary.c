#include <stdio.h>

int main() {
    int a[100], n, key, low, high, mid, i;

    printf("How many numbers? ");
    scanf("%d", &n);

    printf("Enter sorted numbers:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("Search for? ");
    scanf("%d", &key);

    low = 0;
    high = n - 1;

    while(low <= high){
        mid = (low + high) / 2;

        if(a[mid] == key) {
            printf("Found at %d\n", mid);
            return 0;
        }
        if(a[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }

    printf("Not found\n");
    return 0;
}
