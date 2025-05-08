#include <stdio.h>

void sortItems(float w[], float p[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = i + 1; j < n; j++)
            if ((p[i]/w[i]) < (p[j]/w[j])) {
                float temp;
                temp = p[i]; p[i] = p[j]; p[j] = temp;
                temp = w[i]; w[i] = w[j]; w[j] = temp;
            }
}

float knapsack(float w[], float p[], int n, float maxWeight) {
    float profit = 0;
    for (int i = 0; i < n && maxWeight > 0; i++) {
        if (w[i] <= maxWeight) {
            profit += p[i];
            maxWeight -= w[i];
        } else {
            profit += p[i] * (maxWeight / w[i]);
            break;
        }
    }
    return profit;
}

int main() {
    int n;
    float w[20], p[20], maxW;

    printf("Enter number of items: ");
    scanf("%d", &n);
    printf("Enter max weight: ");
    scanf("%f", &maxW);

    printf("Enter weights:\n");
    for (int i = 0; i < n; i++) scanf("%f", &w[i]);

    printf("Enter profits:\n");
    for (int i = 0; i < n; i++) scanf("%f", &p[i]);

    sortItems(w, p, n);
    float result = knapsack(w, p, n, maxW);
    printf("Max profit: %.2f\n", result);

    return 0;
}
