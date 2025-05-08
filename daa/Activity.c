#include <stdio.h>

int main() {
    int n, s[20], f[20], i, j;

    printf("Enter number of activities: ");
    scanf("%d", &n);

    printf("Enter start times:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &s[i]);

    printf("Enter finish times:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &f[i]);

    // Sort by finish time
    for (i = 0; i < n - 1; i++)
        for (j = 0; j < n - i - 1; j++)
            if (f[j] > f[j + 1]) {
                int t;
                t = f[j]; f[j] = f[j + 1]; f[j + 1] = t;
                t = s[j]; s[j] = s[j + 1]; s[j + 1] = t;
            }

    printf("Selected activities:\n");
    printf("Start: %d, Finish: %d\n", s[0], f[0]);
    int last = 0;

    for (i = 1; i < n; i++) {
        if (s[i] >= f[last]) {
            printf("Start: %d, Finish: %d\n", s[i], f[i]);
            last = i;
        }
    }

    return 0;
}
